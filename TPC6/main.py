import ply.lex as lex
import re
code ='''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Função que calcula o factorial dum número n

program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}

'''
tokens = [
    'COMENTARIOMULTILINHA',
    'COMENTARIO',
    'FUNCAO',
    'PROGRAM',
    'VARIAVEL'
    'FOR',
    'WHILE',
    'INT',
    'PONTOVIRGULA',
    'VIRGULA'
    'ABRIR_CHAVETA',
    'FECHAR_CHAVETA',
    'ABRIR_PARENTESES_CURVO',
    'FECHAR_PARENTESES_CURVO',
    'ABRIR_PARENTESES_RETO',
    'FECHAR_PARENTESES_RETO',
    'OPERADORLOGICO',
    'OPERADOR',
    'IF',
    'PASSO',
    'IN',
    'FUN_NAME',
    'PROG_NAME'
]

t_ignore = ' \t\n'

def t_COMENTARIOMULTILINHA(t):
    r'\/\*(.*\n)*\*\/'
    print(t)

def t_COMENTARIO(t):
    r'\/\/.*'
    print(t)

def t_WHILE(t):
    r'while\b'
    print(t)

def t_FOR(t):
    r'for\b'
    print(t)

def t_OPERADOR(t):
    r'\+|-|\*|='
    print(t)

def t_FUNCAO(t):
    r'function\b'
    print(t)

def t_FUN_NAME(t):#(?=pattern)
    r'([a-zA-Z]\w*)(?=\()'
    print(t)

def t_PROGRAM(t):
    r'program\b'
    print(t)

def t_PROG_NAME(t):#(?=pattern)
    r'([a-zA-Z]\w*)(?=\{)'
    print(t)

def t_VARIAVEL(t):
    r'[a-zA-Z]\w*'
    print(t)

def t_OPERADORLOGICO(t):
    r'>|<|==|!=|<=|>='
    print(t)

def t_INT(t):
    r'\d+'
    print(t)

def t_ABRIR_CHAVETA(t):
    r'{'
    print(t)

def t_FECHAR_CHAVETA(t):
    r'}'
    print(t)

def t_ABRIR_PARENTESES_CURVO(t):
    r'\('
    print(t)

def t_FECHAR_PARENTESES_CURVO(t):
    r'\)'
    print(t)

def t_ABRIR_PARENTESES_RETO(t):
    r'\['
    print(t)

def t_FECHAR_PARENTESES_RETO(t):
    r'\]'
    print(t)

def t_PONTOVIRGULA(t):
    r';'
    print(t)

def t_VIRGULA(t):
    r','
    print(t)

def t_IN(t):
    r'\bin\b'
    print(t)

def t_PASSO(t):
    r'\.\.'
    print(t)

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(code)

while tok:=lexer.token():
    print(tok)