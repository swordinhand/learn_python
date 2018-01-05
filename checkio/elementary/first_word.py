'''
https://py.checkio.org/mission/first-word/
这题理论上不用正则很难处理，不过题目限制了text只能是那些字符，所以可以把不能组成单词的字符通通替换成空格，然后strip掉，这就简单了
'''
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    return text.replace(".", ' ').replace(",", ' ').strip().split(' ')[0]

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")