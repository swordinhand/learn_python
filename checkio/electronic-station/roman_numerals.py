'''
https://py.checkio.org/mission/roman-numerals/
没什么难度，就是要考虑各种情况
还有人是把每一位是什么数字对应的字符做成list，然后直接根据这一位的值取字符串来拼接
'''
def checkio(data):
    #replace this for solution
    result = ""
    while data >= 1000:
        data -= 1000
        result += 'M'
    while data >= 900:
        data -= 900
        result += 'CM'
    while data >= 500:
        data -= 500
        result += 'D'
    while data >= 400:
        data -= 400
        result += 'CD'
    while data >= 100:
        data -= 100
        result += 'C'
    while data >= 90:
        data -= 90
        result += 'XC'
    while data >= 50:
        data -= 50
        result += 'L'
    while data >= 40:
        data -= 40
        result += 'XL'
    while data >= 10:
        data -= 10
        result += 'X'
    while data >= 9:
        data -= 9
        result += 'IX'
    while data >= 5:
        data -= 5
        result += 'V'
    while data >= 4:
        data -= 4
        result += 'IV'
    while data > 0:
        data -= 1
        result += 'I'
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'