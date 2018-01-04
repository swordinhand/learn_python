'''
https://py.checkio.org/mission/number-radix/
还以为是要自己实现int函数，不过看了别人的答案，就是直接调用int
当然也有有创造力的使用lambda的解法
'''
def checkio(str_number, radix):
    length = len(str_number)
    result = 0
    for i in range(length):
        ch = str_number[length - i - 1]        
        n = int(ch, 36)       
        if n >= radix:
            return -1
        else:
            result += n * (radix ** i)
    return result        

def checkio_2(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1
#使用lambda实现checkio函数
checkio_3 = lambda s,r: int(s,r) if int(max(s),36) < r else -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")