"""
Analyseur de code existant pour Namz IA
Permet de comprendre et améliorer du code fourni par l'utilisateur
"""

import re
from typing import Dict, List, Optional, Tuple

class CodeAnalyzer:
    """Analyse le code existant pour l'améliorer."""
    
    def __init__(self):
        self.language_patterns = {
            'python': [r'def\s+\w+', r'class\s+\w+', r'import\s+\w+', r'from\s+\w+'],
            'javascript': [r'function\s+\w+', r'const\s+\w+', r'let\s+\w+', r'var\s+\w+', r'=>'],
            'typescript': [r'interface\s+\w+', r'type\s+\w+', r':\s*\w+', r'function\s+\w+'],
            'java': [r'public\s+class', r'private\s+\w+', r'public\s+\w+', r'void\s+\w+'],
            'c': [r'int\s+main', r'#include', r'printf', r'scanf'],
            'cpp': [r'std::', r'cout', r'cin', r'#include\s+<iostream>'],
            'csharp': [r'namespace\s+\w+', r'using\s+System', r'public\s+class'],
            'php': [r'<\?php', r'\$\w+', r'function\s+\w+', r'echo'],
            'ruby': [r'def\s+\w+', r'class\s+\w+', r'end\b', r'puts'],
            'go': [r'func\s+\w+', r'package\s+\w+', r'import\s+\('],
            'rust': [r'fn\s+\w+', r'let\s+mut', r'impl\s+\w+'],
            'swift': [r'func\s+\w+', r'var\s+\w+', r'let\s+\w+', r'import\s+\w+'],
            'kotlin': [r'fun\s+\w+', r'val\s+\w+', r'var\s+\w+', r'class\s+\w+'],
            'sql': [r'SELECT\s+', r'FROM\s+', r'WHERE\s+', r'INSERT\s+INTO'],
            'html': [r'<html>', r'<div', r'<head>', r'<body>'],
            'css': [r'\{[^}]*\}', r'\.[\w-]+', r'#[\w-]+'],
        }
    
    def detect_language(self, code: str) -> Optional[str]:
        """Détecte le langage du code."""
        code_lower = code.lower()
        scores = {}
        
        for lang, patterns in self.language_patterns.items():
            score = 0
            for pattern in patterns:
                if re.search(pattern, code, re.IGNORECASE):
                    score += 1
            if score > 0:
                scores[lang] = score
        
        if scores:
            return max(scores, key=scores.get)
        return None
    
    def analyze_code(self, code: str) -> Dict:
        """Analyse complète du code avec validation."""
        try:
            # Validation
            if not code or not isinstance(code, str):
                return {
                    'error': 'Code vide ou invalide',
                    'language': None,
                    'lines_count': 0
                }
            
            code = code.strip()
            if not code:
                return {
                    'error': 'Code vide',
                    'language': None,
                    'lines_count': 0
                }
            
            # Limite de taille
            if len(code) > 100000:  # 100KB
                return {
                    'error': 'Code trop long (max 100KB)',
                    'language': None,
                    'lines_count': len(code.split('\n'))
                }
            
            language = self.detect_language(code)
            
            analysis = {
                'language': language,
                'lines_count': len(code.split('\n')),
                'issues': [],
                'suggestions': [],
                'complexity': self._estimate_complexity(code),
                'structure': self._analyze_structure(code, language)
            }
            
            # Analyse spécifique selon le langage
            if language == 'python':
                analysis.update(self._analyze_python(code))
            elif language in ['javascript', 'typescript']:
                analysis.update(self._analyze_javascript(code))
            elif language == 'html':
                analysis.update(self._analyze_html(code))
            
            return analysis
        
        except Exception as e:
            return {
                'error': f'Erreur analyse: {str(e)}',
                'language': None,
                'lines_count': 0
            }
    
    def _estimate_complexity(self, code: str) -> str:
        """Estime la complexité du code."""
        lines = len(code.split('\n'))
        
        # Compte les structures de contrôle
        control_structures = len(re.findall(r'\b(if|for|while|switch|case)\b', code, re.IGNORECASE))
        
        # Compte les fonctions
        functions = len(re.findall(r'\b(def|function|func|fn)\s+\w+', code, re.IGNORECASE))
        
        complexity_score = (lines / 10) + (control_structures * 2) + (functions * 1.5)
        
        if complexity_score < 5:
            return 'simple'
        elif complexity_score < 15:
            return 'modérée'
        elif complexity_score < 30:
            return 'élevée'
        else:
            return 'très élevée'
    
    def _analyze_structure(self, code: str, language: Optional[str]) -> Dict:
        """Analyse la structure du code."""
        structure = {
            'functions': [],
            'classes': [],
            'imports': [],
            'comments': 0
        }
        
        # Fonctions
        function_patterns = [
            r'def\s+(\w+)',  # Python
            r'function\s+(\w+)',  # JavaScript
            r'func\s+(\w+)',  # Go, Swift
            r'fn\s+(\w+)',  # Rust
            r'fun\s+(\w+)',  # Kotlin
        ]
        
        for pattern in function_patterns:
            matches = re.findall(pattern, code)
            structure['functions'].extend(matches)
        
        # Classes
        class_matches = re.findall(r'class\s+(\w+)', code, re.IGNORECASE)
        structure['classes'].extend(class_matches)
        
        # Imports
        import_patterns = [
            r'import\s+([\w.]+)',
            r'from\s+([\w.]+)\s+import',
            r'#include\s+[<"](.+)[>"]',
            r'use\s+([\w:]+)',
        ]
        
        for pattern in import_patterns:
            matches = re.findall(pattern, code)
            structure['imports'].extend(matches)
        
        # Commentaires
        comment_patterns = [r'#.*', r'//.*', r'/\*[\s\S]*?\*/']
        for pattern in comment_patterns:
            structure['comments'] += len(re.findall(pattern, code))
        
        return structure
    
    def _analyze_python(self, code: str) -> Dict:
        """Analyse spécifique Python."""
        issues = []
        suggestions = []
        
        # Vérifier les conventions PEP8
        if re.search(r'def\s+[A-Z]\w+', code):
            issues.append("Noms de fonctions en CamelCase (devrait être snake_case)")
            suggestions.append("Renommer les fonctions en snake_case (ex: maFonction → ma_fonction)")
        
        # Vérifier les lignes trop longues
        for line in code.split('\n'):
            if len(line) > 79:
                issues.append("Lignes trop longues (>79 caractères)")
                suggestions.append("Diviser les longues lignes pour respecter PEP8")
                break
        
        # Vérifier les imports
        if 'import *' in code:
            issues.append("Import * trouvé (mauvaise pratique)")
            suggestions.append("Importer uniquement ce dont vous avez besoin")
        
        # Vérifier la gestion d'erreurs
        if re.search(r'except\s*:', code):
            issues.append("Clause except trop large")
            suggestions.append("Spécifier les exceptions à capturer (ex: except ValueError)")
        
        # Suggestions d'optimisation
        if 'for' in code and '+=' in code:
            suggestions.append("Considérer list comprehension pour meilleure performance")
        
        if re.search(r'\.append\(.*\)', code) and 'for' in code:
            suggestions.append("Utiliser list comprehension au lieu de append dans une boucle")
        
        return {'issues': issues, 'suggestions': suggestions}
    
    def _analyze_javascript(self, code: str) -> Dict:
        """Analyse spécifique JavaScript/TypeScript."""
        issues = []
        suggestions = []
        
        # Vérifier var vs let/const
        if re.search(r'\bvar\s+\w+', code):
            issues.append("Utilisation de 'var' (déprécié)")
            suggestions.append("Utiliser 'let' ou 'const' à la place de 'var'")
        
        # Vérifier == vs ===
        if '==' in code and '===' not in code:
            issues.append("Utilisation de == au lieu de ===")
            suggestions.append("Utiliser === pour comparaisons strictes")
        
        # Vérifier les fonctions fléchées
        if 'function(' in code:
            suggestions.append("Considérer les fonctions fléchées (=>) pour plus de concision")
        
        # Vérifier async/await
        if '.then(' in code:
            suggestions.append("Considérer async/await au lieu de .then() pour plus de lisibilité")
        
        return {'issues': issues, 'suggestions': suggestions}
    
    def _analyze_html(self, code: str) -> Dict:
        """Analyse spécifique HTML."""
        issues = []
        suggestions = []
        
        # Vérifier les balises non fermées
        open_tags = re.findall(r'<(\w+)[^>]*>', code)
        close_tags = re.findall(r'</(\w+)>', code)
        
        self_closing = ['img', 'br', 'hr', 'input', 'meta', 'link']
        open_tags = [tag for tag in open_tags if tag not in self_closing]
        
        if len(open_tags) != len(close_tags):
            issues.append("Nombre de balises ouvertes/fermées différent")
            suggestions.append("Vérifier que toutes les balises sont correctement fermées")
        
        # Vérifier les attributs alt pour images
        if '<img' in code and 'alt=' not in code:
            issues.append("Images sans attribut alt")
            suggestions.append("Ajouter des attributs alt pour l'accessibilité")
        
        # Vérifier la sémantique HTML5
        if '<div id="header"' in code or '<div class="header"' in code:
            suggestions.append("Utiliser <header> au lieu de <div> pour l'en-tête")
        
        if '<div id="footer"' in code or '<div class="footer"' in code:
            suggestions.append("Utiliser <footer> au lieu de <div> pour le pied de page")
        
        return {'issues': issues, 'suggestions': suggestions}
    
    def suggest_improvements(self, code: str) -> List[Dict]:
        """Génère des suggestions d'amélioration avec code."""
        analysis = self.analyze_code(code)
        improvements = []
        
        # Créer des suggestions concrètes avec exemples
        for issue in analysis.get('issues', []):
            improvement = {
                'issue': issue,
                'priority': 'high',
                'example': self._generate_fix_example(issue, code, analysis['language'])
            }
            improvements.append(improvement)
        
        for suggestion in analysis.get('suggestions', []):
            improvement = {
                'issue': suggestion,
                'priority': 'medium',
                'example': self._generate_improvement_example(suggestion, code, analysis['language'])
            }
            improvements.append(improvement)
        
        return improvements
    
    def _generate_fix_example(self, issue: str, code: str, language: str) -> str:
        """Génère un exemple de correction."""
        if 'snake_case' in issue and language == 'python':
            # Trouver une fonction en CamelCase
            match = re.search(r'def\s+([A-Z]\w+)', code)
            if match:
                camel_name = match.group(1)
                snake_name = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_name).lower()
                return f"# Avant:\ndef {camel_name}():\n    pass\n\n# Après:\ndef {snake_name}():\n    pass"
        
        if 'var' in issue and language in ['javascript', 'typescript']:
            return "// Avant:\nvar x = 5;\n\n// Après:\nconst x = 5; // ou let x = 5; si modifiable"
        
        if '==' in issue and language in ['javascript', 'typescript']:
            return "// Avant:\nif (x == 5) { }\n\n// Après:\nif (x === 5) { }"
        
        return "Voir la documentation pour plus d'exemples"
    
    def _generate_improvement_example(self, suggestion: str, code: str, language: str) -> str:
        """Génère un exemple d'amélioration."""
        if 'list comprehension' in suggestion and language == 'python':
            return """# Avant:
result = []
for i in range(10):
    result.append(i * 2)

# Après:
result = [i * 2 for i in range(10)]"""
        
        if 'fonctions fléchées' in suggestion:
            return """// Avant:
function add(a, b) {
    return a + b;
}

// Après:
const add = (a, b) => a + b;"""
        
        if 'async/await' in suggestion:
            return """// Avant:
fetch(url).then(response => response.json()).then(data => console.log(data));

// Après:
const response = await fetch(url);
const data = await response.json();
console.log(data);"""
        
        return "Voir la documentation pour plus d'exemples"

# Instance globale
analyzer = CodeAnalyzer()

def get_code_analyzer() -> CodeAnalyzer:
    """Récupère l'instance de l'analyseur de code."""
    return analyzer
