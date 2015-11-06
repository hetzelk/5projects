class Triangle(object):

    def __init__(self, number):
        self.number = number


        number = self.number

        print("First ",number)


    def fib(self, number):
        number = self.number
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return fib(number-1) + fib(number-2)



def main():
    number = int(input("enter a number "))
    print("")

    print(number)
    tri = Triangle(number)

    tri.fib(number)
    print("")

main()