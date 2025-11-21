#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Test progressif pour trouver l'erreur

try:
    from app import code_templates
    print("✓ Import successful!")
except SyntaxError as e:
    print(f"✗ Syntax Error:")
    print(f"  File: {e.filename}")
    print(f"  Line: {e.lineno}")
    print(f"  Message: {e.msg}")
    print(f"  Text: {e.text}")
