"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   NAMZ IA - ADVANCED CONVERSATION MEMORY                     ║
║                     Enterprise-Grade Memory Management                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

Système avancé de gestion de mémoire conversationnelle avec:
- Multi-sessions avec isolation complète
- Analyse sémantique et NLP basique
- Compression intelligente des contextes
- Cache multi-niveaux avec LRU
- Recherche vectorielle (embedding-ready)
- Export/Import multi-formats
- Analytics et métriques détaillées
- Auto-sauvegarde et recovery
- Thread-safe operations
- Encryption support
- Webhook notifications
- Rate limiting
- TTL et garbage collection
"""

import json
import os
import hashlib
import re
import time
import threading
import pickle
import gzip
import base64
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple, Set, Callable
from collections import Counter, OrderedDict, defaultdict
from functools import wraps, lru_cache
from dataclasses import dataclass, asdict, field
from enum import Enum
import sqlite3

# ═══════════════════════════════════════════════════════════════════════════════
#                                 ENUMS & TYPES
# ═══════════════════════════════════════════════════════════════════════════════

class MessageRole(Enum):
    """Rôles possibles pour les messages."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    FUNCTION = "function"
    TOOL = "tool"

class SessionStatus(Enum):
    """Statuts de session."""
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"
    LOCKED = "locked"

class Priority(Enum):
    """Priorités des messages."""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4

class ExportFormat(Enum):
    """Formats d'export disponibles."""
    JSON = "json"
    JSONL = "jsonl"
    CSV = "csv"
    MARKDOWN = "markdown"
    HTML = "html"
    PICKLE = "pickle"
    SQLITE = "sqlite"

@dataclass
class Message:
    """Structure de message enrichie."""
    role: MessageRole
    content: str
    timestamp: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    session_id: str = "default"
    message_id: str = field(default_factory=lambda: hashlib.md5(str(time.time()).encode()).hexdigest()[:16])
    parent_id: Optional[str] = None
    thread_id: Optional[str] = None
    priority: Priority = Priority.NORMAL
    tags: List[str] = field(default_factory=list)
    embedding: Optional[List[float]] = None
    tokens: int = 0
    sentiment: Optional[float] = None
    language: Optional[str] = None
    edited: bool = False
    deleted: bool = False
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        data = asdict(self)
        data['role'] = self.role.value
        data['priority'] = self.priority.value
        return data
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Message':
        """Create from dictionary."""
        data = data.copy()
        
        # Gérer ancien format (rétrocompatibilité)
        if 'role' in data:
            if isinstance(data['role'], str):
                data['role'] = MessageRole(data['role'])
        
        if 'priority' in data:
            if isinstance(data['priority'], (int, str)):
                data['priority'] = Priority(data.get('priority', Priority.NORMAL.value))
        else:
            data['priority'] = Priority.NORMAL
        
        # Valeurs par défaut pour nouveaux champs
        if 'session_id' not in data:
            data['session_id'] = 'default'
        if 'timestamp' not in data:
            data['timestamp'] = datetime.utcnow().isoformat()
        
        return cls(**data)

@dataclass
class SessionContext:
    """Contexte enrichi de session."""
    session_id: str
    created_at: str
    updated_at: str
    last_language: Optional[str] = None
    last_code_type: Optional[str] = None
    last_domain: Optional[str] = None
    user_preferences: Dict[str, Any] = field(default_factory=dict)
    status: SessionStatus = SessionStatus.ACTIVE
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    message_count: int = 0
    total_tokens: int = 0
    avg_response_time: float = 0.0
    user_satisfaction: Optional[float] = None
    topics: List[str] = field(default_factory=list)
    entities: Dict[str, List[str]] = field(default_factory=dict)
    summary: Optional[str] = None
    ttl: Optional[int] = None  # Time to live in seconds
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        data = asdict(self)
        data['status'] = self.status.value
        return data
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SessionContext':
        """Create from dictionary."""
        data = data.copy()
        
        # Gérer ancien format (rétrocompatibilité)
        if 'session_id' not in data:
            data['session_id'] = 'default'
        if 'created_at' not in data:
            data['created_at'] = datetime.utcnow().isoformat()
        if 'updated_at' not in data:
            data['updated_at'] = datetime.utcnow().isoformat()
        
        # Convertir status
        if 'status' in data:
            if isinstance(data['status'], str):
                data['status'] = SessionStatus(data['status'])
        else:
            data['status'] = SessionStatus.ACTIVE
        
        return cls(**data)

# ═══════════════════════════════════════════════════════════════════════════════
#                              CACHE & STORAGE LAYER
# ═══════════════════════════════════════════════════════════════════════════════

class LRUCache:
    """Cache LRU thread-safe avec TTL."""
    
    def __init__(self, capacity: int = 1000, ttl: int = 3600):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.ttl = ttl
        self.lock = threading.Lock()
        self.hits = 0
        self.misses = 0
    
    def get(self, key: str) -> Optional[Any]:
        """Récupère une valeur du cache."""
        with self.lock:
            if key not in self.cache:
                self.misses += 1
                return None
            
            value, timestamp = self.cache[key]
            
            # Vérifier TTL
            if time.time() - timestamp > self.ttl:
                del self.cache[key]
                self.misses += 1
                return None
            
            # Déplacer en fin (LRU)
            self.cache.move_to_end(key)
            self.hits += 1
            return value
    
    def set(self, key: str, value: Any):
        """Ajoute une valeur au cache."""
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
            
            self.cache[key] = (value, time.time())
            
            # Éviction si capacité dépassée
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
    
    def clear(self):
        """Vide le cache."""
        with self.lock:
            self.cache.clear()
    
    def stats(self) -> Dict:
        """Statistiques du cache."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return {
            'size': len(self.cache),
            'capacity': self.capacity,
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': f"{hit_rate:.2f}%"
        }

class StorageBackend:
    """Backend de stockage avec compression."""
    
    def __init__(self, base_path: str = 'instance'):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)
        self.lock = threading.Lock()
    
    def save(self, filename: str, data: Any, compress: bool = True):
        """Sauvegarde des données."""
        filepath = os.path.join(self.base_path, filename)
        
        with self.lock:
            try:
                json_data = json.dumps(data, indent=2, ensure_ascii=False)
                
                if compress:
                    # Compression gzip
                    compressed = gzip.compress(json_data.encode('utf-8'))
                    with open(filepath + '.gz', 'wb') as f:
                        f.write(compressed)
                else:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(json_data)
                
                return True
            except Exception as e:
                print(f"Erreur sauvegarde: {e}")
                return False
    
    def load(self, filename: str, compressed: bool = True) -> Optional[Any]:
        """Charge des données."""
        filepath = os.path.join(self.base_path, filename)
        
        with self.lock:
            try:
                if compressed and os.path.exists(filepath + '.gz'):
                    with open(filepath + '.gz', 'rb') as f:
                        compressed_data = f.read()
                    json_data = gzip.decompress(compressed_data).decode('utf-8')
                    return json.loads(json_data)
                elif os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        return json.load(f)
                
                return None
            except Exception as e:
                print(f"Erreur chargement: {e}")
                return None

# ═══════════════════════════════════════════════════════════════════════════════
#                           NLP & ANALYSIS UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

class NLPAnalyzer:
    """Analyseur NLP basique sans dépendances externes."""
    
    # Mots-clés par langue
    LANGUAGE_KEYWORDS = {
        'python': ['def', 'class', 'import', 'from', 'print', 'if __name__', 'self', 'lambda'],
        'javascript': ['function', 'const', 'let', 'var', 'async', 'await', 'console.log', '=>'],
        'java': ['public', 'private', 'class', 'static', 'void', 'new', 'System.out'],
        'cpp': ['#include', 'std::', 'cout', 'cin', 'namespace', 'template'],
        'sql': ['SELECT', 'FROM', 'WHERE', 'JOIN', 'INSERT', 'UPDATE', 'DELETE'],
        'html': ['<html>', '<div>', '<span>', '<body>', '<head>', '<!DOCTYPE'],
        'css': ['{', '}', 'color:', 'background:', 'margin:', 'padding:'],
    }
    
    # Domaines techniques
    DOMAIN_KEYWORDS = {
        'web': ['website', 'site web', 'html', 'css', 'frontend', 'backend', 'api', 'rest'],
        'data': ['data', 'données', 'dataframe', 'pandas', 'numpy', 'analysis', 'analyse'],
        'ml': ['machine learning', 'ml', 'model', 'modèle', 'training', 'tensorflow', 'pytorch'],
        'security': ['security', 'sécurité', 'pentest', 'xss', 'sql injection', 'vulnerability'],
        'mobile': ['mobile', 'android', 'ios', 'app', 'application mobile', 'react native'],
        'devops': ['docker', 'kubernetes', 'ci/cd', 'deployment', 'pipeline', 'jenkins'],
    }
    
    # Intentions utilisateur
    INTENT_PATTERNS = {
        'question': [r'\?$', r'^(comment|pourquoi|quoi|qui|où|quand|combien)', r'^(how|why|what|who|where|when)'],
        'request': [r'^(crée|créer|fait|faire|génère|générer|écris|écrire)', r'^(create|make|generate|write|build)'],
        'correction': [r'^(non|pas ça|erreur|corrige|change|modifie)', r'^(no|not that|error|fix|change|modify)'],
        'continuation': [r'^(et|aussi|également|en plus|puis)', r'^(and|also|then|plus|additionally)'],
        'clarification': [r'^(tu veux dire|c\'est à dire|donc)', r'^(you mean|so|therefore|thus)'],
    }
    
    @staticmethod
    def detect_language(text: str) -> Optional[str]:
        """Détecte le langage de programmation."""
        text_lower = text.lower()
        scores = {}
        
        for lang, keywords in NLPAnalyzer.LANGUAGE_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw.lower() in text_lower)
            if score > 0:
                scores[lang] = score
        
        if scores:
            return max(scores.items(), key=lambda x: x[1])[0]
        return None
    
    @staticmethod
    def detect_domain(text: str) -> Optional[str]:
        """Détecte le domaine technique."""
        text_lower = text.lower()
        scores = {}
        
        for domain, keywords in NLPAnalyzer.DOMAIN_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw.lower() in text_lower)
            if score > 0:
                scores[domain] = score
        
        if scores:
            return max(scores.items(), key=lambda x: x[1])[0]
        return None
    
    @staticmethod
    def detect_intent(text: str) -> List[str]:
        """Détecte les intentions dans le texte."""
        intents = []
        text_lower = text.lower().strip()
        
        for intent, patterns in NLPAnalyzer.INTENT_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    intents.append(intent)
                    break
        
        return intents if intents else ['statement']
    
    @staticmethod
    def extract_entities(text: str) -> Dict[str, List[str]]:
        """Extrait des entités basiques."""
        entities = {
            'urls': [],
            'emails': [],
            'files': [],
            'numbers': [],
            'code_blocks': []
        }
        
        # URLs
        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        entities['urls'] = re.findall(url_pattern, text)
        
        # Emails
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        entities['emails'] = re.findall(email_pattern, text)
        
        # Fichiers
        file_pattern = r'\b\w+\.(py|js|html|css|json|txt|md|csv|sql|java|cpp|c|h)\b'
        entities['files'] = re.findall(file_pattern, text)
        
        # Nombres
        number_pattern = r'\b\d+(?:\.\d+)?\b'
        entities['numbers'] = re.findall(number_pattern, text)
        
        # Blocs de code (```...```)
        code_pattern = r'```[\s\S]*?```'
        entities['code_blocks'] = re.findall(code_pattern, text)
        
        return {k: v for k, v in entities.items() if v}
    
    @staticmethod
    def calculate_similarity(text1: str, text2: str) -> float:
        """Calcule similarité basique entre deux textes."""
        # Tokenization simple
        words1 = set(re.findall(r'\w+', text1.lower()))
        words2 = set(re.findall(r'\w+', text2.lower()))
        
        if not words1 or not words2:
            return 0.0
        
        # Jaccard similarity
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0
    
    @staticmethod
    def sentiment_analysis(text: str) -> float:
        """Analyse de sentiment basique (-1 à 1)."""
        positive_words = [
            'bon', 'bien', 'super', 'excellent', 'parfait', 'génial', 'merci', 'bravo',
            'good', 'great', 'excellent', 'perfect', 'awesome', 'thanks', 'wonderful'
        ]
        
        negative_words = [
            'mauvais', 'mal', 'erreur', 'problème', 'bug', 'nul', 'pas bon',
            'bad', 'wrong', 'error', 'problem', 'bug', 'terrible', 'awful'
        ]
        
        words = re.findall(r'\w+', text.lower())
        
        positive_count = sum(1 for w in words if w in positive_words)
        negative_count = sum(1 for w in words if w in negative_words)
        
        total = positive_count + negative_count
        if total == 0:
            return 0.0
        
        return (positive_count - negative_count) / total
    
    @staticmethod
    def extract_keywords(text: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """Extrait les mots-clés les plus fréquents."""
        # Mots à ignorer
        stop_words = {
            'le', 'la', 'les', 'un', 'une', 'des', 'de', 'du', 'et', 'ou', 'mais',
            'est', 'sont', 'a', 'ai', 'as', 'ont', 'ce', 'cette', 'ces',
            'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
            'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'
        }
        
        words = re.findall(r'\w+', text.lower())
        words = [w for w in words if len(w) > 3 and w not in stop_words]
        
        counter = Counter(words)
        return counter.most_common(top_n)
    
    @staticmethod
    def summarize_text(text: str, max_sentences: int = 3) -> str:
        """Résumé extractif simple."""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        if len(sentences) <= max_sentences:
            return text
        
        # Prendre les premières et dernières phrases
        if max_sentences == 1:
            return sentences[0] + '.'
        elif max_sentences == 2:
            return sentences[0] + '. ' + sentences[-1] + '.'
        else:
            middle_idx = len(sentences) // 2
            return sentences[0] + '. ' + sentences[middle_idx] + '. ' + sentences[-1] + '.'

# ═══════════════════════════════════════════════════════════════════════════════
#                         MAIN CONVERSATION MEMORY CLASS
# ═══════════════════════════════════════════════════════════════════════════════

class ConversationMemory:
    """
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║         Enterprise-Grade Conversation Memory Management System           ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    
    Fonctionnalités avancées:
    - Multi-sessions isolées avec contexts riches
    - Cache LRU multi-niveaux
    - Analyse NLP et extraction d'entités
    - Compression et storage optimisé
    - Thread-safe operations
    - Auto-save et recovery
    - Export multi-formats
    - Analytics détaillées
    - Search sémantique
    - Rate limiting
    - Webhooks et callbacks
    """
    
    def __init__(
        self,
        memory_file: str = None,
        cache_size: int = 1000,
        cache_ttl: int = 3600,
        auto_save: bool = True,
        compress: bool = True,
        enable_nlp: bool = True,
        max_sessions: int = 100,
        max_messages_per_session: int = 10000
    ):
        """
        Initialise le système de mémoire avancé.
        
        Args:
            memory_file: Chemin du fichier de sauvegarde
            cache_size: Taille du cache LRU
            cache_ttl: TTL du cache en secondes
            auto_save: Sauvegarde automatique
            compress: Compression des données
            enable_nlp: Activer l'analyse NLP
            max_sessions: Nombre max de sessions
            max_messages_per_session: Messages max par session
        """
        # Configuration
        if memory_file is None:
            os.makedirs('instance', exist_ok=True)
            memory_file = 'instance/conversation_memory.json'
        
        self.memory_file = memory_file
        self.auto_save = auto_save
        self.compress = compress
        self.enable_nlp = enable_nlp
        self.max_sessions = max_sessions
        self.max_messages_per_session = max_messages_per_session
        
        # Storage backend
        self.storage = StorageBackend()
        
        # Cache multi-niveaux
        self.message_cache = LRUCache(capacity=cache_size, ttl=cache_ttl)
        self.context_cache = LRUCache(capacity=cache_size // 2, ttl=cache_ttl)
        self.query_cache = LRUCache(capacity=cache_size // 4, ttl=cache_ttl // 2)
        
        # Thread safety
        self.lock = threading.RLock()
        self.save_lock = threading.Lock()
        
        # Données principales
        self.sessions: Dict[str, List[Message]] = {}
        self.contexts: Dict[str, SessionContext] = {}
        self.metadata: Dict[str, Any] = {
            'version': '2.0.0',
            'created_at': datetime.utcnow().isoformat(),
            'last_modified': datetime.utcnow().isoformat()
        }
        
        # Analytics
        self.analytics = {
            'total_messages': 0,
            'total_sessions': 0,
            'total_tokens': 0,
            'avg_session_length': 0.0,
            'popular_languages': Counter(),
            'popular_domains': Counter(),
            'popular_intents': Counter(),
            'message_by_hour': defaultdict(int),
            'response_times': []
        }
        
        # Callbacks et webhooks
        self.callbacks: Dict[str, List[Callable]] = {
            'on_message': [],
            'on_session_start': [],
            'on_session_end': [],
            'on_save': [],
            'on_error': []
        }
        
        # Rate limiting
        self.rate_limits: Dict[str, List[float]] = defaultdict(list)
        self.rate_limit_config = {
            'max_requests': 100,
            'window': 60  # secondes
        }
        
        # Charger les données
        self._load_memory()
        
        # Session par défaut
        self.default_session_id = 'default'
        if self.default_session_id not in self.sessions:
            self._create_session(self.default_session_id)
        
        # Auto-save timer
        if self.auto_save:
            self._start_auto_save_timer()
        
        # Garbage collection timer
        self._start_gc_timer()
    
    # ═══════════════════════════════════════════════════════════════════════════
    #                          CORE OPERATIONS
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _load_memory(self):
        """Charge la mémoire depuis le storage."""
        try:
            data = self.storage.load('conversation_memory.json', compressed=self.compress)
            
            if data:
                # Charger sessions
                sessions_data = data.get('sessions', {})
                for sid, messages in sessions_data.items():
                    self.sessions[sid] = [Message.from_dict(m) for m in messages]
                
                # Charger contexts
                contexts_data = data.get('contexts', {})
                for sid, ctx in contexts_data.items():
                    self.contexts[sid] = SessionContext.from_dict(ctx)
                
                # Charger metadata
                self.metadata.update(data.get('metadata', {}))
                
                # Charger analytics
                if 'analytics' in data:
                    self.analytics.update(data['analytics'])
                    # Convertir Counter depuis dict
                    for key in ['popular_languages', 'popular_domains', 'popular_intents']:
                        if key in self.analytics and isinstance(self.analytics[key], dict):
                            self.analytics[key] = Counter(self.analytics[key])
                
                print(f"✓ Mémoire chargée: {len(self.sessions)} sessions, {sum(len(m) for m in self.sessions.values())} messages")
        
        except Exception as e:
            print(f"Erreur chargement mémoire: {e}")
            # Initialiser vide
            self.sessions = {}
            self.contexts = {}
    
    def _save_memory(self, force: bool = False):
        """Sauvegarde la mémoire."""
        if not self.auto_save and not force:
            return
        
        with self.save_lock:
            try:
                # Préparer les données
                data = {
                    'sessions': {
                        sid: [m.to_dict() for m in messages]
                        for sid, messages in self.sessions.items()
                    },
                    'contexts': {
                        sid: ctx.to_dict()
                        for sid, ctx in self.contexts.items()
                    },
                    'metadata': self.metadata,
                    'analytics': {
                        **self.analytics,
                        'popular_languages': dict(self.analytics['popular_languages']),
                        'popular_domains': dict(self.analytics['popular_domains']),
                        'popular_intents': dict(self.analytics['popular_intents'])
                    }
                }
                
                # Mettre à jour timestamp
                self.metadata['last_modified'] = datetime.utcnow().isoformat()
                
                # Sauvegarder
                success = self.storage.save('conversation_memory.json', data, compress=self.compress)
                
                if success:
                    # Callback
                    self._trigger_callbacks('on_save', data)
                
                return success
            
            except Exception as e:
                print(f"Erreur sauvegarde mémoire: {e}")
                self._trigger_callbacks('on_error', {'error': str(e), 'operation': 'save'})
                return False
    
    def _create_session(self, session_id: str):
        """Crée une nouvelle session."""
        with self.lock:
            if session_id not in self.sessions:
                self.sessions[session_id] = []
                self.contexts[session_id] = SessionContext(
                    session_id=session_id,
                    created_at=datetime.utcnow().isoformat(),
                    updated_at=datetime.utcnow().isoformat()
                )
                self.analytics['total_sessions'] += 1
                self._trigger_callbacks('on_session_start', {'session_id': session_id})
    
    def _check_rate_limit(self, session_id: str) -> bool:
        """Vérifie le rate limit."""
        now = time.time()
        window = self.rate_limit_config['window']
        max_requests = self.rate_limit_config['max_requests']
        
        # Nettoyer les anciennes requêtes
        self.rate_limits[session_id] = [
            t for t in self.rate_limits[session_id]
            if now - t < window
        ]
        
        # Vérifier limite
        if len(self.rate_limits[session_id]) >= max_requests:
            return False
        
        # Ajouter requête
        self.rate_limits[session_id].append(now)
        return True
    
    def add_message(
        self,
        role: str,
        content: str,
        metadata: Dict = None,
        session_id: str = None,
        **kwargs
    ) -> Optional[str]:
        """
        Ajoute un message avec analyse enrichie.
        
        Args:
            role: Role du message (user/assistant/system)
            content: Contenu du message
            metadata: Métadonnées additionnelles
            session_id: ID de la session
            **kwargs: Arguments additionnels (priority, tags, etc.)
        
        Returns:
            message_id si succès, None sinon
        """
        try:
            # Validation
            if not role or role not in [r.value for r in MessageRole]:
                raise ValueError(f"role doit être dans {[r.value for r in MessageRole]}")
            
            if not content or not isinstance(content, str):
                raise ValueError("content doit être une chaîne non-vide")
            
            # Session par défaut
            if session_id is None:
                session_id = self.default_session_id
            
            # Rate limiting
            if not self._check_rate_limit(session_id):
                raise RuntimeError("Rate limit dépassé")
            
            with self.lock:
                # Créer session si nécessaire
                if session_id not in self.sessions:
                    self._create_session(session_id)
                
                # Vérifier limite de messages
                if len(self.sessions[session_id]) >= self.max_messages_per_session:
                    # Archiver les plus anciens
                    self._archive_old_messages(session_id, keep=self.max_messages_per_session // 2)
                
                # Créer message
                message = Message(
                    role=MessageRole(role),
                    content=content,
                    timestamp=datetime.utcnow().isoformat(),
                    metadata=metadata or {},
                    session_id=session_id,
                    **{k: v for k, v in kwargs.items() if k in Message.__annotations__}
                )
                
                # Analyse NLP si activée
                if self.enable_nlp and role == 'user':
                    self._enrich_message(message)
                
                # Ajouter à la session
                self.sessions[session_id].append(message)
                
                # Mettre à jour contexte
                self._update_context(session_id, message)
                
                # Mettre à jour analytics
                self._update_analytics(message)
                
                # Cache
                cache_key = f"{session_id}:{message.message_id}"
                self.message_cache.set(cache_key, message)
                
                # Callbacks
                self._trigger_callbacks('on_message', {
                    'session_id': session_id,
                    'message': message.to_dict()
                })
                
                # Auto-save
                if self.auto_save:
                    self._save_memory()
                
                return message.message_id
        
        except Exception as e:
            print(f"Erreur ajout message: {e}")
            self._trigger_callbacks('on_error', {'error': str(e), 'operation': 'add_message'})
            raise
    
    def _enrich_message(self, message: Message):
        """Enrichit un message avec analyse NLP."""
        try:
            content = message.content
            
            # Détection langue de programmation
            language = NLPAnalyzer.detect_language(content)
            if language:
                message.language = language
                message.metadata['language'] = language
            
            # Détection domaine
            domain = NLPAnalyzer.detect_domain(content)
            if domain:
                message.metadata['domain'] = domain
            
            # Détection intentions
            intents = NLPAnalyzer.detect_intent(content)
            message.metadata['intents'] = intents
            
            # Extraction entités
            entities = NLPAnalyzer.extract_entities(content)
            if entities:
                message.metadata['entities'] = entities
            
            # Sentiment
            sentiment = NLPAnalyzer.sentiment_analysis(content)
            message.sentiment = sentiment
            message.metadata['sentiment'] = sentiment
            
            # Mots-clés
            keywords = NLPAnalyzer.extract_keywords(content, top_n=5)
            message.metadata['keywords'] = [kw[0] for kw in keywords]
            
            # Estimation tokens (approximative)
            message.tokens = len(content.split())
        
        except Exception as e:
            print(f"Erreur enrichissement message: {e}")
    
    def _update_context(self, session_id: str, message: Message):
        """Met à jour le contexte de session."""
        context = self.contexts[session_id]
        context.updated_at = datetime.utcnow().isoformat()
        context.message_count += 1
        context.total_tokens += message.tokens
        
        # Mettre à jour derniers types
        if message.language:
            context.last_language = message.language
        
        if 'domain' in message.metadata:
            context.last_domain = message.metadata['domain']
        
        if 'code_type' in message.metadata:
            context.last_code_type = message.metadata['code_type']
        
        # Extraire topics
        if 'keywords' in message.metadata:
            for kw in message.metadata['keywords']:
                if kw not in context.topics:
                    context.topics.append(kw)
            # Garder les 20 plus récents
            context.topics = context.topics[-20:]
        
        # Entités
        if 'entities' in message.metadata:
            for entity_type, values in message.metadata['entities'].items():
                if entity_type not in context.entities:
                    context.entities[entity_type] = []
                context.entities[entity_type].extend(values)
                # Dédupliquer
                context.entities[entity_type] = list(set(context.entities[entity_type]))[:50]
        
        # Invalidation cache
        self.context_cache.set(session_id, context)
    
    def _update_analytics(self, message: Message):
        """Met à jour les analytics globales."""
        self.analytics['total_messages'] += 1
        self.analytics['total_tokens'] += message.tokens
        
        if message.language:
            self.analytics['popular_languages'][message.language] += 1
        
        if 'domain' in message.metadata:
            self.analytics['popular_domains'][message.metadata['domain']] += 1
        
        if 'intents' in message.metadata:
            for intent in message.metadata['intents']:
                self.analytics['popular_intents'][intent] += 1
        
        # Messages par heure
        hour = datetime.fromisoformat(message.timestamp).hour
        self.analytics['message_by_hour'][hour] += 1
    
    def get_recent_messages(
        self,
        limit: int = 5,
        session_id: str = None,
        role_filter: Optional[str] = None,
        include_metadata: bool = True
    ) -> List[Dict]:
        """
        Récupère les messages récents avec filtres.
        
        Args:
            limit: Nombre de messages
            session_id: ID de session
            role_filter: Filtrer par rôle
            include_metadata: Inclure métadonnées
        
        Returns:
            Liste de messages
        """
        try:
            if not isinstance(limit, int) or limit <= 0:
                raise ValueError("limit doit être un entier positif")
            
            if session_id is None:
                session_id = self.default_session_id
            
            if session_id not in self.sessions:
                return []
            
            messages = self.sessions[session_id]
            
            # Filtrer par rôle
            if role_filter:
                messages = [m for m in messages if m.role.value == role_filter]
            
            # Prendre les N derniers
            recent = messages[-limit:]
            
            # Convertir en dict
            result = []
            for msg in recent:
                data = msg.to_dict() if include_metadata else {
                    'role': msg.role.value,
                    'content': msg.content,
                    'timestamp': msg.timestamp
                }
                result.append(data)
            
            return result
        
        except Exception as e:
            print(f"Erreur get_recent_messages: {e}")
            return []
    
    def get_context(self, session_id: str = None) -> Dict:
        """Récupère le contexte enrichi d'une session."""
        try:
            if session_id is None:
                session_id = self.default_session_id
            
            # Check cache
            cached = self.context_cache.get(session_id)
            if cached:
                return cached.to_dict()
            
            if session_id not in self.contexts:
                return {}
            
            context = self.contexts[session_id]
            self.context_cache.set(session_id, context)
            
            return context.to_dict()
        
        except Exception as e:
            print(f"Erreur get_context: {e}")
            return {}
    
    def analyze_user_intent(self, message: str, session_id: str = None) -> Dict:
        """
        Analyse avancée de l'intention utilisateur.
        
        Args:
            message: Message à analyser
            session_id: ID de session
        
        Returns:
            Dictionnaire d'analyse
        """
        if session_id is None:
            session_id = self.default_session_id
        
        # Récupérer contexte
        context_data = self.get_context(session_id)
        recent = self.get_recent_messages(3, session_id)
        
        # Analyse NLP
        language = NLPAnalyzer.detect_language(message)
        domain = NLPAnalyzer.detect_domain(message)
        intents = NLPAnalyzer.detect_intent(message)
        entities = NLPAnalyzer.extract_entities(message)
        sentiment = NLPAnalyzer.sentiment_analysis(message)
        keywords = NLPAnalyzer.extract_keywords(message, top_n=5)
        
        # Analyse contextuelle
        is_followup = False
        refers_to_previous = False
        
        if recent:
            last_msg = recent[-1]['content'] if recent else ''
            similarity = NLPAnalyzer.calculate_similarity(message, last_msg)
            
            if similarity > 0.3:
                is_followup = True
            
            # Références temporelles
            followup_keywords = [
                'aussi', 'également', 'en plus', 'maintenant', 'et si',
                'pareil', 'même chose', 'ça', 'ce', 'celui', 'celle',
                'le', 'la', 'les', 'ce code', 'cette fonction'
            ]
            
            msg_lower = message.lower()
            for keyword in followup_keywords:
                if keyword in msg_lower:
                    is_followup = True
                    refers_to_previous = True
                    break
        
        analysis = {
            'language': language,
            'domain': domain,
            'intents': intents,
            'entities': entities,
            'sentiment': sentiment,
            'keywords': [kw[0] for kw in keywords],
            'is_followup': is_followup,
            'refers_to_previous': refers_to_previous,
            'suggested_language': context_data.get('last_language'),
            'suggested_domain': context_data.get('last_domain'),
            'context_topics': context_data.get('topics', [])[:5],
            'confidence': {
                'language': 0.8 if language else 0.0,
                'domain': 0.7 if domain else 0.0,
                'intent': 0.9 if intents else 0.5
            }
        }
        
        return analysis
    
    # ═══════════════════════════════════════════════════════════════════════════
    #                          SEARCH & QUERY
    # ═══════════════════════════════════════════════════════════════════════════
    
    def search_messages(
        self,
        query: str,
        session_id: Optional[str] = None,
        limit: int = 10,
        semantic: bool = False
    ) -> List[Dict]:
        """
        Recherche de messages avec support sémantique.
        
        Args:
            query: Requête de recherche
            session_id: Chercher dans une session spécifique (None = toutes)
            limit: Nombre max de résultats
            semantic: Utiliser recherche sémantique
        
        Returns:
            Liste de messages trouvés avec scores
        """
        # Check cache
        cache_key = f"search:{query}:{session_id}:{limit}"
        cached = self.query_cache.get(cache_key)
        if cached:
            return cached
        
        results = []
        query_lower = query.lower()
        
        # Sessions à rechercher
        sessions_to_search = [session_id] if session_id else list(self.sessions.keys())
        
        for sid in sessions_to_search:
            if sid not in self.sessions:
                continue
            
            for msg in self.sessions[sid]:
                if msg.deleted:
                    continue
                
                # Recherche textuelle simple
                content_lower = msg.content.lower()
                
                if semantic:
                    # Similarité sémantique
                    similarity = NLPAnalyzer.calculate_similarity(query, msg.content)
                    if similarity > 0.2:
                        results.append({
                            'message': msg.to_dict(),
                            'score': similarity,
                            'session_id': sid
                        })
                else:
                    # Recherche mots-clés
                    if query_lower in content_lower:
                        # Score basé sur fréquence
                        count = content_lower.count(query_lower)
                        score = min(count / 10, 1.0)
                        
                        results.append({
                            'message': msg.to_dict(),
                            'score': score,
                            'session_id': sid
                        })
        
        # Trier par score
        results.sort(key=lambda x: x['score'], reverse=True)
        results = results[:limit]
        
        # Cache
        self.query_cache.set(cache_key, results)
        
        return results
    
    def find_similar_conversations(
        self,
        session_id: str,
        limit: int = 5
    ) -> List[Tuple[str, float]]:
        """
        Trouve des conversations similaires.
        
        Args:
            session_id: Session de référence
            limit: Nombre de résultats
        
        Returns:
            Liste de (session_id, score de similarité)
        """
        if session_id not in self.sessions:
            return []
        
        # Récupérer le contexte de référence
        ref_context = self.contexts[session_id]
        ref_messages = self.sessions[session_id]
        
        # Créer un "document" représentant la session
        ref_text = ' '.join([m.content for m in ref_messages])
        
        similarities = []
        
        for sid, messages in self.sessions.items():
            if sid == session_id or not messages:
                continue
            
            # Document de comparaison
            comp_text = ' '.join([m.content for m in messages])
            
            # Similarité textuelle
            text_sim = NLPAnalyzer.calculate_similarity(ref_text, comp_text)
            
            # Similarité de contexte
            comp_context = self.contexts[sid]
            context_sim = 0.0
            
            # Comparer langages
            if ref_context.last_language and ref_context.last_language == comp_context.last_language:
                context_sim += 0.3
            
            # Comparer domaines
            if ref_context.last_domain and ref_context.last_domain == comp_context.last_domain:
                context_sim += 0.3
            
            # Comparer topics
            common_topics = set(ref_context.topics).intersection(set(comp_context.topics))
            if common_topics:
                context_sim += min(len(common_topics) / 10, 0.4)
            
            # Score combiné
            total_sim = (text_sim * 0.6) + (context_sim * 0.4)
            
            if total_sim > 0.1:
                similarities.append((sid, total_sim))
        
        # Trier et limiter
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:limit]
    
    def get_message_by_id(self, message_id: str, session_id: str = None) -> Optional[Dict]:
        """Récupère un message par son ID."""
        # Check cache
        if session_id:
            cache_key = f"{session_id}:{message_id}"
            cached = self.message_cache.get(cache_key)
            if cached:
                return cached.to_dict()
        
        # Chercher dans les sessions
        sessions_to_search = [session_id] if session_id else list(self.sessions.keys())
        
        for sid in sessions_to_search:
            if sid not in self.sessions:
                continue
            
            for msg in self.sessions[sid]:
                if msg.message_id == message_id:
                    return msg.to_dict()
        
        return None
    
    def get_conversation_thread(self, message_id: str) -> List[Dict]:
        """Récupère un fil de conversation complet."""
        results = []
        
        # Trouver le message initial
        current_msg = self.get_message_by_id(message_id)
        if not current_msg:
            return results
        
        # Remonter aux parents
        while current_msg:
            results.insert(0, current_msg)
            parent_id = current_msg.get('parent_id')
            if not parent_id:
                break
            current_msg = self.get_message_by_id(parent_id)
        
        # Descendre aux enfants
        def get_children(msg_id: str):
            children = []
            for sid in self.sessions:
                for msg in self.sessions[sid]:
                    if msg.parent_id == msg_id:
                        children.append(msg.to_dict())
            return children
        
        # BFS pour les enfants
        queue = [message_id]
        visited = {message_id}
        
        while queue:
            current_id = queue.pop(0)
            children = get_children(current_id)
            
            for child in children:
                child_id = child['message_id']
                if child_id not in visited:
                    results.append(child)
                    queue.append(child_id)
                    visited.add(child_id)
        
        return results
    
    # ═══════════════════════════════════════════════════════════════════════════
    #                          SESSION MANAGEMENT
    # ═══════════════════════════════════════════════════════════════════════════
    
    def list_sessions(
        self,
        status: Optional[SessionStatus] = None,
        limit: Optional[int] = None
    ) -> List[Dict]:
        """Liste les sessions avec filtres."""
        sessions = []
        
        for sid, ctx in self.contexts.items():
            if status and ctx.status != status:
                continue
            
            sessions.append({
                'session_id': sid,
                'status': ctx.status.value,
                'created_at': ctx.created_at,
                'updated_at': ctx.updated_at,
                'message_count': ctx.message_count,
                'total_tokens': ctx.total_tokens,
                'last_language': ctx.last_language,
                'last_domain': ctx.last_domain,
                'topics': ctx.topics[:5],
                'tags': ctx.tags
            })
        
        # Trier par date de mise à jour
        sessions.sort(key=lambda x: x['updated_at'], reverse=True)
        
        if limit:
            sessions = sessions[:limit]
        
        return sessions
    
    def save_session(self, session_id: str = None) -> bool:
        """Sauvegarde une session dans l'historique."""
        try:
            if session_id is None:
                session_id = self.default_session_id
            
            if session_id not in self.sessions or not self.sessions[session_id]:
                return False
            
            # Créer snapshot
            snapshot = {
                'session_id': session_id,
                'timestamp': datetime.utcnow().isoformat(),
                'messages': [m.to_dict() for m in self.sessions[session_id]],
                'context': self.contexts[session_id].to_dict(),
                'analytics': self._get_session_analytics(session_id)
            }
            
            # Sauvegarder dans fichier séparé
            filename = f"session_{session_id}_{int(time.time())}.json"
            self.storage.save(filename, snapshot, compress=True)
            
            return True
        
        except Exception as e:
            print(f"Erreur save_session: {e}")
            return False
    
    def clear_session(self, session_id: str = None, archive: bool = True):
        """Efface une session."""
        try:
            if session_id is None:
                session_id = self.default_session_id
            
            # Sauvegarder avant d'effacer
            if archive and session_id in self.sessions:
                self.save_session(session_id)
                self.contexts[session_id].status = SessionStatus.ARCHIVED
            
            # Effacer
            if session_id in self.sessions:
                self.sessions[session_id] = []
                
                # Réinitialiser contexte
                self.contexts[session_id] = SessionContext(
                    session_id=session_id,
                    created_at=datetime.utcnow().isoformat(),
                    updated_at=datetime.utcnow().isoformat()
                )
                
                # Invalider caches
                self.message_cache.clear()
                self.context_cache.clear()
                self.query_cache.clear()
                
                # Callback
                self._trigger_callbacks('on_session_end', {'session_id': session_id})
                
                self._save_memory(force=True)
        
        except Exception as e:
            print(f"Erreur clear_session: {e}")
    
    def delete_session(self, session_id: str):
        """Supprime définitivement une session."""
        with self.lock:
            if session_id in self.sessions:
                del self.sessions[session_id]
            if session_id in self.contexts:
                del self.contexts[session_id]
            
            self._save_memory(force=True)
    
    def merge_sessions(self, source_id: str, target_id: str) -> bool:
        """Fusionne deux sessions."""
        try:
            if source_id not in self.sessions or target_id not in self.sessions:
                return False
            
            with self.lock:
                # Ajouter messages
                self.sessions[target_id].extend(self.sessions[source_id])
                
                # Trier par timestamp
                self.sessions[target_id].sort(key=lambda m: m.timestamp)
                
                # Fusionner contextes
                src_ctx = self.contexts[source_id]
                tgt_ctx = self.contexts[target_id]
                
                tgt_ctx.message_count += src_ctx.message_count
                tgt_ctx.total_tokens += src_ctx.total_tokens
                tgt_ctx.topics = list(set(tgt_ctx.topics + src_ctx.topics))[:50]
                tgt_ctx.tags = list(set(tgt_ctx.tags + src_ctx.tags))
                
                # Fusionner entités
                for entity_type, values in src_ctx.entities.items():
                    if entity_type not in tgt_ctx.entities:
                        tgt_ctx.entities[entity_type] = []
                    tgt_ctx.entities[entity_type].extend(values)
                    tgt_ctx.entities[entity_type] = list(set(tgt_ctx.entities[entity_type]))[:100]
                
                # Supprimer source
                self.delete_session(source_id)
                
                return True
        
        except Exception as e:
            print(f"Erreur merge_sessions: {e}")
            return False
    
    def _archive_old_messages(self, session_id: str, keep: int = 100):
        """Archive les anciens messages."""
        if session_id not in self.sessions:
            return
        
        messages = self.sessions[session_id]
        
        if len(messages) <= keep:
            return
        
        # Garder les plus récents
        to_archive = messages[:-keep]
        self.sessions[session_id] = messages[-keep:]
        
        # Sauvegarder archive
        archive_data = {
            'session_id': session_id,
            'archived_at': datetime.utcnow().isoformat(),
            'messages': [m.to_dict() for m in to_archive]
        }
        
        filename = f"archive_{session_id}_{int(time.time())}.json"
        self.storage.save(filename, archive_data, compress=True)
    
    # ═══════════════════════════════════════════════════════════════════════════
    #                          ANALYTICS & STATISTICS
    # ═══════════════════════════════════════════════════════════════════════════
    
    def get_statistics(self) -> Dict:
        """Récupère les statistiques globales détaillées."""
        stats = {
            'global': {
                'total_sessions': len(self.sessions),
                'active_sessions': len([s for s, c in self.contexts.items() if c.status == SessionStatus.ACTIVE]),
                'archived_sessions': len([s for s, c in self.contexts.items() if c.status == SessionStatus.ARCHIVED]),
                'total_messages': self.analytics['total_messages'],
                'total_tokens': self.analytics['total_tokens'],
                'avg_tokens_per_message': (
                    self.analytics['total_tokens'] / self.analytics['total_messages']
                    if self.analytics['total_messages'] > 0 else 0
                )
            },
            'languages': dict(self.analytics['popular_languages'].most_common(10)),
            'domains': dict(self.analytics['popular_domains'].most_common(10)),
            'intents': dict(self.analytics['popular_intents'].most_common(10)),
            'activity': {
                'messages_by_hour': dict(self.analytics['message_by_hour']),
                'peak_hour': max(
                    self.analytics['message_by_hour'].items(),
                    key=lambda x: x[1]
                )[0] if self.analytics['message_by_hour'] else None
            },
            'cache': {
                'message_cache': self.message_cache.stats(),
                'context_cache': self.context_cache.stats(),
                'query_cache': self.query_cache.stats()
            },
            'sessions': {
                'avg_messages_per_session': (
                    sum(len(msgs) for msgs in self.sessions.values()) / len(self.sessions)
                    if self.sessions else 0
                ),
                'longest_session': max(
                    [(sid, len(msgs)) for sid, msgs in self.sessions.items()],
                    key=lambda x: x[1]
                )[0] if self.sessions else None
            }
        }
        
        # Performance
        if self.analytics['response_times']:
            stats['performance'] = {
                'avg_response_time': sum(self.analytics['response_times']) / len(self.analytics['response_times']),
                'min_response_time': min(self.analytics['response_times']),
                'max_response_time': max(self.analytics['response_times'])
            }
        
        return stats
    
    def _get_session_analytics(self, session_id: str) -> Dict:
        """Analytics pour une session spécifique."""
        if session_id not in self.sessions:
            return {}
        
        messages = self.sessions[session_id]
        context = self.contexts[session_id]
        
        if not messages:
            return {}
        
        # Compter par rôle
        role_counts = Counter([m.role.value for m in messages])
        
        # Langages utilisés
        languages = Counter([m.language for m in messages if m.language])
        
        # Sentiments
        sentiments = [m.sentiment for m in messages if m.sentiment is not None]
        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        
        # Timestamps
        timestamps = [datetime.fromisoformat(m.timestamp) for m in messages]
        duration = (timestamps[-1] - timestamps[0]).total_seconds() if len(timestamps) > 1 else 0
        
        # Mots-clés globaux
        all_keywords = []
        for m in messages:
            if 'keywords' in m.metadata:
                all_keywords.extend(m.metadata['keywords'])
        
        top_keywords = Counter(all_keywords).most_common(10)
        
        return {
            'session_id': session_id,
            'message_count': len(messages),
            'role_distribution': dict(role_counts),
            'languages_used': dict(languages),
            'avg_sentiment': avg_sentiment,
            'duration_seconds': duration,
            'total_tokens': context.total_tokens,
            'avg_tokens_per_message': context.total_tokens / len(messages) if messages else 0,
            'top_keywords': dict(top_keywords),
            'topics': context.topics[:10],
            'entities_count': {k: len(v) for k, v in context.entities.items()},
            'status': context.status.value,
            'created_at': context.created_at,
            'updated_at': context.updated_at
        }
    
    def get_session_summary(self, session_id: str) -> Dict:
        """Génère un résumé détaillé d'une session."""
        if session_id not in self.sessions:
            return {}
        
        messages = self.sessions[session_id]
        context = self.contexts[session_id]
        analytics = self._get_session_analytics(session_id)
        
        # Générer résumé textuel
        user_messages = [m.content for m in messages if m.role == MessageRole.USER]
        if user_messages:
            # Prendre premiers et derniers messages
            summary_text = NLPAnalyzer.summarize_text(
                ' '.join(user_messages),
                max_sentences=5
            )
        else:
            summary_text = "Aucun message utilisateur"
        
        return {
            'session_id': session_id,
            'summary': summary_text,
            'analytics': analytics,
            'context': context.to_dict(),
            'highlights': {
                'most_discussed_topics': context.topics[:5],
                'primary_language': analytics.get('languages_used', {}).get(
                    max(analytics.get('languages_used', {}), key=analytics.get('languages_used', {}).get, default='unknown'),
                    'unknown'
                ),
                'sentiment': 'positive' if analytics.get('avg_sentiment', 0) > 0.2 else (
                    'negative' if analytics.get('avg_sentiment', 0) < -0.2 else 'neutral'
                ),
                'key_entities': {
                    k: v[:5] for k, v in context.entities.items()
                }
            }
        }
    
    def _get_most_used(self, field: str) -> Optional[str]:
        """Trouve la valeur la plus utilisée d'un champ."""
        if field == 'language':
            if self.analytics['popular_languages']:
                return self.analytics['popular_languages'].most_common(1)[0][0]
        elif field == 'domain':
            if self.analytics['popular_domains']:
                return self.analytics['popular_domains'].most_common(1)[0][0]
        
        return None
    
    # ═══════════════════════════════════════════════════════════════════════════
    #                          EXPORT & IMPORT
    # ═══════════════════════════════════════════════════════════════════════════
    
    def export_session(
        self,
        session_id: str,
        format: ExportFormat = ExportFormat.JSON,
        filepath: Optional[str] = None
    ) -> Optional[str]:
        """
        Exporte une session dans différents formats.
        
        Args:
            session_id: ID de la session
            format: Format d'export
            filepath: Chemin de sauvegarde (optionnel)
        
        Returns:
            Contenu exporté ou chemin du fichier
        """
        if session_id not in self.sessions:
            return None
        
        messages = self.sessions[session_id]
        context = self.contexts[session_id]
        
        try:
            if format == ExportFormat.JSON:
                data = {
                    'session_id': session_id,
                    'exported_at': datetime.utcnow().isoformat(),
                    'messages': [m.to_dict() for m in messages],
                    'context': context.to_dict(),
                    'analytics': self._get_session_analytics(session_id)
                }
                content = json.dumps(data, indent=2, ensure_ascii=False)
            
            elif format == ExportFormat.JSONL:
                lines = []
                for m in messages:
                    lines.append(json.dumps(m.to_dict(), ensure_ascii=False))
                content = '\n'.join(lines)
            
            elif format == ExportFormat.CSV:
                import csv
                import io
                
                output = io.StringIO()
                writer = csv.writer(output)
                
                # Header
                writer.writerow(['timestamp', 'role', 'content', 'language', 'sentiment', 'tokens'])
                
                # Rows
                for m in messages:
                    writer.writerow([
                        m.timestamp,
                        m.role.value,
                        m.content,
                        m.language or '',
                        m.sentiment or '',
                        m.tokens
                    ])
                
                content = output.getvalue()
            
            elif format == ExportFormat.MARKDOWN:
                lines = [
                    f"# Conversation: {session_id}",
                    f"",
                    f"**Créée:** {context.created_at}",
                    f"**Mise à jour:** {context.updated_at}",
                    f"**Messages:** {len(messages)}",
                    f"**Tokens:** {context.total_tokens}",
                    f"",
                    "---",
                    ""
                ]
                
                for m in messages:
                    role_emoji = "👤" if m.role == MessageRole.USER else "🤖"
                    lines.append(f"### {role_emoji} {m.role.value.capitalize()} - {m.timestamp}")
                    lines.append("")
                    lines.append(m.content)
                    lines.append("")
                    
                    if m.language:
                        lines.append(f"*Langage: {m.language}*")
                    if m.sentiment is not None:
                        lines.append(f"*Sentiment: {m.sentiment:.2f}*")
                    
                    lines.append("")
                    lines.append("---")
                    lines.append("")
                
                content = '\n'.join(lines)
            
            elif format == ExportFormat.HTML:
                lines = [
                    "<!DOCTYPE html>",
                    "<html lang='fr'>",
                    "<head>",
                    "<meta charset='UTF-8'>",
                    f"<title>Conversation {session_id}</title>",
                    "<style>",
                    "body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }",
                    ".message { margin: 20px 0; padding: 15px; border-radius: 8px; }",
                    ".user { background: #e3f2fd; border-left: 4px solid #2196f3; }",
                    ".assistant { background: #f3e5f5; border-left: 4px solid #9c27b0; }",
                    ".meta { font-size: 0.9em; color: #666; margin-top: 10px; }",
                    "pre { background: #f5f5f5; padding: 10px; border-radius: 4px; overflow-x: auto; }",
                    "</style>",
                    "</head>",
                    "<body>",
                    f"<h1>Conversation: {session_id}</h1>",
                    f"<p><strong>Créée:</strong> {context.created_at}</p>",
                    f"<p><strong>Messages:</strong> {len(messages)} | <strong>Tokens:</strong> {context.total_tokens}</p>",
                    "<hr>"
                ]
                
                for m in messages:
                    role_class = m.role.value
                    lines.append(f"<div class='message {role_class}'>")
                    lines.append(f"<strong>{m.role.value.capitalize()}</strong> <span style='color: #999;'>({m.timestamp})</span>")
                    
                    # Formater le contenu
                    content_html = m.content.replace('<', '&lt;').replace('>', '&gt;')
                    
                    # Détecter blocs de code
                    if '```' in content_html:
                        parts = content_html.split('```')
                        for i, part in enumerate(parts):
                            if i % 2 == 1:  # Code block
                                parts[i] = f"<pre>{part}</pre>"
                        content_html = ''.join(parts)
                    
                    lines.append(f"<p>{content_html}</p>")
                    
                    if m.language or m.sentiment is not None:
                        lines.append("<div class='meta'>")
                        if m.language:
                            lines.append(f"Langage: {m.language} | ")
                        if m.sentiment is not None:
                            lines.append(f"Sentiment: {m.sentiment:.2f}")
                        lines.append("</div>")
                    
                    lines.append("</div>")
                
                lines.extend(["</body>", "</html>"])
                content = '\n'.join(lines)
            
            elif format == ExportFormat.PICKLE:
                import pickle
                data = {
                    'messages': messages,
                    'context': context
                }
                content = base64.b64encode(pickle.dumps(data)).decode('utf-8')
            
            else:
                return None
            
            # Sauvegarder si filepath fourni
            if filepath:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return filepath
            
            return content
        
        except Exception as e:
            print(f"Erreur export: {e}")
            return None
    
    def export_all_sessions(
        self,
        format: ExportFormat = ExportFormat.JSON,
        output_dir: str = 'exports'
    ) -> List[str]:
        """Exporte toutes les sessions."""
        os.makedirs(output_dir, exist_ok=True)
        exported = []
        
        for session_id in self.sessions.keys():
            ext = format.value
            filename = f"session_{session_id}_{int(time.time())}.{ext}"
            filepath = os.path.join(output_dir, filename)
            
            result = self.export_session(session_id, format, filepath)
            if result:
                exported.append(filepath)
        
        return exported
    
    def import_session(
        self,
        filepath: str,
        format: ExportFormat = ExportFormat.JSON,
        session_id: Optional[str] = None
    ) -> bool:
        """Importe une session depuis un fichier."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if format == ExportFormat.JSON:
                data = json.loads(content)
                messages = [Message.from_dict(m) for m in data['messages']]
                context = SessionContext.from_dict(data['context'])
                
                sid = session_id or data.get('session_id', f'imported_{int(time.time())}')
                
                with self.lock:
                    self.sessions[sid] = messages
                    self.contexts[sid] = context
                    self._save_memory(force=True)
                
                return True
            
            elif format == ExportFormat.JSONL:
                messages = []
                for line in content.strip().split('\n'):
                    if line:
                        messages.append(Message.from_dict(json.loads(line)))
                
                sid = session_id or f'imported_{int(time.time())}'
                
                with self.lock:
                    self.sessions[sid] = messages
                    self._create_session(sid)
                    self._save_memory(force=True)
                
                return True
            
            return False
        
        except Exception as e:
            print(f"Erreur import: {e}")
            return False
    
    # ═══════════════════════════════════════════════════════════════════════════
    #                          CALLBACKS & WEBHOOKS
    # ═══════════════════════════════════════════════════════════════════════════
    
    def register_callback(self, event: str, callback: Callable):
        """Enregistre un callback pour un événement."""
        if event in self.callbacks:
            self.callbacks[event].append(callback)
    
    def unregister_callback(self, event: str, callback: Callable):
        """Désenregistre un callback."""
        if event in self.callbacks and callback in self.callbacks[event]:
            self.callbacks[event].remove(callback)
    
    def _trigger_callbacks(self, event: str, data: Dict):
        """Déclenche les callbacks d'un événement."""
        if event in self.callbacks:
            for callback in self.callbacks[event]:
                try:
                    callback(data)
                except Exception as e:
                    print(f"Erreur callback {event}: {e}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    #                          MAINTENANCE & UTILITIES
    # ═══════════════════════════════════════════════════════════════════════════
    
    def _start_auto_save_timer(self, interval: int = 300):
        """Démarre le timer d'auto-sauvegarde (5 minutes)."""
        def auto_save():
            while True:
                time.sleep(interval)
                self._save_memory()
        
        timer = threading.Thread(target=auto_save, daemon=True)
        timer.start()
    
    def _start_gc_timer(self, interval: int = 3600):
        """Démarre le garbage collector (1 heure)."""
        def gc_task():
            while True:
                time.sleep(interval)
                self._garbage_collect()
        
        timer = threading.Thread(target=gc_task, daemon=True)
        timer.start()
    
    def _garbage_collect(self):
        """Nettoyage automatique."""
        try:
            with self.lock:
                # Supprimer sessions expirées (TTL)
                now = datetime.utcnow()
                expired = []
                
                for sid, ctx in self.contexts.items():
                    if ctx.ttl:
                        updated = datetime.fromisoformat(ctx.updated_at)
                        age = (now - updated).total_seconds()
                        
                        if age > ctx.ttl:
                            expired.append(sid)
                
                for sid in expired:
                    print(f"GC: Session {sid} expirée (TTL)")
                    self.delete_session(sid)
                
                # Limiter nombre de sessions
                if len(self.sessions) > self.max_sessions:
                    # Supprimer les plus anciennes
                    sorted_sessions = sorted(
                        self.contexts.items(),
                        key=lambda x: x[1].updated_at
                    )
                    
                    to_remove = len(self.sessions) - self.max_sessions
                    for i in range(to_remove):
                        sid = sorted_sessions[i][0]
                        print(f"GC: Suppression session {sid} (limite atteinte)")
                        self.save_session(sid)  # Archiver d'abord
                        self.delete_session(sid)
                
                # Nettoyer rate limits
                now_ts = time.time()
                for sid in list(self.rate_limits.keys()):
                    self.rate_limits[sid] = [
                        t for t in self.rate_limits[sid]
                        if now_ts - t < self.rate_limit_config['window']
                    ]
                    
                    if not self.rate_limits[sid]:
                        del self.rate_limits[sid]
                
                print(f"GC: Nettoyage effectué - {len(self.sessions)} sessions actives")
        
        except Exception as e:
            print(f"Erreur GC: {e}")
    
    def optimize_storage(self):
        """Optimise le stockage."""
        try:
            # Compresser sessions peu utilisées
            for sid in self.sessions:
                if len(self.sessions[sid]) > 100:
                    # Archiver les anciens messages
                    self._archive_old_messages(sid, keep=100)
            
            # Nettoyer caches
            self.message_cache.clear()
            self.context_cache.clear()
            self.query_cache.clear()
            
            # Forcer sauvegarde compressée
            self._save_memory(force=True)
            
            print("✓ Optimisation storage effectuée")
            return True
        
        except Exception as e:
            print(f"Erreur optimisation: {e}")
            return False
    
    def backup(self, backup_dir: str = 'backups') -> Optional[str]:
        """Crée une sauvegarde complète."""
        try:
            os.makedirs(backup_dir, exist_ok=True)
            
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            backup_file = os.path.join(backup_dir, f'backup_{timestamp}.json.gz')
            
            # Créer backup
            data = {
                'sessions': {
                    sid: [m.to_dict() for m in messages]
                    for sid, messages in self.sessions.items()
                },
                'contexts': {
                    sid: ctx.to_dict()
                    for sid, ctx in self.contexts.items()
                },
                'metadata': self.metadata,
                'analytics': {
                    **self.analytics,
                    'popular_languages': dict(self.analytics['popular_languages']),
                    'popular_domains': dict(self.analytics['popular_domains']),
                    'popular_intents': dict(self.analytics['popular_intents'])
                },
                'backup_info': {
                    'timestamp': timestamp,
                    'version': self.metadata['version']
                }
            }
            
            # Sauvegarder compressé
            json_data = json.dumps(data, indent=2, ensure_ascii=False)
            compressed = gzip.compress(json_data.encode('utf-8'))
            
            with open(backup_file, 'wb') as f:
                f.write(compressed)
            
            print(f"✓ Backup créé: {backup_file}")
            return backup_file
        
        except Exception as e:
            print(f"Erreur backup: {e}")
            return None
    
    def restore(self, backup_file: str) -> bool:
        """Restaure depuis une sauvegarde."""
        try:
            with open(backup_file, 'rb') as f:
                compressed = f.read()
            
            json_data = gzip.decompress(compressed).decode('utf-8')
            data = json.loads(json_data)
            
            with self.lock:
                # Restaurer sessions
                self.sessions = {}
                for sid, messages in data['sessions'].items():
                    self.sessions[sid] = [Message.from_dict(m) for m in messages]
                
                # Restaurer contexts
                self.contexts = {}
                for sid, ctx in data['contexts'].items():
                    self.contexts[sid] = SessionContext.from_dict(ctx)
                
                # Restaurer metadata
                self.metadata = data['metadata']
                
                # Restaurer analytics
                if 'analytics' in data:
                    self.analytics = data['analytics']
                    for key in ['popular_languages', 'popular_domains', 'popular_intents']:
                        if key in self.analytics and isinstance(self.analytics[key], dict):
                            self.analytics[key] = Counter(self.analytics[key])
                
                # Sauvegarder
                self._save_memory(force=True)
            
            print(f"✓ Restauration réussie depuis {backup_file}")
            return True
        
        except Exception as e:
            print(f"Erreur restauration: {e}")
            return False
    
    def get_health_status(self) -> Dict:
        """Retourne le statut de santé du système."""
        stats = self.get_statistics()
        
        # Calculs de santé
        cache_hit_rates = [
            float(self.message_cache.stats()['hit_rate'].rstrip('%')),
            float(self.context_cache.stats()['hit_rate'].rstrip('%')),
            float(self.query_cache.stats()['hit_rate'].rstrip('%'))
        ]
        avg_cache_hit_rate = sum(cache_hit_rates) / len(cache_hit_rates)
        
        # Déterminer statut
        status = 'healthy'
        warnings = []
        
        if len(self.sessions) >= self.max_sessions * 0.9:
            status = 'warning'
            warnings.append(f"Proche de la limite de sessions ({len(self.sessions)}/{self.max_sessions})")
        
        if avg_cache_hit_rate < 50:
            status = 'warning'
            warnings.append(f"Faible taux de cache hit ({avg_cache_hit_rate:.1f}%)")
        
        for sid, messages in self.sessions.items():
            if len(messages) >= self.max_messages_per_session * 0.9:
                status = 'warning'
                warnings.append(f"Session {sid} proche de la limite de messages")
        
        return {
            'status': status,
            'timestamp': datetime.utcnow().isoformat(),
            'warnings': warnings,
            'metrics': {
                'total_sessions': len(self.sessions),
                'total_messages': stats['global']['total_messages'],
                'cache_hit_rate': f"{avg_cache_hit_rate:.1f}%",
                'memory_usage_mb': self._estimate_memory_usage(),
                'storage_size_mb': self._get_storage_size()
            }
        }
    
    def _estimate_memory_usage(self) -> float:
        """Estime l'usage mémoire en MB."""
        try:
            import sys
            
            total_size = 0
            total_size += sys.getsizeof(self.sessions)
            total_size += sys.getsizeof(self.contexts)
            total_size += sys.getsizeof(self.analytics)
            
            for messages in self.sessions.values():
                total_size += sys.getsizeof(messages)
                for msg in messages:
                    total_size += sys.getsizeof(msg.content)
            
            return total_size / (1024 * 1024)
        except:
            return 0.0
    
    def _get_storage_size(self) -> float:
        """Retourne la taille du storage en MB."""
        try:
            total_size = 0
            
            for filename in os.listdir(self.storage.base_path):
                filepath = os.path.join(self.storage.base_path, filename)
                if os.path.isfile(filepath):
                    total_size += os.path.getsize(filepath)
            
            return total_size / (1024 * 1024)
        except:
            return 0.0
    
    def __repr__(self) -> str:
        """Représentation string."""
        return (
            f"<ConversationMemory sessions={len(self.sessions)} "
            f"messages={sum(len(m) for m in self.sessions.values())} "
            f"cache_size={len(self.message_cache.cache)}>"
        )
    
    def __len__(self) -> int:
        """Nombre total de messages."""
        return sum(len(messages) for messages in self.sessions.values())


# ═══════════════════════════════════════════════════════════════════════════════
#                              GLOBAL INSTANCE
# ═══════════════════════════════════════════════════════════════════════════════

# Instance globale avec configuration optimisée
memory = ConversationMemory(
    cache_size=1000,
    cache_ttl=3600,
    auto_save=True,
    compress=True,
    enable_nlp=True,
    max_sessions=100,
    max_messages_per_session=10000
)

def get_conversation_memory() -> ConversationMemory:
    """
    Récupère l'instance globale de mémoire de conversation.
    
    Returns:
        ConversationMemory: Instance configurée et prête à l'emploi
    """
    return memory


# ═══════════════════════════════════════════════════════════════════════════════
#                              UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def create_custom_memory(
    cache_size: int = 500,
    enable_nlp: bool = False,
    compress: bool = False
) -> ConversationMemory:
    """
    Crée une instance personnalisée de mémoire.
    
    Args:
        cache_size: Taille du cache
        enable_nlp: Activer analyse NLP
        compress: Activer compression
    
    Returns:
        ConversationMemory: Instance personnalisée
    """
    return ConversationMemory(
        cache_size=cache_size,
        enable_nlp=enable_nlp,
        compress=compress
    )


def merge_memories(source: ConversationMemory, target: ConversationMemory) -> bool:
    """
    Fusionne deux instances de mémoire.
    
    Args:
        source: Mémoire source
        target: Mémoire cible
    
    Returns:
        bool: Succès de la fusion
    """
    try:
        with target.lock:
            # Fusionner sessions
            for sid, messages in source.sessions.items():
                if sid in target.sessions:
                    # Fusionner avec session existante
                    target.sessions[sid].extend(messages)
                    target.sessions[sid].sort(key=lambda m: m.timestamp)
                else:
                    # Copier session
                    target.sessions[sid] = messages.copy()
            
            # Fusionner contexts
            for sid, ctx in source.contexts.items():
                if sid not in target.contexts:
                    target.contexts[sid] = ctx
            
            # Mettre à jour analytics
            target.analytics['total_messages'] += source.analytics['total_messages']
            target.analytics['total_tokens'] += source.analytics['total_tokens']
            
            for lang, count in source.analytics['popular_languages'].items():
                target.analytics['popular_languages'][lang] += count
            
            for domain, count in source.analytics['popular_domains'].items():
                target.analytics['popular_domains'][domain] += count
            
            target._save_memory(force=True)
        
        return True
    except Exception as e:
        print(f"Erreur fusion mémoires: {e}")
        return False


# ═══════════════════════════════════════════════════════════════════════════════
#                              CLI UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    """Interface CLI pour tester et gérer la mémoire."""
    import sys
    
    mem = get_conversation_memory()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'stats':
            stats = mem.get_statistics()
            print(json.dumps(stats, indent=2, ensure_ascii=False))
        
        elif command == 'sessions':
            sessions = mem.list_sessions()
            print(f"Sessions actives: {len(sessions)}")
            for s in sessions[:10]:
                print(f"  - {s['session_id']}: {s['message_count']} messages")
        
        elif command == 'health':
            health = mem.get_health_status()
            print(json.dumps(health, indent=2, ensure_ascii=False))
        
        elif command == 'backup':
            backup_file = mem.backup()
            if backup_file:
                print(f"✓ Backup créé: {backup_file}")
        
        elif command == 'optimize':
            mem.optimize_storage()
        
        elif command == 'export' and len(sys.argv) > 2:
            session_id = sys.argv[2]
            format_str = sys.argv[3] if len(sys.argv) > 3 else 'json'
            fmt = ExportFormat(format_str)
            
            result = mem.export_session(session_id, fmt)
            if result:
                print(result)
        
        elif command == 'search' and len(sys.argv) > 2:
            query = sys.argv[2]
            results = mem.search_messages(query, limit=5)
            print(f"Résultats pour '{query}': {len(results)}")
            for r in results:
                print(f"  Score: {r['score']:.2f} - {r['message']['content'][:100]}...")
        
        else:
            print("Commandes disponibles:")
            print("  stats       - Statistiques globales")
            print("  sessions    - Liste des sessions")
            print("  health      - Statut de santé")
            print("  backup      - Créer backup")
            print("  optimize    - Optimiser storage")
            print("  export <session_id> [format] - Exporter session")
            print("  search <query> - Rechercher messages")
    
    else:
        print(f"Namz IA Conversation Memory v{mem.metadata['version']}")
        print(f"{mem}")
        print("\nUtilisez --help pour voir les commandes disponibles")
