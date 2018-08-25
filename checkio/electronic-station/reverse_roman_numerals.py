'''
https://py.checkio.org/mission/reverse-roman-numerals/
简单写法就是挨个判断，复杂的就有点绕了
'''
reverse_roman = lambda n: __import__('functools').reduce(
    lambda a, r: (a[0] + a[1].count(r[0])*r[1], a[1].replace(r[0], '')),
    zip('CM CD XC XL IX IV M D C L X V I'.split(),(900,400,90,40,9,4,1000,500,100,50,10,5,1)), (0,n))[0]

def reverse_roman_2(roman_string):
    #replace this for solution
    result = 0
    for i in range(len(roman_string)):
        ch = roman_string[i]
        if ch == 'M':
            result += 1000
        elif ch == 'D':
            result += 500
        elif ch == 'C':
            result += 100 if i == len(roman_string) - 1 or (roman_string[i+1] != 'D' and roman_string[i+1] != 'M') else -100
        elif ch == 'L':
            result += 50
        elif ch == 'X':
            result += 10 if i == len(roman_string) - 1 or (roman_string[i+1] != 'C' and roman_string[i+1] != 'L') else -10
        elif ch == 'V':
            result += 5
        else:
            result += 1 if i == len(roman_string) - 1 or (roman_string[i+1] != 'V' and roman_string[i+1] != 'X') else -1
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');