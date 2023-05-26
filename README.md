# Projet 1 : calculateur d'expressions simples

- [x] lien projet : [Github](https://github.com/Spaceiii/expression_calculator/)

## Vérification

Le progamme vérifie avant de calculer l'expression, que celle-ci respecte bien le systeme de parenthésage :

- pas de parentheses non-fermantes
- pas de parentheses non-ouvrantes
- pas de parentheses vides

## Fonctionnement

Le programme regarde d'abord pour les parentheses, s'il y en a, il les hiérarchise.

Suivant cette hiérachie, le programme va calculer les parentheses de plus haut rang puis les remplacer par leur contenu.

Ainsi, $`(1+2)*3`$ va devenir $`3*3`$ à l'itération suivante.

Le calcul du contenu de la parenthese se fait à travers la fonction calcul.

Cette dernière prend une chaine de caractère contenant une expression non-parenthesée et en revoie le résultat. Elle peut prendre en compte plusieurs calculs comme $`1+2*3`$ en s'appelant récursivement.

## Limites 

Le programme ne vérifie pas totalement le contenu passé par l'utilisateur. Si ce dernier tape "bonjour", le programme ne sachant traiter cette expression va retourner une erreur.

De même, le programme est limité au expression suivante : (, ), *, /, +, -. Le programme ne prend pas en compte les expressions implicite comme $`2(3+1)`$