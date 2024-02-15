import random

#task 1
def one():
    x = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
         'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    a, b = int(input()), int(input())
    t = x[a:b]
    m = 0
    for i in range(a, b):
        del x[i-m]
        m += 1

    x1 = t + x
    x2 = x + t
    print(x1)
    print(x2)
    x1.reverse()
    print(x1)
    x2.reverse()
    print(x2)

#task 2
def two():
    a = 0
    b = 0
    c = 0
    v = []
    n = []
    N = int(input())
    X = int(input())

    for i in range(N):
        v.append(random.randint(-9,9))

    for i in v:
        if i == X:
            a += 1

    for i in v:
        if i == X:
            n.append(b)
        b += 1
    if len(n) > 0:
        b = n[0]
        c = n[-1]
    else:
        b = "Нет"
        c = "Нет"
    d = N - a

    print(a, b, c, d)

#task 3
def three():
    x = []
    for i in range(10):
        x.append(random.randint(10, 99))
    S = sum(x) / 10

    a = 0
    b = 0
    c = 0
    d = 0
    v = []

    for i in x:
        if i < S:
            a += 1

    for i in x:
        if i > S:
            d += 1

    for i in x:
        if i > S:
            v.append(i - S)
        elif i < S:
            v.append(S-i)
        else:
            v.append(0)

    b = v.index(min(v))
    c = v.index(max(v))

    print(a, b, c, d, S)

#task 4
def four():
    A = [1, 2, 67, -43, 54, 54, -23, 34, 12, 23, -6, 8, 5]
    B = [A[0]]
    for i in range(len(A) - 1):
        if abs(A[i]) > abs(A[i + 1]):
            B.append(A[i + 1])
    print(" ".join(map(str, A)) + "\n" + " ".join(map(str, B)))

one()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
two()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
three()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
four()