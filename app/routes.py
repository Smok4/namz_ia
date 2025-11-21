
from flask import Blueprint, jsonify, request, current_app, render_template
from .web_fetcher import fetch_stackoverflow_snippets
import json
import os
import datetime
from .code_templates import CODE_TEMPLATES
from .security import require_valid_input, rate_limit
bp = Blueprint('main', __name__)
from app.auto_learn import start_auto_learn, stop_auto_learn, get_auto_learn_log

# API pour démarrer l'apprentissage automatique
@bp.route('/api/auto_learn', methods=['POST'])
def api_auto_learn():
    if request.content_type and 'application/json' in request.content_type:
        data = request.get_json(force=True)
    else:
        data = {}
    action = (data or {}).get('action')
    if action == 'start':
        start_auto_learn()
        return jsonify({'status': 'ok', 'message': 'Apprentissage automatique démarré.'})
    elif action == 'stop':
        stop_auto_learn()
        return jsonify({'status': 'ok', 'message': 'Apprentissage automatique stoppé.'})
    else:
        # Appel périodique pour enrichir
        log = get_auto_learn_log()
        return jsonify({'status': 'ok', 'message': log[-1] if log else 'En attente...', 'log': log})
# Page web pour apprentissage automatique
@bp.route('/auto_learn', methods=['GET'])
def auto_learn_page():
    return render_template('auto_learn.html')

# API pour enrichir la mémoire d'apprentissage utilisateur
@bp.route('/api/learn', methods=['POST'])
def api_learn():
    from .user_examples import save_user_example
    data = request.get_json(force=True)
    question = data.get('question')
    code = data.get('code')
    lang = data.get('lang')
    if not (question and code):
        return jsonify({'error': 'Champs manquants'}), 400
    save_user_example(question, code, lang)
    return jsonify({'ok': True})

@bp.route('/templates', methods=['GET'])
def templates_manager():
    return render_template('templates_manager.html')

# API pour lire/écrire les templates de code dynamiquement
@bp.route('/api/code_templates', methods=['GET', 'POST'])
@rate_limit(max_requests=30, window=60)  # 30 req/min
def api_code_templates():
    templates_path = os.path.join(os.path.dirname(__file__), 'code_templates.py')
    if request.method == 'GET':
        return jsonify(CODE_TEMPLATES)
    if request.method == 'POST':
        data = request.get_json(force=True)
        key = data.get('key')
        patterns = data.get('patterns')
        template = data.get('template')
        if not (key and patterns and template):
            return jsonify({'error': 'Champs manquants'}), 400
        # Met à jour le dict en mémoire
        CODE_TEMPLATES[key] = {'patterns': patterns, 'template': template}
        # Persiste dans le fichier code_templates.py
        with open(templates_path, 'w', encoding='utf-8') as f:
            f.write('CODE_TEMPLATES = ' + json.dumps(CODE_TEMPLATES, ensure_ascii=False, indent=4))
        return jsonify({'ok': True})


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})


# Exemple d’API publique
@bp.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, world!'})

# API IA maison, innovante et efficace
from .ia_engine import analyse_texte
import logging



# Nouvelle route pour apprendre via Internet (StackOverflow)
@bp.route('/api/web_learn', methods=['POST'])
def web_learn():
    data = request.get_json(force=True)
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Missing question'}), 400
    snippets = fetch_stackoverflow_snippets(question)
    return jsonify({'snippets': snippets})

# Page web pour apprentissage via Internet
@bp.route('/web_learn', methods=['GET'])
def web_learn_page():
    return render_template('web_learn.html')

@bp.route('/api/ia', methods=['POST'])
@rate_limit(max_requests=10, window=60)  # 10 req/min
@require_valid_input('message')
def ia():
    from .ia_engine import analyse_texte
    from markupsafe import escape
    import traceback
    
    # Rate limiting
    limiter = current_app.limiter
    limiter.limit("10 per minute")(lambda: None)()
    
    try:
        # Validation du format
        data = request.get_json(force=True)
        if not isinstance(data, dict) or 'message' not in data:
            current_app.logger.warning("Format de requête invalide")
            return jsonify({
                "status": "error",
                "response": "Format invalide. Attendu : { 'message': '...' }",
                "error_type": "validation"
            }), 400
        
        message = data.get('message', '').strip()
        
        # Validation message vide
        if not message:
            return jsonify({
                "status": "error",
                "response": "Message vide",
                "error_type": "validation"
            }), 400
        
        # Validation longueur
        max_length = current_app.config.get('MAX_CONTENT_LENGTH', 10000)
        if len(message) > max_length:
            current_app.logger.warning(f"Message trop long: {len(message)} caractères")
            return jsonify({
                "status": "error",
                "response": f"Message trop long (max {max_length} caractères)",
                "error_type": "validation"
            }), 400
        
        # Sanitization
        message = escape(message)
        
        # Analyse
        resultat = analyse_texte(message)
        current_app.logger.info(f"[IA] Message analysé: {message[:50]}... | Succès")
        return jsonify(resultat)
    
    except ValueError as e:
        current_app.logger.warning(f"Erreur validation: {e}")
        return jsonify({
            "status": "error",
            "response": str(e),
            "error_type": "validation"
        }), 400
    
    except TimeoutError as e:
        current_app.logger.error(f"Timeout: {e}")
        return jsonify({
            "status": "error",
            "response": "Le traitement a pris trop de temps. Essayez une requête plus simple.",
            "error_type": "timeout"
        }), 504
    
    except Exception as e:
        current_app.logger.exception(f"Erreur critique: {e}")
        
        # En production, ne pas exposer les détails
        if current_app.config.get('DEBUG'):
            error_message = str(e)
            stack_trace = traceback.format_exc()
        else:
            error_message = "Erreur interne du serveur"
            stack_trace = None
        
        return jsonify({
            "status": "error",
            "response": error_message,
            "error_type": "internal",
            "stack_trace": stack_trace
        }), 500

# === NOUVELLES ROUTES POUR LES AMÉLIORATIONS ===

@bp.route('/api/memory/stats', methods=['GET'])
def memory_stats():
    """Récupère les statistiques de la mémoire de conversation."""
    from .conversation_memory import get_conversation_memory
    memory = get_conversation_memory()
    stats = memory.get_statistics()
    return jsonify(stats)

@bp.route('/api/memory/clear', methods=['POST'])
def memory_clear():
    """Efface la session de conversation courante."""
    from .conversation_memory import get_conversation_memory
    memory = get_conversation_memory()
    memory.clear_session()
    return jsonify({'status': 'ok', 'message': 'Session effacée'})

@bp.route('/api/memory/context', methods=['GET'])
def memory_context():
    """Récupère le contexte de conversation actuel."""
    from .conversation_memory import get_conversation_memory
    memory = get_conversation_memory()
    context = memory.get_context()
    return jsonify(context)

@bp.route('/api/analyze_code', methods=['POST'])
@rate_limit(max_requests=5, window=60)  # 5 req/min (plus restrictif)
@require_valid_input('code')
def analyze_code():
    """Analyse un code fourni et retourne des suggestions d'amélioration."""
    from .code_analyzer import get_code_analyzer
    from markupsafe import escape
    
    # Rate limiting (plus restrictif pour analyse)
    limiter = current_app.limiter
    limiter.limit("5 per minute")(lambda: None)()
    
    try:
        data = request.get_json(force=True)
        code = data.get('code', '').strip()
        
        if not code:
            return jsonify({
                'error': 'Code manquant',
                'error_type': 'validation'
            }), 400
        
        # Validation longueur
        if len(code) > 100000:  # 100KB max
            return jsonify({
                'error': 'Code trop long (max 100KB)',
                'error_type': 'validation'
            }), 400
        
        analyzer = get_code_analyzer()
        analysis = analyzer.analyze_code(code)
        improvements = analyzer.suggest_improvements(code)
        
        return jsonify({
            'analysis': analysis,
            'improvements': improvements
        })
    
    except Exception as e:
        current_app.logger.exception(f"Erreur analyse code: {e}")
        return jsonify({
            'error': 'Erreur lors de l\'analyse',
            'error_type': 'internal'
        }), 500

@bp.route('/api/generate_project', methods=['POST'])
def generate_project():
    """Génère un projet multi-fichiers complet."""
    from .multi_file_generator import get_multi_file_generator
    
    # Rate limiting (très restrictif)
    limiter = current_app.limiter
    limiter.limit("3 per minute")(lambda: None)()
    
    try:
        data = request.get_json(force=True)
        project_type = data.get('project_type')
        
        if not project_type:
            # Détection automatique depuis le message
            message = data.get('message', '').strip()
            if not message:
                return jsonify({
                    'error': 'project_type ou message requis',
                    'error_type': 'validation'
                }), 400
            
            generator = get_multi_file_generator()
            project_type = generator.detect_project_type(message)
        
        generator = get_multi_file_generator()
        project = generator.generate_project(project_type)
        
        return jsonify(project)
    
    except Exception as e:
        current_app.logger.exception(f"Erreur génération projet: {e}")
        return jsonify({
            'error': 'Erreur lors de la génération',
            'error_type': 'internal'
        }), 500

@bp.route('/api/engine/stats', methods=['GET'])
def engine_stats():
    """Statistiques avancées du moteur IA."""
    try:
        from .ia_engine import get_engine_stats
        
        stats = get_engine_stats()
        stats['timestamp'] = datetime.datetime.utcnow().isoformat()
        
        return jsonify(stats)
    except Exception as e:
        return jsonify({
            'error': str(e),
            'timestamp': datetime.datetime.utcnow().isoformat()
        }), 500

@bp.route('/api/engine/reset', methods=['POST'])
def engine_reset():
    """Réinitialise les statistiques du moteur."""
    try:
        from .ia_engine import reset_engine_stats
        
        reset_engine_stats()
        
        return jsonify({
            'status': 'ok',
            'message': 'Statistiques réinitialisées',
            'timestamp': datetime.datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@bp.route('/api/engine/cache/clear', methods=['POST'])
def clear_engine_cache():
    """Vide le cache du moteur."""
    try:
        from .ia_engine import reset_engine_stats
        reset_engine_stats()
        return jsonify({'status': 'ok', 'message': 'Cache cleared'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/api/projects/list', methods=['GET'])
def list_projects():
    """Liste tous les types de projets disponibles."""
    from .multi_file_generator import get_multi_file_generator
    generator = get_multi_file_generator()
    
    projects = []
    for project_type, template in generator.project_templates.items():
        projects.append({
            'type': project_type,
            'name': template['name'],
            'description': template['description'],
            'files_count': len(template['files'])
        })
    
    return jsonify({'projects': projects})

