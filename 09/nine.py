def erect_pyramid(N):
    for i in range(N):
        print(" " * (N - i - 1), end="")
        print("*" * (2 * i + 1), end="")
        print(" " * (N - i - 1))


def inverted_pyramid(N):
    for i in range(N):
        print(" " * i, end="")
        print("*" * (2 * N - (2 * i + 1)), end="")
        print(" " * i)


N=int(input("Enter the number of rows for the pyramid: "))
erect_pyramid(N)
inverted_pyramid(N)