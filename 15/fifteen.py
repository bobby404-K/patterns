def pattern15(N):
    for i in range(N):
        for j in range(N - i):
            print(chr(65 + j), end=" ")

        print()


N = int(input("please enter the number:"))
pattern15(N)
