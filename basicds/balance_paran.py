from Stack import Stack 

def parcheck(symbolstr):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolstr) and balanced:
        symbol = symbolstr[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False 
        index +=1
    
    if balanced and s.isEmpty():
        return True 
    else:
        return False 

def matches(open, close):
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)

s1 = "{}"
print("{} balanced = {} ".format(s1, parcheck(s1)))
s1 = "(({([])}"
print("{} balanced = {} ".format(s1, parcheck(s1)))
