def one():
    a = []
    n = int(input())
    for i in range(n):
        a.append(int(input()))
    print(*a)
    print(sum(a)/n)

# var1
def two():
    g = 0
    A = [-679, -14, -576, -11, 4, 25235, -87, 64, 678, 235, 9, 4545, 6, 3454, -1, 3453, 231, 7967, -6, 0]
    for i in A:
        if i < 0:
            g += 1
    print(g)

def three():
    A = [-679, -14, -576, -11, 4, 25235, -87, 64, 678, 235, 9, 4545, 6, 3454, -1, 3453, 231, 7967, -6, 0]
    a = max(A)
    i = A.index(a)
    A[i], A[0] = A[0], A[i]
    print(A)

one()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
two()
print("////////////////////////////////////////////////////////////////////////////////////////////////////////////")
three()