import re


def ex1():
    data = {}
    with open("exemplo-utf8.bib") as file:
        for line in file:
            m = re.search(r'@([a-zA-Z]+)', line)
            if (m):
                cat = m.group(1).lower()  # Perguntar Stor
                if cat in data:
                    data[cat] += 1
                else:
                    data[cat] = 1
    for item in sorted(data.items()):
        print("Categoria: " + item[0] + ", Número: " + str(item[1]))

    print("""
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Meu exercicio</title>
    </head>
    <body>
        <dl>""")
    for item in sorted(data.items()):
        print("\t\t\t<dt>" + item[0] + "</dt>")
        print("\t\t\t\t<dd>" + str(item[1]) + "</dd>")
    print("""        </dl>
    </body>
</html>""")


def addDictEx2(key, tokens, data):
    for token in tokens:
        if token in data:
            data[token].append(key)
        else:
            data[token] = [key]

def processTokensEx2(tokens):
    for s,token in enumerate(tokens):
        tokens[s] = re.sub("([^,]+), (.+)", r'\2 \1',token)

def ex2():
    data = {}
    key = ""
    autor = ""
    nextLine = False
    add = False
    number = 0
    with open("exemplo-utf8.bib") as file:
        for line in file:
            if m := re.search(r'@[a-zA-Z]+{([^,]+),', line):
                key = m.group(1)
            elif m := re.search(r'(?i:author) *= *["{]+([^"}]+)["}]+', line):
                autor = m.group(1).strip()
                add = True
            elif m := re.search(r'(?i:author) *= *["{]+([^"}]+)', line):
                autor = m.group(1).strip()
                nextLine = True
            elif (m := re.search(r'^ *([^}"]+)[}"]', line)) and nextLine:
                autor = autor + " " + m.group(1).strip()
                nextLine = False
                add = True
            elif (m := re.search(r'^ *([^\n}"]+)\n$', line)) and nextLine:
                autor = autor + " " + m.group(1).strip()
            if add:
                autor = re.sub(" +", " ", autor)
                tokens = re.split(" and ", autor)
                processTokensEx2(tokens)
                addDictEx2(key, tokens, data)
                autor = ""
                add = False

    for a,b in data.items():
        print("Autor: ",a,", Assets: ",b)
    print(number)
    # NOT COMPLETE



def ex3():
    f = open("exemplo-utf8.bib", "r")
    out = open("bib.json", "w")
    f2 = f.read()
    dictionary = dict()
    id = re.split(r'@(.+){(.+),', f2)
    i = 3

    out.write("{\n\t\"registos\":[\n")

    while i <= len(id):
        out.write("\t  {\n\t\t\"Categoria\": \"" + id[i-2] + "\",\n\t\t\"Identificador\": \"" + id[i-1] + "\",\n")
        recER = re.compile(r'\n (.+) *= *([{\"\d](.+(\n *[^=>%]*)*)[}\"\d])')
        campos = recER.findall(id[i])
        f = 0

        while f < len(campos):
            c = re.sub(r',$|,}$', "", re.sub(r' +', " ", re.sub(r'[\n"]', "", campos[f][1])))
            out.write("\t\t\"" + campos[f][0].strip() + "\": \"" + c + "\"")
            if f != len(campos)-1:
                out.write(", \n")
            f += 1

        out.write("\n\t  },\n")

        i += 3


ex3()