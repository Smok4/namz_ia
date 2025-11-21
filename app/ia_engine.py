from .user_examples import find_best_user_example
from .code_templates import CODE_TEMPLATES
from .knowledge_base import KNOWLEDGE_BASE
from .conversation_memory import get_conversation_memory
from .code_analyzer import get_code_analyzer
from .proactive_suggester import get_proactive_suggester
from .multi_file_generator import get_multi_file_generator
import os
import time
import logging
from collections import OrderedDict
from functools import wraps
from threading import Lock
import hashlib
import json

# Logger
logger = logging.getLogger(__name__)

# Flag pour activer le moteur V2 (mettre False pour utiliser V1 legacy)
USE_ENGINE_V2 = os.getenv('NAMZ_USE_ENGINE_V2', 'true').lower() == 'true'

# ═══════════════════════════════════════════════════════════════════════════════
#                        CACHE LRU INTELLIGENT
# ═══════════════════════════════════════════════════════════════════════════════

class LRUCache:
    """Cache LRU thread-safe avec TTL pour réponses IA."""
    
    def __init__(self, maxsize=1000, ttl=3600):
        self.cache = OrderedDict()
        self.maxsize = maxsize
        self.ttl = ttl  # Time to live en secondes
        self.lock = Lock()
        self.hits = 0
        self.misses = 0
    
    def _make_key(self, message: str) -> str:
        """Génère une clé de cache normalisée."""
        normalized = message.lower().strip()
        return hashlib.md5(normalized.encode()).hexdigest()
    
    def get(self, message: str):
        """Récupère une valeur du cache."""
        key = self._make_key(message)
        
        with self.lock:
            if key not in self.cache:
                self.misses += 1
                return None
            
            # Vérifier TTL
            entry = self.cache[key]
            age = time.time() - entry['timestamp']
            
            if age > self.ttl:
                del self.cache[key]
                self.misses += 1
                return None
            
            # Déplacer en fin (plus récent)
            self.cache.move_to_end(key)
            self.hits += 1
            return entry['value']
    
    def set(self, message: str, value):
        """Ajoute une valeur au cache."""
        key = self._make_key(message)
        
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
            
            self.cache[key] = {
                'value': value,
                'timestamp': time.time()
            }
            
            # Éviction LRU si dépassement
            if len(self.cache) > self.maxsize:
                self.cache.popitem(last=False)
    
    def stats(self):
        """Statistiques du cache."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        
        return {
            'size': len(self.cache),
            'maxsize': self.maxsize,
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': f'{hit_rate:.1f}%'
        }
    
    def clear(self):
        """Vide le cache."""
        with self.lock:
            self.cache.clear()
            self.hits = 0
            self.misses = 0

# ═══════════════════════════════════════════════════════════════════════════════
#                        CIRCUIT BREAKER
# ═══════════════════════════════════════════════════════════════════════════════

class CircuitBreaker:
    """Circuit breaker pour éviter surcharge."""
    
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN
        self.lock = Lock()
    
    def call(self, func, *args, **kwargs):
        """Exécute une fonction avec protection circuit breaker."""
        with self.lock:
            # Vérifier si le circuit doit se refermer
            if self.state == 'OPEN':
                if time.time() - self.last_failure_time > self.timeout:
                    self.state = 'HALF_OPEN'
                    self.failures = 0
                else:
                    raise Exception('Circuit breaker OPEN: système surchargé')
        
        try:
            result = func(*args, **kwargs)
            
            # Succès: réinitialiser compteur
            with self.lock:
                if self.state == 'HALF_OPEN':
                    self.state = 'CLOSED'
                self.failures = 0
            
            return result
        
        except Exception as e:
            # Échec: incrémenter compteur
            with self.lock:
                self.failures += 1
                self.last_failure_time = time.time()
                
                if self.failures >= self.failure_threshold:
                    self.state = 'OPEN'
                    logger.error(f'Circuit breaker OPEN après {self.failures} échecs')
            
            raise e
    
    def status(self):
        """État actuel du circuit breaker."""
        return {
            'state': self.state,
            'failures': self.failures,
            'threshold': self.failure_threshold
        }

# ═══════════════════════════════════════════════════════════════════════════════
#                        MÉTRIQUES DE PERFORMANCE
# ═══════════════════════════════════════════════════════════════════════════════

class PerformanceMetrics:
    """Collecte des métriques de performance."""
    
    def __init__(self):
        self.total_requests = 0
        self.total_time = 0.0
        self.min_time = float('inf')
        self.max_time = 0.0
        self.rule_usage = {}
        self.lock = Lock()
    
    def record(self, duration: float, rule_name: str):
        """Enregistre une métrique."""
        with self.lock:
            self.total_requests += 1
            self.total_time += duration
            self.min_time = min(self.min_time, duration)
            self.max_time = max(self.max_time, duration)
            
            if rule_name not in self.rule_usage:
                self.rule_usage[rule_name] = 0
            self.rule_usage[rule_name] += 1
    
    def stats(self):
        """Statistiques globales."""
        avg_time = (self.total_time / self.total_requests) if self.total_requests > 0 else 0
        
        # Top 5 règles utilisées
        top_rules = sorted(
            self.rule_usage.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        return {
            'total_requests': self.total_requests,
            'avg_response_time': f'{avg_time:.3f}s',
            'min_response_time': f'{self.min_time:.3f}s',
            'max_response_time': f'{self.max_time:.3f}s',
            'top_rules': [{'rule': r, 'count': c} for r, c in top_rules]
        }
    
    def reset(self):
        """Réinitialise les métriques."""
        with self.lock:
            self.total_requests = 0
            self.total_time = 0.0
            self.min_time = float('inf')
            self.max_time = 0.0
            self.rule_usage = {}

# Instances globales
_cache = LRUCache(maxsize=1000, ttl=3600)
_circuit_breaker = CircuitBreaker(failure_threshold=10, timeout=60)
_metrics = PerformanceMetrics()

def _similarity(a: str, b: str) -> float:
    """Score de similarité ultra simple basé sur les mots communs."""
    sa = set(a.lower().split())
    sb = set(b.lower().split())
    if not sa or not sb:
        return 0.0
    inter = len(sa & sb)
    union = len(sa | sb)
    return inter / union
"""
Namz IA Engine - Version avancée, modulaire, multilingue, scoring, logs, 100% maison, sans dépendance IA externe.
Ce module propose un moteur d'analyse textuelle basé sur des règles, heuristiques, scoring, et support multilingue.
Il est conçu pour être rapide, peu gourmand en ressources, facilement personnalisable et prêt pour l'innovation future.

NOUVELLES FONCTIONNALITÉS V1:
- 🧠 Mémoire de conversation (se souvient du contexte)
- 🔍 Analyse de code existant (amélioration et suggestions)
- 💡 Suggestions proactives (propose automatiquement des fonctionnalités)
- 📁 Génération multi-fichiers (projets complets)

NOUVELLES FONCTIONNALITÉS V2 (si USE_ENGINE_V2=true):
- ⚡ Cache LRU avec TTL pour réponses ultra-rapides
- 🛡️ Circuit breaker anti-surcharge
- 📊 Métriques de performance temps réel
- 🎯 Auto-apprentissage des patterns
- 🔍 Analyse sémantique NLP avancée
- ⏱️ Timeout par règle avec thread pool
"""

from typing import List, Callable
import re
import datetime

class IAResponse:
    def __init__(self, status: str, response: str, meta: dict = None):
        self.status = status
        self.response = response
        self.meta = meta or {}
    def to_dict(self):
        return {"status": self.status, "response": self.response, "meta": self.meta}

class Rule:
    def __init__(self, name: str, condition: Callable[[str, str], float], action: Callable[[str, str], str], lang: str = "any"):
        self.name = name
        self.condition = condition  # Retourne un score de confiance (0.0 à 1.0)
        self.action = action
        self.lang = lang

class NamzIAEngine:
    """Moteur IA maison, modulaire, multilingue, scoring, logs."""
    def __init__(self):
        self.rules: List[Rule] = []
        self.memory = get_conversation_memory()
        self.code_analyzer = get_code_analyzer()
        self.suggester = get_proactive_suggester()
        self.multi_file_gen = get_multi_file_generator()
        self.previous_suggestions = []
        self._register_default_rules()

    def _register_default_rules(self):
        # Génération de code intelligente (analyse + synthèse)
        self.add_rule(
            "intelligent_code_generation",
            lambda msg, lang: self._detect_code_request(msg),
            lambda msg, lang: self._generate_code_intelligently(msg),
        )
        # Aide au code via base de connaissances (tous langages)
        self.add_rule(
            "code_helper",
            lambda msg, lang: 0.95 if any(
                kw in msg.lower()
                for kw in [
                    "python", "javascript", "js", "flask", "fonction", "function", "variable", "class", "boucle", "loop", "erreur", "error", "bug",
                    "c#", ".net", "asp.net", "linq", "razor", "c ", "pointeur", "pointer"
                ]
            ) else 0.0,
            lambda msg, lang: self._answer_from_knowledge_base(msg, lang),
        )
        # Salutations multilingues
        self.add_rule(
            "salutation_fr",
            lambda msg, lang: 1.0 if re.search(r"\b(bonjour|salut|coucou)\b", msg, re.IGNORECASE) and lang == "fr" else 0.0,
            lambda msg, lang: "Bonjour ! Comment puis-je vous aider ?",
            lang="fr"
        )
        self.add_rule(
            "salutation_en",
            lambda msg, lang: 1.0 if re.search(r"\b(hello|hi|hey)\b", msg, re.IGNORECASE) and lang == "en" else 0.0,
            lambda msg, lang: "Hello! How can I help you?",
            lang="en"
        )
        # Demande d'aide
        self.add_rule(
            "demande_aide",
            lambda msg, lang: 0.9 if re.search(r"aide|help", msg, re.IGNORECASE) else 0.0,
            lambda msg, lang: "Voici comment je peux vous aider... (documentation, support, etc.)" if lang == "fr" else "Here is how I can help you... (documentation, support, etc.)"
        )
        # Question
        self.add_rule(
            "question",
            lambda msg, lang: 0.8 if msg.strip().endswith("?") else 0.0,
            lambda msg, lang: "C'est une excellente question. Je vais y réfléchir." if lang == "fr" else "That's a great question. I'll think about it."
        )
        # Motivation
        self.add_rule(
            "motivation",
            lambda msg, lang: 0.7 if re.search(r"(courage|force|motivation|bravo|success)", msg, re.IGNORECASE) else 0.0,
            lambda msg, lang: "Vous êtes capable de grandes choses !" if lang == "fr" else "You are capable of great things!"
        )
        # Remerciement
        self.add_rule(
            "remerciement",
            lambda msg, lang: 0.7 if re.search(r"merci|thanks|thank you", msg, re.IGNORECASE) else 0.0,
            lambda msg, lang: "Avec plaisir ! N'hésitez pas si besoin." if lang == "fr" else "You're welcome! Let me know if you need anything."
        )
        # Fallback humoristique
        self.add_rule(
            "humour",
            lambda msg, lang: 0.5 if re.search(r"(blague|joke|rigole)", msg, re.IGNORECASE) else 0.0,
            lambda msg, lang: "Pourquoi les programmeurs confondent Halloween et Noël ? Parce que OCT 31 == DEC 25 !"
        )

    def _answer_from_knowledge_base(self, message: str, lang: str) -> str:
        """Cherche la meilleure réponse de code dans la base de connaissances."""
        best_score = 0.0
        best_answer = "Je n'ai pas encore de connaissance précise sur cette question de code."
        for item in KNOWLEDGE_BASE:
            for pattern in item.get("patterns", []):
                score = _similarity(message, pattern)
                if score > best_score:
                    best_score = score
                    best_answer = item["answer"]
        # On ajoute une petite intro contextuelle
        if best_score > 0.0:
            prefix = "Voici un exemple de code :\n\n" if "fr" in lang else "Here is a code example:\n\n"
            return prefix + best_answer
        return "Je ne trouve pas encore d'exemple exact, mais essaie de préciser ta question (langage, erreur, contexte)."

    def _detect_code_request(self, message: str) -> float:
        """Détecte si c'est une demande de génération de code ou d'amélioration."""
        code_keywords = [
            # Actions de création
            'crée', 'créer', 'create', 'fait', 'fais', 'faire', 'make', 'écris', 'écrire', 'write',
            'génère', 'générer', 'generate', 'développe', 'développer', 'develop', 'build', 'construis',
            'code', 'programme', 'program', 'script', 'app', 'application', 'site', 'page',
            
            # Types de code
            'fonction', 'function', 'classe', 'class', 'méthode', 'method', 'api', 'interface',
            'algorithme', 'algorithm', 'structure', 'module', 'composant', 'component',
            
            # Actions d'amélioration
            'optimise', 'optimiser', 'optimize', 'améliore', 'améliorer', 'improve', 'refactor',
            'refactoriser', 'corriger', 'fix', 'debug', 'débugger', 'réparer', 'repair',
            
            # Langage conversationnel
            'peux-tu', 'peux tu', 'pourrais-tu', 'pourrais tu', 'voudrais', 'aimerais',
            'besoin de', 'besoin d', 'il me faut', 'je veux', 'je voudrais', 'j\'ai besoin',
            'help me', 'aide-moi', 'montre-moi', 'show me', 'comment faire',
            
            # Contextes techniques
            'html', 'css', 'javascript', 'python', 'java', 'php', 'ruby', 'go', 'rust',
            'backend', 'frontend', 'fullstack', 'web', 'mobile', 'desktop',
            'base de données', 'database', 'sql', 'api rest', 'graphql'
        ]
        
        msg_lower = message.lower()
        
        # Détection par mots-clés
        for kw in code_keywords:
            if kw in msg_lower:
                return 1.0
        
        # Détection de patterns conversationnels
        conversational_patterns = [
            r'\b(comment|how)\s+(faire|to|créer|make|coder|code)\b',
            r'\b(je|j\')\s+(veux|voudrais|aimerais|cherche)\b',
            r'\b(peux|pourrais|pourrait)(-tu|s-tu|\stu)\b',
            r'\b(besoin|need)\s+(de|d\'|of)\b',
            r'\b(aide|help)(-moi|me)\b',
            r'\b(montre|show)(-moi|me)\b',
        ]
        
        for pattern in conversational_patterns:
            if re.search(pattern, msg_lower):
                return 1.0
        
        return 0.0
    
    def _generate_code_intelligently(self, message: str) -> str:
        """Génère du code en analysant la demande et en synthétisant depuis les templates existants."""
        msg_lower = message.lower()
        
        # Analyse contextuelle avancée
        context = self._analyze_context(message)
        
        # 1. Détecte le langage de manière plus intelligente
        lang = context.get('language')
        if not lang:
            lang = self._detect_language_from_message(msg_lower)
        
        # 2. Détecte le type de code demandé et l'intention
        code_type = context.get('code_type')
        intent = context.get('intent', 'create')
        
        if not code_type:
            code_type, intent = self._detect_code_type_and_intent(msg_lower)
        
        # 3. Si l'intention est "improve_previous", récupérer le contexte précédent
        if intent == 'improve_previous':
            previous_code = self._get_previous_generated_code(context.get('domain'))
            if previous_code:
                return self._enhance_existing_code(previous_code, message, context)
            else:
                # Pas de code précédent trouvé, créer un nouveau code amélioré
                logger.warning("Aucun code précédent trouvé, génération d'un nouveau code")
                intent = 'create'
        
        # 4. Extrait des informations spécifiques
        name_match = re.search(r'(?:appelée?|nommée?|name|called)\s+["\']?(\w+)["\']?', message, re.IGNORECASE)
        name = name_match.group(1) if name_match else None
        
        # 5. Cherche dans les templates existants pour s'inspirer
        relevant_templates = []
        for key, tpl in CODE_TEMPLATES.items():
            if lang and lang in key.lower():
                if code_type and code_type in key.lower():
                    relevant_templates.append((key, tpl))
        
        # 6. Si on a un template pertinent, l'utiliser comme base
        if relevant_templates:
            best_template = relevant_templates[0][1]
            return self._fill_template_intelligently(best_template['template'], message, lang, code_type, name)
        
        # 7. Sinon, génère du code from scratch avec intention
        return self._synthesize_code_from_scratch(message, lang, code_type, name, intent)
    
    def _get_previous_generated_code(self, domain: str = None) -> str:
        """Récupère le code généré dans la conversation précédente."""
        try:
            # Récupérer l'historique de conversation
            history = self.memory.get_context().get('messages', [])
            
            # Chercher le dernier message de l'assistant contenant du code
            for msg in reversed(history):
                if msg.get('role') == 'assistant':
                    content = msg.get('content', '')
                    
                    # Vérifier si le message contient du code HTML (site web)
                    if '<!DOCTYPE html>' in content and 'html' in content:
                        # Si un domaine est spécifié, vérifier la correspondance
                        if domain:
                            if domain == 'ecommerce' and any(w in content.lower() for w in ['boutique', 'shop', 'panier', 'cart', 'produit', 'product']):
                                return content
                            elif domain in content.lower():
                                return content
                        else:
                            return content
                    
                    # Vérifier si le message contient d'autres types de code
                    elif '```' in content:
                        # Si un domaine est spécifié, vérifier la correspondance
                        if domain and domain in content.lower():
                            return content
                        elif not domain:
                            return content
            
            return None
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du code précédent: {e}")
            return None
    
    def _enhance_existing_code(self, previous_code: str, message: str, context: dict) -> str:
        """Améliore le code existant en fonction de la demande."""
        msg_lower = message.lower()
        domain = context.get('domain', 'general')
        
        # Extraire ce qui doit être amélioré
        improvements = []
        
        if any(w in msg_lower for w in ['design', 'style', 'apparence', 'look']):
            improvements.append('design')
        if any(w in msg_lower for w in ['animation', 'effet', 'effect', 'transition']):
            improvements.append('animations')
        if any(w in msg_lower for w in ['responsive', 'mobile', 'tablette', 'tablet']):
            improvements.append('responsive')
        if any(w in msg_lower for w in ['couleur', 'color', 'palette']):
            improvements.append('colors')
        if any(w in msg_lower for w in ['fonctionnalité', 'feature', 'fonction']):
            improvements.append('features')
        if any(w in msg_lower for w in ['performance', 'rapide', 'fast', 'optimis']):
            improvements.append('performance')
        
        # Si aucune amélioration spécifique, améliorer tout
        if not improvements:
            improvements = ['design', 'animations', 'features']
        
        # Générer une version améliorée selon le domaine
        if domain == 'ecommerce':
            return self._generate_enhanced_ecommerce_site(improvements)
        elif 'html' in previous_code.lower():
            return self._generate_enhanced_website(improvements, context)
        else:
            return f"✅ **Amélioration détectée !**\n\n" \
                   f"Améliorations demandées : {', '.join(improvements)}\n\n" \
                   f"Malheureusement, je ne peux pas encore modifier directement le code précédent.\n" \
                   f"Je vais générer une nouvelle version améliorée :\n\n" + \
                   self._synthesize_code_from_scratch(message, 'html', 'website', None, 'improve')
    
    def _generate_enhanced_ecommerce_site(self, improvements: list) -> str:
        """Génère un site e-commerce amélioré."""
        return f"""✅ **Site E-commerce Amélioré Généré !**

🎨 Améliorations apportées : **{', '.join(improvements)}**

Je vais créer une version ultra-moderne de votre site dropshipping avec :
- ✨ Design moderne et épuré (2025)
- 🎭 Animations fluides et professionnelles
- 📱 100% Responsive (mobile-first)
- 🎨 Palette de couleurs premium
- 🛒 Panier interactif avec modal
- ⭐ Système de notation produits
- 🔥 Badge "Nouveau" et "Promo"
- 💳 Icônes de paiement sécurisé
- 📊 Statistiques en temps réel

Le fichier a déjà été créé dans `/app/templates/dropshipping.html`

Pour le voir : **http://localhost:5000/dropshipping**

Voulez-vous que j'ajoute d'autres fonctionnalités ? (backend, paiement, etc.)
"""
    
    def _generate_enhanced_website(self, improvements: list, context: dict) -> str:
        """Génère un site web générique amélioré."""
        return f"""✅ **Site Web Amélioré !**

Améliorations : {', '.join(improvements)}

Je peux créer une version améliorée. Que souhaitez-vous exactement ?
- Un site vitrine professionnel
- Un portfolio moderne
- Un blog avec CMS
- Une landing page de conversion

Précisez votre besoin pour un résultat optimal !
"""
    
    def _detect_language_from_message(self, msg_lower: str) -> str:
        """Détecte le langage depuis le message avec intelligence contextuelle."""
        # Détection explicite
        if any(w in msg_lower for w in ['python', 'py']):
            return 'python'
        elif any(w in msg_lower for w in ['typescript', 'ts']):
            return 'typescript'
        elif any(w in msg_lower for w in ['javascript', 'js', 'node']):
            return 'javascript'
        elif any(w in msg_lower for w in ['c#', 'csharp', 'dotnet', '.net']):
            return 'csharp'
        elif ' c ' in msg_lower or msg_lower.startswith('c ') or msg_lower.endswith(' c'):
            return 'c'
        elif any(w in msg_lower for w in ['java ', 'java']):
            return 'java'
        elif any(w in msg_lower for w in ['php']):
            return 'php'
        elif any(w in msg_lower for w in ['ruby', 'rb']):
            return 'ruby'
        elif any(w in msg_lower for w in ['go', 'golang']):
            return 'go'
        elif any(w in msg_lower for w in ['rust', 'rs']):
            return 'rust'
        elif any(w in msg_lower for w in ['swift']):
            return 'swift'
        elif any(w in msg_lower for w in ['kotlin', 'kt']):
            return 'kotlin'
        elif any(w in msg_lower for w in ['sql', 'database', 'base de données']):
            return 'sql'
        elif any(w in msg_lower for w in ['bash', 'shell', 'script shell']):
            return 'bash'
        
        # Détection par contexte (site web = HTML)
        elif any(w in msg_lower for w in ['site', 'page web', 'html', 'website']):
            return 'html'
        elif any(w in msg_lower for w in ['style', 'css', 'design']):
            return 'css'
        
        # Détection par contexte projet
        elif any(w in msg_lower for w in ['api rest', 'serveur', 'backend']):
            return 'python'  # Par défaut Python pour backend
        elif any(w in msg_lower for w in ['app mobile', 'android']):
            return 'kotlin'
        elif any(w in msg_lower for w in ['ios', 'iphone', 'ipad']):
            return 'swift'
        elif any(w in msg_lower for w in ['web app', 'frontend', 'spa']):
            return 'javascript'
        
        # Si aucun langage détecté, retourner None
        return None
    
    def _detect_code_type_and_intent(self, msg_lower: str) -> tuple:
        """Détecte le type de code et l'intention depuis le message."""
        intent = 'create'
        code_type = None
        
        # Détection d'intention avec référence au contexte précédent
        if any(w in msg_lower for w in ['améliore', 'améliorer', 'improve', 'enhance', 'mieux', 'better']):
            # Vérifier si on fait référence à quelque chose de précédent
            if any(w in msg_lower for w in ['notre', 'le', 'ce', 'this', 'that', 'précédent', 'previous']):
                intent = 'improve_previous'  # Améliorer quelque chose déjà généré
            else:
                intent = 'improve'
        elif any(w in msg_lower for w in ['optimise', 'optimiser', 'optimize', 'performance', 'plus rapide', 'faster']):
            intent = 'optimize'
        elif any(w in msg_lower for w in ['refactor', 'refactoriser', 'restructure', 'nettoie', 'clean']):
            intent = 'refactor'
        elif any(w in msg_lower for w in ['debug', 'débugger', 'corriger', 'fix', 'réparer', 'repair', 'bug', 'erreur', 'error']):
            intent = 'debug'
        elif any(w in msg_lower for w in ['explique', 'expliquer', 'explain', 'comment', 'how', 'pourquoi', 'why']):
            intent = 'explain'
        
        # Détection de type
        if any(w in msg_lower for w in ['fonction', 'function', 'méthode', 'method', 'def ', 'fn ']):
            code_type = 'function'
        elif any(w in msg_lower for w in ['classe', 'class', 'objet', 'object']):
            code_type = 'class'
        elif any(w in msg_lower for w in ['boucle', 'loop', 'itérer', 'iterate', 'for', 'while']):
            code_type = 'loop'
        elif any(w in msg_lower for w in ['trier', 'sort', 'tri', 'sorting']):
            code_type = 'sort'
        elif any(w in msg_lower for w in ['lire', 'read', 'ouvrir', 'open', 'fichier']):
            code_type = 'read_file'
        elif any(w in msg_lower for w in ['écrire', 'write', 'sauver', 'save', 'enregistrer']):
            code_type = 'write_file'
        elif any(w in msg_lower for w in ['calculatrice', 'calculator', 'calcul', 'calculate']):
            code_type = 'calculator'
        elif any(w in msg_lower for w in ['api', 'requete', 'request', 'fetch', 'http', 'rest']):
            code_type = 'api'
        elif any(w in msg_lower for w in ['select', 'insert', 'update', 'delete', 'requête sql', 'query']):
            code_type = 'sql_query'
        elif any(w in msg_lower for w in ['test', 'unittest', 'tests', 'testing']):
            code_type = 'test'
        elif any(w in msg_lower for w in ['interface', 'ui', 'gui', 'formulaire', 'form']):
            code_type = 'interface'
        elif any(w in msg_lower for w in ['site', 'page', 'website', 'web']):
            code_type = 'website'
        elif any(w in msg_lower for w in ['app', 'application', 'programme', 'program']):
            code_type = 'application'
        
        return code_type, intent
    
    def _analyze_context(self, message: str) -> dict:
        """Analyse approfondie du contexte de la demande."""
        context = {
            'language': None,
            'code_type': None,
            'intent': 'create',
            'complexity': 'simple',
            'requirements': [],
            'constraints': [],
            'domain': None  # Nouveau: domaine spécifique (e-commerce, blog, etc.)
        }
        
        msg_lower = message.lower()
        
        # Détection du domaine/contexte spécifique
        if any(w in msg_lower for w in ['dropshipping', 'e-commerce', 'ecommerce', 'boutique', 'shop', 'magasin', 'vente']):
            context['domain'] = 'ecommerce'
        elif any(w in msg_lower for w in ['blog', 'article', 'news', 'magazine', 'publication']):
            context['domain'] = 'blog'
        elif any(w in msg_lower for w in ['portfolio', 'cv', 'resume', 'professionnel']):
            context['domain'] = 'portfolio'
        elif any(w in msg_lower for w in ['landing', 'page de vente', 'conversion']):
            context['domain'] = 'landing'
        elif any(w in msg_lower for w in ['dashboard', 'admin', 'panneau', 'gestion']):
            context['domain'] = 'dashboard'
        elif any(w in msg_lower for w in ['social', 'réseau social', 'communauté']):
            context['domain'] = 'social'
        elif any(w in msg_lower for w in ['restaurant', 'menu', 'réservation']):
            context['domain'] = 'restaurant'
        elif any(w in msg_lower for w in ['immobilier', 'real estate', 'propriété']):
            context['domain'] = 'realestate'
        elif any(w in msg_lower for w in ['éducation', 'cours', 'formation', 'learning']):
            context['domain'] = 'education'
        elif any(w in msg_lower for w in ['fitness', 'sport', 'gym', 'santé']):
            context['domain'] = 'fitness'
        
        # Analyse de complexité
        if any(w in msg_lower for w in ['avancé', 'advanced', 'complexe', 'complex', 'complet', 'complete']):
            context['complexity'] = 'advanced'
        elif any(w in msg_lower for w in ['professionnel', 'professional', 'production', 'robuste', 'robust']):
            context['complexity'] = 'production'
        
        # Extraction des exigences
        if 'avec' in msg_lower or 'with' in msg_lower:
            requirements_match = re.search(r'(?:avec|with)\s+([^\.]+)', message, re.IGNORECASE)
            if requirements_match:
                context['requirements'] = [req.strip() for req in requirements_match.group(1).split(',')]
        
        # Détection de contraintes
        if any(w in msg_lower for w in ['sans', 'without']):
            constraints_match = re.search(r'(?:sans|without)\s+([^\.]+)', message, re.IGNORECASE)
            if constraints_match:
                context['constraints'] = [const.strip() for const in constraints_match.group(1).split(',')]
        
        return context
    
    def _fill_template_intelligently(self, template: str, message: str, lang: str, code_type: str, name: str) -> str:
        """Remplit un template intelligemment en fonction du contexte."""
        values = {}
        
        # Nom
        if '{name}' in template:
            if name:
                values['name'] = name
            else:
                values['name'] = self._generate_default_name(lang, code_type)
        
        # Arguments
        if '{args}' in template:
            args_match = re.search(r'avec.*?(?:paramètres?|arguments?|params?)\s*[:=]?\s*([^\n\.]+)', message, re.IGNORECASE)
            if args_match:
                values['args'] = args_match.group(1).strip()
            else:
                values['args'] = self._generate_default_args(lang)
        
        # Body
        if '{body}' in template:
            values['body'] = self._generate_body_from_request(message, lang, code_type)
        
        # Autres placeholders
        for placeholder in ['url', 'filename', 'content', 'table', 'colonne', 'colonnes', 'valeur', 'valeurs', 'pattern']:
            if f'{{{placeholder}}}' in template:
                values[placeholder] = self._extract_or_default(message, placeholder)
        
        try:
            result = template.format(**values)
            return f"Voici le code généré :\n\n```{lang or ''}\n{result}\n```"
        except:
            return self._synthesize_code_from_scratch(message, lang, code_type, name)
    
    def _synthesize_code_from_scratch(self, message: str, lang: str, code_type: str, name: str, intent: str = 'create') -> str:
        """Synthétise du code from scratch en analysant les templates existants et l'intention de l'utilisateur."""
        
        # Si pas de langage détecté, proposer intelligemment selon le contexte
        if not lang:
            return self._suggest_language_or_generate(message, code_type, intent)
        
        # Analyse tous les templates du langage pour comprendre la syntaxe
        lang_templates = [tpl['template'] for key, tpl in CODE_TEMPLATES.items() if lang in key.lower()]
        
        if not lang_templates and lang not in ['html', 'css', 'sql']:
            return f"Je n'ai pas encore appris assez de {lang}. Lance l'apprentissage automatique pour enrichir ma base."
        
        # Génère du code basé sur la compréhension des templates et l'intention
        if lang == 'python':
            if intent == 'optimize':
                return """Voici des suggestions d'optimisation pour votre code Python :

```python
# ✅ Optimisations Python

# 1. Utiliser des compréhensions de liste au lieu de boucles
# ❌ Lent
result = []
for i in range(1000):
    result.append(i * 2)

# ✅ Rapide
result = [i * 2 for i in range(1000)]

# 2. Utiliser des générateurs pour économiser la mémoire
# ❌ Charge tout en mémoire
def get_numbers():
    return [i for i in range(1000000)]

# ✅ Génération à la demande
def get_numbers():
    return (i for i in range(1000000))

# 3. Utiliser des sets pour les recherches rapides
# ❌ Lent (O(n))
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("Trouvé")

# ✅ Rapide (O(1))
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    print("Trouvé")

# 4. Utiliser f-strings au lieu de concatenation
# ❌ Lent
name = "Python"
message = "Bonjour " + name + " !"

# ✅ Rapide et lisible
message = f"Bonjour {name} !"

# 5. Éviter les appels répétés de fonctions dans les boucles
# ❌ Lent
for i in range(len(my_list)):
    process(my_list[i])

# ✅ Rapide
length = len(my_list)
for i in range(length):
    process(my_list[i])
```"""
            
            elif intent == 'improve' or intent == 'refactor':
                return """Voici comment améliorer votre code Python :

```python
# ✅ Bonnes pratiques Python

# 1. Type hints pour la clarté
from typing import List, Dict, Optional

def process_data(items: List[int], config: Dict[str, str]) -> Optional[int]:
    \"\"\"
    Traite une liste d'entiers selon la configuration.
    
    Args:
        items: Liste d'entiers à traiter
        config: Configuration du traitement
        
    Returns:
        Résultat du traitement ou None si échec
    \"\"\"
    if not items:
        return None
    return sum(items)

# 2. Gestion d'erreurs explicite
def safe_divide(a: float, b: float) -> Optional[float]:
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Erreur: Division par zéro ({a}/{b})")
        return None
    except TypeError as e:
        print(f"Erreur de type: {e}")
        return None

# 3. Context managers pour les ressources
# ❌ Mauvais
file = open('data.txt', 'r')
data = file.read()
file.close()

# ✅ Bon
with open('data.txt', 'r') as file:
    data = file.read()

# 4. Dataclasses pour les structures de données
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str
    
    def is_adult(self) -> bool:
        return self.age >= 18

# 5. Logging au lieu de print
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process():
    logger.info("Début du traitement")
    logger.error("Une erreur s'est produite")
```"""
            
            elif intent == 'debug':
                return """Voici comment debugger efficacement votre code Python :

```python
# 🐛 Techniques de debugging Python

# 1. Utiliser pdb (Python Debugger)
import pdb

def ma_fonction(x, y):
    pdb.set_trace()  # Point d'arrêt
    result = x + y
    return result

# 2. Logging détaillé
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def process_data(data):
    logging.debug(f"Données reçues: {data}")
    try:
        result = complex_operation(data)
        logging.info(f"Résultat: {result}")
        return result
    except Exception as e:
        logging.exception(f"Erreur lors du traitement: {e}")
        raise

# 3. Assertions pour vérifier les hypothèses
def calculate_average(numbers):
    assert len(numbers) > 0, "La liste ne doit pas être vide"
    assert all(isinstance(n, (int, float)) for n in numbers), "Tous les éléments doivent être numériques"
    return sum(numbers) / len(numbers)

# 4. Try-except avec traceback
import traceback

try:
    risky_operation()
except Exception as e:
    print(f"Erreur: {e}")
    traceback.print_exc()

# 5. Décorateur de debugging
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Appel: {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Retour: {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b
```"""
            
            elif code_type == 'function':
                func_name = name or 'ma_fonction'
                return f"""Voici le code généré :

```python
def {func_name}(param1, param2):
    \"\"\"
    Fonction générée automatiquement.
    Décris ce que fait la fonction ici.
    \"\"\"
    # Votre logique ici
    result = param1 + param2
    return result

# Exemple d'utilisation
if __name__ == "__main__":
    resultat = {func_name}(10, 20)
    print(f"Résultat: {{resultat}}")
```"""
            
            elif code_type == 'class':
                class_name = name or 'MaClasse'
                return f"""Voici le code généré :

```python
class {class_name}:
    \"\"\"Classe générée automatiquement.\"\"\"
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def methode_exemple(self):
        \"\"\"Méthode d'exemple.\"\"\"
        return self.param1 + self.param2
    
    def __str__(self):
        return f"{class_name}({{self.param1}}, {{self.param2}})"
    
    def __repr__(self):
        return self.__str__()

# Exemple d'utilisation
if __name__ == "__main__":
    obj = {class_name}(10, 20)
    print(obj)
    print(obj.methode_exemple())
```"""
        
        elif lang == 'javascript':
            if intent == 'optimize':
                return """Voici des suggestions d'optimisation pour votre code JavaScript :

```javascript
// ✅ Optimisations JavaScript

// 1. Utiliser const/let au lieu de var
// ❌ Mauvais
var count = 0;

// ✅ Bon
const MAX_COUNT = 100;
let count = 0;

// 2. Déstructuration pour la lisibilité
// ❌ Verbeux
const name = user.name;
const age = user.age;

// ✅ Concis
const { name, age } = user;

// 3. Utiliser map/filter/reduce au lieu de boucles
// ❌ Lent
const doubled = [];
for (let i = 0; i < numbers.length; i++) {
    doubled.push(numbers[i] * 2);
}

// ✅ Rapide et lisible
const doubled = numbers.map(n => n * 2);

// 4. Async/await au lieu de callbacks
// ❌ Callback hell
fetchData((data) => {
    processData(data, (result) => {
        saveResult(result, (response) => {
            console.log(response);
        });
    });
});

// ✅ Propre et lisible
const data = await fetchData();
const result = await processData(data);
const response = await saveResult(result);
console.log(response);

// 5. Utiliser Optional Chaining
// ❌ Verbeux
const city = user && user.address && user.address.city;

// ✅ Élégant
const city = user?.address?.city;
```"""
            
            elif code_type == 'function':
                func_name = name or 'maFonction'
                return f"""Voici le code généré :

```javascript
function {func_name}(param1, param2) {{
    // Fonction générée automatiquement
    const result = param1 + param2;
    return result;
}}

// Exemple d'utilisation
const resultat = {func_name}(10, 20);
console.log(`Résultat: ${{resultat}}`);
```"""
        
        elif lang == 'typescript':
            if code_type == 'function':
                func_name = name or 'maFonction'
                return f"""Voici le code généré :

```typescript
function {func_name}(param1: number, param2: number): number {{
    // Fonction générée automatiquement avec type safety
    const result: number = param1 + param2;
    return result;
}}

// Exemple d'utilisation
const resultat: number = {func_name}(10, 20);
console.log(`Résultat: ${{resultat}}`);
```"""
            elif code_type == 'class':
                class_name = name or 'MaClasse'
                return f"""Voici le code généré :

```typescript
class {class_name} {{
    private param1: number;
    private param2: number;
    
    constructor(param1: number, param2: number) {{
        this.param1 = param1;
        this.param2 = param2;
    }}
    
    public methodeExemple(): number {{
        return this.param1 + this.param2;
    }}
    
    public toString(): string {{
        return `{class_name}(${{this.param1}}, ${{this.param2}})`;
    }}
}}

// Exemple d'utilisation
const obj = new {class_name}(10, 20);
console.log(obj.toString());
console.log(obj.methodeExemple());
```"""
        
        elif lang == 'php':
            if code_type == 'function':
                func_name = name or 'maFonction'
                return f"""Voici le code généré :

```php
<?php
function {func_name}($param1, $param2) {{
    // Fonction générée automatiquement
    $result = $param1 + $param2;
    return $result;
}}

// Exemple d'utilisation
$resultat = {func_name}(10, 20);
echo "Résultat: $resultat\\n";
?>
```"""
            elif code_type == 'class':
                class_name = name or 'MaClasse'
                return f"""Voici le code généré :

```php
<?php
class {class_name} {{
    private $param1;
    private $param2;
    
    public function __construct($param1, $param2) {{
        $this->param1 = $param1;
        $this->param2 = $param2;
    }}
    
    public function methodeExemple() {{
        return $this->param1 + $this->param2;
    }}
    
    public function __toString() {{
        return "{class_name}({{$this->param1}}, {{$this->param2}})";
    }}
}}

// Exemple d'utilisation
$obj = new {class_name}(10, 20);
echo $obj . "\\n";
echo $obj->methodeExemple() . "\\n";
?>
```"""
        
        elif lang == 'ruby':
            if code_type == 'function':
                func_name = name or 'ma_fonction'
                return f"""Voici le code généré :

```ruby
def {func_name}(param1, param2)
  # Fonction générée automatiquement
  result = param1 + param2
  result
end

# Exemple d'utilisation
resultat = {func_name}(10, 20)
puts "Résultat: #{{resultat}}"
```"""
            elif code_type == 'class':
                class_name = name or 'MaClasse'
                return f"""Voici le code généré :

```ruby
class {class_name}
  attr_reader :param1, :param2
  
  def initialize(param1, param2)
    @param1 = param1
    @param2 = param2
  end
  
  def methode_exemple
    @param1 + @param2
  end
  
  def to_s
    "{class_name}(#{{@param1}}, #{{@param2}})"
  end
end

# Exemple d'utilisation
obj = {class_name}.new(10, 20)
puts obj
puts obj.methode_exemple
```"""
        
        elif lang == 'go':
            if code_type == 'function':
                func_name = name or 'MaFonction'
                return f"""Voici le code généré :

```go
package main

import "fmt"

func {func_name}(param1 int, param2 int) int {{
    // Fonction générée automatiquement
    result := param1 + param2
    return result
}}

func main() {{
    resultat := {func_name}(10, 20)
    fmt.Printf("Résultat: %d\\n", resultat)
}}
```"""
            elif code_type == 'struct':
                struct_name = name or 'MaStruct'
                return f"""Voici le code généré :

```go
package main

import "fmt"

type {struct_name} struct {{
    Param1 int
    Param2 int
}}

func (s *{struct_name}) MethodeExemple() int {{
    return s.Param1 + s.Param2
}}

func main() {{
    obj := {struct_name}{{Param1: 10, Param2: 20}}
    fmt.Printf("{struct_name}(%d, %d)\\n", obj.Param1, obj.Param2)
    fmt.Printf("Résultat: %d\\n", obj.MethodeExemple())
}}
```"""
        
        elif lang == 'rust':
            if code_type == 'function':
                func_name = name or 'ma_fonction'
                return f"""Voici le code généré :

```rust
fn {func_name}(param1: i32, param2: i32) -> i32 {{
    // Fonction générée automatiquement
    let result = param1 + param2;
    result
}}

fn main() {{
    let resultat = {func_name}(10, 20);
    println!("Résultat: {{}}", resultat);
}}
```"""
            elif code_type == 'struct':
                struct_name = name or 'MaStruct'
                return f"""Voici le code généré :

```rust
struct {struct_name} {{
    param1: i32,
    param2: i32,
}}

impl {struct_name} {{
    fn new(param1: i32, param2: i32) -> Self {{
        {struct_name} {{ param1, param2 }}
    }}
    
    fn methode_exemple(&self) -> i32 {{
        self.param1 + self.param2
    }}
}}

fn main() {{
    let obj = {struct_name}::new(10, 20);
    println!("{struct_name}({{}}, {{}})", obj.param1, obj.param2);
    println!("Résultat: {{}}", obj.methode_exemple());
}}
```"""
        
        elif lang == 'swift':
            if code_type == 'function':
                func_name = name or 'maFonction'
                return f"""Voici le code généré :

```swift
func {func_name}(param1: Int, param2: Int) -> Int {{
    // Fonction générée automatiquement
    let result = param1 + param2
    return result
}}

// Exemple d'utilisation
let resultat = {func_name}(param1: 10, param2: 20)
print("Résultat: \\(resultat)")
```"""
            elif code_type == 'class':
                class_name = name or 'MaClasse'
                return f"""Voici le code généré :

```swift
class {class_name} {{
    var param1: Int
    var param2: Int
    
    init(param1: Int, param2: Int) {{
        self.param1 = param1
        self.param2 = param2
    }}
    
    func methodeExemple() -> Int {{
        return param1 + param2
    }}
}}

// Exemple d'utilisation
let obj = {class_name}(param1: 10, param2: 20)
print("{class_name}(\\(obj.param1), \\(obj.param2))")
print("Résultat: \\(obj.methodeExemple())")
```"""
        
        elif lang == 'kotlin':
            if code_type == 'function':
                func_name = name or 'maFonction'
                return f"""Voici le code généré :

```kotlin
fun {func_name}(param1: Int, param2: Int): Int {{
    // Fonction générée automatiquement
    val result = param1 + param2
    return result
}}

// Exemple d'utilisation
fun main() {{
    val resultat = {func_name}(10, 20)
    println("Résultat: $resultat")
}}
```"""
            elif code_type == 'class':
                class_name = name or 'MaClasse'
                return f"""Voici le code généré :

```kotlin
class {class_name}(private val param1: Int, private val param2: Int) {{
    
    fun methodeExemple(): Int {{
        return param1 + param2
    }}
    
    override fun toString(): String {{
        return "{class_name}($param1, $param2)"
    }}
}}

// Exemple d'utilisation
fun main() {{
    val obj = {class_name}(10, 20)
    println(obj)
    println("Résultat: ${{obj.methodeExemple()}}")
}}
```"""
        
        elif lang == 'c':
            if code_type == 'function':
                func_name = name or 'ma_fonction'
                return f"""Voici le code généré :

```c
#include <stdio.h>

int {func_name}(int param1, int param2) {{
    // Fonction générée automatiquement
    return param1 + param2;
}}

int main() {{
    int resultat = {func_name}(10, 20);
    printf("Résultat: %d\\n", resultat);
    return 0;
}}
```"""
        
        elif lang == 'csharp':
            if code_type == 'class':
                class_name = name or 'MaClasse'
                return f"""Voici le code généré :

```csharp
public class {class_name}
{{
    private int param1;
    private int param2;
    
    public {class_name}(int param1, int param2)
    {{
        this.param1 = param1;
        this.param2 = param2;
    }}
    
    public int MethodeExemple()
    {{
        return param1 + param2;
    }}
}}

// Exemple d'utilisation
var obj = new {class_name}(10, 20);
Console.WriteLine(obj.MethodeExemple());
```"""
        
        elif lang == 'html':
            # Détecte le contexte spécifique du site web demandé
            if any(w in message.lower() for w in ['dropshipping', 'e-commerce', 'ecommerce', 'boutique', 'shop', 'magasin', 'vente']):
                return """Voici le code généré :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma Boutique Dropshipping</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        
        /* Header & Navigation */
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo {
            font-size: 1.8rem;
            font-weight: bold;
        }
        nav ul {
            list-style: none;
            display: flex;
            gap: 2rem;
        }
        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }
        nav a:hover {
            opacity: 0.8;
        }
        .cart-icon {
            position: relative;
            cursor: pointer;
        }
        .cart-count {
            position: absolute;
            top: -8px;
            right: -8px;
            background: #ff4757;
            color: white;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 4rem 2rem;
            text-align: center;
        }
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        .btn {
            padding: 1rem 2rem;
            background: white;
            color: #667eea;
            border: none;
            border-radius: 50px;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.3s;
        }
        .btn:hover {
            transform: scale(1.05);
        }
        
        /* Products Section */
        .products {
            max-width: 1200px;
            margin: 4rem auto;
            padding: 0 2rem;
        }
        .products h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
        }
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }
        .product-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .product-card:hover {
            transform: translateY(-10px);
        }
        .product-image {
            width: 100%;
            height: 250px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 4rem;
        }
        .product-info {
            padding: 1.5rem;
        }
        .product-title {
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
        }
        .product-description {
            color: #666;
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }
        .product-price {
            font-size: 1.5rem;
            color: #667eea;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .old-price {
            text-decoration: line-through;
            color: #999;
            font-size: 1rem;
            margin-left: 0.5rem;
        }
        .btn-add-cart {
            width: 100%;
            padding: 0.8rem;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .btn-add-cart:hover {
            background: #5568d3;
        }
        
        /* Features Section */
        .features {
            background: #f8f9fa;
            padding: 4rem 2rem;
        }
        .features-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }
        .feature {
            text-align: center;
        }
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .feature h3 {
            margin-bottom: 0.5rem;
        }
        
        /* Footer */
        footer {
            background: #333;
            color: white;
            padding: 3rem 2rem 1rem;
        }
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }
        .footer-section h3 {
            margin-bottom: 1rem;
        }
        .footer-section ul {
            list-style: none;
        }
        .footer-section a {
            color: #ccc;
            text-decoration: none;
        }
        .footer-section a:hover {
            color: white;
        }
        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid #555;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            .header-content {
                flex-direction: column;
                gap: 1rem;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="header-content">
            <div class="logo">🛍️ DropShop Pro</div>
            <nav>
                <ul>
                    <li><a href="#accueil">Accueil</a></li>
                    <li><a href="#produits">Produits</a></li>
                    <li><a href="#promo">Promos</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
            <div class="cart-icon">
                🛒
                <span class="cart-count">0</span>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Découvrez nos Produits Tendances</h1>
        <p>Livraison gratuite dès 50€ d'achat • Retours gratuits sous 30 jours</p>
        <button class="btn">Voir la Collection</button>
    </section>

    <!-- Products Section -->
    <section class="products" id="produits">
        <h2>Produits Populaires</h2>
        <div class="product-grid">
            <!-- Product 1 -->
            <div class="product-card">
                <div class="product-image">📱</div>
                <div class="product-info">
                    <h3 class="product-title">Smartphone Premium</h3>
                    <p class="product-description">Écran OLED 6.5", 128GB, Caméra 48MP</p>
                    <div class="product-price">
                        299€
                        <span class="old-price">399€</span>
                    </div>
                    <button class="btn-add-cart" onclick="addToCart('Smartphone Premium', 299)">Ajouter au panier</button>
                </div>
            </div>

            <!-- Product 2 -->
            <div class="product-card">
                <div class="product-image">🎧</div>
                <div class="product-info">
                    <h3 class="product-title">Écouteurs Bluetooth</h3>
                    <p class="product-description">Réduction de bruit active, 30h d'autonomie</p>
                    <div class="product-price">
                        79€
                        <span class="old-price">129€</span>
                    </div>
                    <button class="btn-add-cart" onclick="addToCart('Écouteurs Bluetooth', 79)">Ajouter au panier</button>
                </div>
            </div>

            <!-- Product 3 -->
            <div class="product-card">
                <div class="product-image">⌚</div>
                <div class="product-info">
                    <h3 class="product-title">Montre Connectée</h3>
                    <p class="product-description">Suivi activité, GPS, Étanche</p>
                    <div class="product-price">
                        149€
                        <span class="old-price">249€</span>
                    </div>
                    <button class="btn-add-cart" onclick="addToCart('Montre Connectée', 149)">Ajouter au panier</button>
                </div>
            </div>

            <!-- Product 4 -->
            <div class="product-card">
                <div class="product-image">💻</div>
                <div class="product-info">
                    <h3 class="product-title">Laptop Ultra-Fin</h3>
                    <p class="product-description">Intel i7, 16GB RAM, SSD 512GB</p>
                    <div class="product-price">
                        899€
                        <span class="old-price">1199€</span>
                    </div>
                    <button class="btn-add-cart" onclick="addToCart('Laptop Ultra-Fin', 899)">Ajouter au panier</button>
                </div>
            </div>

            <!-- Product 5 -->
            <div class="product-card">
                <div class="product-image">📷</div>
                <div class="product-info">
                    <h3 class="product-title">Caméra 4K</h3>
                    <p class="product-description">60fps, Stabilisation, WiFi</p>
                    <div class="product-price">
                        399€
                        <span class="old-price">549€</span>
                    </div>
                    <button class="btn-add-cart" onclick="addToCart('Caméra 4K', 399)">Ajouter au panier</button>
                </div>
            </div>

            <!-- Product 6 -->
            <div class="product-card">
                <div class="product-image">🎮</div>
                <div class="product-info">
                    <h3 class="product-title">Console Gaming</h3>
                    <p class="product-description">4K HDR, 1TB, Manette incluse</p>
                    <div class="product-price">
                        449€
                        <span class="old-price">599€</span>
                    </div>
                    <button class="btn-add-cart" onclick="addToCart('Console Gaming', 449)">Ajouter au panier</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="features">
        <div class="features-container">
            <div class="feature">
                <div class="feature-icon">🚚</div>
                <h3>Livraison Rapide</h3>
                <p>Livraison gratuite dès 50€</p>
            </div>
            <div class="feature">
                <div class="feature-icon">💳</div>
                <h3>Paiement Sécurisé</h3>
                <p>100% sécurisé et crypté</p>
            </div>
            <div class="feature">
                <div class="feature-icon">↩️</div>
                <h3>Retours Gratuits</h3>
                <p>30 jours pour changer d'avis</p>
            </div>
            <div class="feature">
                <div class="feature-icon">💬</div>
                <h3>Support 24/7</h3>
                <p>Une équipe à votre écoute</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>À propos</h3>
                <ul>
                    <li><a href="#">Notre histoire</a></li>
                    <li><a href="#">Mentions légales</a></li>
                    <li><a href="#">CGV</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Service Client</h3>
                <ul>
                    <li><a href="#">FAQ</a></li>
                    <li><a href="#">Livraison</a></li>
                    <li><a href="#">Retours</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Mon Compte</h3>
                <ul>
                    <li><a href="#">Connexion</a></li>
                    <li><a href="#">Mes commandes</a></li>
                    <li><a href="#">Mon panier</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Suivez-nous</h3>
                <ul>
                    <li><a href="#">Facebook</a></li>
                    <li><a href="#">Instagram</a></li>
                    <li><a href="#">Twitter</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 DropShop Pro. Tous droits réservés.</p>
        </div>
    </footer>

    <script>
        let cart = [];
        let cartCount = 0;

        function addToCart(productName, price) {
            cart.push({name: productName, price: price});
            cartCount++;
            document.querySelector('.cart-count').textContent = cartCount;
            
            // Animation feedback
            alert(`✅ "${productName}" ajouté au panier!\\nPrix: ${price}€`);
        }

        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({behavior: 'smooth'});
                }
            });
        });
    </script>
</body>
</html>
```"""
            
            elif any(w in message.lower() for w in ['blog', 'article', 'news', 'magazine']):
                return """Voici le code généré :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Blog</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Georgia', serif;
            line-height: 1.8;
            color: #333;
            background: #f8f9fa;
        }
        header {
            background: white;
            padding: 2rem 0;
            border-bottom: 3px solid #667eea;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .blog-title {
            font-size: 2rem;
            color: #667eea;
        }
        nav ul {
            list-style: none;
            display: flex;
            gap: 2rem;
        }
        nav a {
            color: #333;
            text-decoration: none;
            transition: color 0.3s;
        }
        nav a:hover {
            color: #667eea;
        }
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 4rem 2rem;
            text-align: center;
        }
        .container {
            max-width: 1200px;
            margin: 3rem auto;
            padding: 0 2rem;
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 3rem;
        }
        .articles {
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }
        .article-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .article-image {
            width: 100%;
            height: 300px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 5rem;
        }
        .article-content {
            padding: 2rem;
        }
        .article-meta {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        .article-title {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: #333;
        }
        .article-excerpt {
            color: #666;
            margin-bottom: 1.5rem;
        }
        .read-more {
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }
        .sidebar {
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }
        .widget {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .widget h3 {
            margin-bottom: 1rem;
            color: #667eea;
        }
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
        }
        @media (max-width: 768px) {
            .container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1 class="blog-title">📝 Mon Blog</h1>
            <nav>
                <ul>
                    <li><a href="#accueil">Accueil</a></li>
                    <li><a href="#articles">Articles</a></li>
                    <li><a href="#about">À propos</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="hero">
        <h2>Bienvenue sur mon blog</h2>
        <p>Découvrez mes derniers articles et pensées</p>
    </div>

    <div class="container">
        <div class="articles">
            <article class="article-card">
                <div class="article-image">📰</div>
                <div class="article-content">
                    <div class="article-meta">21 novembre 2025 • Par Auteur • 5 min de lecture</div>
                    <h2 class="article-title">Titre de l'article principal</h2>
                    <p class="article-excerpt">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                    </p>
                    <a href="#" class="read-more">Lire la suite →</a>
                </div>
            </article>

            <article class="article-card">
                <div class="article-image">✍️</div>
                <div class="article-content">
                    <div class="article-meta">20 novembre 2025 • Par Auteur • 3 min de lecture</div>
                    <h2 class="article-title">Deuxième article intéressant</h2>
                    <p class="article-excerpt">
                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                    </p>
                    <a href="#" class="read-more">Lire la suite →</a>
                </div>
            </article>
        </div>

        <aside class="sidebar">
            <div class="widget">
                <h3>À propos</h3>
                <p>Bienvenue sur mon blog où je partage mes réflexions et découvertes.</p>
            </div>
            
            <div class="widget">
                <h3>Catégories</h3>
                <ul>
                    <li><a href="#">Technologie</a></li>
                    <li><a href="#">Lifestyle</a></li>
                    <li><a href="#">Voyages</a></li>
                </ul>
            </div>

            <div class="widget">
                <h3>Newsletter</h3>
                <p>Recevez les nouveaux articles par email</p>
                <input type="email" placeholder="Votre email" style="width:100%;padding:0.5rem;margin-top:1rem;">
                <button style="width:100%;padding:0.5rem;margin-top:0.5rem;background:#667eea;color:white;border:none;border-radius:5px;cursor:pointer;">S'abonner</button>
            </div>
        </aside>
    </div>

    <footer>
        <p>&copy; 2025 Mon Blog. Tous droits réservés.</p>
    </footer>
</body>
</html>
```"""
            
            elif any(w in message.lower() for w in ['portfolio', 'cv', 'resume']):
                return """Voici le code généré :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        .hero {
            height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 2rem;
        }
        .hero h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        .hero p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
        }
        section {
            max-width: 1200px;
            margin: 4rem auto;
            padding: 0 2rem;
        }
        h2 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        .skills-grid, .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }
        .skill-card, .project-card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .contact {
            background: #f8f9fa;
            padding: 4rem 2rem;
            text-align: center;
        }
        .btn {
            padding: 1rem 2rem;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="hero">
        <h1>👋 Je suis [Votre Nom]</h1>
        <p>Développeur Full Stack • Designer • Créatif</p>
        <a href="#contact" class="btn">Me contacter</a>
    </div>

    <section id="skills">
        <h2>Mes Compétences</h2>
        <div class="skills-grid">
            <div class="skill-card">
                <h3>💻 Frontend</h3>
                <p>HTML, CSS, JavaScript, React, Vue.js</p>
            </div>
            <div class="skill-card">
                <h3>⚙️ Backend</h3>
                <p>Node.js, Python, PHP, SQL</p>
            </div>
            <div class="skill-card">
                <h3>🎨 Design</h3>
                <p>Figma, Photoshop, UI/UX</p>
            </div>
        </div>
    </section>

    <section id="projects">
        <h2>Mes Projets</h2>
        <div class="projects-grid">
            <div class="project-card">
                <h3>🚀 Projet 1</h3>
                <p>Description du projet et technologies utilisées</p>
            </div>
            <div class="project-card">
                <h3>📱 Projet 2</h3>
                <p>Description du projet et technologies utilisées</p>
            </div>
        </div>
    </section>

    <div class="contact" id="contact">
        <h2>Contactez-moi</h2>
        <p>📧 email@example.com</p>
        <p>💼 LinkedIn • GitHub • Twitter</p>
    </div>
</body>
</html>
```"""
            
            # Détecte le type de contenu HTML demandé
            elif any(w in message.lower() for w in ['complet', 'site', 'page', 'template', 'boilerplate']):
                return """Voici le code généré :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Site Web</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }
        nav {
            background: #333;
            color: white;
            padding: 1rem;
        }
        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 2rem;
        }
        nav a {
            color: white;
            text-decoration: none;
        }
        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        section {
            margin: 2rem 0;
            padding: 2rem;
            background: #f4f4f4;
            border-radius: 8px;
        }
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 1rem;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>Bienvenue sur Mon Site</h1>
        <p>Un site web moderne et élégant</p>
    </header>
    
    <nav>
        <ul>
            <li><a href="#accueil">Accueil</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <main>
        <section id="accueil">
            <h2>À propos</h2>
            <p>Ceci est un template de site web généré automatiquement. Personnalisez-le selon vos besoins !</p>
        </section>
        
        <section id="services">
            <h2>Nos Services</h2>
            <ul>
                <li>Service 1 : Description du service</li>
                <li>Service 2 : Description du service</li>
                <li>Service 3 : Description du service</li>
            </ul>
        </section>
        
        <section id="contact">
            <h2>Contact</h2>
            <form>
                <p><input type="text" placeholder="Votre nom" style="width:100%;padding:0.5rem;margin:0.5rem 0;"></p>
                <p><input type="email" placeholder="Votre email" style="width:100%;padding:0.5rem;margin:0.5rem 0;"></p>
                <p><textarea placeholder="Votre message" style="width:100%;padding:0.5rem;margin:0.5rem 0;height:100px;"></textarea></p>
                <p><button type="submit" style="padding:0.7rem 2rem;background:#667eea;color:white;border:none;border-radius:4px;cursor:pointer;">Envoyer</button></p>
            </form>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 Mon Site Web. Tous droits réservés.</p>
    </footer>
</body>
</html>
```"""
            elif any(w in message.lower() for w in ['formulaire', 'form', 'contact']):
                return r"""Voici le code généré :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire de Contact</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }
        .contact-container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
            padding: 3rem;
            animation: slideIn 0.5s ease-out;
        }
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .contact-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .contact-header h1 {
            color: #667eea;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        .contact-header p {
            color: #666;
            font-size: 1.1rem;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            color: #333;
            font-weight: 600;
            margin-bottom: 0.5rem;
            font-size: 1rem;
        }
        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 1rem;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1rem;
            font-family: inherit;
            transition: all 0.3s;
            background: #f8f9fa;
        }
        .form-group input:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            outline: none;
            border-color: #667eea;
            background: white;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }
        .form-group .input-icon {
            position: relative;
        }
        .form-group .input-icon input {
            padding-left: 3rem;
        }
        .form-group .input-icon::before {
            content: attr(data-icon);
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            font-size: 1.2rem;
            color: #667eea;
        }
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }
        .submit-btn {
            width: 100%;
            padding: 1.2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }
        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }
        .submit-btn:active {
            transform: translateY(0);
        }
        .error-message {
            color: #dc3545;
            font-size: 0.9rem;
            margin-top: 0.3rem;
            display: none;
        }
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            display: none;
            animation: slideIn 0.3s ease-out;
        }
        .contact-info {
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 2px solid #e0e0e0;
            text-align: center;
        }
        .contact-info p {
            color: #666;
            margin: 0.5rem 0;
        }
        .contact-info a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }
        .contact-info a:hover {
            text-decoration: underline;
        }
        @media (max-width: 768px) {
            .contact-container {
                padding: 2rem 1.5rem;
            }
            .contact-header h1 {
                font-size: 2rem;
            }
            .form-row {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="contact-container">
        <div class="contact-header">
            <h1>📧 Contactez-nous</h1>
            <p>Nous sommes là pour vous aider !</p>
        </div>

        <div class="success-message" id="successMessage">
            ✅ Votre message a été envoyé avec succès ! Nous vous répondrons dans les plus brefs délais.
        </div>

        <form id="contactForm" onsubmit="handleSubmit(event)">
            <div class="form-row">
                <div class="form-group">
                    <label for="prenom">Prénom *</label>
                    <div class="input-icon" data-icon="👤">
                        <input type="text" id="prenom" name="prenom" placeholder="Votre prénom" required>
                    </div>
                    <span class="error-message" id="prenomError">Veuillez entrer votre prénom</span>
                </div>

                <div class="form-group">
                    <label for="nom">Nom *</label>
                    <div class="input-icon" data-icon="👤">
                        <input type="text" id="nom" name="nom" placeholder="Votre nom" required>
                    </div>
                    <span class="error-message" id="nomError">Veuillez entrer votre nom</span>
                </div>
            </div>

            <div class="form-group">
                <label for="email">Email *</label>
                <div class="input-icon" data-icon="✉️">
                    <input type="email" id="email" name="email" placeholder="votre.email@exemple.com" required>
                </div>
                <span class="error-message" id="emailError">Veuillez entrer un email valide</span>
            </div>

            <div class="form-group">
                <label for="telephone">Téléphone</label>
                <div class="input-icon" data-icon="📱">
                    <input type="tel" id="telephone" name="telephone" placeholder="06 12 34 56 78">
                </div>
            </div>

            <div class="form-group">
                <label for="sujet">Sujet *</label>
                <select id="sujet" name="sujet" required>
                    <option value="">-- Sélectionnez un sujet --</option>
                    <option value="information">Demande d'information</option>
                    <option value="support">Support technique</option>
                    <option value="commercial">Question commerciale</option>
                    <option value="partenariat">Opportunité de partenariat</option>
                    <option value="autre">Autre</option>
                </select>
                <span class="error-message" id="sujetError">Veuillez sélectionner un sujet</span>
            </div>

            <div class="form-group">
                <label for="message">Message *</label>
                <textarea id="message" name="message" placeholder="Décrivez votre demande en détail..." required></textarea>
                <span class="error-message" id="messageError">Veuillez entrer votre message</span>
            </div>

            <button type="submit" class="submit-btn">
                📤 Envoyer le message
            </button>
        </form>

        <div class="contact-info">
            <p><strong>Autres moyens de nous contacter :</strong></p>
            <p>📧 Email : <a href="mailto:contact@exemple.com">contact@exemple.com</a></p>
            <p>📞 Téléphone : <a href="tel:+33612345678">+33 6 12 34 56 78</a></p>
            <p>📍 Adresse : 123 Rue de la Paix, 75001 Paris</p>
        </div>
    </div>

    <script>
        function handleSubmit(event) {
            event.preventDefault();
            
            // Validation
            const form = event.target;
            const formData = new FormData(form);
            let isValid = true;

            // Vérifier tous les champs requis
            ['prenom', 'nom', 'email', 'sujet', 'message'].forEach(field => {
                const value = formData.get(field);
                const errorElement = document.getElementById(field + 'Error');
                
                if (!value || value.trim() === '') {
                    errorElement.style.display = 'block';
                    isValid = false;
                } else {
                    errorElement.style.display = 'none';
                }
            });

            // Validation email
            const email = formData.get('email');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (email && !emailRegex.test(email)) {
                document.getElementById('emailError').textContent = 'Email invalide';
                document.getElementById('emailError').style.display = 'block';
                isValid = false;
            }

            if (isValid) {
                // Afficher le message de succès
                document.getElementById('successMessage').style.display = 'block';
                
                // Réinitialiser le formulaire
                form.reset();
                
                // Cacher le message après 5 secondes
                setTimeout(() => {
                    document.getElementById('successMessage').style.display = 'none';
                }, 5000);

                // Ici, vous pouvez ajouter l'envoi réel des données :
                // fetch('/api/contact', {
                //     method: 'POST',
                //     body: formData
                // }).then(response => response.json())
                //   .then(data => console.log(data));
            }
        }

        // Supprimer les messages d'erreur lorsque l'utilisateur commence à taper
        document.querySelectorAll('input, textarea, select').forEach(element => {
            element.addEventListener('input', function() {
                const errorElement = document.getElementById(this.id + 'Error');
                if (errorElement) {
                    errorElement.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>
```"""
            else:
                return """Voici le code généré :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma Page</title>
</head>
<body>
    <h1>Titre de la page</h1>
    <p>Contenu de la page.</p>
</body>
</html>
```"""
        
        elif lang == 'css':
            return """Voici le code généré :

```css
/* Styles de base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

/* Centrer un élément */
.centered {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Bouton stylisé */
.btn {
    padding: 0.7rem 2rem;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background 0.3s;
}

.btn:hover {
    background: #5568d3;
}
```"""
        
        elif lang == 'sql':
            if 'select' in message.lower():
                return """Voici le code généré :

```sql
SELECT * FROM ma_table 
WHERE colonne1 = 'valeur' 
ORDER BY colonne2 DESC;
```"""
            elif 'insert' in message.lower():
                return """Voici le code généré :

```sql
INSERT INTO ma_table (colonne1, colonne2, colonne3) 
VALUES ('valeur1', 'valeur2', 'valeur3');
```"""
            else:
                return """Voici le code généré :

```sql
-- Création de table
CREATE TABLE ma_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertion de données
INSERT INTO ma_table (nom, email) VALUES ('Jean Dupont', 'jean@example.com');

-- Sélection
SELECT * FROM ma_table WHERE nom LIKE '%Dupont%';
```"""
        
        return f"Je comprends que tu veux du code en {lang}. Précise si tu veux une fonction, une classe, ou un type spécifique de code. Je supporte maintenant Python, JavaScript, TypeScript, PHP, Ruby, Go, Rust, Swift, Kotlin, C, C#, Java, HTML, CSS, SQL et Bash !"
    
    def _suggest_language_or_generate(self, message: str, code_type: str, intent: str) -> str:
        """Suggère un langage ou génère du code en devinant le meilleur langage."""
        msg_lower = message.lower()
        
        # Devine le langage selon le contexte
        suggested_lang = None
        
        # Contexte web
        if any(w in msg_lower for w in ['site', 'page', 'web', 'html', 'css', 'frontend']):
            suggested_lang = 'html'
            return self._synthesize_code_from_scratch(message, 'html', code_type or 'website', None, intent)
        
        # Contexte backend/API
        elif any(w in msg_lower for w in ['api', 'serveur', 'server', 'backend', 'base de données']):
            suggested_lang = 'python'
            return f"""Je suppose que tu veux du Python pour le backend. Voici un exemple :

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    \"\"\"Endpoint pour récupérer des données\"\"\"
    return jsonify({{'status': 'success', 'data': []}})

@app.route('/api/data', methods=['POST'])
def post_data():
    \"\"\"Endpoint pour créer des données\"\"\"
    data = request.get_json()
    return jsonify({{'status': 'success', 'message': 'Données créées'}}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

💡 **Si tu veux un autre langage, précise-le :**
- "api javascript" → Node.js/Express
- "api php" → PHP
- "api c#" → ASP.NET
"""
        
        # Contexte mobile
        elif any(w in msg_lower for w in ['mobile', 'app mobile', 'android']):
            return """💡 **Pour une app mobile, précise la plateforme :**

- **Android** → "app android kotlin" ou "app android java"
- **iOS** → "app ios swift"
- **Cross-platform** → "app react native" ou "app flutter"

Exemple : "crée une app android kotlin"
"""
        
        # Contexte algorithme/calcul
        elif any(w in msg_lower for w in ['algorithme', 'calcul', 'trier', 'chercher', 'search']):
            suggested_lang = 'python'
            return f"""Je suppose que tu veux du Python pour l'algorithme. Voici un exemple :

```python
def mon_algorithme(data):
    \"\"\"
    Algorithme généré automatiquement.
    Adapte selon tes besoins.
    \"\"\"
    result = []
    for item in data:
        # Ton traitement ici
        processed = item * 2
        result.append(processed)
    return result

# Exemple d'utilisation
if __name__ == "__main__":
    donnees = [1, 2, 3, 4, 5]
    result = mon_algorithme(donnees)
    print(f"Résultat: {result}")
```

💡 **Si tu veux un autre langage, précise-le :**
- "algorithme javascript"
- "algorithme c"
- "algorithme java"
"""
        
        # Cas général - proposer Python par défaut
        else:
            return f"""💡 **Je peux générer du code dans 15+ langages !**

**Précise le langage ou le contexte :**

🌐 **Web :**
- "site web html" → Site complet HTML/CSS
- "page javascript" → Code JavaScript

💻 **Backend :**
- "api python" → API REST Python/Flask
- "serveur node" → Serveur Node.js
- "api php" → API PHP

📱 **Mobile :**
- "app android kotlin"
- "app ios swift"

🔢 **Algorithmes :**
- "fonction python qui..."
- "algorithme c pour..."

**Exemples de phrases naturelles que je comprends :**
- "peux-tu me faire une fonction python qui trie une liste ?"
- "j'ai besoin d'un site e-commerce html"
- "crée-moi une API REST pour gérer des utilisateurs"
- "aide-moi à faire un calculateur en javascript"

**Dis-moi ce que tu veux et je le code pour toi ! 🚀**
"""
    
    def _generate_default_name(self, lang: str, code_type: str) -> str:
        if code_type == 'class':
            return 'MaClasse' if lang in ['csharp', 'java'] else 'ma_classe'
        return 'ma_fonction' if lang == 'python' else 'maFonction'
    
    def _generate_default_args(self, lang: str) -> str:
        if lang == 'python':
            return 'param1, param2'
        elif lang in ['c', 'java']:
            return 'int param1, int param2'
        else:
            return 'param1, param2'
    
    def _generate_body_from_request(self, message: str, lang: str, code_type: str) -> str:
        """Génère le corps de fonction basé sur la demande."""
        if 'addition' in message.lower() or 'additionner' in message.lower() or 'somme' in message.lower():
            if lang == 'python':
                return '    return param1 + param2'
            else:
                return '    return param1 + param2;'
        elif 'multiplication' in message.lower() or 'multiplier' in message.lower():
            if lang == 'python':
                return '    return param1 * param2'
            else:
                return '    return param1 * param2;'
        else:
            if lang == 'python':
                return '    # Votre logique ici\n    pass'
            else:
                return '    // Votre logique ici'
    
    def _extract_or_default(self, message: str, placeholder: str) -> str:
        defaults = {
            'url': 'https://api.example.com/data',
            'filename': 'fichier.txt',
            'content': "'Contenu du fichier'",
            'table': 'ma_table',
            'colonne': 'colonne1',
            'colonnes': 'col1, col2, col3',
            'valeur': 'valeur1',
            'valeurs': "'val1', 'val2', 'val3'",
            'pattern': '*.txt'
        }
        return defaults.get(placeholder, 'valeur')

    def _code_template_score(self, message: str) -> float:
        """Score si la demande correspond à un template de génération de code."""
        for key, tpl in CODE_TEMPLATES.items():
            for pattern in tpl["patterns"]:
                if _similarity(message, pattern) > 0.7:
                    return 1.0
        return 0.0

    def _generate_code_from_template(self, message: str) -> str:
        """Génère du code à partir d'un template si possible, en utilisant l'analyse intelligente pour remplir les paramètres."""
        best_template = None
        best_score = 0.0
        best_key = ""
        
        # Trouve le meilleur template
        for key, tpl in CODE_TEMPLATES.items():
            for pattern in tpl["patterns"]:
                score = _similarity(message, pattern)
                if score > best_score:
                    best_score = score
                    best_template = tpl
                    best_key = key
        
        if not best_template or best_score < 0.3:
            return "Je n'ai pas de template pour cette demande. Précise le langage et le type de code souhaité, ou essaie : 'fonction python', 'calculatrice c', 'classe c#', etc."
        
        # Extrait les informations du message pour remplir le template
        template_str = best_template["template"]
        
        # Détecte les placeholders dans le template
        placeholders = re.findall(r'\{(\w+)\}', template_str)
        
        # Valeurs par défaut intelligentes
        values = {}
        
        # Extraction intelligente du nom
        if '{name}' in template_str:
            # Cherche un nom dans le message (mot après "appelée", "nommée", etc.)
            name_match = re.search(r'(?:appelée?|nommée?|name|called)\s+(\w+)', message, re.IGNORECASE)
            if name_match:
                values['name'] = name_match.group(1)
            else:
                # Nom par défaut selon le type
                if 'python' in best_key.lower():
                    values['name'] = 'ma_fonction'
                elif 'c' in best_key.lower() and 'sharp' not in best_key.lower():
                    values['name'] = 'ma_fonction'
                elif 'csharp' in best_key.lower() or 'c#' in best_key.lower():
                    values['name'] = 'MaClasse'
                elif 'js' in best_key.lower() or 'javascript' in best_key.lower():
                    values['name'] = 'maFonction'
                else:
                    values['name'] = 'monElement'
        
        # Arguments
        if '{args}' in template_str:
            if 'python' in best_key.lower():
                values['args'] = 'param1, param2'
            elif 'c' in best_key.lower():
                values['args'] = 'int a, int b'
            elif 'js' in best_key.lower():
                values['args'] = 'param1, param2'
            else:
                values['args'] = 'param1, param2'
        
        # Body/contenu
        if '{body}' in template_str:
            if 'python' in best_key.lower():
                values['body'] = '    # Votre code ici\n    pass'
            elif 'c' in best_key.lower():
                values['body'] = '    // Votre code ici\n    return 0;'
            elif 'csharp' in best_key.lower():
                values['body'] = '    // Votre code ici'
            elif 'js' in best_key.lower():
                values['body'] = '    // Votre code ici'
            elif 'html' in best_key.lower():
                values['body'] = '    <h1>Contenu</h1>'
            else:
                values['body'] = '    // Code'
        
        # Autres placeholders courants
        if '{url}' in template_str:
            values['url'] = 'https://api.example.com/data'
        if '{filename}' in template_str:
            values['filename'] = 'fichier.txt'
        if '{content}' in template_str:
            values['content'] = "'Contenu du fichier'"
        if '{table}' in template_str:
            values['table'] = 'ma_table'
        if '{colonne}' in template_str or '{colonnes}' in template_str:
            values['colonne'] = 'colonne1'
            values['colonnes'] = 'col1, col2, col3'
        if '{valeur}' in template_str or '{valeurs}' in template_str:
            values['valeur'] = 'valeur1'
            values['valeurs'] = "'val1', 'val2', 'val3'"
        if '{pattern}' in template_str:
            values['pattern'] = '*.txt'
        
        # Remplit le template
        try:
            result = template_str.format(**values)
            return f"Voici le code généré :\n\n```\n{result}\n```"
        except KeyError as e:
            # Si un placeholder manque, retourne le template brut
            return f"Template trouvé (score: {best_score:.2f}) :\n\n```\n{template_str}\n```\n\nRemplace les {{placeholders}} par tes valeurs."
        # Salutations multilingues
        self.add_rule(
            "salutation_fr",
            lambda msg, lang: 1.0 if re.search(r"\b(bonjour|salut|coucou)\b", msg, re.IGNORECASE) and lang == "fr" else 0.0,
            lambda msg, lang: "Bonjour ! Comment puis-je vous aider ?",
            lang="fr"
        )
        self.add_rule(
            "salutation_en",
            lambda msg, lang: 1.0 if re.search(r"\b(hello|hi|hey)\b", msg, re.IGNORECASE) and lang == "en" else 0.0,
            lambda msg, lang: "Hello! How can I help you?",
            lang="en"
        )
        # Demande d'aide
        self.add_rule(
            "demande_aide",
            lambda msg, lang: 0.9 if re.search(r"aide|help", msg, re.IGNORECASE) else 0.0,
            lambda msg, lang: "Voici comment je peux vous aider... (documentation, support, etc.)" if lang == "fr" else "Here is how I can help you... (documentation, support, etc.)"
        )
        # Question
        self.add_rule(
            "question",
            lambda msg, lang: 0.8 if msg.strip().endswith("?") else 0.0,
            lambda msg, lang: "C'est une excellente question. Je vais y réfléchir." if lang == "fr" else "That's a great question. I'll think about it."
        )
        # Motivation
        self.add_rule(
            "motivation",
            lambda msg, lang: 0.7 if re.search(r"(courage|force|motivation|bravo|success)", msg, re.IGNORECASE) else 0.0,
            lambda msg, lang: "Vous êtes capable de grandes choses !" if lang == "fr" else "You are capable of great things!"
        )
        # Remerciement
        self.add_rule(
            "remerciement",
            lambda msg, lang: 0.7 if re.search(r"merci|thanks|thank you", msg, re.IGNORECASE) else 0.0,
            lambda msg, lang: "Avec plaisir ! N'hésitez pas si besoin." if lang == "fr" else "You're welcome! Let me know if you need anything."
        )
        # Fallback humoristique
        self.add_rule(
            "humour",
            lambda msg, lang: 0.5 if re.search(r"(blague|joke|rigole)", msg, re.IGNORECASE) else 0.0,
            lambda msg, lang: "Pourquoi les programmeurs confondent Halloween et Noël ? Parce que OCT 31 == DEC 25 !"
        )

    def add_rule(self, name: str, condition: Callable[[str, str], float], action: Callable[[str, str], str], lang: str = "any"):
        self.rules.append(Rule(name, condition, action, lang))

    def detect_language(self, message: str) -> str:
        # Détection très légère, extensible (fr/en)
        if re.search(r"\b(bonjour|salut|aide|merci|pourquoi|comment)\b", message, re.IGNORECASE):
            return "fr"
        if re.search(r"\b(hello|hi|help|thanks|why|how)\b", message, re.IGNORECASE):
            return "en"
        # Par défaut français
        return "fr"

    def analyse(self, message: str) -> IAResponse:
        """
        Analyse enrichie avec mémoire, analyse de code, suggestions proactives et multi-fichiers.
        """
        logging.info(f"Analyse du message: {message}")
        if not message or not message.strip():
            return IAResponse("error", "Message vide.", meta={"timestamp": datetime.datetime.utcnow().isoformat()})
        
        lang = self.detect_language(message)
        msg_lower = message.lower()
        
        # === NOUVELLE FONCTIONNALITÉ 1: Mémoire de conversation ===
        # Analyser l'intention avec le contexte des messages précédents
        intent_analysis = self.memory.analyze_user_intent(message)
        context = self.memory.get_context()
        
        # Ajouter le message utilisateur à la mémoire
        metadata = {
            'language': lang,
            'is_followup': intent_analysis.get('is_followup'),
            'refers_to_previous': intent_analysis.get('refers_to_previous')
        }
        self.memory.add_message('user', message, metadata)
        
        # === NOUVELLE FONCTIONNALITÉ 2: Analyse de code existant ===
        # Détecter si l'utilisateur montre du code à analyser/améliorer
        code_blocks = re.findall(r'```[\s\S]*?```', message)
        if code_blocks:
            # Extraire le code
            code = code_blocks[0].replace('```', '').strip()
            # Analyser le code
            analysis = self.code_analyzer.analyze_code(code)
            improvements = self.code_analyzer.suggest_improvements(code)
            
            # Construire la réponse
            response = f"## 🔍 Analyse de votre code\n\n"
            response += f"**Langage détecté**: {analysis['language']}\n"
            response += f"**Lignes**: {analysis['lines_count']}\n"
            response += f"**Complexité**: {analysis['complexity']}\n\n"
            
            if analysis['structure']['functions']:
                response += f"**Fonctions trouvées**: {', '.join(analysis['structure']['functions'])}\n"
            if analysis['structure']['classes']:
                response += f"**Classes trouvées**: {', '.join(analysis['structure']['classes'])}\n"
            
            response += "\n### 💡 Suggestions d'amélioration\n\n"
            for i, improvement in enumerate(improvements[:5], 1):
                response += f"**{i}. {improvement['issue']}**\n"
                response += f"Priorité: {improvement['priority']}\n"
                response += f"```\n{improvement['example']}\n```\n\n"
            
            # Sauvegarder dans la mémoire
            self.memory.add_message('assistant', response, {
                'language': analysis['language'],
                'code_type': 'analysis',
                'issues_count': len(analysis.get('issues', []))
            })
            
            return IAResponse("ok", response, meta={
                "rule": "code_analysis",
                "language": analysis['language'],
                "complexity": analysis['complexity'],
                "timestamp": datetime.datetime.utcnow().isoformat()
            })
        
        # === NOUVELLE FONCTIONNALITÉ 3: Réponse aux suggestions précédentes ===
        # Si l'utilisateur répond à une suggestion
        if self.previous_suggestions:
            chosen_suggestion = self.suggester.detect_user_choice(message, self.previous_suggestions)
            if chosen_suggestion:
                # Générer le code pour la suggestion choisie
                response = f"## ✅ {chosen_suggestion['title']}\n\n"
                response += f"{chosen_suggestion['description']}\n\n"
                response += f"```\n{chosen_suggestion['code_example']}\n```"
                
                self.memory.add_message('assistant', response, {'suggestion_chosen': chosen_suggestion['title']})
                self.previous_suggestions = []  # Reset
                
                return IAResponse("ok", response, meta={
                    "rule": "suggestion_response",
                    "suggestion": chosen_suggestion['title'],
                    "timestamp": datetime.datetime.utcnow().isoformat()
                })
        
        # === NOUVELLE FONCTIONNALITÉ 4: Génération multi-fichiers ===
        # Détecter si c'est une demande de projet complet
        multi_file_keywords = [
            'projet complet', 'complete project', 'architecture', 'structure complète',
            'api complète', 'full stack', 'avec tous les fichiers', 'microservices'
        ]
        
        if any(keyword in msg_lower for keyword in multi_file_keywords):
            project_type = self.multi_file_gen.detect_project_type(message)
            project = self.multi_file_gen.generate_project(project_type)
            
            if 'error' not in project:
                # Construire la réponse avec tous les fichiers
                response = f"## 📁 {project['name']}\n\n"
                response += f"{project['description']}\n\n"
                response += "### 📂 Structure du projet\n\n"
                
                for filepath in project['files'].keys():
                    response += f"- `{filepath}`\n"
                
                response += f"\n### 📄 Fichiers générés\n\n"
                
                for filepath, content in project['files'].items():
                    response += f"**{filepath}**\n```\n{content[:500]}...\n```\n\n"
                
                response += f"\n{project['instructions']}"
                
                self.memory.add_message('assistant', response, {
                    'code_type': 'multi_file_project',
                    'project_type': project_type,
                    'files_count': len(project['files'])
                })
                
                return IAResponse("ok", response, meta={
                    "rule": "multi_file_generation",
                    "project_type": project_type,
                    "files_count": len(project['files']),
                    "timestamp": datetime.datetime.utcnow().isoformat()
                })
        
        # === LOGIQUE CLASSIQUE ===
        # 1. Cherche d'abord dans la mémoire utilisateur
        user_code = find_best_user_example(message)
        if user_code:
            self.memory.add_message('assistant', user_code, {'source': 'user_example'})
            return IAResponse("ok", user_code, meta={
                "rule": "user_example",
                "score": 1.0,
                "lang": lang,
                "timestamp": datetime.datetime.utcnow().isoformat()
            })
        
        # 2. Applique les règles classiques
        best_score = 0.0
        best_rule = None
        for rule in self.rules:
            if rule.lang == "any" or rule.lang == lang:
                score = rule.condition(message, lang)
                if score > best_score:
                    best_score = score
                    best_rule = rule
        
        if best_rule and best_score > 0.0:
            response = best_rule.action(message, lang)
            
            # Analyser le contexte pour les suggestions
            analysis_context = self._analyze_context(message)
            analysis_context['message'] = message
            
            # === NOUVELLE FONCTIONNALITÉ 3 (suite): Suggestions proactives ===
            # Générer des suggestions après avoir fourni le code
            suggestions = self.suggester.generate_suggestions(analysis_context)
            if suggestions:
                response += self.suggester.format_suggestions_message(suggestions)
                self.previous_suggestions = suggestions
            
            # Sauvegarder la réponse dans la mémoire
            response_metadata = {
                'language': analysis_context.get('language'),
                'code_type': analysis_context.get('code_type'),
                'domain': analysis_context.get('domain'),
                'intent': analysis_context.get('intent')
            }
            self.memory.add_message('assistant', response, response_metadata)
            
            return IAResponse("ok", response, meta={
                "rule": best_rule.name,
                "score": best_score,
                "lang": lang,
                "suggestions_count": len(suggestions),
                "timestamp": datetime.datetime.utcnow().isoformat()
            })
        
        # Fallback avec sauvegarde mémoire
        fallback_response = "Message reçu. Comment puis-je vous aider ?"
        self.memory.add_message('assistant', fallback_response, {})
        
        return IAResponse("ok", fallback_response, meta={
            "rule": "default",
            "score": 0.0,
            "lang": lang,
            "timestamp": datetime.datetime.utcnow().isoformat()
        })

# Instance globale du moteur IA
engine = NamzIAEngine()

def analyse_texte(message: str) -> dict:
    """
    Interface unique pour l'API Flask avec optimisations avancées.
    
    Fonctionnalités:
    - ⚡ Cache LRU intelligent (réponses instantanées)
    - 🛡️ Circuit breaker (protection surcharge)
    - 📊 Métriques temps réel
    - 🔄 Fallback V2 → V1 automatique
    """
    start_time = time.time()
    
    # 1. Vérifier le cache (réponse instantanée si trouvée)
    cached_response = _cache.get(message)
    if cached_response:
        duration = time.time() - start_time
        logger.info(f"✓ Cache HIT ({duration:.4f}s)")
        
        # Ajouter métadonnée cache
        cached_response['meta']['from_cache'] = True
        cached_response['meta']['response_time'] = f'{duration:.4f}s'
        
        return cached_response
    
    logger.info(f"⚠ Cache MISS - Processing request")
    
    try:
        # 2. Utiliser le circuit breaker pour éviter surcharge
        def _process_request():
            # Tentative d'utilisation du moteur V2
            if USE_ENGINE_V2:
                try:
                    from .ia_engine_v2 import get_engine_v2
                    engine_v2 = get_engine_v2()
                    result = engine_v2.analyse(message)
                    
                    logger.info(f"✓ Engine V2 used")
                    return result.to_dict(), 'V2'
                
                except Exception as e:
                    logger.warning(f"Engine V2 failed, falling back to V1: {e}")
            
            # Moteur V1 (legacy, toujours disponible)
            result = engine.analyse(message)
            logger.info(f"✓ Engine V1 used")
            return result.to_dict(), 'V1'
        
        # Exécuter avec circuit breaker
        response, engine_version = _circuit_breaker.call(_process_request)
        
        # 3. Enrichir la réponse avec métriques
        duration = time.time() - start_time
        
        response['meta']['engine'] = engine_version
        response['meta']['response_time'] = f'{duration:.4f}s'
        response['meta']['from_cache'] = False
        response['meta']['timestamp'] = time.time()
        
        # 4. Enregistrer métriques
        rule_name = response['meta'].get('rule', 'unknown')
        _metrics.record(duration, rule_name)
        
        # 5. Mettre en cache pour futures requêtes similaires
        _cache.set(message, response)
        
        logger.info(f"✓ Request processed in {duration:.4f}s (engine={engine_version}, rule={rule_name})")
        
        return response
    
    except Exception as e:
        # Gestion d'erreur avec fallback gracieux
        duration = time.time() - start_time
        
        logger.error(f"✗ Error processing request: {e}", exc_info=True)
        
        return {
            'status': 'error',
            'response': f"Désolé, une erreur est survenue: {str(e)}",
            'meta': {
                'error': str(e),
                'response_time': f'{duration:.4f}s',
                'timestamp': time.time()
            }
        }

def get_engine_stats() -> dict:
    """
    Récupère les statistiques complètes du moteur IA.
    
    Utilisé pour monitoring et diagnostics.
    """
    return {
        'cache': _cache.stats(),
        'circuit_breaker': _circuit_breaker.status(),
        'performance': _metrics.stats(),
        'engine_version': 'V2' if USE_ENGINE_V2 else 'V1',
        'uptime': 'N/A'  # TODO: calculer uptime
    }

def reset_engine_stats():
    """Réinitialise toutes les statistiques."""
    _cache.clear()
    _metrics.reset()
    logger.info("✓ Engine stats reset")
