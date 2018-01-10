'''
https://py.checkio.org/mission/median/
python3需要用//做整数除，用/结果是浮点数
如果不想用循环，可以把排序后的列表[::-1]，然后取两个列表的data[len//2]再除以2
'''
def checkio(data):
    data = sorted(data)
    datalen = len(data)
    if datalen % 2 == 0:
        return (data[datalen//2-1] + data[datalen//2]) / 2
    else:
        return data[datalen//2]

#checkio=lambda data:(sorted(data)[len(data)//2]+sorted(data)[::-1][len(data)//2])/2    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")