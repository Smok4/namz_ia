"""
Training Queries - Requêtes clés pour former l'IA à devenir experte en code
Ces requêtes couvrent les cas d'usage les plus courants en programmation
"""

TRAINING_QUERIES = {
    # Python - Bases
    "python_function": "crée une fonction python",
    "python_class": "crée une classe python",
    "python_loop": "crée une boucle python",
    "python_file_read": "lire un fichier en python",
    "python_file_write": "écrire dans un fichier en python",
    "python_api_call": "faire une requête http en python",
    "python_json": "parser du json en python",
    "python_csv": "lire un fichier csv en python",
    "python_database": "se connecter à une base de données en python",
    
    # Python - Avancé
    "python_async": "fonction asynchrone python",
    "python_decorator": "créer un décorateur python",
    "python_context_manager": "context manager python",
    "python_generator": "générateur python",
    "python_threading": "utiliser les threads en python",
    "python_multiprocessing": "multiprocessing python",
    "python_regex": "expressions régulières python",
    "python_exception": "gestion d'erreurs python",
    
    # Python - Data Science
    "python_pandas": "utiliser pandas pour analyser des données",
    "python_numpy": "calculs avec numpy",
    "python_matplotlib": "créer un graphique avec matplotlib",
    "python_sklearn": "machine learning avec scikit-learn",
    
    # JavaScript/TypeScript - Bases
    "js_function": "crée une fonction javascript",
    "js_class": "crée une classe javascript",
    "js_async": "fonction async javascript",
    "js_promise": "utiliser les promises javascript",
    "js_fetch": "faire une requête fetch javascript",
    "js_dom": "manipuler le DOM javascript",
    "js_event": "gérer les événements javascript",
    
    # TypeScript
    "ts_interface": "créer une interface typescript",
    "ts_type": "créer un type typescript",
    "ts_generic": "fonction générique typescript",
    "ts_enum": "enum typescript",
    
    # Web Development
    "html_form": "créer un formulaire html",
    "html_page": "créer une page html complète",
    "css_flex": "utiliser flexbox css",
    "css_grid": "utiliser css grid",
    "css_animation": "créer une animation css",
    "css_responsive": "design responsive css",
    
    # C/C++
    "c_function": "créer une fonction en c",
    "c_struct": "créer une structure en c",
    "c_pointer": "utiliser les pointeurs en c",
    "c_memory": "allocation mémoire en c",
    "c_file": "lire un fichier en c",
    
    # C#/.NET
    "csharp_class": "créer une classe c#",
    "csharp_interface": "créer une interface c#",
    "csharp_async": "méthode asynchrone c#",
    "csharp_linq": "utiliser linq c#",
    "csharp_ef": "entity framework c#",
    
    # Java
    "java_class": "créer une classe java",
    "java_interface": "créer une interface java",
    "java_exception": "gestion d'exceptions java",
    "java_collections": "utiliser les collections java",
    "java_stream": "stream api java",
    
    # PHP
    "php_function": "créer une fonction php",
    "php_class": "créer une classe php",
    "php_pdo": "connexion base de données php pdo",
    "php_session": "gérer les sessions php",
    
    # Ruby
    "ruby_class": "créer une classe ruby",
    "ruby_module": "créer un module ruby",
    "ruby_block": "utiliser les blocks ruby",
    
    # Go
    "go_function": "créer une fonction go",
    "go_struct": "créer une struct go",
    "go_goroutine": "utiliser les goroutines go",
    "go_channel": "utiliser les channels go",
    
    # Rust
    "rust_function": "créer une fonction rust",
    "rust_struct": "créer une struct rust",
    "rust_ownership": "ownership en rust",
    "rust_trait": "créer un trait rust",
    
    # Swift
    "swift_class": "créer une classe swift",
    "swift_struct": "créer une struct swift",
    "swift_protocol": "créer un protocol swift",
    "swift_closure": "utiliser les closures swift",
    
    # Kotlin
    "kotlin_class": "créer une classe kotlin",
    "kotlin_data_class": "data class kotlin",
    "kotlin_coroutine": "utiliser les coroutines kotlin",
    "kotlin_extension": "fonction d'extension kotlin",
    
    # SQL
    "sql_select": "requête select sql",
    "sql_insert": "insérer des données sql",
    "sql_update": "mettre à jour des données sql",
    "sql_delete": "supprimer des données sql",
    "sql_join": "jointure sql",
    "sql_index": "créer un index sql",
    "sql_procedure": "procédure stockée sql",
    
    # DevOps
    "bash_script": "créer un script bash",
    "docker_file": "créer un dockerfile",
    "docker_compose": "docker-compose.yml",
    
    # Patterns et Optimisation
    "optimize_python": "optimiser du code python",
    "optimize_js": "optimiser du code javascript",
    "refactor_code": "refactoriser du code",
    "debug_code": "debugger du code",
    "improve_code": "améliorer du code",
    "code_review": "revue de code",
    "best_practices": "bonnes pratiques de code",
    
    # Architecture
    "design_pattern": "design patterns",
    "singleton": "pattern singleton",
    "factory": "pattern factory",
    "observer": "pattern observer",
    "mvc": "architecture mvc",
    "rest_api": "créer une api rest",
    "graphql": "api graphql",
    
    # Tests
    "unit_test_python": "test unitaire python",
    "unit_test_js": "test unitaire javascript",
    "mock_test": "mock pour les tests",
    "integration_test": "test d'intégration",
    
    # Sécurité
    "hash_password": "hasher un mot de passe",
    "jwt_token": "créer un token jwt",
    "input_validation": "valider les entrées utilisateur",
    "sql_injection": "prévenir les injections sql",
    "xss_protection": "protection contre xss",
    
    # Performance
    "cache_implementation": "implémenter un cache",
    "pagination": "pagination de résultats",
    "lazy_loading": "lazy loading",
    "database_optimization": "optimiser les requêtes base de données",
}

# Instructions d'entraînement pour chaque catégorie
TRAINING_INSTRUCTIONS = {
    "generation": [
        "Je dois pouvoir générer du code complet et fonctionnel",
        "Le code doit inclure des commentaires explicatifs",
        "Fournir des exemples d'utilisation",
        "Respecter les conventions de nommage du langage",
        "Inclure la gestion d'erreurs appropriée"
    ],
    
    "optimization": [
        "Analyser le code pour identifier les goulots d'étranglement",
        "Proposer plusieurs alternatives d'optimisation",
        "Expliquer le gain de performance attendu",
        "Considérer la lisibilité vs performance",
        "Utiliser les structures de données appropriées"
    ],
    
    "debugging": [
        "Identifier les erreurs courantes",
        "Proposer des outils de debugging appropriés",
        "Fournir des techniques de logging",
        "Expliquer comment reproduire et isoler les bugs",
        "Suggérer des tests pour prévenir les régressions"
    ],
    
    "refactoring": [
        "Améliorer la lisibilité du code",
        "Réduire la duplication",
        "Respecter les principes SOLID",
        "Améliorer la maintenabilité",
        "Conserver le comportement existant"
    ],
    
    "best_practices": [
        "Suivre les conventions du langage",
        "Utiliser les idiomes appropriés",
        "Documenter le code de manière appropriée",
        "Considérer la sécurité",
        "Penser à l'évolutivité"
    ]
}

def get_training_query_by_category(category: str) -> list:
    """Retourne toutes les requêtes d'entraînement pour une catégorie donnée."""
    return [query for key, query in TRAINING_QUERIES.items() if category in key]

def get_all_training_queries() -> list:
    """Retourne toutes les requêtes d'entraînement."""
    return list(TRAINING_QUERIES.values())

def get_training_instructions(category: str) -> list:
    """Retourne les instructions d'entraînement pour une catégorie."""
    return TRAINING_INSTRUCTIONS.get(category, [])
