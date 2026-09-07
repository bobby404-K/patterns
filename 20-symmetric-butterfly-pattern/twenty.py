def P20(n):
    spaces = 2 * n - 2

    for i in range(1, 2 * n):
        stars = i if i <= n else 2 * n - i

        print("*" * stars, end="")
        print(" " * spaces, end="")
        print("*" * stars)

        if i < n:
            spaces -= 2
        else:
            spaces += 2


N = int(input("please enter the number:"))
P20(N)
