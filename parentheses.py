def valid_parentheses(expression: str) -> bool:
    assert expression
    pile = []
    for char in expression:
        if char == "(":
            pile.append(char)
        elif char == ")":
            if len(pile) == 0:
                return False
            pile.pop()
    return len(pile) == 0


def parentheses_position(expression: str):
    pos = []
    lvl = 0
    for idx in range(len(expression)):
        if expression[idx] == "(":
            lvl += 1
            pos.append((lvl, idx))
        elif expression[idx] == ")":
            pos.append((lvl, idx))
            lvl -= 1
    return pos


def is_valid(expression: str) -> bool:
    if not valid_parentheses(expression):
        return False
    return True


def extract_data_from_parentheses(expression: str) -> list:
    parentheses_pos = parentheses_position(expression)
    parentheses_pos.sort(reverse=True, key=lambda k: k[0])
    calculs = []
    while len(parentheses_pos) != 0:
        pos1 = parentheses_pos.pop(0)[1]
        pos2 = parentheses_pos.pop(0)[1]
        print(pos1, pos2, expression[pos1+1:pos2])
        calculs.append(expression[pos1+1:pos2])

    return [iner_calcul(c) for c in calculs]


def iner_calcul(expression: str) -> float:
    i = 0
    for char in expression:
        if char in ["+", "-", "/", "*"]:
            break
        i += 1
    if i == len(expression):
        return expression
    symbol = expression[i]
    if symbol == "+":
        return int(expression[:i]) + int(expression[i+1:])
    return int(expression[:i]) - int(expression[i+1:])


print(extract_data_from_parentheses("(19)+((18)())"))
