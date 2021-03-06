'''
https://py.checkio.org/mission/monkey-typing/
简单的count和对结果集的二次处理，可以先拆成几行来写然后再合并成一行
'''
def count_words(text, words):    
    text = text.lower()   
    return sum([1 for d in [text.count(word) for word in words] if d > 0])   


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")