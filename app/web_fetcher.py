def fetch_the_algorithms_snippets(lang, max_results=10):
    """Récupère des snippets de base depuis The Algorithms (GitHub public, sans token)."""
    import requests
    import re
    lang_map = {
        'python': 'Python',
        'js': 'Javascript',
        'javascript': 'Javascript',
        'c': 'C',
        'java': 'Java',
        'cpp': 'C-Plus-Plus',
        'go': 'Go',
        'ruby': 'Ruby',
        'php': 'PHP',
        'rust': 'Rust',
        'swift': 'Swift',
    }
    repo_lang = lang_map.get(lang.lower())
    if not repo_lang:
        return []
    api_url = f'https://api.github.com/repos/TheAlgorithms/{repo_lang}/git/trees/master?recursive=1'
    resp = requests.get(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    if resp.status_code != 200:
        return []
    data = resp.json()
    files = [f['path'] for f in data.get('tree', []) if f['path'].endswith(('.py','.js','.c','.java','.cpp','.go','.rb','.php','.rs','.swift'))]
    snippets = []
    for path in files[:max_results*2]:  # Essayer plus de fichiers
        try:
            raw_url = f'https://raw.githubusercontent.com/TheAlgorithms/{repo_lang}/master/{path}'
            code_resp = requests.get(raw_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
            if code_resp.status_code != 200:
                continue
            code = code_resp.text
            # Découpe en fonctions (pour Python, JS, C)
            if lang.lower() == 'python':
                funcs = re.findall(r'def [\w_]+\(.*?\):[\s\S]*?(?=^def |\Z)', code, re.MULTILINE)
                for f in funcs:
                    if len(f.strip()) > 20:
                        snippets.append({'source': raw_url, 'code': f.strip()})
                        if len(snippets) >= max_results:
                            return snippets
            elif lang.lower() in ('js','javascript'):
                funcs = re.findall(r'function [\w_]+\(.*?\) ?{[\s\S]*?}', code)
                for f in funcs:
                    if len(f.strip()) > 20:
                        snippets.append({'source': raw_url, 'code': f.strip()})
                        if len(snippets) >= max_results:
                            return snippets
            else:
                if len(code.strip()) > 20:
                    snippets.append({'source': raw_url, 'code': code.strip()})
                    if len(snippets) >= max_results:
                        return snippets
        except Exception:
            continue
    return snippets[:max_results]
def fetch_rosetta_code_snippets(task, lang, max_results=3):
    """Récupère des snippets pour une tâche donnée sur Rosetta Code (multi-langages)."""
    import urllib.parse
    # Convertit les underscores en espaces pour RosettaCode
    task_formatted = task.replace('_', ' ')
    url = f'https://rosettacode.org/wiki/{urllib.parse.quote(task_formatted.replace(" ", "_"))}'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if resp.status_code != 200:
        return [{'source': url, 'code': f'[CAPTCHA/HTTP {resp.status_code} détecté sur RosettaCode]'}]
    if 'captcha' in resp.text.lower() or 'cloudflare' in resp.text.lower():
        return [{'source': url, 'code': '[CAPTCHA détecté sur RosettaCode]'}]
    soup = BeautifulSoup(resp.text, 'html.parser')
    snippets = []
    found = soup.find_all('h2')
    for h in found:
        span = h.find('span', class_='mw-headline')
        if span and lang.lower() in span.text.lower():
            code_blocks = []
            sib = h
            while True:
                sib = sib.find_next_sibling()
                if sib is None or sib.name == 'h2':
                    break
                if sib.name == 'pre':
                    code_blocks.append(sib.get_text().strip())
            for code in code_blocks:
                if len(code) > 20:
                    snippets.append({'source': url, 'code': code})
                    if len(snippets) >= max_results:
                        return snippets
    return snippets

def fetch_github_code_search(query, lang, max_results=3):
    """Recherche du code sur GitHub via l'API search/code (nécessite un token pour gros volume)."""
    # Pour usage public limité, pas de token ici
    url = f'https://api.github.com/search/code?q={query}+language:{lang}&per_page={max_results}'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if resp.status_code != 200:
        return [{'source': url, 'code': f'[CAPTCHA/HTTP {resp.status_code} détecté sur GitHub CodeSearch]'}]
    if 'captcha' in resp.text.lower() or 'cloudflare' in resp.text.lower():
        return [{'source': url, 'code': '[CAPTCHA détecté sur GitHub CodeSearch]'}]
    data = resp.json()
    snippets = []
    for item in data.get('items', []):
        raw_url = item['html_url'].replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
        code = requests.get(raw_url).text
        if len(code.strip()) > 20:
            snippets.append({'source': item['html_url'], 'code': code.strip()})
            if len(snippets) >= max_results:
                break
    return snippets
import requests
import re
from bs4 import BeautifulSoup

def fetch_stackoverflow_snippets(query, max_results=3):
    """Recherche tous les snippets pertinents sur StackOverflow pour une question donnée (toutes réponses, filtrage taille et unicité)."""
    search_url = f"https://stackoverflow.com/search?q={query.replace(' ', '+')}"
    resp = requests.get(search_url, headers={'User-Agent': 'Mozilla/5.0'})
    if resp.status_code != 200:
        return [{'source': search_url, 'code': f'[CAPTCHA/HTTP {resp.status_code} détecté sur StackOverflow]'}]
    if 'captcha' in resp.text.lower() or 'cloudflare' in resp.text.lower():
        return [{'source': search_url, 'code': '[CAPTCHA détecté sur StackOverflow]'}]
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = [a['href'] for a in soup.select('.result-link a')][:max_results*4]
    snippets = []
    seen = set()
    for link in links:
        url = f"https://stackoverflow.com{link}"
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if page.status_code != 200:
            snippets.append({'source': url, 'code': f'[CAPTCHA/HTTP {page.status_code} détecté sur StackOverflow]'});
            continue
        if 'captcha' in page.text.lower() or 'cloudflare' in page.text.lower():
            snippets.append({'source': url, 'code': '[CAPTCHA détecté sur StackOverflow]'});
            continue
        psoup = BeautifulSoup(page.text, 'html.parser')
        answers = psoup.select('.answer')
        for ans in answers:
            codes = ans.select('pre code')
            for code in codes:
                snippet = code.get_text().strip()
                if len(snippet) > 20 and snippet not in seen:
                    seen.add(snippet)
                    snippets.append({'source': url, 'code': snippet})
                    if len(snippets) >= max_results:
                        return snippets
    return snippets

def fetch_github_gist_snippets(query, max_results=3):
    """Recherche des snippets publics sur GitHub Gist via l'API (cherche dans tous les fichiers, pas juste la description)."""
    url = f'https://api.github.com/gists/public'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if resp.status_code != 200:
        return [{'source': url, 'code': f'[CAPTCHA/HTTP {resp.status_code} détecté sur GitHub Gist]'}]
    if 'captcha' in resp.text.lower() or 'cloudflare' in resp.text.lower():
        return [{'source': url, 'code': '[CAPTCHA détecté sur GitHub Gist]'}]
    data = resp.json()
    snippets = []
    for gist in data:
        for file in gist.get('files', {}).values():
            content_url = file.get('raw_url')
            if content_url:
                code = requests.get(content_url).text
                if len(code.strip()) > 20 and query.lower() in code.lower():
                    snippets.append({'source': gist['html_url'], 'code': code.strip()})
                    if len(snippets) >= max_results:
                        return snippets
    return snippets
