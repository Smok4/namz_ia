"""
Générateur de projets multi-fichiers pour Namz IA
Génère des structures complètes de projets avec plusieurs fichiers liés
"""

from typing import Dict, List
import os

class MultiFileGenerator:
    """Génère des projets multi-fichiers complets."""
    
    def __init__(self):
        self.project_templates = self._initialize_templates()
    
    def _initialize_templates(self) -> Dict:
        """Initialise les templates de projets multi-fichiers."""
        return {
            'flask_api': {
                'name': 'API REST Flask complète',
                'description': 'API REST avec Flask, SQLAlchemy, JWT, tests',
                'files': {
                    'app/__init__.py': self._flask_init,
                    'app/models.py': self._flask_models,
                    'app/routes.py': self._flask_routes,
                    'app/auth.py': self._flask_auth,
                    'app/config.py': self._flask_config,
                    'tests/test_api.py': self._flask_tests,
                    'requirements.txt': self._flask_requirements,
                    'README.md': self._flask_readme,
                    '.env.example': self._flask_env,
                    'run.py': self._flask_run
                }
            },
            'react_app': {
                'name': 'Application React complète',
                'description': 'App React avec Router, Redux, API calls',
                'files': {
                    'src/App.js': self._react_app,
                    'src/index.js': self._react_index,
                    'src/store/store.js': self._react_store,
                    'src/components/Header.js': self._react_header,
                    'src/components/Footer.js': self._react_footer,
                    'src/pages/Home.js': self._react_home,
                    'src/services/api.js': self._react_api,
                    'src/App.css': self._react_css,
                    'package.json': self._react_package,
                    'README.md': self._react_readme
                }
            },
            'django_project': {
                'name': 'Projet Django complet',
                'description': 'Projet Django avec app, models, views, templates',
                'files': {
                    'myproject/settings.py': self._django_settings,
                    'myproject/urls.py': self._django_urls,
                    'myapp/models.py': self._django_models,
                    'myapp/views.py': self._django_views,
                    'myapp/serializers.py': self._django_serializers,
                    'myapp/urls.py': self._django_app_urls,
                    'templates/base.html': self._django_base_template,
                    'requirements.txt': self._django_requirements,
                    'README.md': self._django_readme
                }
            },
            'ecommerce_full': {
                'name': 'Site e-commerce complet',
                'description': 'Site e-commerce HTML/CSS/JS avec backend',
                'files': {
                    'frontend/index.html': self._ecommerce_html,
                    'frontend/style.css': self._ecommerce_css,
                    'frontend/script.js': self._ecommerce_js,
                    'frontend/cart.html': self._ecommerce_cart_html,
                    'backend/app.py': self._ecommerce_backend,
                    'backend/models.py': self._ecommerce_models,
                    'backend/config.py': self._ecommerce_config,
                    'README.md': self._ecommerce_readme
                }
            },
            'mobile_app': {
                'name': 'Application mobile React Native',
                'description': 'App mobile cross-platform avec navigation',
                'files': {
                    'App.js': self._rn_app,
                    'src/screens/HomeScreen.js': self._rn_home,
                    'src/screens/ProfileScreen.js': self._rn_profile,
                    'src/navigation/Navigator.js': self._rn_navigation,
                    'src/components/Button.js': self._rn_button,
                    'src/services/api.js': self._rn_api,
                    'package.json': self._rn_package,
                    'README.md': self._rn_readme
                }
            },
            'microservices': {
                'name': 'Architecture microservices',
                'description': 'Multiple services avec Docker',
                'files': {
                    'auth-service/app.py': self._micro_auth,
                    'user-service/app.py': self._micro_user,
                    'product-service/app.py': self._micro_product,
                    'docker-compose.yml': self._micro_docker_compose,
                    'gateway/nginx.conf': self._micro_nginx,
                    'README.md': self._micro_readme
                }
            }
        }
    
    def detect_project_type(self, message: str) -> str:
        """Détecte le type de projet à générer."""
        msg_lower = message.lower()
        
        patterns = {
            'flask_api': ['api flask', 'rest flask', 'backend flask'],
            'react_app': ['app react', 'react', 'frontend react'],
            'django_project': ['django', 'projet django'],
            'ecommerce_full': ['ecommerce complet', 'boutique complète', 'shop complet'],
            'mobile_app': ['app mobile', 'react native', 'application mobile'],
            'microservices': ['microservices', 'micro-services', 'architecture distribuée']
        }
        
        for project_type, keywords in patterns.items():
            if any(keyword in msg_lower for keyword in keywords):
                return project_type
        
        return 'flask_api'  # Par défaut
    
    def generate_project(self, project_type: str) -> Dict:
        """Génère un projet complet avec validation."""
        try:
            # Validation
            if not project_type or not isinstance(project_type, str):
                return {
                    'error': 'Type de projet invalide',
                    'available_types': list(self.project_templates.keys())
                }
            
            project_type = project_type.strip().lower()
            
            if project_type not in self.project_templates:
                return {
                    'error': f'Type de projet inconnu: {project_type}',
                    'available_types': list(self.project_templates.keys())
                }
            
            template = self.project_templates[project_type]
            files = {}
            
            # Générer chaque fichier avec gestion d'erreur
            for filepath, generator_func in template['files'].items():
                try:
                    files[filepath] = generator_func()
                except Exception as e:
                    files[filepath] = f"# Erreur génération: {str(e)}"
                    print(f"Erreur génération {filepath}: {e}")
            
            return {
                'name': template['name'],
                'description': template['description'],
                'files': files,
                'instructions': self._get_project_instructions(project_type)
            }
        
        except Exception as e:
            return {
                'error': f'Erreur génération projet: {str(e)}',
                'available_types': list(self.project_templates.keys())
            }
    
    def _get_project_instructions(self, project_type: str) -> str:
        """Retourne les instructions d'utilisation du projet."""
        instructions = {
            'flask_api': """
## Installation et lancement

1. Créer un environnement virtuel:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\\Scripts\\activate     # Windows

2. Installer les dépendances:
   pip install -r requirements.txt

3. Configurer les variables d'environnement:
   cp .env.example .env
   # Éditer .env avec vos valeurs

4. Lancer l'application:
   python run.py

5. Tester l'API:
   pytest tests/
""",
            'react_app': """
## Installation et lancement

1. Installer les dépendances:
   npm install

2. Lancer en mode développement:
   npm start

3. Build de production:
   npm run build

4. L'app sera disponible sur http://localhost:3000
""",
            'ecommerce_full': """
## Installation et lancement

### Frontend
- Ouvrir frontend/index.html dans un navigateur
- Ou utiliser un serveur local: python -m http.server 8000

### Backend
1. cd backend
2. pip install -r requirements.txt
3. python app.py

Le site sera sur http://localhost:8000 (frontend)
L'API sera sur http://localhost:5000 (backend)
"""
        }
        
        return instructions.get(project_type, "Voir README.md pour les instructions")
    
    # === TEMPLATES FLASK API ===
    
    def _flask_init(self) -> str:
        return '''"""Application Flask principale."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    jwt.init_app(app)
    
    from app.routes import api_bp
    from app.auth import auth_bp
    
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    with app.app_context():
        db.create_all()
    
    return app
'''
    
    def _flask_models(self) -> str:
        return '''"""Modèles de données."""
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """Modèle utilisateur."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

class Item(db.Model):
    """Modèle item."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='items')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }
'''
    
    def _flask_routes(self) -> str:
        return '''"""Routes API."""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Item

api_bp = Blueprint('api', __name__)

@api_bp.route('/items', methods=['GET'])
def get_items():
    """Liste tous les items."""
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@api_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Récupère un item par ID."""
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@api_bp.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    """Crée un nouvel item."""
    data = request.get_json()
    user_id = get_jwt_identity()
    
    item = Item(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        user_id=user_id
    )
    db.session.add(item)
    db.session.commit()
    
    return jsonify(item.to_dict()), 201

@api_bp.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    """Met à jour un item."""
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)
    
    db.session.commit()
    return jsonify(item.to_dict())

@api_bp.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    """Supprime un item."""
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204
'''
    
    def _flask_auth(self) -> str:
        return '''"""Authentification JWT."""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Inscription utilisateur."""
    data = request.get_json()
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify(user.to_dict()), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """Connexion utilisateur."""
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token, 'user': user.to_dict()})

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Récupère l'utilisateur connecté."""
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())
'''
    
    def _flask_config(self) -> str:
        return '''"""Configuration Flask."""
import os

class Config:
    """Configuration de l'application."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key-change-in-production'
'''
    
    def _flask_tests(self) -> str:
        return '''"""Tests de l'API."""
import pytest
from app import create_app, db
from app.models import User, Item

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_register(client):
    """Test inscription."""
    response = client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert 'id' in response.json

def test_login(client):
    """Test connexion."""
    # Créer un utilisateur
    client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    
    # Se connecter
    response = client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_create_item(client):
    """Test création item."""
    # Créer et connecter utilisateur
    client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    login_response = client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    token = login_response.json['access_token']
    
    # Créer un item
    response = client.post('/api/items', json={
        'name': 'Test Item',
        'description': 'A test item',
        'price': 19.99
    }, headers={'Authorization': f'Bearer {token}'})
    
    assert response.status_code == 201
    assert response.json['name'] == 'Test Item'
'''
    
    def _flask_requirements(self) -> str:
        return '''Flask==2.3.0
Flask-SQLAlchemy==3.0.5
Flask-JWT-Extended==4.5.2
python-dotenv==1.0.0
pytest==7.4.0
'''
    
    def _flask_readme(self) -> str:
        return '''# API REST Flask

API REST complète avec Flask, SQLAlchemy et JWT.

## Fonctionnalités

- ✅ Authentification JWT
- ✅ CRUD complet sur les items
- ✅ Gestion des utilisateurs
- ✅ Tests unitaires
- ✅ Base de données SQLite/PostgreSQL

## Structure

```
app/
  __init__.py     # Initialisation Flask
  models.py       # Modèles SQLAlchemy
  routes.py       # Routes API
  auth.py         # Authentification
  config.py       # Configuration
tests/
  test_api.py     # Tests
requirements.txt  # Dépendances
run.py           # Point d'entrée
```

## API Endpoints

### Authentification
- `POST /auth/register` - Inscription
- `POST /auth/login` - Connexion
- `GET /auth/me` - Utilisateur connecté

### Items
- `GET /api/items` - Liste items
- `GET /api/items/<id>` - Item par ID
- `POST /api/items` - Créer item (auth requise)
- `PUT /api/items/<id>` - Modifier item (auth requise)
- `DELETE /api/items/<id>` - Supprimer item (auth requise)

## Installation

Voir instructions dans le projet.
'''
    
    def _flask_env(self) -> str:
        return '''SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URL=sqlite:///app.db
FLASK_ENV=development
'''
    
    def _flask_run(self) -> str:
        return '''"""Point d'entrée de l'application."""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''
    
    # === TEMPLATES REACT ===
    
    def _react_app(self) -> str:
        return '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store/store';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import './App.css';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="App">
          <Header />
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </Provider>
  );
}

export default App;
'''
    
    def _react_index(self) -> str:
        return '''import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
'''
    
    def _react_store(self) -> str:
        return '''import { configureStore } from '@reduxjs/toolkit';

const initialState = {
  user: null,
  items: []
};

function rootReducer(state = initialState, action) {
  switch (action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };
    case 'SET_ITEMS':
      return { ...state, items: action.payload };
    default:
      return state;
  }
}

const store = configureStore({
  reducer: rootReducer
});

export default store;
'''
    
    def _react_header(self) -> str:
        return '''import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <nav>
        <Link to="/">Accueil</Link>
      </nav>
    </header>
  );
}

export default Header;
'''
    
    def _react_footer(self) -> str:
        return '''import React from 'react';

function Footer() {
  return (
    <footer>
      <p>&copy; 2024 Mon Application</p>
    </footer>
  );
}

export default Footer;
'''
    
    def _react_home(self) -> str:
        return '''import React, { useEffect, useState } from 'react';
import { fetchItems } from '../services/api';

function Home() {
  const [items, setItems] = useState([]);
  
  useEffect(() => {
    loadItems();
  }, []);
  
  const loadItems = async () => {
    try {
      const data = await fetchItems();
      setItems(data);
    } catch (error) {
      console.error('Erreur chargement:', error);
    }
  };
  
  return (
    <div className="home">
      <h1>Bienvenue</h1>
      <div className="items">
        {items.map(item => (
          <div key={item.id} className="item">
            <h3>{item.name}</h3>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
'''
    
    def _react_api(self) -> str:
        return '''const API_URL = 'http://localhost:5000/api';

export async function fetchItems() {
  const response = await fetch(`${API_URL}/items`);
  if (!response.ok) throw new Error('Erreur chargement items');
  return response.json();
}

export async function createItem(item) {
  const response = await fetch(`${API_URL}/items`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(item)
  });
  if (!response.ok) throw new Error('Erreur création item');
  return response.json();
}
'''
    
    def _react_css(self) -> str:
        return '''* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
}

.App {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  background: #333;
  color: white;
  padding: 1rem;
}

main {
  flex: 1;
  padding: 2rem;
}

footer {
  background: #333;
  color: white;
  padding: 1rem;
  text-align: center;
}
'''
    
    def _react_package(self) -> str:
        return '''{
  "name": "mon-app-react",
  "version": "1.0.0",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.14.0",
    "react-redux": "^8.1.0",
    "@reduxjs/toolkit": "^1.9.5"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test"
  }
}
'''
    
    def _react_readme(self) -> str:
        return '''# Application React

Application React complète avec Router et Redux.

## Installation

```bash
npm install
npm start
```

L'app sera sur http://localhost:3000
'''
    
    # === TEMPLATES DJANGO ===
    
    def _django_settings(self) -> str:
        return '''"""Configuration Django."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-me')
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
'''
    
    def _django_urls(self) -> str:
        return '''"""URLs Django."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]
'''
    
    def _django_models(self) -> str:
        return '''"""Modèles Django."""
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
'''
    
    def _django_views(self) -> str:
        return '''"""Vues Django REST."""
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
'''
    
    def _django_serializers(self) -> str:
        return '''"""Serializers Django REST."""
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
'''
    
    def _django_app_urls(self) -> str:
        return '''"""URLs de l'app."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register('items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
'''
    
    def _django_base_template(self) -> str:
        return '''<!DOCTYPE html>
<html>
<head>
    <title>Mon Projet Django</title>
</head>
<body>
    <header>
        <h1>Mon Projet Django</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
'''
    
    def _django_requirements(self) -> str:
        return '''Django==4.2.0
djangorestframework==3.14.0
'''
    
    def _django_readme(self) -> str:
        return '''# Projet Django

Projet Django avec REST API.

## Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
'''
    
    # === TEMPLATES E-COMMERCE ===
    
    def _ecommerce_html(self) -> str:
        return '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Ma Boutique</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Ma Boutique</h1>
        <div id="cart-icon">🛒 <span id="cart-count">0</span></div>
    </header>
    <main>
        <div id="products"></div>
    </main>
    <script src="script.js"></script>
</body>
</html>
'''
    
    def _ecommerce_css(self) -> str:
        return '''* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: Arial; }
header { background: #333; color: white; padding: 1rem; display: flex; justify-content: space-between; }
#products { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; padding: 2rem; }
.product { border: 1px solid #ddd; padding: 1rem; }
'''
    
    def _ecommerce_js(self) -> str:
        return '''let cart = [];
const products = [
    { id: 1, name: 'Produit 1', price: 29.99 },
    { id: 2, name: 'Produit 2', price: 39.99 }
];

function displayProducts() {
    const container = document.getElementById('products');
    products.forEach(p => {
        const div = document.createElement('div');
        div.className = 'product';
        div.innerHTML = `
            <h3>${p.name}</h3>
            <p>${p.price}€</p>
            <button onclick="addToCart(${p.id})">Ajouter au panier</button>
        `;
        container.appendChild(div);
    });
}

function addToCart(id) {
    cart.push(id);
    document.getElementById('cart-count').textContent = cart.length;
}

displayProducts();
'''
    
    def _ecommerce_cart_html(self) -> str:
        return '''<!DOCTYPE html>
<html>
<head><title>Panier</title></head>
<body>
    <h1>Mon Panier</h1>
    <div id="cart-items"></div>
</body>
</html>
'''
    
    def _ecommerce_backend(self) -> str:
        return '''from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/products')
def get_products():
    return jsonify([
        {'id': 1, 'name': 'Produit 1', 'price': 29.99},
        {'id': 2, 'name': 'Produit 2', 'price': 39.99}
    ])

if __name__ == '__main__':
    app.run(port=5000)
'''
    
    def _ecommerce_models(self) -> str:
        return '''from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
'''
    
    def _ecommerce_config(self) -> str:
        return '''class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'
'''
    
    def _ecommerce_readme(self) -> str:
        return '''# Site E-commerce

Site e-commerce complet avec frontend et backend.
'''
    
    # === TEMPLATES REACT NATIVE ===
    
    def _rn_app(self) -> str:
        return '''import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import Navigator from './src/navigation/Navigator';

export default function App() {
  return (
    <NavigationContainer>
      <Navigator />
    </NavigationContainer>
  );
}
'''
    
    def _rn_home(self) -> str:
        return '''import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text>Home Screen</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' }
});
'''
    
    def _rn_profile(self) -> str:
        return '''import React from 'react';
import { View, Text } from 'react-native';

export default function ProfileScreen() {
  return (
    <View><Text>Profile</Text></View>
  );
}
'''
    
    def _rn_navigation(self) -> str:
        return '''import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import HomeScreen from '../screens/HomeScreen';
import ProfileScreen from '../screens/ProfileScreen';

const Tab = createBottomTabNavigator();

export default function Navigator() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
}
'''
    
    def _rn_button(self) -> str:
        return '''import React from 'react';
import { TouchableOpacity, Text, StyleSheet } from 'react-native';

export default function Button({ title, onPress }) {
  return (
    <TouchableOpacity style={styles.button} onPress={onPress}>
      <Text style={styles.text}>{title}</Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  button: { padding: 15, backgroundColor: '#007bff', borderRadius: 5 },
  text: { color: 'white', textAlign: 'center' }
});
'''
    
    def _rn_api(self) -> str:
        return '''export async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  return response.json();
}
'''
    
    def _rn_package(self) -> str:
        return '''{
  "name": "mon-app-mobile",
  "dependencies": {
    "react": "^18.2.0",
    "react-native": "^0.72.0",
    "@react-navigation/native": "^6.1.0",
    "@react-navigation/bottom-tabs": "^6.5.0"
  }
}
'''
    
    def _rn_readme(self) -> str:
        return '''# App Mobile React Native

Application mobile cross-platform.

## Installation
```
npm install
npm start
```
'''
    
    # === TEMPLATES MICROSERVICES ===
    
    def _micro_auth(self) -> str:
        return '''from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

@app.route('/auth/login', methods=['POST'])
def login():
    # Logique d'authentification
    token = jwt.encode({'user_id': 1}, 'secret', algorithm='HS256')
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(port=5001)
'''
    
    def _micro_user(self) -> str:
        return '''from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([{'id': 1, 'name': 'User 1'}])

if __name__ == '__main__':
    app.run(port=5002)
'''
    
    def _micro_product(self) -> str:
        return '''from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([{'id': 1, 'name': 'Product 1'}])

if __name__ == '__main__':
    app.run(port=5003)
'''
    
    def _micro_docker_compose(self) -> str:
        return '''version: '3.8'
services:
  auth:
    build: ./auth-service
    ports:
      - "5001:5001"
  user:
    build: ./user-service
    ports:
      - "5002:5002"
  product:
    build: ./product-service
    ports:
      - "5003:5003"
  gateway:
    image: nginx
    ports:
      - "80:80"
    volumes:
      - ./gateway/nginx.conf:/etc/nginx/nginx.conf
'''
    
    def _micro_nginx(self) -> str:
        return '''events {}
http {
  upstream auth {
    server auth:5001;
  }
  upstream user {
    server user:5002;
  }
  server {
    listen 80;
    location /auth/ {
      proxy_pass http://auth/;
    }
    location /users/ {
      proxy_pass http://user/;
    }
  }
}
'''
    
    def _micro_readme(self) -> str:
        return '''# Architecture Microservices

Architecture distribuée avec plusieurs services.

## Lancement
```
docker-compose up
```
'''

# Instance globale
multi_file_generator = MultiFileGenerator()

def get_multi_file_generator() -> MultiFileGenerator:
    """Récupère l'instance du générateur multi-fichiers."""
    return multi_file_generator
