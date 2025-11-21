"""
Système de suggestions proactives pour Namz IA
Propose automatiquement des améliorations et fonctionnalités
"""

from typing import Dict, List, Optional

class ProactiveSuggester:
    """Génère des suggestions proactives basées sur le contexte."""
    
    def __init__(self):
        self.suggestion_rules = self._initialize_rules()
    
    def _initialize_rules(self) -> Dict:
        """Initialise les règles de suggestions."""
        return {
            'web': {
                'triggers': ['html', 'site', 'page', 'web'],
                'suggestions': [
                    {
                        'title': 'Ajouter du CSS',
                        'description': 'Veux-tu que j\'ajoute du style CSS pour rendre le site plus beau ?',
                        'code_example': 'CSS avec design moderne et responsive'
                    },
                    {
                        'title': 'Ajouter JavaScript',
                        'description': 'Je peux ajouter des interactions JavaScript (menus, animations, etc.) ?',
                        'code_example': 'JavaScript pour interactivité'
                    },
                    {
                        'title': 'Version responsive',
                        'description': 'Veux-tu une version responsive pour mobile et tablette ?',
                        'code_example': 'Media queries et design adaptatif'
                    },
                    {
                        'title': 'Formulaire de contact',
                        'description': 'Tu veux que j\'ajoute un formulaire de contact fonctionnel ?',
                        'code_example': 'Formulaire avec validation'
                    }
                ]
            },
            'api': {
                'triggers': ['api', 'rest', 'endpoint', 'backend'],
                'suggestions': [
                    {
                        'title': 'Authentification JWT',
                        'description': 'Veux-tu que j\'ajoute l\'authentification JWT pour sécuriser l\'API ?',
                        'code_example': 'JWT avec login/logout'
                    },
                    {
                        'title': 'Validation des données',
                        'description': 'Je peux ajouter la validation des entrées avec des schémas ?',
                        'code_example': 'Validation avec marshmallow ou pydantic'
                    },
                    {
                        'title': 'Documentation Swagger',
                        'description': 'Tu veux une documentation Swagger automatique de l\'API ?',
                        'code_example': 'Configuration Swagger/OpenAPI'
                    },
                    {
                        'title': 'Tests unitaires',
                        'description': 'Veux-tu que je génère des tests unitaires pour l\'API ?',
                        'code_example': 'Tests avec pytest ou unittest'
                    },
                    {
                        'title': 'Gestion d\'erreurs',
                        'description': 'Je peux ajouter une gestion d\'erreurs robuste avec codes HTTP ?',
                        'code_example': 'Error handlers personnalisés'
                    }
                ]
            },
            'database': {
                'triggers': ['database', 'db', 'sql', 'mongodb', 'données'],
                'suggestions': [
                    {
                        'title': 'Migrations',
                        'description': 'Veux-tu un système de migrations pour gérer les changements de schéma ?',
                        'code_example': 'Alembic ou Flask-Migrate'
                    },
                    {
                        'title': 'Relations',
                        'description': 'Je peux définir les relations entre les tables (OneToMany, ManyToMany) ?',
                        'code_example': 'Relations SQLAlchemy'
                    },
                    {
                        'title': 'Seeders',
                        'description': 'Tu veux des données de test pour remplir la base ?',
                        'code_example': 'Scripts de seeding'
                    }
                ]
            },
            'function': {
                'triggers': ['fonction', 'function', 'def', 'method'],
                'suggestions': [
                    {
                        'title': 'Tests unitaires',
                        'description': 'Veux-tu que je crée des tests pour cette fonction ?',
                        'code_example': 'Tests avec assertions'
                    },
                    {
                        'title': 'Documentation',
                        'description': 'Je peux ajouter une docstring détaillée ?',
                        'code_example': 'Docstring format Google ou NumPy'
                    },
                    {
                        'title': 'Gestion d\'erreurs',
                        'description': 'Tu veux que j\'ajoute la gestion d\'erreurs (try/except) ?',
                        'code_example': 'Try/except avec messages clairs'
                    },
                    {
                        'title': 'Validation des entrées',
                        'description': 'Je peux valider les paramètres d\'entrée ?',
                        'code_example': 'Validation avec assertions ou type hints'
                    }
                ]
            },
            'ecommerce': {
                'triggers': ['ecommerce', 'boutique', 'shop', 'dropshipping'],
                'suggestions': [
                    {
                        'title': 'Système de paiement',
                        'description': 'Veux-tu intégrer Stripe ou PayPal pour les paiements ?',
                        'code_example': 'Intégration Stripe/PayPal'
                    },
                    {
                        'title': 'Gestion du panier',
                        'description': 'Je peux ajouter la persistance du panier (localStorage/session) ?',
                        'code_example': 'Panier avec localStorage'
                    },
                    {
                        'title': 'Système de recherche',
                        'description': 'Tu veux un système de recherche et filtres de produits ?',
                        'code_example': 'Recherche et filtres avancés'
                    },
                    {
                        'title': 'Compte utilisateur',
                        'description': 'Veux-tu ajouter l\'inscription et connexion utilisateur ?',
                        'code_example': 'Système d\'authentification'
                    },
                    {
                        'title': 'Panel admin',
                        'description': 'Je peux créer un panel admin pour gérer les produits ?',
                        'code_example': 'Interface admin CRUD'
                    }
                ]
            },
            'mobile': {
                'triggers': ['app', 'mobile', 'android', 'ios'],
                'suggestions': [
                    {
                        'title': 'Navigation',
                        'description': 'Veux-tu que j\'ajoute un système de navigation entre écrans ?',
                        'code_example': 'Navigation avec routes'
                    },
                    {
                        'title': 'État global',
                        'description': 'Je peux ajouter la gestion d\'état (Redux, MobX, Provider) ?',
                        'code_example': 'State management'
                    },
                    {
                        'title': 'API calls',
                        'description': 'Tu veux que j\'ajoute les appels API avec gestion d\'erreurs ?',
                        'code_example': 'Fetch/Axios avec error handling'
                    }
                ]
            },
            'algorithm': {
                'triggers': ['algorithme', 'tri', 'recherche', 'optimisation'],
                'suggestions': [
                    {
                        'title': 'Complexité temporelle',
                        'description': 'Veux-tu que j\'analyse et optimise la complexité (O notation) ?',
                        'code_example': 'Optimisation Big O'
                    },
                    {
                        'title': 'Cas limites',
                        'description': 'Je peux ajouter la gestion des cas limites (listes vides, etc.) ?',
                        'code_example': 'Edge cases handling'
                    },
                    {
                        'title': 'Visualisation',
                        'description': 'Tu veux un code pour visualiser l\'algorithme étape par étape ?',
                        'code_example': 'Logs de débogage'
                    },
                    {
                        'title': 'Benchmark',
                        'description': 'Veux-tu un benchmark pour comparer avec d\'autres implémentations ?',
                        'code_example': 'Tests de performance'
                    }
                ]
            }
        }
    
    def generate_suggestions(self, context: Dict) -> List[Dict]:
        """Génère des suggestions basées sur le contexte avec validation."""
        try:
            # Validation
            if not context or not isinstance(context, dict):
                return []
            
            suggestions = []
            
            # Analyser le contexte pour déterminer les suggestions pertinentes
            for category, rules in self.suggestion_rules.items():
                try:
                    # Vérifier si le contexte correspond aux triggers
                    triggers = rules.get('triggers', [])
                    
                    # Vérification sécurisée des valeurs
                    message = str(context.get('message', '')).lower()
                    code_type = str(context.get('code_type', '')).lower()
                    domain = str(context.get('domain', '')).lower()
                    language = str(context.get('language', '')).lower()
                    
                    # Si un trigger correspond
                    if any(trigger in message or trigger in code_type or trigger in domain for trigger in triggers):
                        # Ajouter les suggestions de cette catégorie
                        category_suggestions = rules.get('suggestions', [])
                        suggestions.extend(category_suggestions)
                
                except Exception as e:
                    # Continuer avec les autres catégories en cas d'erreur
                    print(f"Erreur catégorie {category}: {e}")
                    continue
            
            # Ajouter des suggestions générales
            try:
                language = str(context.get('language', '')).lower()
                message = str(context.get('message', '')).lower()
                code_type = str(context.get('code_type', '')).lower()
                
                if language and 'test' not in message:
                    suggestions.append({
                        'title': 'Tests',
                        'description': f'Veux-tu que je crée des tests unitaires en {language.title()} ?',
                        'code_example': f'Tests {language}'
                    })
                
                if code_type and 'documentation' not in message:
                    suggestions.append({
                        'title': 'Documentation',
                        'description': 'Tu veux que j\'ajoute de la documentation détaillée ?',
                        'code_example': 'Documentation complète'
                    })
            
            except Exception as e:
                print(f"Erreur suggestions générales: {e}")
            
            return suggestions[:5]  # Limiter à 5 suggestions
        
        except Exception as e:
            print(f"Erreur generate_suggestions: {e}")
            return []
    
    def format_suggestions_message(self, suggestions: List[Dict]) -> str:
        """Formate les suggestions en message convivial."""
        if not suggestions:
            return ""
        
        message = "\n\n💡 **Suggestions** :\n"
        
        for i, suggestion in enumerate(suggestions, 1):
            message += f"\n**{i}. {suggestion['title']}**\n"
            message += f"   {suggestion['description']}\n"
        
        message += "\n_Réponds avec le numéro ou décris ce que tu veux !_"
        
        return message
    
    def detect_user_choice(self, message: str, previous_suggestions: List[Dict]) -> Optional[Dict]:
        """Détecte si l'utilisateur répond à une suggestion."""
        msg_lower = message.lower().strip()
        
        # Détection par numéro
        if msg_lower.isdigit():
            index = int(msg_lower) - 1
            if 0 <= index < len(previous_suggestions):
                return previous_suggestions[index]
        
        # Détection par mots-clés
        for suggestion in previous_suggestions:
            title_lower = suggestion['title'].lower()
            if title_lower in msg_lower or any(word in msg_lower for word in title_lower.split()):
                return suggestion
        
        # Détection des réponses affirmatives
        affirmative = ['oui', 'yes', 'ok', 'd\'accord', 'go', 'ouais', 'carrément', 'vas-y']
        if any(word in msg_lower for word in affirmative) and len(previous_suggestions) == 1:
            return previous_suggestions[0]
        
        return None
    
    def generate_contextual_questions(self, context: Dict) -> List[str]:
        """Génère des questions contextuelles pour clarifier les besoins."""
        questions = []
        
        code_type = context.get('code_type', '').lower()
        language = context.get('language', '')
        
        if code_type == 'site' and not language:
            questions.append("Tu veux juste du HTML ou aussi du CSS et JavaScript ?")
        
        if 'api' in code_type and not context.get('has_auth'):
            questions.append("L'API doit être publique ou nécessiter une authentification ?")
        
        if 'database' in code_type.lower():
            questions.append("Quel type de base de données ? (SQL, MongoDB, etc.)")
        
        if code_type == 'app' and not language:
            questions.append("App web, mobile Android, ou iOS ?")
        
        return questions

# Instance globale
suggester = ProactiveSuggester()

def get_proactive_suggester() -> ProactiveSuggester:
    """Récupère l'instance du suggester proactif."""
    return suggester
