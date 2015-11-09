#this is the fibbonaci that you helped me with. I couldn't figure it out, so I used a loop instead because it works the way you want.

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






def fib(number):
    list1 = []
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        next = fib(number-1) + fib(number-2)
        return next



print(fib(number))