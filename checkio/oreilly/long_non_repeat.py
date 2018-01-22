'''
https://py.checkio.org/mission/long-non-repeat/
简单的想法，就是从第一个字符开始，向后检查到有重复字符为止
看了别人的解法，也没什么好的思路，代码想简短，可以把所有的不包含重复字符的字符串都放到一个list里，最后选出最长的那个
'''
def non_repeat(line):    
    if len(line) == 0:
        return line
    lst = []
    for i in range(len(line)):
        for j in range(i, len(line)):
            if line[j] not in line[i:j]:  
                lst.append(line[i:j+1])
            else:
                break
    
    return max(lst, key=len)

def non_repeat_2(line):
    """
        the longest substring without repeating chars
    """
    # your code here
    result = ''    
    for i in range(len(line)):
        for j in range(i, len(line)):
            if line[j] not in line[i:j]:                
                if j == len(line) - 1:
                    if j - i + 1 > len(result):
                        result = line[i:]                    
            else:
                if j - i > len(result):
                    result = line[i:j]                    
                break    
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat('w') == 'w', "Fourth"
    assert non_repeat('abcbde') == 'cbde', "Fifth"
    print('"Run" is good. How is "Check"?')