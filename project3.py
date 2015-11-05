

#Problem #3
#    The fibbonacci sequence goes as follows: 1,1,2,3,5,8,13,21 etc
#    Write a class fibbonacci that contains a function to calculate the nth fibbonacci number. The constructor will take in a shift, so if the shift is 5, then the fibbonacci goes as follows: 5,5,10,15,25 etc...
#    The catch? You may not use any iteration in the entire program nor may you call on any frameworks within python that use iteration. This must be solved using recurson.

#    Extra points if the recursive function only takes in one parameter.
import os
os.system("cls")

class Fido(object):

    def __init__(self, number):
        self.number = number

        number = self.number

    def fib(self, number):
        number = self.number
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return self.fib(number-1) + self.fib(number-2)




def main():
    number = int(input("1. Pick a nth number to multiply by Fibbonacci. "))
    print(number)
    print("")
    fido = Fido(number)
    fido.fib(number)






number = int(input("2. Pick a nth number to multiply by Fibbonacci. "))

def fib(number):
    list1 = []
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        next = fib(number-1) + fib(number-2)
        return next


#print(fib(number))


a = 0
b = 1
fibo=[a, b]
while b < 1000:
    a, b = b, a+b
    fibo.append(b)
print (fibo)



