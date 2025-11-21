import json
import os

EXAMPLES_PATH = os.path.join(os.path.dirname(__file__), 'user_examples_data.json')

def load_user_examples():
    if not os.path.exists(EXAMPLES_PATH):
        return []
    with open(EXAMPLES_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_user_example(question, code, lang=None):
    examples = load_user_examples()
    examples.append({"question": question, "code": code, "lang": lang})
    with open(EXAMPLES_PATH, 'w', encoding='utf-8') as f:
        json.dump(examples, f, ensure_ascii=False, indent=2)

def find_best_user_example(message):
    examples = load_user_examples()
    def sim(a, b):
        sa = set(a.lower().split())
        sb = set(b.lower().split())
        if not sa or not sb:
            return 0.0
        return len(sa & sb) / len(sa | sb)
    best = None
    best_score = 0.0
    for ex in examples:
        score = sim(message, ex["question"])
        if score > best_score:
            best_score = score
            best = ex
    if best and best_score > 0.5:
        return best["code"]
    return None
