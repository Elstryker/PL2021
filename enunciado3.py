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


def ex2():
    data = {}
    num = 0
    isAutor = True
    with open("exemplo-utf8.bib") as file:
        for line in file:
            if isAutor:
                m = re.search(r'author *= *["{]+([^"}]+)["}]+', line)
            if m:
                print(m.group(1))
                num+=1
    print(num)
    #NOT COMPLETE



ex2()
