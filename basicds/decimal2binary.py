from pythonds.basic import Stack

def divideby2(decNum):
    print("divideby2 %d" % decNum)
    remstack = Stack()

    while decNum > 0:
        rem = decNum % 2
        remstack.push(rem)
        decNum = decNum // 2

    binstring = ""
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())
    return binstring

dec = 100
print("binary string of {} is {}".format(dec, divideby2(dec)))
