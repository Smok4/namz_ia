# 🎓 Guide d'entraînement - Queries clés pour Namz IA

## 📖 Vue d'ensemble

Ce document liste toutes les requêtes clés (key queries) pour entraîner et tester l'IA Namz. Ces requêtes couvrent les cas d'usage les plus courants en programmation.

## 🎯 Catégories de requêtes

### 1. Python - Basics (Niveau débutant)

**Génération de fonctions**
```
- "crée une fonction python"
- "fais une fonction python qui calcule la factorielle"
- "écris une fonction python pour inverser une chaîne"
- "fonction python pour vérifier si un nombre est premier"
```

**Génération de classes**
```
- "crée une classe python"
- "fais une classe python pour gérer des utilisateurs"
- "classe python avec héritage"
- "classe python avec méthodes magiques"
```

**Manipulation de fichiers**
```
- "lire un fichier en python"
- "écrire dans un fichier en python"
- "parser un fichier json en python"
- "lire un fichier csv en python"
```

### 2. Python - Advanced (Niveau avancé)

**Programmation asynchrone**
```
- "fonction asynchrone python"
- "créer un serveur async python"
- "utiliser asyncio en python"
```

**Décorateurs et context managers**
```
- "créer un décorateur python"
- "context manager python"
- "décorateur avec paramètres python"
```

**Threads et multiprocessing**
```
- "utiliser les threads en python"
- "multiprocessing python"
- "pool de threads python"
```

### 3. JavaScript/Node.js

**Fonctions et async**
```
- "crée une fonction javascript"
- "fonction async javascript"
- "promise javascript"
- "async/await javascript"
```

**Manipulation DOM**
```
- "manipuler le DOM javascript"
- "ajouter un élément au DOM"
- "événements javascript"
```

**Requêtes HTTP**
```
- "fetch javascript"
- "requête axios javascript"
- "appeler une API javascript"
```

### 4. TypeScript

**Types et interfaces**
```
- "créer une interface typescript"
- "type typescript"
- "générique typescript"
- "enum typescript"
```

**Classes**
```
- "classe typescript"
- "classe typescript avec interface"
- "héritage typescript"
```

### 5. Web Development

**HTML**
```
- "créer un formulaire html"
- "page html complète"
- "template html"
- "formulaire avec validation html"
```

**CSS**
```
- "utiliser flexbox css"
- "css grid"
- "animation css"
- "design responsive css"
- "css pour navbar"
```

### 6. Backend Development

**C#/.NET**
```
- "créer une classe c#"
- "api rest c#"
- "utiliser linq c#"
- "entity framework c#"
```

**Java**
```
- "créer une classe java"
- "collections java"
- "stream api java"
- "spring boot java"
```

**PHP**
```
- "créer une classe php"
- "connexion base de données php"
- "session php"
- "api rest php"
```

### 7. Langages systèmes

**C**
```
- "créer une fonction en c"
- "struct c"
- "pointeurs c"
- "allocation mémoire c"
```

**Rust**
```
- "fonction rust"
- "struct rust"
- "ownership rust"
- "trait rust"
```

**Go**
```
- "fonction go"
- "struct go"
- "goroutine go"
- "channels go"
```

### 8. Mobile Development

**Swift (iOS)**
```
- "créer une classe swift"
- "struct swift"
- "protocol swift"
- "closure swift"
```

**Kotlin (Android)**
```
- "classe kotlin"
- "data class kotlin"
- "coroutine kotlin"
- "extension kotlin"
```

### 9. Base de données (SQL)

**Requêtes de base**
```
- "requête select sql"
- "insérer des données sql"
- "update sql"
- "delete sql"
```

**Requêtes avancées**
```
- "jointure sql"
- "inner join sql"
- "left join sql"
- "group by sql"
- "sous-requête sql"
```

### 10. Optimisation et amélioration

**Optimisation**
```
- "optimise du code python"
- "optimise cette fonction"
- "améliore la performance"
- "code plus rapide"
```

**Refactoring**
```
- "refactorise ce code"
- "améliore ce code"
- "rends ce code plus lisible"
- "bonnes pratiques"
```

**Debugging**
```
- "debug ce code"
- "corrige cette erreur"
- "pourquoi ce code ne marche pas"
- "trouve le bug"
```

## 🎯 Format optimal des requêtes

### Structure recommandée

```
[ACTION] [TYPE] [LANGAGE] [DESCRIPTION] [OPTIONS]
```

**Exemples:**
- ✅ "crée une fonction python qui trie une liste"
- ✅ "optimise ce code javascript avec async/await"
- ✅ "améliore cette classe C# avec LINQ"

### Actions reconnues

- **Création**: crée, créer, fait, fais, faire, écris, écrire, génère
- **Optimisation**: optimise, optimiser, améliore la performance
- **Amélioration**: améliore, améliorer, refactorise
- **Debug**: debug, débugger, corrige, corriger, répare
- **Explication**: explique, expliquer, comment

### Types reconnus

- fonction, function
- classe, class
- interface
- méthode, method
- algorithme, algorithm
- api
- test

## 🔥 Requêtes complexes (Production-ready)

### API REST complète
```
"crée une API REST Python avec:
- authentification JWT
- validation des données
- gestion d'erreurs
- logging
- documentation"
```

### Système de cache
```
"implémente un système de cache en Python avec:
- LRU eviction
- thread-safe
- TTL configurable
- métriques de performance"
```

### Architecture microservices
```
"crée un microservice Node.js avec:
- API REST
- connexion MongoDB
- authentification
- rate limiting
- health checks"
```

## 📊 Métriques de qualité

### Critères d'évaluation

Pour chaque requête, l'IA doit fournir:

1. **Code fonctionnel** ✅
   - Syntaxe correcte
   - Logique cohérente
   - Exécutable sans erreur

2. **Documentation** 📝
   - Commentaires explicatifs
   - Docstrings/JSDoc
   - Exemples d'utilisation

3. **Bonnes pratiques** 🎯
   - Conventions du langage
   - Gestion d'erreurs
   - Type hints (si applicable)

4. **Performance** ⚡
   - Complexité optimale
   - Structures de données appropriées
   - Pas de goulots d'étranglement

5. **Sécurité** 🔒
   - Validation des entrées
   - Protection contre injections
   - Gestion sécurisée des données

## 🧪 Tests de régression

### Tests essentiels à exécuter

1. **Génération basique** (100% success attendu)
   - Fonction simple Python
   - Classe simple JavaScript
   - Requête SQL SELECT

2. **Génération avancée** (95% success attendu)
   - Fonction async avec gestion d'erreurs
   - Classe avec héritage multiple
   - API REST complète

3. **Optimisation** (90% success attendu)
   - Optimisation de boucles
   - Refactoring de code legacy
   - Amélioration de performance

## 💡 Tips pour de meilleurs résultats

### DO ✅
- Soyez spécifique sur le langage
- Donnez du contexte (use case, contraintes)
- Mentionnez les bibliothèques si nécessaire
- Précisez le niveau de complexité souhaité

### DON'T ❌
- Requêtes trop vagues ("fais du code")
- Pas de langage spécifié
- Demandes contradictoires
- Trop de contraintes simultanées

## 🚀 Roadmap des requêtes

### Phase 1 : Fondations (Actuel) ✅
- Génération de base dans 15+ langages
- Optimisation simple
- Debug basique

### Phase 2 : Avancé (En cours) 🔄
- Architecture complète (MVC, microservices)
- Tests automatiques
- Documentation auto-générée

### Phase 3 : Expert (Futur) 🎯
- Code review automatique
- Conversion entre langages
- Suggestions proactives
- Analyse de sécurité

## 📚 Ressources

### Documentation interne
- [CAPABILITIES.md](../CAPABILITIES.md) - Capacités complètes
- [training_queries.py](../app/training_queries.py) - Queries programmatiques
- [test_ia.py](../test_ia.py) - Tests automatisés

### Pour contribuer
1. Ajoutez vos requêtes à `training_queries.py`
2. Testez avec `test_ia.py`
3. Documentez les cas d'usage ici

---

**Namz IA** - Entraîné pour l'excellence en programmation 🚀
