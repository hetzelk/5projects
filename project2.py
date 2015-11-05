
#Problem #2
#    In this problem, you MUST use a 2 dimensional list, and you MUST use nested loops
#    Write a class has a constructor which takes in a number and creates a 2 dimensional list with length and height #  matching that number.

#    Write three functions, Triangle, BackwardsTriangle, and UpsideDown Triangle
#   given the number 4, Triangle will output
#   .
#   ..
#   ...
#   ....

#   BackwardsTriange will output
#      .
#     ..
#    ...
#   ....

#   UpsideDownTriangle will output
#  ....
#  ...
#  ..
#  .

class Triangle(object):

    def __init__(self, number):
        self.number = number


        number = self.number
        for each in range(1, (number+1)):
            print (str(".") * each)



    def upsidedown(self):

        number = self.number
        for each in reversed(range(1, (number+1))):
            print (str(".") * each)



    def reverse(self):

        number = self.number
        for each in reversed(range(1, (number+1))):
            space = number * each
            print (str(" ") * each + str("."))


def main():
    number = int(input("enter a number "))
    print("")

    print(number)
    tri = Triangle(number)
    print("")

    print(number)
    tri.upsidedown()
    print("")

    print(number)
    tri.reverse()
    print("")

main()