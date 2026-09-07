def P5(N ):
        
        for i in range(N):
            for j in range(N, i, -1):
                print("*", end=" ")
    
            print()

N=int(input("enter your number"))
P5(N)