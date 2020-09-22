#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = number * (-1)
        return number
    else:
        return number

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    name = []
    for a in prefixes:
        name.append(a+suffixe)
    return name

def is_premier(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


def prime_integer_summation() -> int:
    prime = [2, 3, 5, ]
    number = 6
    while len(prime) < 100:
        if is_premier(number):
            prime.append(number)
        number += 1
    return sum(prime)


def factorial(number: int) -> int:
    for i in range(number - 1, 1, -1):
        number =  number * i
    return number


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print (i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    list = []
    for a in groups:
        if len(a) > 10 or len(a) < 3:
            list.append(False)
            continue
        if 25 in a:
            list.append(True)
            continue
        if (min(a) < 18) or (50 in a and max(a) <70):
            list.append(False)

        list.append(True)

    return list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
