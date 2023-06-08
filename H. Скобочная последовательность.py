def is_correct_bracket(text):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    matching_brackets = {'(': ')', '[': ']', '{': '}'}

    for bracket in text:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if bracket != matching_brackets[last_opening_bracket]:
                return False

    return len(stack) == 0


txt = input()
print(is_correct_bracket(txt))
