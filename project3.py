#Project #3

import os
os.system("cls")


number = int(input("2. Pick a nth number to multiply by Fibbonacci. "))
a = 0
b = 1
fibo=[a, b]
while b < 10000000000000000000000:
    a, b = b, a+b
    fibo.append(b)
print (fibo)



