'''
https://py.checkio.org/mission/house-password/
这题也不难，本来想用for循环的，后来想起有个any函数
如果追求执行效率应该用for循环，毕竟只要循环一次，不过python显然追求代码简单写得快
'''

def checkio(data):
    #replace this for solution
    hasLength = len(data) >= 10
    hasDigit = any([ch.isdigit() for ch in data])
    hasLower = any([ch.isalpha() and ch.islower() for ch in data])
    hasUpper = any([ch.isalpha() and ch.isupper() for ch in data])

    return hasLength and hasDigit and hasLower and hasUpper

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")