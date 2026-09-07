def pattern11(N):
    for i in range(N):
        start = 1 if i % 2 == 0 else 0
        row = ""
        for j in range(i + 1):
            row += str(start)
            start = 1 - start
        print(row)


N = int(input("enter your number "))
pattern11(N)
