from pythonds.basic import Stack

def baseConvertor(decNum, base):

    digits="0123456789ABCDEF"
    remstack = Stack()
    while decNum > 0:
        rem = decNum % base
        remstack.push(rem)
        decNum = decNum // base

    newstring=""
    while not remstack.isEmpty():
        newstring = newstring + digits[remstack.pop()]
    return newstring

num=9876543
base=16
print("{} in base {} is {}".format(num, base, baseConvertor(num, base)))
