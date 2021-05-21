
import ply.yacc as yacc
import sys
from calc_lex import tokens


def p_Comando_ler(p):
    "Comando : '?' id"
    valor = input("Introduza um valor inteiro: ")
    p.parser.registers.update({p[2]: int(valor)})


def p_Comando_escrever(p):
    "Comando : '!' Exp"
    print(p[2])

def p_Comando_atrib(p):
    "Comando : id '=' Exp"
    p.parser.registers.update({p[1]: p[3]})

def p_Comando_despejar(p):
    "Comando : '!' '!'"
    print(p.parser.registers)



def p_Exp_add(p):
    "Exp : Exp '+' Termo"
    p[0] = p[1]+p[3] 

def p_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = p[1]-p[3] 

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Termo : Termo '*' Factor"
    p[0] = p[1]*p[3] 

def p_Termo_div(p):
    "Termo : Termo '/' Factor"
    if (p[3]!= 0):
        p[0] = p[1]/p[3] 
    else:
        print("Erro: divisao por 0. A continuar com o dividendo: ",p[1])
        p[0]=p[1]


def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

def p_Factor_num(p):
    "Factor : num"
    p[0] = int(p[1])

def p_Factor_id(p):
    "Factor : id"
    p[0] = p.parser.registers.get(p[1])


    


def p_error(p):
    print("Syntax error in input: ",p)

parser = yacc.yacc()


#creating the model

parser.registers = {}


for linha in sys.stdin:
    result = parser.parse(linha)
    print(result)