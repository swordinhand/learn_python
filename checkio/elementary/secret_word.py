'''
https://py.checkio.org/mission/secret-message/
就是考察upper函数，不过我的for if这种写法太不pythonic了
提交之后看了别人的代码，一句话就可以了，这种代码也经常看到，但是自己写的时候总是想不起来这么写
还是写的太少了
'''
def find_message(text):
    """Find a secret message"""
    return ''.join([c for c in text if c.isalpha() and c.isupper()])

def find_message2(text):
    result = ""
    for c in text:
        if c.isupper():
            result += c
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")