'''
https://py.checkio.org/mission/even-last/
这个使用range和len的组合来根据index遍历列表的方法很好用
'''
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    #这个一句话的写法看起来很pythonic，不过感觉不如分开写容易维护
    #return sum([array[i] for i in range(len(array)) if i % 2 == 0]) * array[-1] if len(array) > 0 else 0
    if len(array) == 0:
        return 0
    else:
        return sum([array[i] for i in range(len(array)) if i % 2 == 0]) * array[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")