
thislist = [2, 8, 17, 5, 41, 77, 3, 11]

newlist = []

index = 0

listlength = len(thislist)

while index < listlength:
    value = 0
    while thislist[index] >= 0:
        value += thislist[index]
        value += 2 * value
        index += 1
    value += thislist[index]
    index += 1
    newlist.append(value)

print newlist




def checkmultiples():
    ask = True
    result = 0
    while ask == True:
        usernumber = int(input("1Enter a number"))
        if usernumber == result:
            print("try again with a different number")
        else:
            result = usernumber







for each number in list
