def pattern7(N):
    for i in range(N):
        for j in range(N - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        for j in range(N - i - 1):
            print(" ", end="")
        print()


N = int(input("enter your number "))
pattern7(N)
