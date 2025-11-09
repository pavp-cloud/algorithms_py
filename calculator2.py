def myNumeric(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def postfix(equation):
    operation = equation.split(' ')
    stack = []
    for i in operation:
        if myNumeric(i):
            digit = int(i)
            stack.append(digit)
        if i in '-+*:':
            operand1 = stack.pop()
            operand2 = stack.pop()
            match i:
                case '+':
                    stack.append(operand2 + operand1)
                case '-':
                    stack.append(operand2 - operand1)
                case '*':
                    stack.append(operand2 * operand1)
                case ':':
                    stack.append(operand2 // operand1)
    return stack.pop()

def isHigherEqual(operator1, operator2):
    result = True
    if operator1 in '(':
        result = False
    elif operator1 in '+-' and operator2 in '*/':
        result = False
    return result
# +  -  = True
# +  +  = True
# -  -  = True
# -  +  = True
# *  *  = True
# +  *  = False
# *  +  = True

def infToPost(equation):
    result = []
    stack = []
    splitEquation = equation.split(' ')
    for i in splitEquation:
        if myNumeric(i):
            result.append(i)
        elif i in '+-*/':
            while stack and isHigherEqual(stack[-1], i):
                result.append(stack.pop())
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

    while stack:
        result.append(stack.pop())
    print(result)
    postEquation = ' '.join(result)
    print(postEquation)
    return postEquation

def calc(equation):
    postEquation = infToPost(equation)
    return postfix(postEquation)



def main():
    #assert 5 == postfix('2 3 +')
    assert myNumeric('-3')
    assert myNumeric('2')
    assert isHigherEqual('*', '+')
    assert isHigherEqual('+', '+')
    assert not isHigherEqual('-', '*')
    #assert "2 3 +" == infToPost("2 + 3")
    #assert 5 == calc("5")
    #assert 5 == calc("2 + 3")
    #assert 0 == calc("3 - 2 - 1")
    #assert 6 == calc("3 * 2")
    #assert 7 == calc("1 + 3 * 2")
    assert -52 == calc("( -2 * ( 10 + 3 ) ) * 2")

    pass


if __name__ == "__main__":
    main()