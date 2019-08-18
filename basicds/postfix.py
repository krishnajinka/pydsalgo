from Stack import Stack

def postfixeval(postfixexpr):
    operandStack=Stack()
    tokenList = list(postfixexpr)

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(token)
        else:
            op2 = operandStack.pop()
            op1 = operandStack.pop()
            res = doMath(token, op1, op2)
            operandStack.push(res)
    return operandStack.pop()

def doMath(op, op1, op2):
    op1 = int(op1)
    op2 = int(op2)
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1  / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

expr="456*+"
print("Result of expr {} is {}".format(expr, postfixeval(expr)))
