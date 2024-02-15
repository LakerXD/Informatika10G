def one():
    a = input()
    b = input()

    c = a+b
    print(c)

    print(len(c))

    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    else:
        print("Строки равны")

    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Строки равны")

def two():
    a = "ИНФОРМАТИКА"
    print(a[2:7])
    print(a[2] + a[0] + a[4:7])
    print(a[5:7] + a[-2])

def three():
    g = 0
    a = "У Аграфены и Арины растут георгины."
    for i in a:
        if i == "а" or i == "A":
            g += 1
    a = a.replace("а", "б")
    a = a.replace("А", "В")
    print(a, g)

def four():
    g = 0
    a = "ay Rag ran across a rough road. Across a rough road Ray Rag ran"
    a = a.split(" ")
    for i in a:
        if i[0] == "R":
            g += 1
    print(g)

def five():
    a = "Мама мыла раму."
    if len(a) % 2 == 0:
        n = len(a)//2
        a1 = a[0:n]
        a2 = a[n:n*2+2]
        print(a1 + a2)
        print(a1 + '\n' + a2)
    else:
        n = len(a)//2 + 1
        a1 = a[0:n]
        a2 = a[n:n*2]
        print(a1 + a2)
        print(a1 + '\n' + a2)

def six():
    a = "eins zwei"
    a = a.split(" ")
    print(a[-1] + ' ' + a[0])

def seven():
    a = "Петров Михаил Николаевич"
    a = a.split(" ")
    print(a[-2][0] + ". " + a[-1][0] + ". " + a[0])

def eight():
    a = []
    g = []
    m = 0
    with open("grade.txt", "r", encoding="utf8") as file:
        line = file.readline()
        while line:
            a.append(line.rstrip())
            line = file.readline()
        file.close()
    for i in a:
        if i[-2] == " ":
            m += int(i[-1])
            if int(i[-1]) < 4:
                g.append(i)
        else:
            m += 10
    print(a)
    print(g)
    print(m/len(a))

one()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
two()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
three()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
four()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
five()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
six()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
seven()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
eight()
