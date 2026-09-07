def p3(n):
       
        for i in range(1, n + 1): 
            for j in range(1, i + 1):
                print(j, end=" ")
            
            print()

n=int(input("enter the number"))

p3(n)