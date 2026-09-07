def pattern12(N):
    spaces = 2 * (N - 1)

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(j, end="")

        for _ in range(spaces):
            print(" ", end="")

        for j in range(i, 0, -1):
            print(j, end="")

        print()
        spaces -= 2


N = int(input("please enter the number:"))
pattern12(N)
