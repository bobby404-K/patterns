def pattern10(N):
    for i in range(1, 2 * N):
        stars = i
        if i > N:
            stars = 2 * N - i
        print("*" * stars)

if __name__ == "__main__":
    N = int(input("enter your number "))
    pattern10(N)
