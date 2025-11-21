"""
Script de test pour démontrer les capacités de Namz IA
Lance automatiquement des requêtes tests et affiche les résultats
"""

import requests
import json
import time

# URL de l'API
API_URL = "http://localhost:5000/api/ia"

# Tests à exécuter
TESTS = [
    # Python - Génération
    {
        "name": "Python - Fonction simple",
        "query": "crée une fonction python qui calcule la factorielle"
    },
    {
        "name": "Python - Classe",
        "query": "crée une classe python pour gérer une file d'attente"
    },
    {
        "name": "Python - Optimisation",
        "query": "optimise du code python"
    },
    {
        "name": "Python - Amélioration",
        "query": "améliore ce code python avec bonnes pratiques"
    },
    {
        "name": "Python - Debug",
        "query": "debug du code python"
    },
    
    # JavaScript
    {
        "name": "JavaScript - Fonction",
        "query": "crée une fonction javascript async pour fetch des données"
    },
    {
        "name": "JavaScript - Optimisation",
        "query": "optimise ce code javascript"
    },
    
    # TypeScript
    {
        "name": "TypeScript - Classe",
        "query": "crée une classe typescript avec interfaces"
    },
    
    # C
    {
        "name": "C - Fonction",
        "query": "crée une fonction en c pour trier un tableau"
    },
    
    # C#
    {
        "name": "C# - Classe",
        "query": "crée une classe c# avec LINQ"
    },
    
    # PHP
    {
        "name": "PHP - Classe",
        "query": "crée une classe php pour connexion base de données"
    },
    
    # Ruby
    {
        "name": "Ruby - Classe",
        "query": "crée une classe ruby avec modules"
    },
    
    # Go
    {
        "name": "Go - Struct",
        "query": "crée une struct go avec méthodes"
    },
    
    # Rust
    {
        "name": "Rust - Struct",
        "query": "crée une struct rust avec traits"
    },
    
    # Swift
    {
        "name": "Swift - Classe",
        "query": "crée une classe swift pour iOS"
    },
    
    # Kotlin
    {
        "name": "Kotlin - Data Class",
        "query": "crée une data class kotlin"
    },
    
    # Web
    {
        "name": "HTML - Page complète",
        "query": "crée une page html complète avec navigation"
    },
    {
        "name": "CSS - Responsive",
        "query": "crée du css responsive avec flexbox"
    },
    
    # SQL
    {
        "name": "SQL - Requête complexe",
        "query": "crée une requête sql avec join"
    },
]

def run_test(test):
    """Exécute un test et affiche le résultat"""
    print(f"\n{'='*80}")
    print(f"TEST: {test['name']}")
    print(f"QUERY: {test['query']}")
    print(f"{'='*80}")
    
    try:
        start_time = time.time()
        response = requests.post(
            API_URL,
            json={"message": test['query']},
            timeout=10
        )
        elapsed_time = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS ({elapsed_time:.2f}s)")
            print(f"\nRESPONSE:")
            print(data.get('response', 'No response'))
            print(f"\nMETA: {json.dumps(data.get('meta', {}), indent=2)}")
            return True
        else:
            print(f"❌ FAILED (Status: {response.status_code})")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def run_all_tests():
    """Exécute tous les tests"""
    print("🚀 DÉMARRAGE DES TESTS NAMZ IA")
    print(f"API URL: {API_URL}")
    print(f"Nombre de tests: {len(TESTS)}")
    
    # Vérifier que l'API est accessible
    try:
        response = requests.get("http://localhost:5000/")
        print("✅ Serveur accessible")
    except:
        print("❌ Serveur non accessible. Assurez-vous qu'il est démarré.")
        return
    
    # Exécuter les tests
    results = []
    for test in TESTS:
        result = run_test(test)
        results.append((test['name'], result))
        time.sleep(0.5)  # Pause entre les tests
    
    # Résumé
    print("\n" + "="*80)
    print("📊 RÉSUMÉ DES TESTS")
    print("="*80)
    
    success_count = sum(1 for _, result in results if result)
    total_count = len(results)
    success_rate = (success_count / total_count) * 100
    
    print(f"\nRésultats: {success_count}/{total_count} ({success_rate:.1f}%)")
    print("\nDétail:")
    for name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {name}")
    
    if success_rate >= 90:
        print("\n🎉 EXCELLENT ! L'IA fonctionne parfaitement.")
    elif success_rate >= 75:
        print("\n👍 BON ! Quelques améliorations possibles.")
    else:
        print("\n⚠️ ATTENTION ! Vérifiez la configuration.")

def test_auto_learn():
    """Test l'apprentissage automatique"""
    print("\n" + "="*80)
    print("🎓 TEST AUTO-APPRENTISSAGE")
    print("="*80)
    
    try:
        response = requests.post("http://localhost:5000/api/auto_learn", timeout=30)
        if response.status_code == 200:
            print("✅ Auto-apprentissage réussi")
            print(response.json())
        else:
            print(f"❌ Échec: {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--learn":
        test_auto_learn()
    else:
        run_all_tests()
        
        print("\n" + "="*80)
        print("Pour tester l'auto-apprentissage:")
        print("python test_ia.py --learn")
        print("="*80)
