"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   NAMZ IA - SECURITY & VALIDATION MODULE                     ║
║                        Input Validation & Sanitization                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

Module de sécurité pour:
- Validation des entrées utilisateur
- Sanitization des données
- Protection contre injections
- Rate limiting
- Authentification (future)
"""

import re
import html
from typing import Any, Dict, Optional, List
from functools import wraps
from flask import request, jsonify
import time
from collections import defaultdict, deque

# ═══════════════════════════════════════════════════════════════════════════════
#                          INPUT VALIDATION
# ═══════════════════════════════════════════════════════════════════════════════

class InputValidator:
    """Validation des entrées utilisateur."""
    
    # Patterns dangereux
    DANGEROUS_PATTERNS = [
        r'<script[^>]*>.*?</script>',  # XSS
        r'javascript:',
        r'on\w+\s*=',  # Event handlers
        r'eval\s*\(',
        r'exec\s*\(',
        r'__import__',
        r'\bDROP\s+TABLE\b',  # SQL injection
        r'\bDELETE\s+FROM\b',
        r'\bUPDATE\s+.*\s+SET\b',
        r';\s*DROP\s+',
        r'--\s*$',  # SQL comments
        r'/\*.*\*/',
    ]
    
    # Limites
    MAX_MESSAGE_LENGTH = 50000
    MAX_CODE_LENGTH = 100000
    MAX_SESSION_ID_LENGTH = 100
    MAX_LANGUAGE_LENGTH = 50
    
    @staticmethod
    def validate_message(message: str) -> tuple[bool, Optional[str]]:
        """
        Valide un message utilisateur.
        
        Args:
            message: Message à valider
        
        Returns:
            (valide, erreur si invalide)
        """
        if not message or not isinstance(message, str):
            return False, "Message doit être une chaîne non-vide"
        
        # Longueur
        if len(message) > InputValidator.MAX_MESSAGE_LENGTH:
            return False, f"Message trop long (max {InputValidator.MAX_MESSAGE_LENGTH} caractères)"
        
        # Patterns dangereux
        for pattern in InputValidator.DANGEROUS_PATTERNS:
            if re.search(pattern, message, re.IGNORECASE):
                return False, f"Pattern dangereux détecté: {pattern}"
        
        return True, None
    
    @staticmethod
    def validate_code(code: str) -> tuple[bool, Optional[str]]:
        """Valide du code."""
        if not code or not isinstance(code, str):
            return False, "Code doit être une chaîne non-vide"
        
        if len(code) > InputValidator.MAX_CODE_LENGTH:
            return False, f"Code trop long (max {InputValidator.MAX_CODE_LENGTH} caractères)"
        
        return True, None
    
    @staticmethod
    def validate_session_id(session_id: str) -> tuple[bool, Optional[str]]:
        """Valide un ID de session."""
        if not session_id or not isinstance(session_id, str):
            return False, "Session ID invalide"
        
        if len(session_id) > InputValidator.MAX_SESSION_ID_LENGTH:
            return False, "Session ID trop long"
        
        # Alphanumeric + underscore/hyphen seulement
        if not re.match(r'^[a-zA-Z0-9_-]+$', session_id):
            return False, "Session ID contient des caractères invalides"
        
        return True, None
    
    @staticmethod
    def validate_language(language: str) -> tuple[bool, Optional[str]]:
        """Valide un nom de langage."""
        if not language or not isinstance(language, str):
            return False, "Langage invalide"
        
        if len(language) > InputValidator.MAX_LANGUAGE_LENGTH:
            return False, "Nom de langage trop long"
        
        # Lettres, chiffres, +, # seulement
        if not re.match(r'^[a-zA-Z0-9+#_-]+$', language):
            return False, "Nom de langage contient des caractères invalides"
        
        return True, None
    
    @staticmethod
    def sanitize_html(text: str) -> str:
        """Échappe HTML pour éviter XSS."""
        return html.escape(text)
    
    @staticmethod
    def sanitize_for_display(text: str) -> str:
        """Sanitize pour affichage sécurisé."""
        # Échapper HTML
        text = InputValidator.sanitize_html(text)
        
        # Limiter longueur pour affichage
        if len(text) > 10000:
            text = text[:10000] + "..."
        
        return text

# ═══════════════════════════════════════════════════════════════════════════════
#                          RATE LIMITING
# ═══════════════════════════════════════════════════════════════════════════════

class RateLimiter:
    """Rate limiting simple basé sur IP."""
    
    def __init__(self, max_requests: int = 100, window: int = 3600):
        """
        Initialise le rate limiter.
        
        Args:
            max_requests: Nombre max de requêtes
            window: Fenêtre de temps en secondes
        """
        self.max_requests = max_requests
        self.window = window
        self.requests = defaultdict(lambda: deque(maxlen=max_requests))
    
    def is_allowed(self, key: str) -> tuple[bool, Optional[int]]:
        """
        Vérifie si la requête est autorisée.
        
        Args:
            key: Clé d'identification (IP, user_id, etc.)
        
        Returns:
            (autorisé, secondes avant reset si refusé)
        """
        now = time.time()
        
        # Nettoyer anciennes requêtes
        requests = self.requests[key]
        while requests and now - requests[0] > self.window:
            requests.popleft()
        
        # Vérifier limite
        if len(requests) >= self.max_requests:
            # Calculer temps avant reset
            oldest = requests[0]
            reset_time = int(self.window - (now - oldest))
            return False, reset_time
        
        # Ajouter requête
        requests.append(now)
        return True, None
    
    def reset(self, key: str):
        """Reset le compteur pour une clé."""
        if key in self.requests:
            del self.requests[key]
    
    def get_remaining(self, key: str) -> int:
        """Retourne le nombre de requêtes restantes."""
        now = time.time()
        requests = self.requests[key]
        
        # Nettoyer anciennes
        while requests and now - requests[0] > self.window:
            requests.popleft()
        
        return max(0, self.max_requests - len(requests))

# Instance globale
rate_limiter = RateLimiter(max_requests=100, window=3600)

# ═══════════════════════════════════════════════════════════════════════════════
#                          DECORATORS
# ═══════════════════════════════════════════════════════════════════════════════

def require_valid_input(message_field: str = 'message'):
    """
    Décorateur pour valider les entrées.
    
    Args:
        message_field: Nom du champ à valider
    """
    @wraps(require_valid_input)
    def validation_decorator(f):
        @wraps(f)
        def validation_wrapper(*args, **kwargs):
            data = request.get_json()
            
            if not data:
                return jsonify({'error': 'Données manquantes'}), 400
            
            # Valider message
            if message_field in data:
                message = data[message_field]
                valid, error = InputValidator.validate_message(message)
                if not valid:
                    return jsonify({'error': f'Message invalide: {error}'}), 400
            
            # Valider code si présent
            if 'code' in data:
                code = data['code']
                valid, error = InputValidator.validate_code(code)
                if not valid:
                    return jsonify({'error': f'Code invalide: {error}'}), 400
            
            # Valider session_id si présent
            if 'session_id' in data:
                session_id = data['session_id']
                valid, error = InputValidator.validate_session_id(session_id)
                if not valid:
                    return jsonify({'error': f'Session ID invalide: {error}'}), 400
            
            # Valider language si présent
            if 'language' in data:
                language = data['language']
                valid, error = InputValidator.validate_language(language)
                if not valid:
                    return jsonify({'error': f'Langage invalide: {error}'}), 400
            
            return f(*args, **kwargs)
        return validation_wrapper
    return validation_decorator

def rate_limit(max_requests: int = None, window: int = None):
    """
    Décorateur pour rate limiting.
    
    Args:
        max_requests: Nombre max de requêtes (None = utiliser global)
        window: Fenêtre en secondes (None = utiliser global)
    """
    @wraps(rate_limit)
    def rate_limit_decorator(f):
        @wraps(f)
        def rate_limit_wrapper(*args, **kwargs):
            # Utiliser IP comme clé
            key = request.remote_addr
            
            # Créer limiter custom ou utiliser global
            if max_requests is not None and window is not None:
                limiter = RateLimiter(max_requests, window)
            else:
                limiter = rate_limiter
            
            # Vérifier limite
            allowed, reset_time = limiter.is_allowed(key)
            
            if not allowed:
                return jsonify({
                    'error': 'Rate limit dépassé',
                    'retry_after': reset_time
                }), 429
            
            # Ajouter headers de rate limit
            remaining = limiter.get_remaining(key)
            response = f(*args, **kwargs)
            
            if isinstance(response, tuple):
                response_obj, status_code = response
            else:
                response_obj = response
                status_code = 200
            
            # Ajouter headers si c'est une response Flask
            if hasattr(response_obj, 'headers'):
                response_obj.headers['X-RateLimit-Limit'] = str(limiter.max_requests)
                response_obj.headers['X-RateLimit-Remaining'] = str(remaining)
                response_obj.headers['X-RateLimit-Reset'] = str(int(time.time() + limiter.window))
            
            return response_obj, status_code
        
        return rate_limit_wrapper
    return rate_limit_decorator

def log_request(include_body: bool = False):
    """
    Décorateur pour logger les requêtes.
    
    Args:
        include_body: Inclure le corps de la requête
    """
    @wraps(log_request)
    def log_decorator(f):
        @wraps(f)
        def log_wrapper(*args, **kwargs):
            import logging
            logger = logging.getLogger(__name__)
            
            # Log requête
            log_data = {
                'method': request.method,
                'path': request.path,
                'ip': request.remote_addr,
                'user_agent': request.user_agent.string,
            }
            
            if include_body:
                log_data['body'] = request.get_json()
            
            logger.info(f"Request: {log_data}")
            
            # Exécuter
            try:
                result = f(*args, **kwargs)
                logger.info(f"Response: success")
                return result
            except Exception as e:
                logger.error(f"Response: error - {str(e)}")
                raise
        
        return log_wrapper
    return log_decorator

# ═══════════════════════════════════════════════════════════════════════════════
#                          ERROR HANDLERS
# ═══════════════════════════════════════════════════════════════════════════════

def register_error_handlers(app):
    """Enregistre les gestionnaires d'erreurs."""
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'error': 'Requête invalide',
            'message': str(error)
        }), 400
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Ressource non trouvée',
            'message': str(error)
        }), 404
    
    @app.errorhandler(429)
    def rate_limit_exceeded(error):
        return jsonify({
            'error': 'Rate limit dépassé',
            'message': 'Trop de requêtes, réessayez plus tard'
        }), 429
    
    @app.errorhandler(500)
    def internal_error(error):
        import logging
        logger = logging.getLogger(__name__)
        logger.exception("Erreur serveur interne")
        
        return jsonify({
            'error': 'Erreur serveur',
            'message': 'Une erreur est survenue'
        }), 500
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        import logging
        logger = logging.getLogger(__name__)
        logger.exception(f"Exception non gérée: {error}")
        
        return jsonify({
            'error': 'Erreur inattendue',
            'message': str(error) if app.debug else 'Une erreur est survenue'
        }), 500

# ═══════════════════════════════════════════════════════════════════════════════
#                          SECURITY HEADERS
# ═══════════════════════════════════════════════════════════════════════════════

def add_security_headers(response):
    """Ajoute les headers de sécurité."""
    # Protection XSS
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # CSP
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net; "
        "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
        "img-src 'self' data: https:; "
        "font-src 'self' data: https://cdn.jsdelivr.net;"
    )
    
    # HSTS (uniquement si HTTPS)
    # response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    
    return response

def configure_security(app):
    """Configure la sécurité de l'application."""
    # Enregistrer error handlers
    register_error_handlers(app)
    
    # Ajouter headers de sécurité
    app.after_request(add_security_headers)
    
    # Limiter taille des uploads
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
    
    print("✓ Sécurité configurée")
