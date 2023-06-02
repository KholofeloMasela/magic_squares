def magic_square(n):
    square = [[0] * n for _ in range(n)]

    i = 0
    j = n // 2

    num = 1
    while num <= (n * n):
        square[i][j] = num
        num += 1

        i -= 1
        j += 1

        if i < 0 and j >= n:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j >= n:
            j = 0
        elif square[i][j] != 0:
            i += 2
            j -= 1

    for i in range(0,n):
        for j in range(0, n):
            print(square[i][j], end="\t")
        print()


n = int(input("enter a number: "))
while (n % 2) == 0:
    n = int(input("enter a number: "))
else:
    magic_square(n)