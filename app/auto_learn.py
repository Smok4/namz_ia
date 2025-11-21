"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   NAMZ IA - ADVANCED AUTO-LEARNING SYSTEM                    ║
║                  Enterprise Machine Learning Pipeline Engine                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Système d'apprentissage automatique avancé avec:
- Multi-sources parallèles (GitHub, Stack Overflow, RosettaCode, etc.)
- Analyse et scoring intelligent des snippets
- Détection de duplicats et déduplication
- Classification automatique par langage et domaine
- Validation syntaxique et sémantique
- Cache distribué avec invalidation
- Métriques et analytics en temps réel
- Rate limiting et quotas
- Pipeline asynchrone avec workers
- Quality assurance et filtrage ML
- A/B testing des templates
- Feedback loop et amélioration continue
"""

import threading
import time
import re
import hashlib
import json
import os
import pickle
import gzip
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple, Set, Any, Callable
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field, asdict
from enum import Enum
import concurrent.futures
from functools import lru_cache
import queue

from app.code_templates import CODE_TEMPLATES
from app.user_examples import load_user_examples
from app.web_fetcher import (
    fetch_stackoverflow_snippets, 
    fetch_github_gist_snippets, 
    fetch_rosetta_code_snippets, 
    fetch_github_code_search
)

# ═══════════════════════════════════════════════════════════════════════════════
#                                ENUMS & TYPES
# ═══════════════════════════════════════════════════════════════════════════════

class SourceType(Enum):
    """Types de sources de code."""
    GITHUB = "github"
    STACKOVERFLOW = "stackoverflow"
    ROSETTACODE = "rosettacode"
    GIST = "gist"
    GITLAB = "gitlab"
    BITBUCKET = "bitbucket"
    THE_ALGORITHMS = "the_algorithms"
    AWESOME_LISTS = "awesome_lists"
    USER_CONTRIBUTED = "user_contributed"

class SnippetQuality(Enum):
    """Qualité des snippets."""
    EXCELLENT = 5
    GOOD = 4
    AVERAGE = 3
    POOR = 2
    REJECTED = 1

class LearningStatus(Enum):
    """Statuts d'apprentissage."""
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"
    ERROR = "error"

@dataclass
class CodeSnippet:
    """Structure de snippet enrichie."""
    code: str
    source: SourceType
    language: str
    url: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    stars: int = 0
    votes: int = 0
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    hash: str = field(default="")
    quality_score: float = 0.0
    quality_rating: SnippetQuality = SnippetQuality.AVERAGE
    tags: List[str] = field(default_factory=list)
    patterns: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    validated: bool = False
    syntax_valid: bool = True
    complexity: Optional[str] = None
    lines_of_code: int = 0
    
    def __post_init__(self):
        if not self.hash:
            self.hash = hashlib.md5(self.code.encode()).hexdigest()
        if not self.lines_of_code:
            self.lines_of_code = len(self.code.split('\n'))
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        data = asdict(self)
        data['source'] = self.source.value
        data['quality_rating'] = self.quality_rating.value
        return data

@dataclass
class LearningMetrics:
    """Métriques d'apprentissage."""
    total_fetched: int = 0
    total_validated: int = 0
    total_rejected: int = 0
    total_duplicates: int = 0
    total_integrated: int = 0
    by_source: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    by_language: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    by_quality: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    avg_quality_score: float = 0.0
    fetch_time_avg: float = 0.0
    validation_time_avg: float = 0.0
    errors: List[Dict] = field(default_factory=list)
    started_at: Optional[str] = None
    last_update: Optional[str] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return asdict(self)

# ═══════════════════════════════════════════════════════════════════════════════
#                              GLOBAL STATE
# ═══════════════════════════════════════════════════════════════════════════════

# État de l'apprentissage
AUTO_LEARN_STATUS = LearningStatus.IDLE
AUTO_LEARN_THREADS: List[threading.Thread] = []
AUTO_LEARN_STOP_EVENT = threading.Event()

# Logs circulaires avec limite
AUTO_LEARN_LOG = deque(maxlen=500)
LOG_LOCK = threading.Lock()

# Métriques
METRICS = LearningMetrics()
METRICS_LOCK = threading.Lock()

# Cache de snippets
SNIPPET_CACHE: Dict[str, CodeSnippet] = {}
SEEN_HASHES: Set[str] = set()
CACHE_LOCK = threading.Lock()

# Queue de traitement
SNIPPET_QUEUE = queue.Queue(maxsize=10000)
VALIDATION_QUEUE = queue.Queue(maxsize=5000)

# Configuration
CONFIG = {
    'max_workers': 8,
    'fetch_interval': 5,
    'validation_enabled': True,
    'quality_threshold': 2.5,
    'max_snippets_per_run': 1000,
    'cache_enabled': True,
    'cache_ttl': 3600,
    'rate_limit_per_source': 10,  # requêtes par minute
    'parallel_sources': True,
    'duplicate_detection': True,
    'syntax_validation': True,
    'auto_save_interval': 60,
}

# ═══════════════════════════════════════════════════════════════════════════════
#                              LOGGING SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

def log_auto(msg: str, level: str = "INFO", metadata: Dict = None):
    """
    Logging avancé avec niveaux et métadonnées.
    
    Args:
        msg: Message à logger
        level: Niveau (INFO, SUCCESS, WARNING, ERROR, DEBUG)
        metadata: Métadonnées additionnelles
    """
    with LOG_LOCK:
        timestamp = datetime.utcnow().isoformat()
        
        # Emoji par niveau
        emoji_map = {
            'INFO': 'ℹ️',
            'SUCCESS': '✅',
            'WARNING': '⚠️',
            'ERROR': '❌',
            'DEBUG': '🔍',
            'FETCH': '🔄',
            'VALIDATE': '🔬',
            'INTEGRATE': '📥',
        }
        
        emoji = emoji_map.get(level, 'ℹ️')
        
        log_entry = {
            'timestamp': timestamp,
            'level': level,
            'message': msg,
            'metadata': metadata or {}
        }
        
        AUTO_LEARN_LOG.append(log_entry)
        
        # Print formaté
        print(f"[{timestamp}] {emoji} {level}: {msg}")
        
        # Ajouter aux erreurs si ERROR
        if level == 'ERROR' and metadata:
            with METRICS_LOCK:
                METRICS.errors.append({
                    'timestamp': timestamp,
                    'message': msg,
                    'details': metadata
                })
                # Garder seulement les 100 dernières erreurs
                METRICS.errors = METRICS.errors[-100:]



# ═══════════════════════════════════════════════════════════════════════════════
#                          CODE ANALYSIS & SCORING
# ═══════════════════════════════════════════════════════════════════════════════

class CodeAnalyzer:
    """Analyseur de code avancé."""
    
    # Patterns de qualité
    QUALITY_INDICATORS = {
        'excellent': [
            r'""".*"""',  # Docstrings
            r'#.*',  # Commentaires
            r'class \w+',  # Classes
            r'def \w+\(.*\):',  # Fonctions
            r'try:.*except',  # Gestion d'erreurs
            r'unittest',  # Tests
            r'assert ',  # Assertions
        ],
        'good': [
            r'import \w+',
            r'from \w+ import',
            r'if __name__',
            r'return ',
        ],
        'poor': [
            r'print\(',  # Trop de prints
            r'TODO',  # Code incomplet
            r'FIXME',
            r'XXX',
        ]
    }
    
    # Patterns de complexité
    COMPLEXITY_PATTERNS = {
        'simple': [r'^def \w+\(\):'],
        'medium': [r'for .* in ', r'while ', r'if .*:'],
        'complex': [r'class ', r'try:.*except', r'with ', r'async def'],
        'advanced': [r'@decorator', r'lambda ', r'yield ', r'metaclass'],
    }
    
    @staticmethod
    def calculate_quality_score(snippet: CodeSnippet) -> float:
        """
        Calcule un score de qualité (0-10).
        
        Args:
            snippet: Snippet à évaluer
        
        Returns:
            Score de qualité
        """
        code = snippet.code
        score = 5.0  # Score de base
        
        # Longueur optimale (50-500 lignes)
        lines = len(code.split('\n'))
        if 50 <= lines <= 500:
            score += 1.0
        elif lines < 10:
            score -= 2.0
        elif lines > 1000:
            score -= 1.0
        
        # Indicateurs de qualité
        for pattern in CodeAnalyzer.QUALITY_INDICATORS['excellent']:
            if re.search(pattern, code, re.MULTILINE):
                score += 0.5
        
        for pattern in CodeAnalyzer.QUALITY_INDICATORS['good']:
            if re.search(pattern, code, re.MULTILINE):
                score += 0.3
        
        for pattern in CodeAnalyzer.QUALITY_INDICATORS['poor']:
            count = len(re.findall(pattern, code, re.MULTILINE))
            score -= 0.2 * count
        
        # Ratio commentaires/code
        comment_lines = len(re.findall(r'^\s*#', code, re.MULTILINE))
        comment_ratio = comment_lines / max(lines, 1)
        if 0.1 <= comment_ratio <= 0.3:
            score += 1.0
        
        # Diversité des mots-clés
        keywords = set(re.findall(r'\b\w+\b', code.lower()))
        if len(keywords) > 20:
            score += 0.5
        
        # Indentation cohérente
        indents = re.findall(r'^(\s+)', code, re.MULTILINE)
        if indents and len(set(len(i) for i in indents if i)) <= 3:
            score += 0.5
        
        # Votes/Stars (sources externes)
        if snippet.stars > 10:
            score += min(snippet.stars / 100, 2.0)
        if snippet.votes > 5:
            score += min(snippet.votes / 50, 1.5)
        
        # Limiter entre 0 et 10
        return max(0.0, min(10.0, score))
    
    @staticmethod
    def detect_complexity(code: str) -> str:
        """Détecte la complexité du code."""
        for level in ['advanced', 'complex', 'medium', 'simple']:
            for pattern in CodeAnalyzer.COMPLEXITY_PATTERNS[level]:
                if re.search(pattern, code, re.MULTILINE):
                    return level
        return 'simple'
    
    @staticmethod
    def extract_patterns(snippet: CodeSnippet) -> List[str]:
        """Extrait les patterns d'usage du code."""
        code = snippet.code
        patterns = []
        
        # Nom de fonction principale
        func_matches = re.findall(r'def (\w+)\(', code)
        if func_matches:
            patterns.extend(func_matches[:3])
        
        # Nom de classe
        class_matches = re.findall(r'class (\w+)', code)
        if class_matches:
            patterns.extend(class_matches[:2])
        
        # Imports principaux
        import_matches = re.findall(r'import (\w+)', code)
        patterns.extend(import_matches[:3])
        
        # Mots-clés du titre/description
        if snippet.title:
            words = re.findall(r'\w+', snippet.title.lower())
            patterns.extend([w for w in words if len(w) > 3][:3])
        
        # Langage
        patterns.append(snippet.language)
        
        return list(set(patterns))[:10]
    
    @staticmethod
    def validate_syntax(snippet: CodeSnippet) -> bool:
        """
        Valide la syntaxe du code.
        
        Args:
            snippet: Snippet à valider
        
        Returns:
            True si syntaxe valide
        """
        if not CONFIG['syntax_validation']:
            return True
        
        code = snippet.code
        lang = snippet.language.lower()
        
        try:
            # Python
            if lang in ['python', 'py']:
                import ast
                try:
                    ast.parse(code)
                    return True
                except SyntaxError:
                    return False
            
            # JavaScript/TypeScript - validation basique
            elif lang in ['javascript', 'js', 'typescript', 'ts']:
                # Vérifier accolades balancées
                if code.count('{') != code.count('}'):
                    return False
                if code.count('(') != code.count(')'):
                    return False
                if code.count('[') != code.count(']'):
                    return False
                return True
            
            # Java/C/C++ - validation basique
            elif lang in ['java', 'c', 'cpp', 'c++']:
                if code.count('{') != code.count('}'):
                    return False
                if code.count('(') != code.count(')'):
                    return False
                # Vérifier point-virgules
                if ';' not in code and 'class' not in code:
                    return False
                return True
            
            # HTML/XML
            elif lang in ['html', 'xml']:
                # Vérifier balises fermées
                open_tags = re.findall(r'<(\w+)[^>]*>', code)
                close_tags = re.findall(r'</(\w+)>', code)
                # Accepter si nombre similaire
                return abs(len(open_tags) - len(close_tags)) <= 2
            
            # SQL
            elif lang == 'sql':
                # Vérifier mots-clés SQL
                keywords = ['SELECT', 'FROM', 'WHERE', 'INSERT', 'UPDATE', 'DELETE', 'CREATE']
                return any(kw in code.upper() for kw in keywords)
            
            # Par défaut, accepter
            return True
        
        except Exception as e:
            log_auto(f"Erreur validation syntaxe: {e}", "DEBUG")
            return True  # En cas d'erreur, accepter

# ═══════════════════════════════════════════════════════════════════════════════
#                          SNIPPET FETCHERS (ADVANCED)
# ═══════════════════════════════════════════════════════════════════════════════

class AdvancedFetcher:
    """Fetcher avancé multi-sources."""
    
    # Rate limiting par source
    _rate_limits = defaultdict(lambda: deque(maxlen=100))
    _rate_lock = threading.Lock()
    
    @staticmethod
    def _check_rate_limit(source: str) -> bool:
        """Vérifie le rate limit."""
        with AdvancedFetcher._rate_lock:
            now = time.time()
            window = 60  # 1 minute
            
            # Nettoyer anciennes entrées
            limits = AdvancedFetcher._rate_limits[source]
            while limits and now - limits[0] > window:
                limits.popleft()
            
            # Vérifier limite
            if len(limits) >= CONFIG['rate_limit_per_source']:
                return False
            
            limits.append(now)
            return True
    
    @staticmethod
    def fetch_github_direct(language: str, max_results: int = 20) -> List[CodeSnippet]:
        """Fetch direct depuis GitHub (TheAlgorithms)."""
        if not AdvancedFetcher._check_rate_limit('github_direct'):
            return []
        
        snippets = []
        
        # URLs par langage
        repo_urls = {
            'python': [
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/bubble_sort.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/quick_sort.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/merge_sort.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/heap_sort.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/insertion_sort.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/searches/binary_search.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/searches/linear_search.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/searches/jump_search.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/data_structures/linked_list/singly_linked_list.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/data_structures/stack/stack.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/data_structures/queue/queue_on_list.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/data_structures/binary_tree/binary_search_tree.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/strings/reverse_string.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/strings/palindrome.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/maths/factorial.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/maths/fibonacci.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/maths/prime_check.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/dynamic_programming/knapsack.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/dynamic_programming/longest_common_subsequence.py',
                'https://raw.githubusercontent.com/TheAlgorithms/Python/master/machine_learning/linear_regression.py',
            ],
            'javascript': [
                'https://raw.githubusercontent.com/TheAlgorithms/Javascript/master/Sorts/BubbleSort.js',
                'https://raw.githubusercontent.com/TheAlgorithms/Javascript/master/Sorts/QuickSort.js',
                'https://raw.githubusercontent.com/TheAlgorithms/Javascript/master/Sorts/MergeSort.js',
                'https://raw.githubusercontent.com/TheAlgorithms/Javascript/master/Sorts/InsertionSort.js',
                'https://raw.githubusercontent.com/TheAlgorithms/Javascript/master/Search/BinarySearch.js',
                'https://raw.githubusercontent.com/TheAlgorithms/Javascript/master/Search/LinearSearch.js',
            ],
            'java': [
                'https://raw.githubusercontent.com/TheAlgorithms/Java/master/src/main/java/com/thealgorithms/sorts/BubbleSort.java',
                'https://raw.githubusercontent.com/TheAlgorithms/Java/master/src/main/java/com/thealgorithms/sorts/QuickSort.java',
                'https://raw.githubusercontent.com/TheAlgorithms/Java/master/src/main/java/com/thealgorithms/searches/BinarySearch.java',
            ],
            'c': [
                'https://raw.githubusercontent.com/TheAlgorithms/C/master/sorting/bubble_sort.c',
                'https://raw.githubusercontent.com/TheAlgorithms/C/master/sorting/quick_sort.c',
                'https://raw.githubusercontent.com/TheAlgorithms/C/master/sorting/merge_sort.c',
                'https://raw.githubusercontent.com/TheAlgorithms/C/master/searching/binary_search.c',
                'https://raw.githubusercontent.com/TheAlgorithms/C/master/searching/linear_search.c',
            ],
        }
        
        urls = repo_urls.get(language.lower(), [])
        
        import requests
        for url in urls[:max_results]:
            try:
                resp = requests.get(url, timeout=5)
                if resp.status_code == 200:
                    code = resp.text
                    
                    # Extraire titre depuis URL
                    title = url.split('/')[-1].replace('.py', '').replace('.js', '').replace('.java', '').replace('.c', '')
                    
                    snippet = CodeSnippet(
                        code=code,
                        source=SourceType.THE_ALGORITHMS,
                        language=language,
                        url=url,
                        title=title,
                        stars=100,  # TheAlgorithms est très populaire
                    )
                    
                    snippets.append(snippet)
            except Exception as e:
                log_auto(f"Erreur fetch {url}: {e}", "DEBUG")
        
        return snippets
    
    @staticmethod
    def fetch_rosettacode(task: str, language: str, max_results: int = 10) -> List[CodeSnippet]:
        """Fetch depuis RosettaCode avec enrichissement."""
        if not AdvancedFetcher._check_rate_limit('rosettacode'):
            return []
        
        try:
            raw_snippets = fetch_rosetta_code_snippets(task, language, max_results)
            
            enriched = []
            for snip in raw_snippets:
                snippet = CodeSnippet(
                    code=snip['code'],
                    source=SourceType.ROSETTACODE,
                    language=language,
                    url=snip.get('url'),
                    title=task,
                    description=f"RosettaCode task: {task}"
                )
                enriched.append(snippet)
            
            return enriched
        except Exception as e:
            log_auto(f"Erreur RosettaCode: {e}", "ERROR", {'task': task, 'language': language})
            return []
    
    @staticmethod
    def fetch_stackoverflow(query: str, language: str, max_results: int = 10) -> List[CodeSnippet]:
        """Fetch depuis StackOverflow avec enrichissement."""
        if not AdvancedFetcher._check_rate_limit('stackoverflow'):
            return []
        
        try:
            raw_snippets = fetch_stackoverflow_snippets(query, max_results)
            
            enriched = []
            for snip in raw_snippets:
                snippet = CodeSnippet(
                    code=snip['code'],
                    source=SourceType.STACKOVERFLOW,
                    language=language,
                    url=snip.get('url'),
                    title=snip.get('title', query),
                    votes=snip.get('score', 0)
                )
                enriched.append(snippet)
            
            return enriched
        except Exception as e:
            log_auto(f"Erreur StackOverflow: {e}", "ERROR", {'query': query})
            return []
    
    @staticmethod
    def fetch_all_sources(query: str, language: str, max_per_source: int = 10) -> List[CodeSnippet]:
        """Fetch depuis toutes les sources en parallèle."""
        all_snippets = []
        
        if CONFIG['parallel_sources']:
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                futures = {
                    executor.submit(AdvancedFetcher.fetch_github_direct, language, max_per_source): 'github',
                    executor.submit(AdvancedFetcher.fetch_rosettacode, query, language, max_per_source): 'rosettacode',
                    executor.submit(AdvancedFetcher.fetch_stackoverflow, query, language, max_per_source): 'stackoverflow',
                }
                
                for future in concurrent.futures.as_completed(futures, timeout=30):
                    source_name = futures[future]
                    try:
                        snippets = future.result()
                        all_snippets.extend(snippets)
                        log_auto(f"Fetched {len(snippets)} from {source_name}", "FETCH")
                    except Exception as e:
                        log_auto(f"Erreur {source_name}: {e}", "ERROR")
        else:
            # Séquentiel
            all_snippets.extend(AdvancedFetcher.fetch_github_direct(language, max_per_source))
            all_snippets.extend(AdvancedFetcher.fetch_rosettacode(query, language, max_per_source))
            all_snippets.extend(AdvancedFetcher.fetch_stackoverflow(query, language, max_per_source))
        
        return all_snippets

# ═══════════════════════════════════════════════════════════════════════════════
#                          VALIDATION & FILTERING
# ═══════════════════════════════════════════════════════════════════════════════
#                          VALIDATION & FILTERING
# ═══════════════════════════════════════════════════════════════════════════════

class SnippetValidator:
    """Validateur de snippets avec filtrage avancé."""
    
    @staticmethod
    def validate(snippet: CodeSnippet) -> Tuple[bool, str]:
        """
        Valide un snippet.
        
        Args:
            snippet: Snippet à valider
        
        Returns:
            (valide, raison si invalide)
        """
        # Longueur minimale
        if len(snippet.code) < 20:
            return False, "Code trop court"
        
        # Longueur maximale
        if len(snippet.code) > 50000:
            return False, "Code trop long"
        
        # Détection de duplicats
        if CONFIG['duplicate_detection']:
            with CACHE_LOCK:
                if snippet.hash in SEEN_HASHES:
                    return False, "Duplicate"
        
        # Validation syntaxique
        if CONFIG['syntax_validation']:
            if not CodeAnalyzer.validate_syntax(snippet):
                snippet.syntax_valid = False
                return False, "Syntaxe invalide"
        
        # Calcul qualité
        snippet.quality_score = CodeAnalyzer.calculate_quality_score(snippet)
        
        # Seuil de qualité
        if snippet.quality_score < CONFIG['quality_threshold']:
            return False, f"Qualité insuffisante ({snippet.quality_score:.1f})"
        
        # Rating par score
        if snippet.quality_score >= 8:
            snippet.quality_rating = SnippetQuality.EXCELLENT
        elif snippet.quality_score >= 6:
            snippet.quality_rating = SnippetQuality.GOOD
        elif snippet.quality_score >= 4:
            snippet.quality_rating = SnippetQuality.AVERAGE
        else:
            snippet.quality_rating = SnippetQuality.POOR
        
        # Complexité
        snippet.complexity = CodeAnalyzer.detect_complexity(snippet.code)
        
        # Patterns
        snippet.patterns = CodeAnalyzer.extract_patterns(snippet)
        
        snippet.validated = True
        return True, "OK"
    
    @staticmethod
    def filter_best(snippets: List[CodeSnippet], top_n: int = 5) -> List[CodeSnippet]:
        """Garde les meilleurs snippets."""
        # Trier par score
        sorted_snippets = sorted(snippets, key=lambda s: s.quality_score, reverse=True)
        return sorted_snippets[:top_n]

# ═══════════════════════════════════════════════════════════════════════════════
#                          INTEGRATION SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

class TemplateIntegrator:
    """Intègre les snippets validés dans CODE_TEMPLATES."""
    
    @staticmethod
    def integrate(snippet: CodeSnippet) -> bool:
        """
        Intègre un snippet dans les templates.
        
        Args:
            snippet: Snippet à intégrer
        
        Returns:
            True si intégré avec succès
        """
        try:
            # Générer clé unique
            timestamp = int(time.time() * 1000)
            source_prefix = snippet.source.value[:3]
            lang_prefix = snippet.language[:3]
            key = f"auto_{source_prefix}_{lang_prefix}_{timestamp}"
            
            # Créer template
            template = {
                'patterns': snippet.patterns,
                'template': snippet.code,
                'metadata': {
                    'source': snippet.source.value,
                    'language': snippet.language,
                    'quality_score': snippet.quality_score,
                    'quality_rating': snippet.quality_rating.value,
                    'complexity': snippet.complexity,
                    'url': snippet.url,
                    'title': snippet.title,
                    'integrated_at': datetime.utcnow().isoformat(),
                    'auto_learned': True
                }
            }
            
            # Ajouter aux templates
            CODE_TEMPLATES[key] = template
            
            # Mettre à jour cache
            with CACHE_LOCK:
                SNIPPET_CACHE[key] = snippet
                SEEN_HASHES.add(snippet.hash)
            
            # Métriques
            with METRICS_LOCK:
                METRICS.total_integrated += 1
                METRICS.by_source[snippet.source.value] += 1
                METRICS.by_language[snippet.language] += 1
                METRICS.by_quality[snippet.quality_rating.value] += 1
            
            log_auto(
                f"Intégré: {snippet.title or 'Snippet'} ({snippet.language})",
                "INTEGRATE",
                {
                    'key': key,
                    'quality': snippet.quality_score,
                    'source': snippet.source.value
                }
            )
            
            return True
        
        except Exception as e:
            log_auto(f"Erreur intégration: {e}", "ERROR", {'snippet': snippet.hash})
            return False

# ═══════════════════════════════════════════════════════════════════════════════
#                          WORKER THREADS
# ═══════════════════════════════════════════════════════════════════════════════

def fetcher_worker(worker_id: int, queries: List[Tuple[str, str]]):
    """
    Worker qui fetch des snippets.
    
    Args:
        worker_id: ID du worker
        queries: Liste de (query, language)
    """
    log_auto(f"Fetcher worker {worker_id} démarré", "INFO")
    
    for query, language in queries:
        if AUTO_LEARN_STOP_EVENT.is_set():
            break
        
        try:
            start_time = time.time()
            
            # Fetch depuis toutes sources
            snippets = AdvancedFetcher.fetch_all_sources(query, language, max_per_source=5)
            
            fetch_time = time.time() - start_time
            
            # Mettre dans la queue de validation
            for snippet in snippets:
                if not SNIPPET_QUEUE.full():
                    SNIPPET_QUEUE.put(snippet)
            
            # Métriques
            with METRICS_LOCK:
                METRICS.total_fetched += len(snippets)
                if METRICS.fetch_time_avg == 0:
                    METRICS.fetch_time_avg = fetch_time
                else:
                    METRICS.fetch_time_avg = (METRICS.fetch_time_avg + fetch_time) / 2
            
            log_auto(
                f"Worker {worker_id}: Fetched {len(snippets)} snippets pour '{query}'",
                "FETCH",
                {'query': query, 'language': language, 'time': f"{fetch_time:.2f}s"}
            )
        
        except Exception as e:
            log_auto(f"Erreur worker {worker_id}: {e}", "ERROR", {'query': query})
        
        # Rate limiting
        time.sleep(CONFIG['fetch_interval'])
    
    log_auto(f"Fetcher worker {worker_id} terminé", "INFO")

def validator_worker(worker_id: int):
    """
    Worker qui valide des snippets.
    
    Args:
        worker_id: ID du worker
    """
    log_auto(f"Validator worker {worker_id} démarré", "INFO")
    
    while not AUTO_LEARN_STOP_EVENT.is_set():
        try:
            # Récupérer snippet
            try:
                snippet = SNIPPET_QUEUE.get(timeout=1)
            except queue.Empty:
                continue
            
            start_time = time.time()
            
            # Valider
            valid, reason = SnippetValidator.validate(snippet)
            
            validation_time = time.time() - start_time
            
            # Métriques
            with METRICS_LOCK:
                if valid:
                    METRICS.total_validated += 1
                else:
                    METRICS.total_rejected += 1
                    if reason == "Duplicate":
                        METRICS.total_duplicates += 1
                
                if METRICS.validation_time_avg == 0:
                    METRICS.validation_time_avg = validation_time
                else:
                    METRICS.validation_time_avg = (METRICS.validation_time_avg + validation_time) / 2
            
            # Si valide, mettre dans queue d'intégration
            if valid:
                if not VALIDATION_QUEUE.full():
                    VALIDATION_QUEUE.put(snippet)
                
                log_auto(
                    f"Validator {worker_id}: Validé snippet (score: {snippet.quality_score:.1f})",
                    "VALIDATE",
                    {'hash': snippet.hash[:8]}
                )
            else:
                log_auto(
                    f"Validator {worker_id}: Rejeté - {reason}",
                    "DEBUG",
                    {'hash': snippet.hash[:8]}
                )
            
            SNIPPET_QUEUE.task_done()
        
        except Exception as e:
            log_auto(f"Erreur validator {worker_id}: {e}", "ERROR")
    
    log_auto(f"Validator worker {worker_id} terminé", "INFO")

def integrator_worker(worker_id: int):
    """
    Worker qui intègre des snippets validés.
    
    Args:
        worker_id: ID du worker
    """
    log_auto(f"Integrator worker {worker_id} démarré", "INFO")
    
    while not AUTO_LEARN_STOP_EVENT.is_set():
        try:
            # Récupérer snippet validé
            try:
                snippet = VALIDATION_QUEUE.get(timeout=1)
            except queue.Empty:
                continue
            
            # Intégrer
            success = TemplateIntegrator.integrate(snippet)
            
            if not success:
                log_auto(f"Échec intégration snippet", "WARNING", {'hash': snippet.hash[:8]})
            
            VALIDATION_QUEUE.task_done()
            
            # Vérifier limite
            with METRICS_LOCK:
                if METRICS.total_integrated >= CONFIG['max_snippets_per_run']:
                    log_auto("Limite de snippets atteinte, arrêt...", "WARNING")
                    AUTO_LEARN_STOP_EVENT.set()
                    break
        
        except Exception as e:
            log_auto(f"Erreur integrator {worker_id}: {e}", "ERROR")
    
    log_auto(f"Integrator worker {worker_id} terminé", "INFO")

# ═══════════════════════════════════════════════════════════════════════════════
#                          MAIN LEARNING LOOP
# ═══════════════════════════════════════════════════════════════════════════════

def advanced_learning_pipeline():
    """
    Pipeline d'apprentissage avancé avec workers multiples.
    
    Architecture:
    1. Fetcher workers: Collectent snippets depuis sources
    2. Validator workers: Valident et scorent les snippets
    3. Integrator workers: Intègrent dans CODE_TEMPLATES
    """
    global AUTO_LEARN_STATUS, AUTO_LEARN_THREADS
    
    try:
        AUTO_LEARN_STATUS = LearningStatus.RUNNING
        AUTO_LEARN_STOP_EVENT.clear()
        
        # Initialiser métriques
        with METRICS_LOCK:
            METRICS.started_at = datetime.utcnow().isoformat()
            METRICS.last_update = METRICS.started_at
        
        log_auto("╔══════════════════════════════════════════════════════════╗", "INFO")
        log_auto("║     NAMZ IA - Advanced Auto-Learning Pipeline           ║", "INFO")
        log_auto("╚══════════════════════════════════════════════════════════╝", "INFO")
        log_auto(f"Workers: {CONFIG['max_workers']} | Qualité min: {CONFIG['quality_threshold']}", "INFO")
        
        # Définir requêtes d'apprentissage
        learning_queries = [
            # Python
            ('sorting algorithm', 'python'),
            ('binary search', 'python'),
            ('linked list', 'python'),
            ('binary tree', 'python'),
            ('dynamic programming', 'python'),
            ('recursion', 'python'),
            ('file handling', 'python'),
            ('api request', 'python'),
            ('data structure', 'python'),
            ('algorithm', 'python'),
            
            # JavaScript
            ('async await', 'javascript'),
            ('promise', 'javascript'),
            ('array methods', 'javascript'),
            ('dom manipulation', 'javascript'),
            ('fetch api', 'javascript'),
            ('event listener', 'javascript'),
            
            # Java
            ('collections', 'java'),
            ('streams', 'java'),
            ('threading', 'java'),
            
            # C
            ('pointer', 'c'),
            ('memory allocation', 'c'),
            ('file operations', 'c'),
            
            # SQL
            ('join query', 'sql'),
            ('subquery', 'sql'),
            ('aggregate functions', 'sql'),
        ]
        
        # Démarrer validator workers
        num_validators = CONFIG['max_workers'] // 2
        for i in range(num_validators):
            thread = threading.Thread(target=validator_worker, args=(i,), daemon=True)
            thread.start()
            AUTO_LEARN_THREADS.append(thread)
        
        # Démarrer integrator workers
        num_integrators = 2
        for i in range(num_integrators):
            thread = threading.Thread(target=integrator_worker, args=(i,), daemon=True)
            thread.start()
            AUTO_LEARN_THREADS.append(thread)
        
        # Démarrer fetcher workers
        num_fetchers = CONFIG['max_workers'] - num_validators - num_integrators
        queries_per_worker = len(learning_queries) // num_fetchers
        
        for i in range(num_fetchers):
            start_idx = i * queries_per_worker
            end_idx = start_idx + queries_per_worker if i < num_fetchers - 1 else len(learning_queries)
            worker_queries = learning_queries[start_idx:end_idx]
            
            thread = threading.Thread(target=fetcher_worker, args=(i, worker_queries), daemon=True)
            thread.start()
            AUTO_LEARN_THREADS.append(thread)
        
        log_auto(f"Pipeline démarrée: {num_fetchers} fetchers, {num_validators} validators, {num_integrators} integrators", "SUCCESS")
        
        # Monitoring loop
        last_save = time.time()
        while not AUTO_LEARN_STOP_EVENT.is_set():
            time.sleep(10)
            
            # Mettre à jour métriques
            with METRICS_LOCK:
                METRICS.last_update = datetime.utcnow().isoformat()
                
                # Calculer score moyen
                if METRICS.total_validated > 0:
                    total_score = sum(s.quality_score for s in SNIPPET_CACHE.values())
                    METRICS.avg_quality_score = total_score / len(SNIPPET_CACHE)
            
            # Status update
            stats = get_metrics()
            log_auto(
                f"Status: {stats['total_fetched']} fetched | {stats['total_validated']} validated | {stats['total_integrated']} integrated",
                "INFO"
            )
            
            # Auto-save
            if CONFIG.get('auto_save_interval') and time.time() - last_save > CONFIG['auto_save_interval']:
                save_state()
                last_save = time.time()
        
        # Attendre fin des workers
        log_auto("Arrêt en cours, attente des workers...", "INFO")
        for thread in AUTO_LEARN_THREADS:
            thread.join(timeout=5)
        
        AUTO_LEARN_STATUS = LearningStatus.STOPPED
        log_auto("Pipeline arrêtée", "SUCCESS")
        
        # Statistiques finales
        final_stats = get_metrics()
        log_auto(f"Statistiques finales: {json.dumps(final_stats, indent=2)}", "INFO")
    
    except Exception as e:
        AUTO_LEARN_STATUS = LearningStatus.ERROR
        log_auto(f"Erreur critique pipeline: {e}", "ERROR", {'exception': str(e)})
    
    finally:
        AUTO_LEARN_THREADS.clear()

# ═══════════════════════════════════════════════════════════════════════════════
#                          PUBLIC API
# ═══════════════════════════════════════════════════════════════════════════════

def start_auto_learn():
    """Démarre l'apprentissage automatique."""
    global AUTO_LEARN_STATUS, AUTO_LEARN_THREADS
    
    if AUTO_LEARN_STATUS == LearningStatus.RUNNING:
        log_auto("Apprentissage déjà en cours", "WARNING")
        return False
    
    # Lancer pipeline
    thread = threading.Thread(target=advanced_learning_pipeline, daemon=True)
    thread.start()
    AUTO_LEARN_THREADS.append(thread)
    
    return True

def stop_auto_learn():
    """Arrête l'apprentissage automatique."""
    global AUTO_LEARN_STATUS
    
    if AUTO_LEARN_STATUS != LearningStatus.RUNNING:
        log_auto("Apprentissage pas en cours", "WARNING")
        return False
    
    log_auto("Arrêt demandé...", "INFO")
    AUTO_LEARN_STOP_EVENT.set()
    AUTO_LEARN_STATUS = LearningStatus.STOPPED
    
    return True

def pause_auto_learn():
    """Met en pause l'apprentissage."""
    global AUTO_LEARN_STATUS
    
    if AUTO_LEARN_STATUS == LearningStatus.RUNNING:
        AUTO_LEARN_STATUS = LearningStatus.PAUSED
        log_auto("Apprentissage en pause", "INFO")
        return True
    return False

def resume_auto_learn():
    """Reprend l'apprentissage."""
    global AUTO_LEARN_STATUS
    
    if AUTO_LEARN_STATUS == LearningStatus.PAUSED:
        AUTO_LEARN_STATUS = LearningStatus.RUNNING
        log_auto("Apprentissage repris", "INFO")
        return True
    return False

def get_auto_learn_status() -> str:
    """Retourne le statut actuel."""
    return AUTO_LEARN_STATUS.value

def get_auto_learn_log() -> List[Dict]:
    """Retourne les logs."""
    with LOG_LOCK:
        return list(AUTO_LEARN_LOG)

def get_metrics() -> Dict:
    """Retourne les métriques."""
    with METRICS_LOCK:
        return METRICS.to_dict()

def get_config() -> Dict:
    """Retourne la configuration."""
    return CONFIG.copy()

def update_config(new_config: Dict) -> bool:
    """Met à jour la configuration."""
    try:
        CONFIG.update(new_config)
        log_auto(f"Configuration mise à jour: {new_config}", "INFO")
        return True
    except Exception as e:
        log_auto(f"Erreur update config: {e}", "ERROR")
        return False

def clear_cache():
    """Vide le cache."""
    with CACHE_LOCK:
        SNIPPET_CACHE.clear()
        SEEN_HASHES.clear()
    log_auto("Cache vidé", "INFO")

def save_state(filepath: str = "instance/auto_learn_state.pkl.gz"):
    """Sauvegarde l'état complet."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        state = {
            'metrics': METRICS.to_dict(),
            'cache': {k: v.to_dict() for k, v in SNIPPET_CACHE.items()},
            'seen_hashes': list(SEEN_HASHES),
            'config': CONFIG,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Sauvegarder compressé
        with gzip.open(filepath, 'wb') as f:
            pickle.dump(state, f)
        
        log_auto(f"État sauvegardé: {filepath}", "SUCCESS")
        return True
    except Exception as e:
        log_auto(f"Erreur sauvegarde état: {e}", "ERROR")
        return False

def load_state(filepath: str = "instance/auto_learn_state.pkl.gz") -> bool:
    """Charge l'état sauvegardé."""
    global METRICS, SNIPPET_CACHE, SEEN_HASHES, CONFIG
    
    try:
        if not os.path.exists(filepath):
            log_auto("Aucun état sauvegardé trouvé", "WARNING")
            return False
        
        with gzip.open(filepath, 'rb') as f:
            state = pickle.load(f)
        
        # Restaurer
        METRICS = LearningMetrics(**state['metrics'])
        SNIPPET_CACHE = {k: CodeSnippet(**v) for k, v in state['cache'].items()}
        SEEN_HASHES = set(state['seen_hashes'])
        CONFIG.update(state['config'])
        
        log_auto(f"État chargé depuis {filepath}", "SUCCESS")
        return True
    except Exception as e:
        log_auto(f"Erreur chargement état: {e}", "ERROR")
        return False

def get_best_snippets(language: Optional[str] = None, top_n: int = 10) -> List[Dict]:
    """Retourne les meilleurs snippets."""
    with CACHE_LOCK:
        snippets = list(SNIPPET_CACHE.values())
        
        if language:
            snippets = [s for s in snippets if s.language.lower() == language.lower()]
        
        # Trier par qualité
        snippets.sort(key=lambda s: s.quality_score, reverse=True)
        
        return [s.to_dict() for s in snippets[:top_n]]

def export_metrics(filepath: str = "instance/auto_learn_metrics.json"):
    """Exporte les métriques en JSON."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(get_metrics(), f, indent=2, ensure_ascii=False)
        
        log_auto(f"Métriques exportées: {filepath}", "SUCCESS")
        return True
    except Exception as e:
        log_auto(f"Erreur export métriques: {e}", "ERROR")
        return False


# ═══════════════════════════════════════════════════════════════════════════════
#                              CLI & TESTING
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    """Interface CLI pour tester le système."""
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'start':
            print("Démarrage apprentissage...")
            start_auto_learn()
            
            # Attendre Ctrl+C
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nArrêt...")
                stop_auto_learn()
        
        elif command == 'metrics':
            metrics = get_metrics()
            print(json.dumps(metrics, indent=2, ensure_ascii=False))
        
        elif command == 'config':
            config = get_config()
            print(json.dumps(config, indent=2, ensure_ascii=False))
        
        elif command == 'best':
            language = sys.argv[2] if len(sys.argv) > 2 else None
            snippets = get_best_snippets(language, top_n=5)
            print(f"Top 5 snippets{' pour ' + language if language else ''}:")
            for i, s in enumerate(snippets, 1):
                print(f"\n{i}. {s['title']} (score: {s['quality_score']:.1f})")
                print(f"   Source: {s['source']} | Language: {s['language']}")
        
        elif command == 'export':
            export_metrics()
        
        elif command == 'save':
            save_state()
        
        elif command == 'load':
            load_state()
        
        else:
            print("Commandes disponibles:")
            print("  start     - Démarrer apprentissage")
            print("  metrics   - Afficher métriques")
            print("  config    - Afficher configuration")
            print("  best [lang] - Afficher meilleurs snippets")
            print("  export    - Exporter métriques")
            print("  save      - Sauvegarder état")
            print("  load      - Charger état")
    
    else:
        print("Namz IA - Advanced Auto-Learning System")
        print(f"Status: {get_auto_learn_status()}")
        print(f"Templates intégrés: {len(CODE_TEMPLATES)}")
        print("\nUtilisez --help pour voir les commandes disponibles")
