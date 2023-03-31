"""
Author/GOAT: Billmack; Spaceiii3; Arma
objectif:                                                           


"""
from calcul import is_valid, calculate_expression


def calcul(expression: str):
    is_valid(expression)
    return calculate_expression(expression)
    

resolve = input("Résoudre: ")
print(calcul(resolve))
