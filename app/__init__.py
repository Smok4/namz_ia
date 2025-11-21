from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import logging
from logging.handlers import RotatingFileHandler

from .routes import bp
from .config import get_config
from .security import configure_security


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(get_config())
    
    # CORS restrictif
    CORS(app, resources={
        r"/api/*": {
            "origins": app.config['CORS_ORIGINS'],
            "methods": ["GET", "POST"],
            "allow_headers": ["Content-Type", "Authorization"],
            "max_age": 3600
        }
    })
    
    # Rate Limiting
    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=[app.config['RATELIMIT_DEFAULT']],
        storage_uri=app.config['RATELIMIT_STORAGE_URL']
    )
    
    # Stocker limiter dans app pour usage dans routes
    app.limiter = limiter
    
    # Configuration Logging
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(
            app.config['LOG_FILE'],
            maxBytes=10240000,  # 10MB
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Namz IA startup')
    
    # Configuration de la sécurité (headers, validation, error handlers)
    configure_security(app)
    
    app.register_blueprint(bp)
    return app
