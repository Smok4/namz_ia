#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_brackets(filename, start_line=11840, end_line=12370):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    stack = []
    in_string = False
    string_char = None
    escape_next = False
    in_triple_quote = False
    triple_quote_char = None
    
    for line_num in range(start_line - 1, min(end_line, len(lines))):
        line = lines[line_num]
        i = 0
        while i < len(line):
            char = line[i]
            
            # Gérer les échappements
            if escape_next:
                escape_next = False
                i += 1
                continue
            
            if char == '\\':
                escape_next = True
                i += 1
                continue
            
            # Gérer les triple quotes
            if i + 2 < len(line) and line[i:i+3] in ('"""', "'''"):
                if not in_string:
                    if not in_triple_quote:
                        in_triple_quote = True
                        triple_quote_char = line[i:i+3]
                    elif line[i:i+3] == triple_quote_char:
                        in_triple_quote = False
                        triple_quote_char = None
                    i += 3
                    continue
            
            # Si on est dans une string, ignorer les brackets
            if in_triple_quote:
                i += 1
                continue
            
            # Gérer les simples quotes
            if char in ('"', "'"):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = None
                i += 1
                continue
            
            if not in_string:
                if char in '({[':
                    stack.append((char, line_num + 1, i))
                elif char in ')}]':
                    matching = {')':'(', '}':'{', ']':'['}
                    if not stack:
                        print(f"❌ Closing bracket '{char}' without opening at line {line_num + 1}, col {i}")
                        return False
                    if stack[-1][0] != matching[char]:
                        print(f"❌ Mismatched brackets at line {line_num + 1}: expected '{matching[char]}', got '{char}'")
                        print(f"   Opening bracket was at line {stack[-1][1]}")
                        return False
                    stack.pop()
            
            i += 1
    
    if stack:
        print(f"❌ Unclosed brackets found:")
        for bracket, line, col in stack:
            print(f"   '{bracket}' at line {line}, column {col}")
        return False
    
    print(f"✓ All brackets matched in lines {start_line}-{end_line}")
    return True

if __name__ == '__main__':
    check_brackets('c:\\Users\\Public\\namz_ia\\app\\code_templates.py', 11320, 12370)
