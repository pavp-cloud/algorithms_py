a = ['a','b','c']

#очередь
#fifo - first input first output
#2 операции - добавить в конец, взять с начала

#stack - стопочка чего-то
#добавить на вершину - убрать с вершины - проверить что сверху стека
#last input first output - lifo

#dictionary - сопоставляем ключ со значением
#tree - узлы данных могут иметь дочерние узлы
#graph - узлы данных могут иметь связи с другими узлами
def is_balanced(equation):
    result = True
    stack = [] #pop or append
    for i in equation:
        if i not in '()[]{}':
            continue
        else:
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                if not stack:
                    result = False
                    break
                peek = stack.pop()
                if not ((peek == '(' and i == ')') or (peek == '[' and i == ']') or (peek == '{' and i == '}')):
                    result = False
                    break
    if stack:
        result = False

    return result



def main():
    print("a")
    #1) есть выражение со скобками 3-х видов квадратные круглые и фигурные
    #необходимо проверить выражение на баланс скобок
    #()[]{} - true
    #    - true
    #( - false
    #([)] - false
    assert is_balanced('()[]{}')
    assert is_balanced('')
    assert is_balanced('(1+3)-[{5+3}]=5')
    assert is_balanced('([1+3+5][])')
    assert not is_balanced('(')
    assert not is_balanced('([)]')
    assert not is_balanced('([1+3+5}[])')



if __name__ == "__main__":
    main()