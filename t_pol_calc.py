def evaluate(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    return stack[0]


expression = input()
result = evaluate(expression)
print(result)
