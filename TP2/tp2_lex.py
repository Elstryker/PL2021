import ply.lex as lex

# Tokens
tokens = ['DEFF', 'DEFI','ID', 'NUM', 'FLOAT', 'COS', 'SIN', 'MAIORIG', 'MENORIG', 'MAIOR', 'MENOR', 'IGUAL'
          ,'IGUALDADE','IF', 'ELSE', 'OR', 'AND', 'TRUE', 'FALSE', 'GETLINE', 'PRINTF', 'TEXTO', 'RETURN', 'DEF',
          'CALL', 'FOR', 'WHILE', 'DIFERENTE', 'REPEAT', 'UNTIL', 'MAISMAIS', 'MENOSMENOS']

literals = ['+', '*', '/','-','%','(',')','{','}','[',']',';', ":"]

def t_MENOSMENOS(t):
    r'\-\-'
    return t

def t_MAISMAIS(t):
    r'\+\+'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    return t

def t_NUM(t):
    r'-?\d+'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_MALLOC(t):
    r'malloc'
    return t

def t_IGUALDADE(t):
    r'=='
    return t

def t_DIFERENTE(t):
    r'!='
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_CALL(t):
    r'call'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_DEF(t):
    r'def'
    return t

def t_GETLINE(t):
    r'getline\(\)'
    return t

def t_PRINTF(t):
    r'printf'
    return t

def t_TEXTO(t):
    r'\"[^"]+\"'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_AND(t):
    r'&&'
    return t

def t_OR(t):
    r'\|\|'
    return t

def t_IF(t):
    r'if'
    return t

def t_MAIORIG(t):
    r'>='
    return t

def t_MENORIG(t):
    r'<='
    return t

def t_MENOR(t):
    r'<'
    return t

def t_MAIOR(t):
    r'>'
    return t

def t_IGUAL(t):
    r'='
    return t

def t_COS(t):
    r'cos'
    return t

def t_SIN(t):
    r'sin'
    return t

def t_DEFF(t):
    r'float'
    return t

def t_DEFI(t):
    r'int'
    return t

def t_ID(t):
    r'\w+'
    return t

t_ignore = " \t\n"

def t_error(t):
    print("Caráter ilegal: ", t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()