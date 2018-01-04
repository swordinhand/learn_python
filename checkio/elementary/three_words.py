'''
https://py.checkio.org/mission/three-words/
一开始的想法是用re模块来判断是不是word，但是看标签是text，应该只是普通的文本处理
看了一下hint，才知道str类有isalpha, isdigit这样的函数
不管什么语言，字符串处理都是很重要的，api不能靠死记硬背，只能多写代码学习了
'''
def checkio(words):
    count = 0
    for word in words.split():
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")