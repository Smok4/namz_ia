# 🛡️ Sécurité Namz IA - État des lieux

## ✅ DÉJÀ IMPLÉMENTÉ

### 1. Configuration avancée ✅
- ✅ Fichier `config.py` avec classes d'environnement
- ✅ Variables d'environnement `.env`
- ✅ CORS restrictif avec whitelist
- ✅ Limiter (Flask-Limiter) configuré

### 2. Rate Limiting ✅
- ✅ `flask-limiter` installé et configuré
- ✅ Limite par IP
- ✅ Endpoints protégés

### 3. Logging ✅
- ✅ `RotatingFileHandler` configuré
- ✅ Logs dans `/logs`
- ✅ Rotation automatique

### 4. Headers de sécurité ✅
- ✅ `X-Content-Type-Options: nosniff`
- ✅ CSRF protection
- ✅ Secure cookies

## 🔧 AMÉLIORATIONS PRIORITAIRES

### 1. Module `security.py` créé ✅
**Ajouté aujourd'hui** : Validation complète des entrées

**Fonctionnalités** :
```python
- InputValidator : Validation messages, code, session_id
- RateLimiter : Rate limiting personnalisé
- Decorators : @require_valid_input, @rate_limit, @log_request
- Error handlers : 400, 404, 429, 500
- Security headers : CSP, XSS Protection
```

**Utilisation** :
```python
from app.security import require_valid_input, rate_limit

@app.route('/api/chat', methods=['POST'])
@rate_limit(max_requests=50, window=3600)
@require_valid_input('message')
def chat():
    # Entrées déjà validées automatiquement
    data = request.get_json()
    message = data['message']  # Sécurisé
```

### 2. Intégration dans routes.py
**À faire** : Ajouter décorateurs aux endpoints sensibles

```python
# AVANT
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    # Pas de validation

# APRÈS  
@app.route('/api/chat', methods=['POST'])
@rate_limit(max_requests=50, window=3600)
@require_valid_input('message')
def chat():
    data = request.get_json()
    # Validé automatiquement
```

### 3. Protection XSS renforcée
**Déjà corrigé** dans `templates_manager.html` ✅
- Fonction `escapeHtml()` ajoutée
- XSS payloads affichés comme texte

### 4. Gestion d'erreurs robuste
**À améliorer** dans `conversation_memory.py`

```python
# ACTUELLEMENT
try:
    # code
except Exception as e:
    print(f"Erreur: {e}")  # Silencieux

# RECOMMANDÉ
try:
    # code
except ValueError as e:
    logger.error(f"Erreur validation: {e}")
    raise
except IOError as e:
    logger.error(f"Erreur I/O: {e}")
    raise
```

## 📋 CHECKLIST SÉCURITÉ

### Phase 1 - CRITIQUE 🔴 (Cette semaine)
- [x] Module security.py créé
- [x] Validation entrées implémentée
- [x] Rate limiting personnalisé
- [ ] Intégrer dans routes.py
- [ ] Tests de sécurité
- [x] XSS protection (templates)
- [x] CORS configuré
- [x] Variables environnement

### Phase 2 - IMPORTANT 🟠 (Semaine prochaine)
- [ ] Timeout sur opérations longues
- [ ] Monitoring avec Prometheus
- [ ] Alertes sur anomalies
- [ ] Backup automatique
- [ ] Circuit breakers
- [ ] Retry logic

### Phase 3 - AMÉLIORATION 🟡 (Mois prochain)
- [ ] Authentification JWT
- [ ] API Keys pour utilisateurs
- [ ] Audit logs
- [ ] Encryption at rest
- [ ] HTTPS obligatoire
- [ ] WAF (Web Application Firewall)

## 🚀 MISE EN PRODUCTION

### Checklist avant déploiement
```bash
# 1. Variables d'environnement
cp .env.example .env
# Éditer .env avec vraies valeurs

# 2. Secret key sécurisée
python -c "import secrets; print(secrets.token_hex(32))"
# Copier dans FLASK_SECRET_KEY

# 3. Désactiver debug
DEBUG=False
FLASK_ENV=production

# 4. HTTPS
# Configurer reverse proxy (nginx/Apache)
# Certificat SSL (Let's Encrypt)

# 5. Base de données
# Migrer de JSON vers PostgreSQL/MySQL

# 6. Monitoring
# Configurer Sentry, Datadog, ou Prometheus

# 7. Backups
# Cron job pour backups quotidiens
```

### Configuration nginx (exemple)
```nginx
server {
    listen 443 ssl http2;
    server_name namz-ia.example.com;
    
    ssl_certificate /etc/letsencrypt/live/namz-ia.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/namz-ia.example.com/privkey.pem;
    
    # Headers de sécurité
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeout
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
        
        # Rate limiting
        limit_req zone=api burst=10 nodelay;
    }
}
```

## 🧪 TESTS DE SÉCURITÉ

### Tests automatisés
```python
# tests/test_security.py
import pytest
from app import create_app
from app.security import InputValidator

def test_xss_protection():
    \"\"\"Teste protection XSS.\"\"\"
    malicious = "<script>alert('XSS')</script>"
    valid, error = InputValidator.validate_message(malicious)
    assert not valid
    assert "dangereux" in error

def test_sql_injection():
    \"\"\"Teste protection SQL injection.\"\"\"
    malicious = "'; DROP TABLE users; --"
    valid, error = InputValidator.validate_message(malicious)
    assert not valid

def test_rate_limiting():
    \"\"\"Teste rate limiting.\"\"\"
    app = create_app()
    client = app.test_client()
    
    # 50 requêtes OK
    for i in range(50):
        resp = client.post('/api/chat', json={'message': 'test'})
        assert resp.status_code == 200
    
    # 51ème requête bloquée
    resp = client.post('/api/chat', json={'message': 'test'})
    assert resp.status_code == 429
```

### Tests manuels
```bash
# 1. XSS
curl -X POST http://localhost:5000/api/chat \\
  -H "Content-Type: application/json" \\
  -d '{"message": "<script>alert(1)</script>"}'
# Attendu: 400 Bad Request

# 2. SQL Injection
curl -X POST http://localhost:5000/api/chat \\
  -H "Content-Type: application/json" \\
  -d '{"message": "'; DROP TABLE users; --"}'
# Attendu: 400 Bad Request

# 3. Rate limiting
for i in {1..60}; do
  curl -X POST http://localhost:5000/api/chat \\
    -H "Content-Type: application/json" \\
    -d '{"message": "test"}';
done
# Attendu: 429 après 50 requêtes

# 4. Payload trop grand
dd if=/dev/zero bs=20M count=1 | \\
  curl -X POST http://localhost:5000/api/chat \\
    -H "Content-Type: application/json" \\
    --data-binary @- 
# Attendu: 413 Payload Too Large
```

## 📊 MÉTRIQUES DE SÉCURITÉ

### KPIs à suivre
- **Requêtes bloquées** : XSS, SQLi, rate limit
- **Temps de réponse** : Détection anomalies
- **Erreurs 5xx** : Stabilité
- **Sessions actives** : Usage
- **Tentatives d'intrusion** : Alertes

### Dashboard recommandé
```python
# Prometheus + Grafana
from prometheus_client import Counter, Histogram

requests_blocked = Counter('requests_blocked_total', 'Blocked requests', ['reason'])
response_time = Histogram('response_time_seconds', 'Response time')

# Dans routes.py
@requests_blocked.count_exceptions()
@response_time.time()
def chat():
    # ...
```

## 🎯 PROCHAINES ÉTAPES

1. **Immédiat** (Aujourd'hui)
   - [x] Créer `security.py` ✅
   - [ ] Intégrer dans `routes.py`
   - [ ] Tests de validation

2. **Court terme** (Cette semaine)
   - [ ] Authentification JWT
   - [ ] Logging structuré JSON
   - [ ] Monitoring basique

3. **Moyen terme** (Ce mois)
   - [ ] Migration PostgreSQL
   - [ ] Caching Redis
   - [ ] Async I/O

4. **Long terme** (Trimestre)
   - [ ] Multi-tenancy
   - [ ] Kubernetes deployment
   - [ ] HA (High Availability)

---

**Développé avec 🛡️ sécurité first**

_Dernière mise à jour : 21 novembre 2025_
