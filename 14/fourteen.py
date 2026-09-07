def pattern14(N):
    for i in range(N):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")

        print()


N = int(input("please enter the number:"))
pattern14(N)
