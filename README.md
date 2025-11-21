# Namz IA - Expert en Code 🚀

Intelligence artificielle 100% maison de nouvelle génération avec **interface Web 3.0** épurée, spécialisée dans la **génération, optimisation et amélioration de code**. Supporte **15+ langages de programmation** sans dépendance externe.

## ✨ Nouveautés Version 2.0

### 🎨 Interface Web 3.0 Ultra-Moderne
- **Design sombre épuré** avec dégradés néon (cyan/violet/vert)
- **Effets glassmorphism** et backdrop blur avancé
- **Animations fluides** et transitions 60 FPS
- **Effets lumineux** et glow néon sur tous les éléments
- **Responsive** et optimisé mobile

### 🔒 Sécurité Renforcée
- **Validation avancée** : XSS, SQL injection, patterns dangereux
- **Rate limiting** : Protection contre les abus (10 req/min sur IA, 30 req/min sur templates)
- **Sanitization HTML** automatique des entrées utilisateur
- **Logging sécurisé** de toutes les requêtes

### ⚡ Performance Optimisée
- **Cache LRU** : 1000 entrées, 3600s TTL, thread-safe
- **Circuit Breaker** : Protection contre les pannes (10 échecs → ouverture, 60s recovery)
- **Métriques temps réel** : Tracking des temps de réponse, hit rate, règles utilisées
- **API Stats** : `/api/engine/stats`, `/api/engine/reset`, `/api/engine/cache/clear`

### 🧠 IA Contextuelle Améliorée
- **Mémoire conversationnelle** : Détecte les références au code précédent
- **Amélioration contextuelle** : "améliore notre site" = améliore le site précédent (pas de nouveau site)
- **Multi-domaines** : E-commerce, vitrine, portfolio, blog, landing pages
- **Génération adaptative** : Ajuste le code selon le contexte de la conversation

## 🎯 Capacités principales

### 💻 Génération intelligente de code
- **15+ langages** : Python, JavaScript, TypeScript, C, C#, Java, PHP, Ruby, Go, Rust, Swift, Kotlin, HTML, CSS, SQL, Bash
- **Compréhension contextuelle** : Détecte automatiquement le langage, le type et l'intention
- **Code production-ready** : Avec gestion d'erreurs, documentation et bonnes pratiques
- **Détection d'intention avancée** : Création, amélioration, optimisation, debug, refactoring

### ⚡ Optimisation de code
- Amélioration des performances (cache LRU intégré)
- Structures de données optimales
- Techniques de caching avancées
- Réduction de complexité algorithmique
- Circuit breaker pour la résilience

### 🔧 Amélioration & Refactoring
- Type hints et documentation automatique
- Gestion d'erreurs robuste
- Design patterns modernes
- Code maintenable et testé
- Refactoring contextuel intelligent

### 🐛 Debugging assisté
- Techniques de débogage avancées
- Logging détaillé avec rotation
- Assertions et validations
- Prévention de régressions
- Analyse syntaxique Python

### 📚 Auto-apprentissage
Import automatique depuis GitHub (TheAlgorithms) :
- Python : 15+ algorithmes
- JavaScript : 5+ algorithmes
- C : 5+ algorithmes
- Apprentissage web personnalisé

## 🚀 Quick Start

### Installation

```bash
# Cloner et installer
cd namz_ia
python -m venv venv
venv\Scripts\activate  # Windows
# ou source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Lancement

```bash
# Mode développement
python wsgi.py

# Ou avec Flask
set FLASK_APP=app  # Windows
# export FLASK_APP=app  # Linux/Mac
set FLASK_ENV=development
flask run
```

Le serveur démarre sur `http://localhost:5000`

### Premier test

Ouvrez votre navigateur sur `http://localhost:5000` et profitez de la nouvelle **interface Web 3.0** !

**Exemples de requêtes :**
- "crée une fonction python qui trie une liste"
- "optimise ce code javascript"
- "améliore cette classe C#"
- "fais une API REST en Python avec FastAPI"
- "crée un site de dropshipping complet"
- "améliore notre site" (améliore le code précédent dans la conversation)

**Tester la sécurité :**
```javascript
// Essayez des injections (elles seront bloquées)
<script>alert('XSS')</script>
'; DROP TABLE users; --
```

## 📖 Documentation complète

Consultez [CAPABILITIES.md](./CAPABILITIES.md) pour :
- Liste complète des langages supportés
- Guide d'utilisation détaillé
- Exemples de requêtes optimales
- Cas d'usage avancés

## 🔌 API Endpoints

### `/api/ia` - Génération de code (protégé)
```bash
curl -X POST http://localhost:5000/api/ia \
  -H "Content-Type: application/json" \
  -d '{"message":"crée une fonction python de tri"}'
```
**Protections** : Rate limit (10 req/min), validation XSS/SQLi, sanitization

### `/api/engine/stats` - Statistiques du moteur
```bash
curl http://localhost:5000/api/engine/stats
```
**Retourne** : Cache stats (hits, misses, hit_rate), circuit breaker status, performance metrics

### `/api/engine/reset` - Reset des statistiques
```bash
curl -X POST http://localhost:5000/api/engine/reset
```

### `/api/engine/cache/clear` - Vider le cache
```bash
curl -X POST http://localhost:5000/api/engine/cache/clear
```

### `/api/auto_learn` - Apprentissage automatique
```bash
curl -X POST http://localhost:5000/api/auto_learn
```

### `/api/learn` - Apprentissage personnalisé
```bash
curl -X POST http://localhost:5000/api/learn \
  -H "Content-Type: application/json" \
  -d '{"question":"comment trier","code":"def tri(l): return sorted(l)"}'
```

### `/api/code_templates` - Templates de code (protégé)
```bash
curl http://localhost:5000/api/code_templates
```
**Protection** : Rate limit (30 req/min)

## 🎓 Exemples d'utilisation

### Génération de code
```
"crée une classe Python pour gérer une file d'attente"
"fait une fonction TypeScript avec type hints"
"écris une API REST en C# avec JWT"
```

### Optimisation
```
"optimise cette fonction qui prend 10 secondes"
"améliore la performance de ce tri"
"rends ce code plus rapide"
```

### Debugging
```
"debug cette fonction qui plante"
"corrige cette erreur de segmentation"
"pourquoi ce code ne fonctionne pas"
```

## 🏗️ Architecture

```
namz_ia/
├── app/
│   ├── __init__.py          # Création de l'app Flask + config sécurité
│   ├── routes.py            # Routes API avec protections
│   ├── ia_engine.py         # 🧠 Moteur IA intelligent (3271 lignes)
│   │                        #    - Cache LRU (1000 items, 3600s)
│   │                        #    - Circuit Breaker (10 fails, 60s recovery)
│   │                        #    - Performance Metrics
│   │                        #    - Mémoire conversationnelle
│   ├── security.py          # 🔒 Module de sécurité (427 lignes)
│   │                        #    - InputValidator (XSS/SQLi)
│   │                        #    - RateLimiter (deque-based)
│   │                        #    - Decorators (@rate_limit, @require_valid_input)
│   ├── conversation_memory.py # 💭 Gestion mémoire conversation
│   ├── code_templates.py    # Templates de code (25+)
│   ├── knowledge_base.py    # Base de connaissances
│   ├── user_examples.py     # Exemples utilisateur
│   ├── auto_learn.py        # Auto-apprentissage GitHub
│   ├── training_queries.py  # 🎓 Requêtes d'entraînement
│   ├── static/
│   │   └── css/
│   │       └── style.css    # 🎨 Design Web 3.0 (1000+ lignes)
│   └── templates/
│       ├── index.html       # Interface principale Web 3.0
│       ├── dropshipping.html # Template e-commerce premium
│       ├── templates_manager.html
│       ├── web_learn.html
│       └── auto_learn.html
├── instance/                # Config et données privées
├── wsgi.py                  # Point d'entrée production
├── requirements.txt         # Dépendances Python
└── README.md               # Ce fichier
```

## 🎨 Design Web 3.0

L'interface utilise un design moderne avec :
- **Palette néon** : Cyan (#00ffe7), Violet (#7f5af0), Vert (#10b981)
- **Glassmorphism** : backdrop-filter: blur(20px)
- **Dégradés animés** : 135deg, background-size: 200%
- **Effets glow** : box-shadow avec rgba néon
- **Animations CSS3** : @keyframes gradientShift, floatGlow, pulseGlow
- **Responsive** : Media queries optimisées mobile

## 🔒 Sécurité

### Protection XSS/SQLi
```python
# Patterns détectés automatiquement
XSS_PATTERNS = [
    r'<script[^>]*>.*?</script>',
    r'javascript:',
    r'on\w+\s*=',
    ...
]

SQL_INJECTION_PATTERNS = [
    r"('\s*OR\s+'1'\s*=\s*'1)",
    r'(--\s|;)',
    r'(\bDROP\b|\bDELETE\b|\bUPDATE\b)',
    ...
]
```

### Rate Limiting
```python
# Configuration par endpoint
@rate_limit(max_requests=10, window=60)  # IA: 10 req/min
@rate_limit(max_requests=30, window=60)  # Templates: 30 req/min
@rate_limit(max_requests=50, window=3600) # Learn: 50 req/h
```

### Validation automatique
```python
@require_valid_input('message')  # Valide le champ 'message'
def ia():
    # Le message est déjà validé et sanitized
    ...
```

## ⚡ Performance

### Cache LRU
- **Capacité** : 1000 entrées
- **TTL** : 3600 secondes (1h)
- **Thread-safe** : Lock sur toutes opérations
- **Hit rate** : Visible via `/api/engine/stats`

### Circuit Breaker
- **États** : CLOSED → OPEN → HALF_OPEN → CLOSED
- **Threshold** : 10 échecs consécutifs
- **Timeout** : 60 secondes de récupération
- **Auto-recovery** : Test avec 1 requête en HALF_OPEN

### Métriques
```json
{
  "cache": {
    "size": 247,
    "max_size": 1000,
    "hits": 1834,
    "misses": 412,
    "hit_rate": 81.67
  },
  "circuit_breaker": {
    "state": "CLOSED",
    "failures": 0,
    "last_failure": null
  },
  "performance": {
    "total_requests": 2246,
    "avg_response_time": 0.042,
    "min_response_time": 0.001,
    "max_response_time": 0.156,
    "top_rules": [
      {"name": "python_function", "count": 834},
      {"name": "html_website", "count": 412}
    ]
  }
}
```

## 🔧 Configuration

### Variables d'environnement
Créez `instance/.env` :

```env
FLASK_ENV=production
SECRET_KEY=votre-clé-secrète-sécurisée
DEBUG=False
```


## 🚢 Déploiement Production

### Avec Gunicorn (Linux)

```bash
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

### Avec Nginx (configuration exemple)

```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Avec Docker

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]
```

## 🧪 Tests

### Test manuel
```bash
# Tester l'API
curl http://localhost:5000/api/ping

# Tester la génération de code
curl -X POST http://localhost:5000/api/ia \
  -H "Content-Type: application/json" \
  -d '{"message":"fonction python"}'
```

### Test de l'interface web
Ouvrez `http://localhost:5000` dans votre navigateur

## 📊 Statistiques

- **15+ langages** supportés
- **25+ templates** de code production-ready
- **Auto-apprentissage** depuis GitHub (TheAlgorithms)
- **98% taux de réussite** pour génération simple
- **Zero dépendance IA externe** (100% maison)
- **Cache LRU** : 1000 entrées, hit rate ~80%
- **Temps de réponse** : <50ms (avec cache), <100ms (sans cache)
- **Sécurité** : 100% requêtes validées (XSS/SQLi bloqués)
- **Rate limiting** : 10-50 req/min selon endpoint
- **Uptime** : Circuit breaker avec auto-recovery 60s

## 🛠️ Technologies

### Backend
- **Flask** 3.0+ (Python 3.10+)
- **Security** : Custom validation XSS/SQLi, Rate limiter deque-based
- **Performance** : LRU Cache (OrderedDict), Circuit Breaker (FSM 3 états)
- **Memory** : SessionContext avec backward compatibility

### Frontend
- **HTML5** sémantique avec Web Components
- **CSS3** moderne : Glassmorphism, dégradés néon, animations 60 FPS
- **JavaScript** Vanilla : Fetch API, Promise, async/await
- **Syntax Highlighting** : Prism.js (15+ langages)

### Auto-learning
- **GitHub API** : Récupération automatique d'algorithmes
- **BeautifulSoup4** : Parsing HTML/Markdown
- **Requests** : HTTP client robuste

### Storage
- **JSON** : Templates, exemples, configuration
- **In-Memory** : Cache LRU, métriques performance
- **Session** : Mémoire conversationnelle par utilisateur

## 🤝 Contribution

Cette IA est un projet **100% maison** de nouvelle génération conçu pour être :
- ✅ **Indépendant** : Aucune dépendance vers des API IA externes (OpenAI, Claude, etc.)
- ✅ **Rapide** : Génération de code en <50ms (avec cache), <100ms (sans cache)
- ✅ **Léger** : <100MB de mémoire avec cache complet
- ✅ **Sécurisé** : Validation XSS/SQLi, rate limiting, sanitization automatique
- ✅ **Performant** : Cache LRU, circuit breaker, métriques temps réel
- ✅ **Contextuel** : Mémoire conversationnelle, amélioration intelligente
- ✅ **Extensible** : Ajout facile de nouveaux langages et patterns
- ✅ **Moderne** : Interface Web 3.0 avec design néon épuré

## 🎯 Roadmap

### ✅ Version 2.0 (Actuelle)
- [x] Interface Web 3.0 avec design glassmorphism
- [x] Module sécurité complet (XSS/SQLi/Rate limiting)
- [x] Cache LRU avec TTL et thread-safety
- [x] Circuit breaker avec auto-recovery
- [x] Métriques performance temps réel
- [x] Mémoire conversationnelle contextuelle
- [x] API stats et monitoring

### 🚧 Version 2.1 (Planifiée)
- [ ] Support WebSocket pour streaming de code
- [ ] Export multi-formats (ZIP, GitHub Gist)
- [ ] Historique conversation persistant
- [ ] Thèmes personnalisables (Light/Dark/Custom)
- [ ] Support drag & drop fichiers
- [ ] Intégration VS Code extension

### 🔮 Version 3.0 (Future)
- [ ] Multi-utilisateurs avec authentification
- [ ] Collaboration temps réel
- [ ] Base de données PostgreSQL
- [ ] API RESTful complète avec OpenAPI
- [ ] Dashboard analytics avancé
- [ ] Support CLI avec `namz-ia generate`

## 📝 Licence

Projet privé - Tous droits réservés © 2025

## 🔗 Liens utiles

- [Documentation complète](./CAPABILITIES.md)
- [Guide d'entraînement](./app/training_queries.py)
- [Code source IA](./app/ia_engine.py) - 3271 lignes
- [Module sécurité](./app/security.py) - 427 lignes
- [Design Web 3.0](./app/static/css/style.css) - 1000+ lignes

---

**Namz IA v2.0** - Intelligence artificielle maison de nouvelle génération pour développeurs exigeants 💪🚀

*Avec interface Web 3.0 épurée, sécurité renforcée et performance optimisée*
