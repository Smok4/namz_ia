import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class Config:
    """Configuration de base."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY non définie. Créez un fichier .env avec SECRET_KEY=...")
    
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///instance/namz_ia.db')
    
    # CORS
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:5000').split(',')
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = os.environ.get('LOG_FILE', 'logs/namz_ia.log')
    
    # Rate Limiting
    RATELIMIT_STORAGE_URL = os.environ.get('RATELIMIT_STORAGE_URL', 'memory://')
    RATELIMIT_DEFAULT = os.environ.get('RATELIMIT_DEFAULT', '100 per hour')
    
    # Session
    SESSION_TIMEOUT = int(os.environ.get('SESSION_TIMEOUT', 3600))
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 10000))
    
    # Cache
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
    CACHE_DEFAULT_TIMEOUT = int(os.environ.get('CACHE_DEFAULT_TIMEOUT', 300))
    
    DEBUG = False
    TESTING = False
    JSONIFY_PRETTYPRINT_REGULAR = False

class DevelopmentConfig(Config):
    """Configuration développement."""
    DEBUG = True
    # En dev, SECRET_KEY peut être moins sécurisée
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-non-securise-change-moi'

class ProductionConfig(Config):
    """Configuration production."""
    DEBUG = False
    
    # En production, tous les secrets sont obligatoires
    @staticmethod
    def validate():
        required = ['SECRET_KEY', 'DATABASE_URL']
        missing = [key for key in required if not os.environ.get(key)]
        if missing:
            raise ValueError(f"Variables d'environnement manquantes en production: {', '.join(missing)}")

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Sélection automatique de la configuration selon l'environnement
def get_config():
    env = os.environ.get('FLASK_ENV', 'development').lower()
    return config.get(env, DevelopmentConfig)
