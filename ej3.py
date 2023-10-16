def numero (num1):
    for i in range(1, num1+1, 2):
        print(i,end=",")
num1 = int(input("INTRODUCE UN NUMERO:"))
numero(num1)