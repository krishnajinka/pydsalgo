from deque import Deque

def palchecker(astr):
    chardeque = Deque()
    print("%s verify" % astr)
    for ch in astr: 
        chardeque.addRear(ch)
    print(chardeque.items)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

ele = 'radar'
print("String dd %s is palidrome: %s" % (ele, palchecker(ele)))


