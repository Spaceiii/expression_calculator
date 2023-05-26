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


def extract_calcul_from_parentheses(expression: str) -> list:
    parentheses_pos = parentheses_position(expression)
    parentheses_pos.sort(reverse=True, key=lambda k: k[0])
    calculs = []
    while len(parentheses_pos) != 0:
        pos1 = parentheses_pos.pop(0)[1]
        pos2 = parentheses_pos.pop(0)[1]
        calculs.append(expression[pos1+1:pos2])
    return calculs


def calculate_expression(expression):
    calcs = extract_calcul_from_parentheses(expression)
    parentheses_pos = parentheses_position(expression)
    if len(parentheses_pos) == 0:
        return calcul(expression)
    parentheses_pos.sort(reverse=True)
    first_layer_nbr = [i[0] for i in parentheses_pos].count(parentheses_pos[0][0])//2
    i = 0
    for calc in calcs:
        if i == first_layer_nbr:
            break
        expression = expression.replace("(" + calc + ")", str(calcul(calc)))
        i += 1
    return calculate_expression(expression)


def calcul(expression):
    """
    expression: str forme de n1 (operation) n2
    """
    index = 0
    for index_caractere in range(len(expression)-1):
        if expression[index_caractere] in ['+', '-'] :
            index = index_caractere
            break
        if expression[index_caractere] in ["*", "/"]:
            index = index_caractere
    if index == 0:
        return expression
    elif expression[index] == "+":
        return float(calcul(expression[:index])) + float(calcul(expression[index+1:]))
    elif expression[index] == "-":
        return float(calcul(expression[:index])) - float(calcul(expression[index+1:]))
    elif expression[index] == "*":
        return float(calcul(expression[:index])) * float(calcul(expression[index+1:]))
    elif expression[index] == "/":
        if expression[index+1:] == 0:
            raise ZeroDivisionError("Pas de division par 0")
        return float(calcul(expression[:index])) / float(calcul(expression[index+1:]))
    return expression
