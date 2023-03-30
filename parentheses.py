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


def extract_data_from_parentheses(expression: str):
    parentheses_pos = parentheses_position(expression)
    parentheses_pos.sort()
    calculs = []
    while len(parentheses_pos) != 0:
        pos1 = parentheses_pos.pop()[1]
        pos2 = parentheses_pos.pop()[1]
        print(pos1, pos2)
        calculs.append(expression[pos1:pos2])
    return calculs


print(extract_data_from_parentheses("(19)((18)())"))
