#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tester ligne par ligne

with open('c:\\Users\\Public\\namz_ia\\app\\code_templates.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Essayer de compiler jusqu'à différentes lignes
test_lines = [11320, 11400, 11500, 11600, 11700, 11800, 11835, 11840]

for line_num in test_lines:
    code = ''.join(lines[:line_num])
    try:
        compile(code, 'test', 'exec')
        print(f"✓ Lines 1-{line_num}: OK")
    except SyntaxError as e:
        print(f"❌ Lines 1-{line_num}: Syntax Error at line {e.lineno}")
        print(f"   {e.msg}")
        break
