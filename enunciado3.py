import re


def ex1():
    # Dicionário da informação obtida
    data = {}
    with open("exemplo-utf8.bib") as file:
        for line in file:
            # Parse de cada categoria do ficheiro
            m = re.search(r'@([a-zA-Z]+)', line)
            if (m):
                # O lower é para incluir o case sensitive na inserção dos dados
                cat = m.group(1).lower()
                # Aumentar o numero caso a chave exista
                if cat in data:
                    data[cat] += 1
                # Adicionar a entrada ao dicionário
                else:
                    data[cat] = 1
    # Ordenar como foi pedido no enunciado e geração do ficheiro HTML
    generateHTML(data)


def ex2():
    data = {}
    key = ""
    autor = ""
    nextLine = False
    add = False
    with open("exemplo-utf8.bib") as file:
        for line in file:
            # Captura da chave de citação
            if m := re.search(r'@[a-zA-Z]+{([^,]+),', line):
                key = m.group(1)
            # Captura de autores que constam numa só linha
            elif m := re.search(r'(?i:author) *= *["{]+([^"}]+)["}]+', line):
                autor = m.group(1).strip()
                add = True
            # Captura de autores que constam em multiplas linhas, tornando o semáforo True
            elif m := re.search(r'(?i:author) *= *["{]+([^"}]+)', line):
                autor = m.group(1).strip()
                nextLine = True
            # Captura de autores multilinha com a informação no semáforo se se trata de autores, terminando na mesma
            elif (m := re.search(r'^ *([^}"]+)[}"]', line)) and nextLine:
                autor = autor + " " + m.group(1).strip()
                nextLine = False
                add = True
            # Captura de autores multilinha com a informação no semáforo se se trata de autores, não terminando na mesma
            elif (m := re.search(r'^ *([^\n}"]+)\n$', line)) and nextLine:
                autor = autor + " " + m.group(1).strip()
            # Ao detetar a chave e o autor adiciona ao dicionário os dados obtidos
            if add:
                # Retira múltiplos espaços consecutivos nas strings
                autor = re.sub(" +", " ", autor)
                # Tokeniza todos os autores presentes, através da keyword "and"
                tokens = re.split(" and ", autor)
                processTokensEx2(tokens)
                addDictEx2(key, tokens, data)
                # Reseta as variáveis para a próxima categoria
                autor = ""
                add = False
    # Print dos resultados obtidos
    generateHTML2(data)
    # KINDA COMPLETE


def ex3():
    f = open("exemplo-utf8.bib", "r")
    out = open("bib.json", "w")
    f2 = f.read()
    dictionary = dict()
    id = re.split(r'@(.+){(.+),', f2)
    i = 3

    out.write("{\n\t\"registos\":[\n")

    while i <= len(id):
        out.write("\t  {\n\t\t\"Categoria\": \"" + id[i - 2] + "\",\n\t\t\"Identificador\": \"" + id[i - 1] + "\",\n")
        recER = re.compile(r'\n (.+) *= *([{\"\d](.+(\n *[^=>%]*)*)[}\"\d])')
        campos = recER.findall(id[i])
        f = 0

        while f < len(campos):
            c = re.sub(r',$|,}$', "", re.sub(r' +', " ", re.sub(r'[\n"]', "", campos[f][1])))
            out.write("\t\t\"" + campos[f][0].strip() + "\": \"" + c + "\"")
            if f != len(campos) - 1:
                out.write(", \n")
            f += 1

        out.write("\n\t  },\n")

        i += 3


def ex4(inp):
    data = set()
    autor = ""
    add = False
    nextLine = False
    with open("exemplo-utf8.bib") as file:
        for line in file:
            # Captura de autores que constam numa só linha
            if m := re.search(r'(?i:author) *= *["{]+([^"}]+)["}]+', line):
                autor = m.group(1).strip()
                add = True
            # Captura de autores que constam em multiplas linhas, tornando o semáforo True
            elif m := re.search(r'(?i:author) *= *["{]+([^"}]+)', line):
                autor = m.group(1).strip()
                nextLine = True
            # Captura de autores multilinha com a informação no semáforo se se trata de autores, terminando na mesma
            elif (m := re.search(r'^ *([^}"]+)[}"]', line)) and nextLine:
                autor = autor + " " + m.group(1).strip()
                nextLine = False
                add = True
            # Captura de autores multilinha com a informação no semáforo se se trata de autores, não terminando na mesma
            elif (m := re.search(r'^ *([^\n}"]+)\n$', line)) and nextLine:
                autor = autor + " " + m.group(1).strip()
            # Ao detetar a chave e o autor adiciona ao dicionário os dados obtidos
            if add:
                # Retira múltiplos espaços consecutivos nas strings
                autor = re.sub(" +", " ", autor)
                # Tokeniza todos os autores presentes, através da keyword "and"
                tokens = re.split(" and ", autor)
                processTokensEx2(tokens)
                # Se encontra o autor do input na lista de autores, adiciona os restantes à estrutura
                if inp in tokens:
                    tokens.remove(inp)
                    data.update(tokens)
                # Reseta as variáveis para a próxima categoria
                autor = ""
                add = False
    # Gera o ficheiro .dot
    generateDOT(inp, data)


def generateHTML(data):
    with open("output1.html", "w") as f:
        f.write("""<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>PL2021</title>
    </head>
    <body>
        <dl>\n""")
        for item in sorted(data.items()):
            f.write("\t\t\t<dt>" + item[0] + "</dt>\n")
            f.write("\t\t\t\t<dd>" + str(item[1]) + "</dd>\n")
        f.write("""\t\t</dl>
    </body>
</html>""")
        f.flush()

def generateHTML2(data):
    with open("output2.html", "w") as f:
        f.write("""<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>PL2021</title>
    </head>
    <body>
        <ul>\n""")
        for a, b in data.items():
            f.write("\t\t\t<li>" + a + "</li>\n")
            f.write("\t\t\t\t<ul>\n")
            for el in b:
                f.write("\t\t\t\t\t<li>"+el+"</li>\n")
            f.write("\t\t\t\t</ul>\n")
        f.write("""\t\t</ul>
    </body>
</html>""")
        f.flush()


# Adição de valores no dicionário, adicionar o valor categoria em cada entrada
# do dicionário incluido no array tokens, ou seja, array de autores.
def addDictEx2(key, tokens, data):
    for token in tokens:
        if token in data:
            data[token].append(key)
        else:
            data[token] = [key]


# Correção de casos (Apelido, Nome) para (Nome Apelido)
def processTokensEx2(tokens):
    for s, token in enumerate(tokens):
        tokens[s] = re.sub("([^,]+), (.+)", r'\2 \1', token)


def generateDOT(inp, data):
    with open("output4.dot", "w") as f:
        f.write("graph {\n")
        for aut in data:
            f.write("\t \"" + inp + "\" -- \"" + aut + '\"\n')
        f.write("}")
        f.flush()

opcao = -1
while opcao != 5:
    opcao = int(input("""
Escolha opção:
1 - Cálculo de número de entradas por categoria.
2 - Criação de índice de autor para as respetivas chaves de citaçãos.
3 - Conversão para JSON.
4 - Dado um autor, geração do respetivo DOT de autores com quem trabalhou.
5 - Sair.
Opção: """))

    if opcao == 1:
        ex1()
    elif opcao == 2:
        ex2()
    elif opcao == 3:
        ex3()
    elif opcao == 4:
        autor = input("\nInserir nome do autor: ")
        ex4(autor)
    elif opcao == 5:
        pass
    else:
        print("\nComando Inválido!\n")
