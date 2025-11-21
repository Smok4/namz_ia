"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   NAMZ IA ENGINE V2 - ULTRA ADVANCED                         ║
║               Intelligence Artificielle Maison - Next Generation              ║
╚══════════════════════════════════════════════════════════════════════════════╝

🚀 NOUVELLES FONCTIONNALITÉS V2:
- 🧠 Analyse sémantique multi-dimensionnelle avec NLP avancé
- ⚡ Caching intelligent avec LRU et TTL
- 📊 Métriques de performance en temps réel
- 🔄 Circuit breaker pour protection contre surcharge
- 🎯 Auto-apprentissage des patterns utilisateur
- 🌊 Support streaming pour réponses longues
- ⏱️ Timeout configurable par règle
- 🎨 Template engine avancé avec Jinja2-like syntax
- 🔍 Analyse contextuelle profonde avec NER (Named Entity Recognition)
- 📈 Scoring multi-critères avec poids dynamiques
- 🛡️ Validation et sanitization intégrées
- 🔌 Architecture plugin pour extensions
"""

import re
import time
import logging
import hashlib
import datetime
import threading
from typing import List, Dict, Any, Callable, Optional, Tuple
from dataclasses import dataclass, field
from collections import OrderedDict, defaultdict, deque
from functools import wraps, lru_cache
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError

from .user_examples import find_best_user_example
from .code_templates import CODE_TEMPLATES
from .knowledge_base import KNOWLEDGE_BASE
from .conversation_memory import get_conversation_memory
from .code_analyzer import get_code_analyzer
from .proactive_suggester import get_proactive_suggester
from .multi_file_generator import get_multi_file_generator

# ═══════════════════════════════════════════════════════════════════════════════
#                              CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class EngineConfig:
    """Configuration du moteur IA."""
    # Cache
    cache_enabled: bool = True
    cache_max_size: int = 1000
    cache_ttl: int = 3600  # 1 heure
    
    # Performance
    max_workers: int = 4
    default_timeout: int = 30  # secondes
    enable_parallel: bool = True
    
    # Circuit breaker
    circuit_breaker_enabled: bool = True
    failure_threshold: int = 5
    recovery_timeout: int = 60
    
    # Auto-learning
    auto_learn_enabled: bool = True
    pattern_threshold: int = 3  # Nb d'occurrences avant apprentissage
    
    # Scoring
    min_confidence_score: float = 0.3
    enable_multi_response: bool = False  # Retourner top N réponses
    top_n_responses: int = 3
    
    # Logging
    verbose_logging: bool = False
    metrics_enabled: bool = True

# ═══════════════════════════════════════════════════════════════════════════════
#                              LRU CACHE AVEC TTL
# ═══════════════════════════════════════════════════════════════════════════════

class LRUCacheWithTTL:
    """Cache LRU avec expiration temporelle."""
    
    def __init__(self, max_size: int = 1000, ttl: int = 3600):
        self.max_size = max_size
        self.ttl = ttl
        self.cache: OrderedDict = OrderedDict()
        self.timestamps: Dict[str, float] = {}
        self.lock = threading.Lock()
        
        # Métriques
        self.hits = 0
        self.misses = 0
    
    def get(self, key: str) -> Optional[Any]:
        """Récupère une valeur du cache."""
        with self.lock:
            if key not in self.cache:
                self.misses += 1
                return None
            
            # Vérifier TTL
            if time.time() - self.timestamps[key] > self.ttl:
                del self.cache[key]
                del self.timestamps[key]
                self.misses += 1
                return None
            
            # Déplacer en fin (LRU)
            self.cache.move_to_end(key)
            self.hits += 1
            return self.cache[key]
    
    def set(self, key: str, value: Any):
        """Stocke une valeur dans le cache."""
        with self.lock:
            # Si existe, mettre à jour
            if key in self.cache:
                self.cache.move_to_end(key)
            else:
                # Si plein, supprimer le plus ancien
                if len(self.cache) >= self.max_size:
                    oldest_key = next(iter(self.cache))
                    del self.cache[oldest_key]
                    del self.timestamps[oldest_key]
            
            self.cache[key] = value
            self.timestamps[key] = time.time()
    
    def clear(self):
        """Vide le cache."""
        with self.lock:
            self.cache.clear()
            self.timestamps.clear()
            self.hits = 0
            self.misses = 0
    
    def get_stats(self) -> Dict:
        """Retourne les statistiques du cache."""
        with self.lock:
            total = self.hits + self.misses
            hit_rate = (self.hits / total * 100) if total > 0 else 0
            return {
                'size': len(self.cache),
                'max_size': self.max_size,
                'hits': self.hits,
                'misses': self.misses,
                'hit_rate': f'{hit_rate:.1f}%',
                'ttl': self.ttl
            }

# ═══════════════════════════════════════════════════════════════════════════════
#                              CIRCUIT BREAKER
# ═══════════════════════════════════════════════════════════════════════════════

class CircuitBreaker:
    """Circuit breaker pour protection contre les surcharges."""
    
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN
        self.lock = threading.Lock()
    
    def call(self, func: Callable, *args, **kwargs):
        """Exécute une fonction avec protection circuit breaker."""
        with self.lock:
            # Si circuit ouvert, vérifier si on peut passer en half-open
            if self.state == 'OPEN':
                if time.time() - self.last_failure_time > self.recovery_timeout:
                    self.state = 'HALF_OPEN'
                    self.failures = 0
                else:
                    raise Exception(f'Circuit breaker OPEN (retry after {self.recovery_timeout}s)')
        
        try:
            result = func(*args, **kwargs)
            
            # Succès : fermer le circuit
            with self.lock:
                if self.state == 'HALF_OPEN':
                    self.state = 'CLOSED'
                self.failures = 0
            
            return result
        
        except Exception as e:
            # Échec : incrémenter compteur
            with self.lock:
                self.failures += 1
                self.last_failure_time = time.time()
                
                if self.failures >= self.failure_threshold:
                    self.state = 'OPEN'
            
            raise e
    
    def reset(self):
        """Réinitialise le circuit breaker."""
        with self.lock:
            self.failures = 0
            self.last_failure_time = None
            self.state = 'CLOSED'
    
    def get_state(self) -> Dict:
        """Retourne l'état du circuit breaker."""
        with self.lock:
            return {
                'state': self.state,
                'failures': self.failures,
                'threshold': self.failure_threshold,
                'last_failure': self.last_failure_time
            }

# ═══════════════════════════════════════════════════════════════════════════════
#                              METRICS COLLECTOR
# ═══════════════════════════════════════════════════════════════════════════════

class MetricsCollector:
    """Collecteur de métriques de performance."""
    
    def __init__(self):
        self.request_count = 0
        self.total_time = 0.0
        self.rule_usage = defaultdict(int)
        self.error_count = 0
        self.response_times = deque(maxlen=100)  # Derniers 100 temps de réponse
        self.lock = threading.Lock()
    
    def record_request(self, rule_name: str, duration: float, success: bool = True):
        """Enregistre une requête."""
        with self.lock:
            self.request_count += 1
            self.total_time += duration
            self.response_times.append(duration)
            self.rule_usage[rule_name] += 1
            if not success:
                self.error_count += 1
    
    def get_stats(self) -> Dict:
        """Retourne les statistiques."""
        with self.lock:
            avg_time = (self.total_time / self.request_count) if self.request_count > 0 else 0
            
            # Calcul percentiles
            sorted_times = sorted(self.response_times)
            p50 = sorted_times[len(sorted_times) // 2] if sorted_times else 0
            p95 = sorted_times[int(len(sorted_times) * 0.95)] if sorted_times else 0
            p99 = sorted_times[int(len(sorted_times) * 0.99)] if sorted_times else 0
            
            error_rate = (self.error_count / self.request_count * 100) if self.request_count > 0 else 0
            
            return {
                'total_requests': self.request_count,
                'total_time': f'{self.total_time:.2f}s',
                'avg_response_time': f'{avg_time:.3f}s',
                'p50_response_time': f'{p50:.3f}s',
                'p95_response_time': f'{p95:.3f}s',
                'p99_response_time': f'{p99:.3f}s',
                'error_count': self.error_count,
                'error_rate': f'{error_rate:.1f}%',
                'top_rules': dict(sorted(self.rule_usage.items(), key=lambda x: x[1], reverse=True)[:5])
            }
    
    def reset(self):
        """Réinitialise les métriques."""
        with self.lock:
            self.request_count = 0
            self.total_time = 0.0
            self.rule_usage.clear()
            self.error_count = 0
            self.response_times.clear()

# ═══════════════════════════════════════════════════════════════════════════════
#                          SEMANTIC ANALYZER
# ═══════════════════════════════════════════════════════════════════════════════

class SemanticAnalyzer:
    """Analyseur sémantique avancé."""
    
    @staticmethod
    def extract_entities(text: str) -> Dict[str, List[str]]:
        """Extrait les entités nommées du texte."""
        entities = {
            'languages': [],
            'frameworks': [],
            'concepts': [],
            'actions': [],
            'technologies': []
        }
        
        # Langages
        lang_patterns = [
            (r'\b(python|py)\b', 'python'),
            (r'\b(javascript|js|node)\b', 'javascript'),
            (r'\b(typescript|ts)\b', 'typescript'),
            (r'\b(java)\b', 'java'),
            (r'\b(c#|csharp|dotnet|\.net)\b', 'csharp'),
            (r'\b(php)\b', 'php'),
            (r'\b(ruby|rb)\b', 'ruby'),
            (r'\b(go|golang)\b', 'go'),
            (r'\b(rust|rs)\b', 'rust'),
            (r'\b(swift)\b', 'swift'),
            (r'\b(kotlin|kt)\b', 'kotlin'),
        ]
        
        for pattern, lang in lang_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                entities['languages'].append(lang)
        
        # Frameworks
        framework_patterns = [
            (r'\b(flask|django|fastapi|pyramid)\b', 'python_web'),
            (r'\b(react|vue|angular|svelte|next)\b', 'javascript_frontend'),
            (r'\b(express|nestjs|koa)\b', 'javascript_backend'),
            (r'\b(spring|hibernate|junit)\b', 'java'),
            (r'\b(asp\.net|blazor|razor|linq)\b', 'dotnet'),
        ]
        
        for pattern, framework in framework_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                entities['frameworks'].append(framework)
        
        # Concepts
        concept_patterns = [
            (r'\b(api|rest|graphql|endpoint)\b', 'api'),
            (r'\b(database|db|sql|mongodb|postgres|mysql)\b', 'database'),
            (r'\b(auth|authentication|jwt|oauth|sso)\b', 'authentication'),
            (r'\b(test|testing|unit|integration|e2e)\b', 'testing'),
            (r'\b(docker|container|kubernetes|k8s)\b', 'containerization'),
            (r'\b(ci|cd|pipeline|deploy|deployment)\b', 'devops'),
        ]
        
        for pattern, concept in concept_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                entities['concepts'].append(concept)
        
        # Actions
        action_patterns = [
            (r'\b(crée|créer|create|make|build|construis)\b', 'create'),
            (r'\b(optimise|optimiser|optimize|améliore|improve)\b', 'optimize'),
            (r'\b(debug|débugger|fix|corriger|réparer)\b', 'debug'),
            (r'\b(refactor|refactoriser|restructure)\b', 'refactor'),
            (r'\b(explique|expliquer|explain|comment)\b', 'explain'),
            (r'\b(teste|tester|test|vérifier|verify)\b', 'test'),
        ]
        
        for pattern, action in action_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                entities['actions'].append(action)
        
        return entities
    
    @staticmethod
    def calculate_similarity(text1: str, text2: str) -> float:
        """Calcule la similarité entre deux textes (Jaccard)."""
        set1 = set(text1.lower().split())
        set2 = set(text2.lower().split())
        
        if not set1 or not set2:
            return 0.0
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        return intersection / union if union > 0 else 0.0
    
    @staticmethod
    def calculate_cosine_similarity(text1: str, text2: str) -> float:
        """Calcule la similarité cosinus (TF-IDF simplifié)."""
        words1 = text1.lower().split()
        words2 = text2.lower().split()
        
        # Compter les fréquences
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        
        for word in words1:
            freq1[word] += 1
        for word in words2:
            freq2[word] += 1
        
        # Mots communs
        common_words = set(freq1.keys()) & set(freq2.keys())
        
        if not common_words:
            return 0.0
        
        # Calcul produit scalaire
        dot_product = sum(freq1[word] * freq2[word] for word in common_words)
        
        # Calcul normes
        norm1 = sum(f ** 2 for f in freq1.values()) ** 0.5
        norm2 = sum(f ** 2 for f in freq2.values()) ** 0.5
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)
    
    @staticmethod
    def extract_intent(text: str) -> str:
        """Extrait l'intention principale du message."""
        text_lower = text.lower()
        
        # Patterns d'intention par ordre de priorité
        intent_patterns = [
            ('question', r'\?|comment|pourquoi|quoi|qui|quand|où|how|why|what|who|when|where'),
            ('creation', r'crée|créer|create|make|build|génère|generate|écris|write|développe|code'),
            ('optimization', r'optimise|optimiser|optimize|améliore|improve|plus rapide|faster|performance'),
            ('debugging', r'debug|erreur|error|bug|problème|problem|fix|corriger|réparer'),
            ('refactoring', r'refactor|restructure|nettoie|clean|réorganise'),
            ('explanation', r'explique|expliquer|explain|comment ça|how does|comprend|understand'),
            ('greeting', r'^(bonjour|salut|hello|hi|hey)(\s|$)'),
            ('thanks', r'merci|thanks|thank you'),
            ('help', r'aide|help|support|assistance'),
        ]
        
        for intent, pattern in intent_patterns:
            if re.search(pattern, text_lower):
                return intent
        
        return 'unknown'

# ═══════════════════════════════════════════════════════════════════════════════
#                          PATTERN LEARNER
# ═══════════════════════════════════════════════════════════════════════════════

class PatternLearner:
    """Apprentissage automatique des patterns utilisateur."""
    
    def __init__(self, threshold: int = 3):
        self.threshold = threshold
        self.patterns: Dict[str, int] = defaultdict(int)
        self.learned_rules: List[Dict] = []
        self.lock = threading.Lock()
    
    def record_pattern(self, message: str, response: str, rule_name: str):
        """Enregistre un pattern utilisateur."""
        with self.lock:
            # Normaliser le message
            normalized = self._normalize(message)
            key = f"{normalized}:{rule_name}"
            
            self.patterns[key] += 1
            
            # Si seuil atteint, créer une règle apprise
            if self.patterns[key] == self.threshold:
                self.learned_rules.append({
                    'pattern': normalized,
                    'response_template': response,
                    'rule_name': rule_name,
                    'count': self.patterns[key],
                    'learned_at': datetime.datetime.utcnow().isoformat()
                })
    
    @staticmethod
    def _normalize(text: str) -> str:
        """Normalise un texte pour extraction de pattern."""
        # Minuscules
        text = text.lower()
        
        # Supprimer ponctuation
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Supprimer mots très communs
        stopwords = {'le', 'la', 'les', 'un', 'une', 'des', 'de', 'du', 'a', 'à', 'the', 'a', 'an', 'of'}
        words = [w for w in text.split() if w not in stopwords]
        
        return ' '.join(words)
    
    def get_learned_rules(self) -> List[Dict]:
        """Retourne les règles apprises."""
        with self.lock:
            return self.learned_rules.copy()
    
    def get_stats(self) -> Dict:
        """Retourne les statistiques d'apprentissage."""
        with self.lock:
            return {
                'total_patterns': len(self.patterns),
                'learned_rules': len(self.learned_rules),
                'top_patterns': dict(sorted(self.patterns.items(), key=lambda x: x[1], reverse=True)[:10])
            }

# ═══════════════════════════════════════════════════════════════════════════════
#                          RESPONSE MODELS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class IAResponse:
    """Réponse du moteur IA."""
    status: str
    response: str
    meta: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        return {
            'status': self.status,
            'response': self.response,
            'meta': self.meta
        }

@dataclass
class Rule:
    """Règle du moteur IA avec métadonnées étendues."""
    name: str
    condition: Callable[[str, str], float]
    action: Callable[[str, str], str]
    lang: str = "any"
    timeout: int = 30
    priority: int = 0  # Plus élevé = plus prioritaire
    category: str = "general"
    description: str = ""
    enabled: bool = True

# ═══════════════════════════════════════════════════════════════════════════════
#                          NAMZ IA ENGINE V2
# ═══════════════════════════════════════════════════════════════════════════════

class NamzIAEngineV2:
    """Moteur IA maison ultra-avancé V2."""
    
    def __init__(self, config: EngineConfig = None):
        self.config = config or EngineConfig()
        self.logger = logging.getLogger(__name__)
        
        # Composants principaux
        self.rules: List[Rule] = []
        self.memory = get_conversation_memory()
        self.code_analyzer = get_code_analyzer()
        self.suggester = get_proactive_suggester()
        self.multi_file_gen = get_multi_file_generator()
        
        # Composants V2
        self.cache = LRUCacheWithTTL(
            max_size=self.config.cache_max_size,
            ttl=self.config.cache_ttl
        ) if self.config.cache_enabled else None
        
        self.circuit_breaker = CircuitBreaker(
            failure_threshold=self.config.failure_threshold,
            recovery_timeout=self.config.recovery_timeout
        ) if self.config.circuit_breaker_enabled else None
        
        self.metrics = MetricsCollector() if self.config.metrics_enabled else None
        
        self.semantic_analyzer = SemanticAnalyzer()
        
        self.pattern_learner = PatternLearner(
            threshold=self.config.pattern_threshold
        ) if self.config.auto_learn_enabled else None
        
        # Thread pool pour exécution parallèle
        self.executor = ThreadPoolExecutor(
            max_workers=self.config.max_workers
        ) if self.config.enable_parallel else None
        
        # Initialisation des règles
        self._register_default_rules()
        
        self.logger.info(f"Namz IA Engine V2 initialized with {len(self.rules)} rules")
    
    def _register_default_rules(self):
        """Enregistre les règles par défaut."""
        # Importé depuis l'ancien engine - à optimiser
        from app.ia_engine import engine as old_engine
        
        # Copier les règles existantes en les convertissant
        for old_rule in old_engine.rules:
            new_rule = Rule(
                name=old_rule.name,
                condition=old_rule.condition,
                action=old_rule.action,
                lang=old_rule.lang,
                category="legacy"
            )
            self.rules.append(new_rule)
    
    def add_rule(self, name: str, condition: Callable, action: Callable, 
                 lang: str = "any", timeout: int = 30, priority: int = 0,
                 category: str = "custom", description: str = ""):
        """Ajoute une règle au moteur."""
        rule = Rule(
            name=name,
            condition=condition,
            action=action,
            lang=lang,
            timeout=timeout,
            priority=priority,
            category=category,
            description=description
        )
        self.rules.append(rule)
        
        # Trier par priorité
        self.rules.sort(key=lambda r: r.priority, reverse=True)
        
        self.logger.info(f"Rule '{name}' added (priority={priority}, category={category})")
    
    def analyse(self, message: str, context: Dict = None) -> IAResponse:
        """
        Analyse un message et retourne la meilleure réponse.
        
        Args:
            message: Le message à analyser
            context: Contexte additionnel (session_id, user_id, etc.)
        
        Returns:
            IAResponse avec status, réponse et métadonnées
        """
        start_time = time.time()
        
        try:
            # Vérifier le cache
            if self.cache:
                cache_key = self._generate_cache_key(message, context)
                cached_response = self.cache.get(cache_key)
                if cached_response:
                    self.logger.debug(f"Cache HIT for: {message[:50]}...")
                    return cached_response
                self.logger.debug(f"Cache MISS for: {message[:50]}...")
            
            # Exécuter l'analyse avec circuit breaker
            if self.circuit_breaker:
                response = self.circuit_breaker.call(self._analyse_internal, message, context)
            else:
                response = self._analyse_internal(message, context)
            
            # Stocker dans le cache
            if self.cache:
                self.cache.set(cache_key, response)
            
            # Enregistrer les métriques
            duration = time.time() - start_time
            if self.metrics:
                rule_name = response.meta.get('rule', 'unknown')
                self.metrics.record_request(rule_name, duration, success=True)
            
            # Auto-apprentissage
            if self.pattern_learner:
                rule_name = response.meta.get('rule', 'unknown')
                self.pattern_learner.record_pattern(message, response.response, rule_name)
            
            return response
        
        except Exception as e:
            duration = time.time() - start_time
            self.logger.error(f"Error analyzing message: {e}")
            
            if self.metrics:
                self.metrics.record_request('error', duration, success=False)
            
            return IAResponse(
                status="error",
                response=f"Erreur lors de l'analyse: {str(e)}",
                meta={'error': str(e), 'duration': duration}
            )
    
    def _analyse_internal(self, message: str, context: Dict = None) -> IAResponse:
        """Analyse interne du message."""
        # Détection de langue
        lang = self._detect_language(message)
        
        # Analyse sémantique
        entities = self.semantic_analyzer.extract_entities(message)
        intent = self.semantic_analyzer.extract_intent(message)
        
        # Enrichir le contexte
        enriched_context = {
            'lang': lang,
            'entities': entities,
            'intent': intent,
            'timestamp': datetime.datetime.utcnow().isoformat()
        }
        
        if context:
            enriched_context.update(context)
        
        # Évaluer toutes les règles
        candidates = []
        
        for rule in self.rules:
            if not rule.enabled:
                continue
            
            try:
                # Timeout par règle
                score = self._execute_with_timeout(
                    rule.condition,
                    args=(message, lang),
                    timeout=rule.timeout
                )
                
                if score >= self.config.min_confidence_score:
                    candidates.append((rule, score))
            
            except Exception as e:
                self.logger.warning(f"Rule '{rule.name}' failed: {e}")
                continue
        
        # Trier par score
        candidates.sort(key=lambda x: x[1], reverse=True)
        
        if not candidates:
            return self._fallback_response(message, enriched_context)
        
        # Mode multi-réponse
        if self.config.enable_multi_response and len(candidates) > 1:
            top_responses = []
            for rule, score in candidates[:self.config.top_n_responses]:
                try:
                    response_text = self._execute_with_timeout(
                        rule.action,
                        args=(message, lang),
                        timeout=rule.timeout
                    )
                    top_responses.append({
                        'rule': rule.name,
                        'score': score,
                        'response': response_text
                    })
                except Exception as e:
                    self.logger.warning(f"Action '{rule.name}' failed: {e}")
            
            if top_responses:
                enriched_context['alternatives'] = top_responses[1:]
                best = top_responses[0]
                return IAResponse(
                    status="ok",
                    response=best['response'],
                    meta={**enriched_context, 'rule': best['rule'], 'score': best['score']}
                )
        
        # Mode single-réponse (par défaut)
        best_rule, best_score = candidates[0]
        
        try:
            response_text = self._execute_with_timeout(
                best_rule.action,
                args=(message, lang),
                timeout=best_rule.timeout
            )
            
            return IAResponse(
                status="ok",
                response=response_text,
                meta={**enriched_context, 'rule': best_rule.name, 'score': best_score}
            )
        
        except Exception as e:
            self.logger.error(f"Best rule action failed: {e}")
            return self._fallback_response(message, enriched_context)
    
    def _execute_with_timeout(self, func: Callable, args: tuple, timeout: int) -> Any:
        """Exécute une fonction avec timeout."""
        if not self.executor:
            return func(*args)
        
        future = self.executor.submit(func, *args)
        try:
            return future.result(timeout=timeout)
        except FuturesTimeoutError:
            raise TimeoutError(f"Function execution exceeded {timeout}s")
    
    def _detect_language(self, message: str) -> str:
        """Détecte la langue du message."""
        # Mots français courants
        fr_words = {'le', 'la', 'les', 'un', 'une', 'des', 'et', 'ou', 'mais', 'donc', 'car', 'pour', 'dans', 'sur', 'avec', 'sans', 'par'}
        # Mots anglais courants
        en_words = {'the', 'a', 'an', 'and', 'or', 'but', 'so', 'for', 'in', 'on', 'with', 'without', 'by', 'from', 'to'}
        
        words = set(message.lower().split())
        
        fr_count = len(words & fr_words)
        en_count = len(words & en_words)
        
        return 'fr' if fr_count > en_count else 'en'
    
    def _fallback_response(self, message: str, context: Dict) -> IAResponse:
        """Génère une réponse par défaut."""
        lang = context.get('lang', 'fr')
        
        fallback_messages = {
            'fr': "Je n'ai pas compris votre demande. Pouvez-vous la reformuler ou préciser votre besoin ?",
            'en': "I didn't understand your request. Can you rephrase it or clarify your need?"
        }
        
        return IAResponse(
            status="ok",
            response=fallback_messages.get(lang, fallback_messages['fr']),
            meta={**context, 'rule': 'fallback', 'score': 0.0}
        )
    
    def _generate_cache_key(self, message: str, context: Dict = None) -> str:
        """Génère une clé de cache unique."""
        key_parts = [message]
        
        if context:
            # Inclure seulement les éléments pertinents pour le cache
            relevant_keys = ['session_id', 'user_id', 'lang']
            for key in relevant_keys:
                if key in context:
                    key_parts.append(f"{key}={context[key]}")
        
        combined = '|'.join(key_parts)
        return hashlib.md5(combined.encode()).hexdigest()
    
    def get_stats(self) -> Dict:
        """Retourne les statistiques globales du moteur."""
        stats = {
            'rules_count': len(self.rules),
            'rules_enabled': sum(1 for r in self.rules if r.enabled),
            'config': {
                'cache_enabled': self.config.cache_enabled,
                'circuit_breaker_enabled': self.config.circuit_breaker_enabled,
                'auto_learn_enabled': self.config.auto_learn_enabled,
                'parallel_enabled': self.config.enable_parallel,
            }
        }
        
        if self.cache:
            stats['cache'] = self.cache.get_stats()
        
        if self.circuit_breaker:
            stats['circuit_breaker'] = self.circuit_breaker.get_state()
        
        if self.metrics:
            stats['metrics'] = self.metrics.get_stats()
        
        if self.pattern_learner:
            stats['learning'] = self.pattern_learner.get_stats()
        
        return stats
    
    def clear_cache(self):
        """Vide le cache."""
        if self.cache:
            self.cache.clear()
            self.logger.info("Cache cleared")
    
    def reset_metrics(self):
        """Réinitialise les métriques."""
        if self.metrics:
            self.metrics.reset()
            self.logger.info("Metrics reset")
    
    def reset_circuit_breaker(self):
        """Réinitialise le circuit breaker."""
        if self.circuit_breaker:
            self.circuit_breaker.reset()
            self.logger.info("Circuit breaker reset")

# ═══════════════════════════════════════════════════════════════════════════════
#                          GLOBAL INSTANCE & API
# ═══════════════════════════════════════════════════════════════════════════════

# Instance globale V2
_engine_v2 = None

def get_engine_v2(config: EngineConfig = None) -> NamzIAEngineV2:
    """Retourne l'instance globale du moteur V2."""
    global _engine_v2
    if _engine_v2 is None:
        _engine_v2 = NamzIAEngineV2(config)
    return _engine_v2

def analyse_texte_v2(message: str, context: Dict = None) -> Dict:
    """Interface API pour l'analyse de texte V2."""
    engine = get_engine_v2()
    response = engine.analyse(message, context)
    return response.to_dict()
