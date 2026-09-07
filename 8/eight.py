def pattern8(N):
    for i in range(N):
        for j in range(i):
            print(" ", end="")

        for j in range(2 * N - (2 * i + 1)):
            print("*", end="")

        for j in range(i):
            print(" ", end="")

        print()


N=int(input("Enter the number of rows for the pyramid: "))
pattern8(N)