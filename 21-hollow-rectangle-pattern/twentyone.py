def P21(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")

        print()


N = int(input("please enter the number:"))
P21(N)
