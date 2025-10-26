
def calculator(operation):
    stack = []
    separator = True
    for i in operation:
        if i in ' ':
            separator = True
            continue
        if i in '1234567890':
            digit = int(i)
            if separator:
                stack.append(digit)
                separator = False
            else:
                stack.append(stack.pop()*10+digit)
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





def main():
    assert 3 == calculator('1 2 +')
    assert 1 == calculator('1')
    assert 5 == calculator('7 1 1 + -') #1 + 1 = 2, 7 - 2 = 5
    assert 5 == calculator('7 3 1 - -') #3 - 1 = 2, 7 - 2 = 5
    assert 5 == calculator('7 3 - 1 +') #7 - 3 = 4, 4 + 1 = 5
    assert 12 == calculator('12 0 -')
    assert 123 == calculator('100 20 3 + +')
    assert 123 != calculator('100 20 2 + +')
    assert 6 == calculator('3 2 *')
    assert 6 == calculator('12 2 :')

    #как бонус многозначные числа и умножение/деление
    #постфиксная запись
    #решать через стек

if __name__ == '__main__':
    main()
