'''
https://py.checkio.org/mission/long-repeat/
最容易理解的方法就是遍历了
有个solution是对每个字符，检查line是否包含它重复1-70次，严重怀疑这个70是他根据testcase试出来的，因为题目并没有说字符最多连续重复70次
'''
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if len(line) == 0:
        return 0
    ch = line[0]
    count = 0
    maxcount = 0
    for x in line:
        if x == ch:
            count += 1
        else:
            maxcount = count if maxcount < count else maxcount
            ch = x
            count = 1    
    return maxcount if maxcount > count else count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')