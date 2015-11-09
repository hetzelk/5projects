#Problem #2

#   .
#   ..
#   ...
#   ....
#   UpsideDownTriangle will output
#  ....
#  ...
#  ..
#  .
#   BackwardsTriange will output
#      .
#     ..
#    ...
#   ....



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