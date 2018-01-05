'''
https://py.checkio.org/mission/digits-multiplication/
简单的做法就是循环了，复杂的就是reduce
'''
from functools import reduce
def checkio(number):
    return reduce(int.__mul__, [int(x) for x in str(number) if x != '0'])
    
def checkio_2(number):
    result = 1
    for x in str(number):
        if x != '0':
            result *= int(x)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")