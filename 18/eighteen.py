def pattern18(N):
    for i in range(N):
        for ch in range(ord("A") + N - 1 - i, ord("A") + N):
            print(chr(ch), end=" ")

        print()


N = int(input("please enter the number:"))
pattern18(N)
