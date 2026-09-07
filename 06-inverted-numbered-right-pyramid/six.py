def pattern6(N):
    for i in range(N):
        for j in range(N, i, -1):
            print(N - j + 1, end=" ")
        print()


N = int(input("enter your number "))
pattern6(N)
