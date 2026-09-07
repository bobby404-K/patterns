def pattern16(N):
    for i in range(N):
        ch = chr(65 + i)
        for _ in range(i + 1):
            print(ch, end=" ")

        print()


N = int(input("please enter the number:"))
pattern16(N)
