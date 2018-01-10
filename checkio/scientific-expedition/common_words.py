'''
https://py.checkio.org/mission/common-words/
最简单的想法是for循环，高级点的数据结构是split之后转成set，然后一个&操作就可以取并集了
还有用filter的，感觉这就是forxunh写法的变种，看了一下文档，filter等价于[item for item in xx if xx]
'''
def checkio_2(first, second):    
    result = set(first.split(',')) & set(second.split(','))
    return ",".join(sorted(result))

def checkio(first, second):
    lst1 = first.split(',')
    lst2 = second.split(',')
    #下面这两种写法等价
    #result = [x for x in lst1 if x in lst2]    
    result = filter(lambda x: x in lst2, lst1)
    return ",".join(sorted(result))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"