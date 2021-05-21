import ply.yacc as yacc
import sys

# Get the token map from the lexer.
from tp2_lex import tokens

#--------------------------------------PROGRAMA + INICIALIZACOES------------------------------------------------

def p_programa(p):
    "programa : inicializacoes declararFuncs codigo"

    print('STOP')

def p_inicializacoes(p):
    "inicializacoes : inicializacoes inicializacao"

def p_inicializacoes_nul(p):
    "inicializacoes : "

def p_inicializacao(p):
    "inicializacao : DEFI ID IGUAL MATI"

    if p[2] not in p.parser.vars:
        fp = p.parser.fp.pop()
        p.parser.vars[p[2]] = fp
        p.parser.fp.append(fp+1)
    else:
        print('Essa variavel já existe')
        p_error(p)
        exit()

def p_inicializacao_array(p):
    "inicializacao : DEFI '[' NUM ']' ID"

    if p[5] not in p.parser.vars:
        fp = p.parser.fp.pop()
        num = int(p[3])
        p.parser.vars[p[5]] = [fp,num]
        print("PUSHN", num)
        p.parser.fp.append(fp + num)
    else:
        print('Essa variavel já existe')
        p_error(p)
        exit()

def p_inicializacao_array2d(p):
    "inicializacao : DEFI '[' NUM ']' '[' NUM ']' ID"

    if p[8] not in p.parser.vars:
        linhas = int(p[3])
        colunas = int(p[6])

        fp = p.parser.fp.pop()
        p.parser.vars[p[8]] = [fp,colunas]
        print("PUSHN", linhas*colunas)
        p.parser.fp.append(fp+linhas*colunas)
    else:
        print('Essa variavel já existe')
        p_error(p)
        exit()

def p_inicializacao_nul(p):
    "inicializacao : DEFI ID"

    if p[2] not in p.parser.vars:
        fp = p.parser.fp.pop()
        p.parser.vars[p[2]] = fp
        p.parser.fp.append(fp + 1)
    else:
        print('Essa variavel já existe')
        p_error(p)
        exit()
    print("PUSHI 0")

def p_inicializacao_float(p):
    "inicializacao : DEFF ID IGUAL MATF"

    if p[2] not in p.parser.vars:
        fp = p.parser.fp.pop()
        p.parser.vars[p[2]] = fp
        p.parser.fp.append(fp + 1)
    else:
        print('Essa variavel já existe')
        p_error(p)
        exit()

def p_declararFuncs(p):
    "declararFuncs : "

def p_declararFuncsF(p):
    "declararFuncs : declararFuncs declaracao"


#--------------------------------- OPERAÇÕES COM INTEIROS ------------------------------------------

def p_MATI_operando(p):
    "MATI : operando"

def p_Termo_factor(p):
    "operando : factor"

def p_MATI_SOMA(p):
    "MATI : MATI '+' operando"

    print("ADD")

def p_MATI_SUB(p):
    "MATI : MATI '-' operando"

    print("SUB")

def p_MATI_MUL(p):
    "operando : operando '*' factor"

    print("MUL")

def p_MATI_DIV(p):
    "operando : operando '/' factor"

    print("DIV")

def p_MATI_MOD(p):
    "operando : operando '%' factor"

    print("MOD")

def p_operando(p):
    "factor : NUM"

    print("PUSHI", p[1])

def p_operandoID(p):
    "factor : ID"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("PUSHL", p.parser.vars[p[1]])

def p_Factor_group(p):
    "factor : '(' MATI ')'"

# ------------------------------------------ ARRAYS --------------------------------------------

def p_Arr(p):
    "arr : ID"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("PUSHFP")
    print("PUSHI", p.parser.vars[p[1]][0])
    print("PADD")
    p[0] = p[1]

def p_operandoArrayVar(p):
    "operando : arr '[' MATI ']'"

    print("LOADN")

def p_operandoArray2d(p):
    "operando : arr '[' MATI ']' '[' MATI ']'"

    print("SWAP")
    print("PUSHI", p.parser.vars[p[1]][1])
    print("MUL")
    print("ADD")
    print("LOADN")


#-------------------------------------- OPERAÇÕES COM FLOATS -----------------------------------------

def p_MATF_NUM(p):
    "MATF : FEXP"

def p_MATF_SOMA(p):
    "MATF : MATF '+' FEXP"

    print("FADD")

def p_FEXP_F(p):
    "FEXP : FLOAT"

    print("PUSHF", p[1])

def p_FEXP_C(p):
    "FEXP : COS '(' MATF ')'"

    print("FCOS")

def p_FEXP_S(p):
    "FEXP : SIN '(' MATF ')'"

    print("FSIN")

def p_MATF_SUB(p):
    "MATF : MATF '-' FLOAT"

    print("PUSHF", p[3])
    print("FSUB")

def p_MATF_MUL(p):
    "MATF : MATF '*' FLOAT"

    print("PUSHF", p[3])
    print("FMUL")

def p_MATF_DIV(p):
    "MATF : MATF '/' FLOAT"

    print("PUSHF", p[3])
    print("FDIV")

# -------------------------------------------- CODIGO ------------------------------------------------

def p_codigo(p):
    "codigo : "

def p_codigo2(p):
    "codigo : codigo bloco"

def p_bloco_atribArray(p):
    "bloco : arr '[' MATI ']' IGUAL MATI"

    print("STOREN")


def p_matriz(p):
    "matriz : arr posicoes"

    print("PUSHI", p.parser.vars[p[1]][1])
    print("MUL")
    print("ADD")

def p_posicoes(p):
    "posicoes : '[' MATI ']' '[' MATI ']'"

    print("SWAP")

def p_bloco_atribArray2d(p):
    "bloco : matriz IGUAL MATI"

    print("STOREN")


def p_bloco_menosmenos(p):
    "bloco : ID MENOSMENOS"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("PUSHL", p.parser.vars[p[1]])
    print("PUSHI 1")
    print("SUB")
    print("STOREL", p.parser.vars[p[1]])


def p_bloco_maismais(p):
    "bloco : ID MAISMAIS"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("PUSHL", p.parser.vars[p[1]])
    print("PUSHI 1")
    print("ADD")
    print("STOREL", p.parser.vars[p[1]])

def p_bloco_bool(p):
    "bloco : ID IGUAL bool"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("STOREL", p.parser.vars[p[1]])

def p_bloco_mati(p):
    "bloco : ID IGUAL MATI"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("STOREL", p.parser.vars[p[1]])

# ------------------------------------------------ CHAMADA DE FUNÇÕES -----------------------------------------------

def p_callF(p):
    "callF : CALL ID '(' ')'"

    print("PUSHI 0")

    if p[2] not in p.parser.funcs:
        p_error(p)
        print("A função que está a chamar não existe, adeus")
        exit()

    print("PUSHA f" + p.parser.funcs[p[2]])
    print("CALL")

def p_codigo_callF(p):
    "bloco : callF"

def p_bloco_atrib(p):
    "bloco : ID IGUAL callF"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()
    print("STOREL", p.parser.vars[p[1]])

def p_declaracao(p):
    "declaracao : defFunc '(' ')' '{' inicializacoes codigo return '}'"

    print("l" + str(p[1]) + ":")

def p_defFunc(p):
    "defFunc : DEF ID"

    if p[2] not in p.parser.funcs:
        parser.funcs[p[2]] = str(p.parser.base)
        #print("isto dá ", parser.funcs[p[2]][0], parser.funcs[p[2]][1])
    else:
        print('Essa função já existe')
        p_error(p)
        exit()

    label = parser.numLabel
    print("JUMP l" + str(label))
    print("f" + parser.funcs[p[2]] + ":")
    p.parser.base += 1
    p.parser.fp.append(0)
    p[0] = p.parser.numLabel
    p.parser.numLabel += 2

def p_return(p):
    "return : RETURN NUM"

    p.parser.fp.pop()
    print("PUSHI", p[2])
    print("STOREL -1")
    print("RETURN")

def p_return_var(p):
    "return : RETURN ID"

    if p[2] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    p.parser.fp.pop()
    print("PUSHL", p.parser.vars[p[2]])
    print("STOREL -1")
    print("RETURN")

# ----------------------------------------- READS / WRITES ------------------------------------------

def p_bloco_write(p):
    "bloco : PRINTF '(' textos ')'"

    print("WRITES")
    print('PUSHS "\\n"')
    print("WRITES")

def p_textos(p):
    "textos : TEXTO"

    print("PUSHS", p[1])

def p_textos_arr(p):
    "textos : TEXTO '+' arr '[' MATI ']'"

    print("LOADN")
    print("STRI")
    print("PUSHS", p[1])
    print("CONCAT")

def p_textos_arrSTR(p):
    "textos : TEXTO '+' array '+' TEXTO"

    print("PUSHS", p[5])
    print("CONCAT")
    print("PUSHS", p[1])
    print("CONCAT")

def p_textos_array(p):
    "array : arr '[' MATI ']'"

    print("LOADN")
    print("STRI")


def p_textos_nn(p):
    "textos : TEXTO '+' ID '+' TEXTO"

    if p[3] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("PUSHS", p[5])
    print("PUSHL", p.parser.vars[p[3]])
    print("STRI")
    print("CONCAT")
    print("PUSHS", p[1])
    print("CONCAT")

def p_textos_id(p):
    "textos : TEXTO '+' ID"

def p_bloco_writeS(p):
    "bloco : PRINTF '(' MATI ')'"

    print("WRITEI")
    print('PUSHS "\\n"')
    print("WRITES")

def p_bloco_read(p):
    "bloco : ID IGUAL GETLINE"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("READ")
    print("ATOI")
    print("STOREL", p.parser.vars[p[1]])

def p_bloco_readArr(p):
    "bloco : arr '[' MATI ']' IGUAL GETLINE"

    print("READ")
    print("ATOI")
    print("STOREN")

# ------------------------------------------------------- IFS -----------------------------------------------

def p_bloco_if_else(p):
    "bloco : initIF '{' codigo '}' else '{' codigo '}'"

    lbl = p.parser.ifs.pop()
    print("if" + str(p[5]) + ":")

def p_bloco_if(p):
    "bloco : initIF '{' codigo '}'"

    lbl = p.parser.ifs.pop()
    print("if" + str(lbl) + ":")

def p_initIF(p):
    "initIF : IF '(' bool ')'"

    print("JZ if" + str(p.parser.numIfs))
    p.parser.ifs.append(p.parser.numIfs)
    p.parser.numIfs += 1

def p_else(p):
    "else : ELSE"

    numero = p.parser.numIfs
    print("JUMP if" + str(numero))
    p[0] = numero
    lbl = p.parser.ifs.pop()
    print("if" + str(lbl) + ":")
    p.parser.ifs.append(lbl)

# ----------------------------------------- CICLOS FOR ---------------------------------------------

def p_bloco_for(p):
    "bloco : FOR '(' cFor ')' '{' codigo '}'"

    print("JUMP for" + p[3][3])
    print("for" + p[3][1] + ":")

def p_cFor(p):
    "cFor : initFor ';' ID IGUAL MATI"

    if p[3] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("STOREL", p.parser.vars[p[3]])
    print("JUMP for" + p[1][0])
    print("for" + p[1][2] + ":")
    p[0] = p[1]

def p_cFormais(p):
    "cFor : initEBool ';' incremento"

    print("JUMP for" + p[1][0])
    print("for" + p[1][2] + ":")
    p[0] = p[1]

def p_initFor(p):
    "initFor : ID IGUAL MATI"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("STOREL", p.parser.vars[p[1]])
    lbl = str(p.parser.numLabel)
    print("for" + lbl + ":")
    p.parser.numLabel += 1
    p[0] = lbl

def p_initEBool(p):
    "initEBool : initFor ';' bool"

    lbl1 = str(p.parser.numLabel)
    p.parser.numLabel += 1
    print("JZ for" + lbl1)
    lbl2 = str(p.parser.numLabel)
    print("JUMP for" + lbl2)
    p.parser.numLabel += 1
    lbl3 = str(p.parser.numLabel)
    print("for" + lbl3 + ":")
    p[0] = [p[1], lbl1, lbl2, lbl3]

def p_incrementoEXP(p):
    "incremento : ID IGUAL MATI"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("STOREL", p.parser.vars[p[1]])


def p_incrementoMENOS(p):
    "incremento : ID MENOSMENOS"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("PUSHL", p.parser.vars[p[1]])
    print("PUSHI 1")
    print("SUB")
    print("STOREL", p.parser.vars[p[1]])

def p_incrementoMM(p):
    "incremento : ID MAISMAIS"

    if p[1] not in p.parser.vars:
        p_error(p)
        print("A variável não existe, adeus")
        exit()

    print("PUSHL", p.parser.vars[p[1]])
    print("PUSHI 1")
    print("ADD")
    print("STOREL", p.parser.vars[p[1]])

# ------------------------------------------------- BOLEANOS -----------------------------------------------------


def p_bool_and(p):
    "bool : bool AND boolexp"

    print("ADD")
    print("PUSHI 2")
    print("EQUAL")

def p_bool_or(p):
    "bool : bool OR boolexp"

    print("ADD")
    print("PUSHI 1")
    print("SUPEQ")

def p_boolf(p):
    "bool : boolexp"

def p_boolexp(p):
    "boolexp : MATI MAIORIG MATI"

    print('SUPEQ')

def p_boolexp_true(p):
    "boolexp : TRUE"

    print("PUSHI 1")

def p_booexp_false(p):
    "boolexp : FALSE"

    print("PUSHI 0")

def p_boolexp_menorig(p):
    "boolexp : MATI MENORIG MATI"

    print('INFEQ')

def p_boolexp_menor(p):
    "boolexp : MATI MENOR MATI"

    print('INF')

def p_boolexp_maior(p):
    "boolexp : MATI MAIOR MATI"

    print('SUP')

def p_boolexp_igual(p):
    "boolexp : MATI IGUALDADE MATI"

    print('EQUAL')

def p_boolexp_diferente(p):
    "boolexp : MATI DIFERENTE MATI"

    print('EQUAL')
    print('NOT')

# ------------------------------------------ REPEAT UNTIL -----------------------------------------------

def p_bloco_repeatUntil(p):
    "bloco : repeat '{' codigo '}' UNTIL '(' bool ')'"

    print("JZ r" + p[1])

def p_repeat(p):
    "repeat : REPEAT"

    lbl = str(p.parser.numLabel)
    print("r" + lbl + ":")
    p.parser.numLabel += 1
    p[0] = lbl

# ------------------------------------------ WHILE -----------------------------------------------------

def p_bloco_while(p):
    "bloco : while  '{' codigo '}'"

    lbl = p.parser.ifs.pop()
    print("JUMP lbwhile" + str(p[1]))
    print("while" + str(lbl) + ":")

def p_while(p):
    "while :  labelW '(' bool ')'"

    print("JZ while" + str(p.parser.numIfs))
    p.parser.ifs.append(p.parser.numIfs)
    p[0] = p.parser.numIfs
    p.parser.numIfs += 1

def p_labelW(p):
    "labelW : WHILE"

    print("lbwhile" + str(p.parser.numIfs) + ":")

# ------------------------------------------------- ERROS -------------------------------------------------------------

def p_error(p):
    print("Syntax error in input!")
    print(p)

# ---------------------------------------------------------------------------------------------------------------------

# Build the parser and initialize variables
parser = yacc.yacc()
parser.vars = dict()
parser.funcs = dict()
parser.fp = [0]
parser.ifs = []
parser.base = 0
parser.numLabel = 0
parser.numIfs = 0

print('START')

# reading input

f = open(sys.argv[1])
contents = f.read()
parser.parse(contents)

