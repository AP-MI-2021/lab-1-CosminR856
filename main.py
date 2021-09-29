'''
Returneaza true daca n este prim si false daca nu.
'''

import math


def is_prime(n):
    for divisor in range(2, int(math.sqrt(n))):
        if n % divisor == 0:
            return False
    return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    product = 1
    for number in lst:
        product *= number
    return product

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    while x % y:
        x, y = y, x % y
    return y

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    if x == 0:
        return y
    if y == 0:
        return x

    if x == y:
        return x

    if x > y:
        return get_cmmdc_v2(x - y, y)
    return get_cmmdc_v2(x, y - x)


def main():
    print(is_prime(7))
    print(get_product([1, 2, 3, 4, 5]))
    print(get_cmmdc_v1(25, 10))
    print(get_cmmdc_v2(10, 25))


if __name__ == '__main__':
    main()
