KNOWLEDGE_BASE = [
    # Python - Boucles
    {
        "tags": ["python", "boucle", "for"],
        "patterns": [
            "boucle for en python", "loop for python", "for loop example", "exemple boucle python", "parcourir une liste python"
        ],
        "answer": "En Python, une boucle for simple :\n\nfor i in range(5):\n    print(i)"
    },
    {
        "tags": ["python", "boucle", "while"],
        "patterns": [
            "boucle while python", "while loop python", "exemple while python", "loop while example"
        ],
        "answer": "Boucle while en Python :\n\ni = 0\nwhile i < 5:\n    print(i)\n    i += 1"
    },
    # Python - Fonctions
    {
        "tags": ["python", "fonction"],
        "patterns": [
            "définir une fonction en python", "python function", "def function", "exemple fonction python", "function example python"
        ],
        "answer": "Définir une fonction en Python :\n\ndef ma_fonction(arg1, arg2):\n    return arg1 + arg2"
    },
    {
        "tags": ["python", "lambda"],
        "patterns": [
            "lambda python", "fonction anonyme python", "anonymous function python"
        ],
        "answer": "Fonction lambda (anonyme) en Python :\n\nadd = lambda x, y: x + y\nprint(add(2, 3))  # Affiche 5"
    },
    # Python - Listes et dictionnaires
    {
        "tags": ["python", "liste"],
        "patterns": [
            "créer une liste python", "list python", "exemple liste python", "python list example"
        ],
        "answer": "Créer et parcourir une liste :\n\nma_liste = [1, 2, 3]\nfor item in ma_liste:\n    print(item)"
    },
    {
        "tags": ["python", "dictionnaire", "dict"],
        "patterns": [
            "dictionnaire python", "dict python", "exemple dictionnaire python", "python dict example"
        ],
        "answer": "Créer et parcourir un dictionnaire :\n\nmon_dict = {'a': 1, 'b': 2}\nfor cle, valeur in mon_dict.items():\n    print(cle, valeur)"
    },
    # Python - Classes
    {
        "tags": ["python", "classe", "oop"],
        "patterns": [
            "classe python", "class python", "oop python", "exemple classe python"
        ],
        "answer": "Définir une classe en Python :\n\nclass Animal:\n    def __init__(self, nom):\n        self.nom = nom\n    def parler(self):\n        print(f'Je suis {self.nom}')"
    },
    # Python - Exceptions
    {
        "tags": ["python", "exception", "try except"],
        "patterns": [
            "gestion d'exception python", "try except python", "python error handling"
        ],
        "answer": "Gestion d'exception en Python :\n\ntry:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Division par zéro !')"
    },
    # Python - Fichiers
    {
        "tags": ["python", "fichier", "file"],
        "patterns": [
            "ouvrir fichier python", "read file python", "écrire fichier python", "write file python"
        ],
        "answer": "Lire un fichier texte en Python :\n\nwith open('monfichier.txt', 'r') as f:\n    contenu = f.read()\n\nÉcrire dans un fichier :\n\nwith open('monfichier.txt', 'w') as f:\n    f.write('Bonjour !')"
    },
    # Python - Décorateurs
    {
        "tags": ["python", "decorateur", "decorator"],
        "patterns": [
            "decorateur python", "python decorator", "exemple decorateur python"
        ],
        "answer": "Exemple de décorateur en Python :\n\ndef mon_decorateur(fonction):\n    def wrapper(*args, **kwargs):\n        print('Avant')\n        resultat = fonction(*args, **kwargs)\n        print('Après')\n        return resultat\n    return wrapper\n\n@mon_decorateur\ndef dire_hello():\n    print('Hello')"
    },
    # Python - Tests unitaires
    {
        "tags": ["python", "test", "unittest"],
        "patterns": [
            "test unitaire python", "unittest python", "exemple test python"
        ],
        "answer": "Test unitaire avec unittest :\n\nimport unittest\n\nclass TestAddition(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(1 + 1, 2)\n\nif __name__ == '__main__':\n    unittest.main()"
    },
    # JavaScript - Variables et fonctions
    {
        "tags": ["javascript", "variable"],
        "patterns": [
            "variable javascript", "js variable", "déclarer variable js"
        ],
        "answer": "Déclarer une variable en JS :\n\nlet x = 5;\nconst y = 'Hello';"
    },
    {
        "tags": ["javascript", "fonction"],
        "patterns": [
            "fonction javascript", "js function", "function js", "exemple fonction js"
        ],
        "answer": "Définir une fonction en JS :\n\nfunction add(a, b) {\n    return a + b;\n}\n\nconst res = add(2, 3);"
    },
    # JavaScript - Boucles
    {
        "tags": ["javascript", "boucle", "for"],
        "patterns": [
            "boucle for js", "for loop js", "exemple boucle js"
        ],
        "answer": "Boucle for en JS :\n\nfor (let i = 0; i < 5; i++) {\n    console.log(i);\n}"
    },
    # JavaScript - Promises et fetch
    {
        "tags": ["javascript", "fetch", "http", "promise"],
        "patterns": [
            "fetch javascript", "appel api js", "http request js", "promise js"
        ],
        "answer": "Appel HTTP avec fetch :\n\nfetch('https://api.example.com/data')\n  .then(res => res.json())\n  .then(data => console.log(data))\n  .catch(err => console.error(err));"
    },
    # JavaScript - Manipulation DOM
    {
        "tags": ["javascript", "dom"],
        "patterns": [
            "manipuler dom js", "js dom", "exemple dom js"
        ],
        "answer": "Changer le texte d'un élément :\n\ndocument.getElementById('monId').textContent = 'Nouveau texte';"
    },
    # Flask - Routes et API
    {
        "tags": ["flask", "route", "api"],
        "patterns": [
            "créer une route flask", "flask route example", "flask api", "exemple api flask"
        ],
        "answer": "Exemple de route Flask :\n\nfrom flask import Flask, jsonify\napp = Flask(__name__)\n\n@app.route('/api/hello')\ndef hello():\n    return jsonify({'message': 'Hello'})"
    },
    # Flask - Templates
    {
        "tags": ["flask", "template", "html"],
        "patterns": [
            "template flask", "flask html", "render template flask"
        ],
        "answer": "Rendre un template HTML avec Flask :\n\nfrom flask import render_template\n\n@app.route('/')\ndef index():\n    return render_template('index.html')"
    },
    # Flask - Formulaires
    {
        "tags": ["flask", "form", "formulaire"],
        "patterns": [
            "formulaire flask", "flask form", "exemple form flask"
        ],
        "answer": "Gérer un formulaire avec Flask :\n\nfrom flask import request\n\n@app.route('/form', methods=['POST'])\ndef form():\n    data = request.form\n    return 'Vous avez envoyé : ' + data['champ']"
    },
    # Flask - JSON
    {
        "tags": ["flask", "json"],
        "patterns": [
            "json flask", "flask json response", "envoyer json flask"
        ],
        "answer": "Retourner du JSON avec Flask :\n\nfrom flask import jsonify\n\n@app.route('/api/data')\ndef data():\n    return jsonify({'clé': 'valeur'})"
    },
    # Git - Commandes de base
    {
        "tags": ["git", "commande"],
        "patterns": [
            "git clone", "git commit", "git push", "commande git"
        ],
        "answer": "Commandes Git de base :\n\ngit clone <url>\ngit status\ngit add .\ngit commit -m 'message'\ngit push"
    },
    # Linux - Commandes de base
    {
        "tags": ["linux", "commande"],
        "patterns": [
            "commande linux", "ls linux", "cd linux", "linux terminal"
        ],
        "answer": "Commandes Linux utiles :\n\nls  # lister les fichiers\ncd dossier  # changer de dossier\ncat fichier.txt  # afficher le contenu"
    },
    # SQL - Sélection de données
    {
        "tags": ["sql", "select"],
        "patterns": [
            "requete select sql", "sql select", "exemple select sql"
        ],
        "answer": "Sélectionner des données en SQL :\n\nSELECT * FROM ma_table WHERE colonne = 'valeur';"
    },
    # Docker - Commandes de base
    {
        "tags": ["docker", "commande"],
        "patterns": [
            "docker run", "docker build", "commande docker"
        ],
        "answer": "Commandes Docker de base :\n\ndocker build -t monimage .\ndocker run -p 5000:5000 monimage\ndocker ps\ndocker stop <id>"
    },
    # Markdown - Syntaxe
    {
        "tags": ["markdown", "syntaxe"],
        "patterns": [
            "syntaxe markdown", "markdown example", "exemple markdown"
        ],
        "answer": "Exemple de syntaxe Markdown :\n\n# Titre\n**gras**\n*italique*\n- liste\n[un lien](https://example.com)"
    },
    # C - Boucle for
    {
        "tags": ["c", "boucle", "for"],
        "patterns": [
            "boucle for en c", "for loop c", "exemple boucle c"
        ],
        "answer": "Boucle for en C :\n\n#include <stdio.h>\n\nint main() {\n    for (int i = 0; i < 5; i++) {\n        printf(\"%d\\n\", i);\n    }\n    return 0;\n}"
    },
    # C - Fonction
    {
        "tags": ["c", "fonction"],
        "patterns": [
            "fonction en c", "function c", "exemple fonction c"
        ],
        "answer": "Définir une fonction en C :\n\nint add(int a, int b) {\n    return a + b;\n}\n\nint main() {\n    printf(\"%d\\n\", add(2, 3));\n    return 0;\n}"
    },
    # C - Pointeurs
    {
        "tags": ["c", "pointeur", "pointer"],
        "patterns": [
            "pointeur c", "pointer c", "exemple pointeur c"
        ],
        "answer": "Exemple de pointeur en C :\n\nint x = 10;\nint *p = &x;\nprintf(\"%d\\n\", *p);"
    },
    # C# - Déclaration de variable
    {
        "tags": ["c#", ".net", "variable"],
        "patterns": [
            "variable c#", "declarer variable c#", "c# variable"
        ],
        "answer": "Déclarer une variable en C# :\n\nint x = 5;\nstring nom = \"Alice\";"
    },
    # C# - Classe
    {
        "tags": ["c#", ".net", "classe", "oop"],
        "patterns": [
            "classe c#", "class c#", "exemple classe c#"
        ],
        "answer": "Définir une classe en C# :\n\npublic class Person {\n    public string Name { get; set; }\n    public Person(string name) { Name = name; }\n    public void SayHello() {\n        Console.WriteLine($\"Hello, I am {Name}\");\n    }\n}"
    },
    # C# - Boucle foreach
    {
        "tags": ["c#", ".net", "foreach", "boucle"],
        "patterns": [
            "foreach c#", "boucle foreach c#", "exemple foreach c#"
        ],
        "answer": "Boucle foreach en C# :\n\nstring[] noms = { \"Alice\", \"Bob\" };\nforeach (string nom in noms) {\n    Console.WriteLine(nom);\n}"
    },
    # C# - LINQ
    {
        "tags": ["c#", ".net", "linq"],
        "patterns": [
            "linq c#", "exemple linq c#", "query linq c#"
        ],
        "answer": "Exemple LINQ en C# :\n\nvar nombres = new int[] { 1, 2, 3, 4, 5 };\nvar pairs = nombres.Where(n => n % 2 == 0);\nforeach (var n in pairs) {\n    Console.WriteLine(n);\n}"
    },
    # ASP.NET - Contrôleur API
    {
        "tags": ["asp.net", ".net", "api", "controller"],
        "patterns": [
            "api controller asp.net", "exemple controller asp.net", "asp.net api"
        ],
        "answer": "Exemple de contrôleur API en ASP.NET Core :\n\n[ApiController]\n[Route(\"api/[controller]\")]\npublic class HelloController : ControllerBase {\n    [HttpGet]\n    public IActionResult Get() {\n        return Ok(new { message = \"Hello\" });\n    }\n}"
    },
    # ASP.NET - Vue Razor
    {
        "tags": ["asp.net", ".net", "razor", "vue"],
        "patterns": [
            "razor asp.net", "vue razor asp.net", "exemple razor asp.net"
        ],
        "answer": "Exemple de vue Razor :\n\n@model string\n<h1>Hello @Model!</h1>"
    },
]
