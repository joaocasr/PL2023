import ply.lex as lex
import re

listamista='[ 1,5, palavra, False ,3.14,   0, fim]'
tokens = [
    'WORD',
    'BOOL',
    'INT',
    'FLOAT'
    ]
literals='[],'
t_INT=r'\d+'


t_ignore = ' \t\n'

#(int,123) => (t.type,t.value)

def t_WORD(t):
    r'[a-zA-Z]+' 
    if t.value in ('True','False'):
        t.type='BOOL'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value=float(t.value)
    return t

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(listamista)

while tok:=lexer.token():
    print(tok)