def P22(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top = i
            left = j
            bottom = (2 * n - 2) - i
            right = (2 * n - 2) - j

            min_dist = min(top, bottom, left, right)
            print(n - min_dist, end=" ")

        print()


N = int(input("please enter the number:"))
P22(N)
