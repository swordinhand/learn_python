'''
https://py.checkio.org/mission/popular-words/
字典的简单操作
'''
def popular_words(text, words):
    # your code here
    amap = {}
    lines = text.split('\n')
    for line in lines:        
        singles = line.lower()[0:-1].split() if len(line) > 0 else []
        for single in singles: 
            amap[single] = amap[single] + 1 if single in amap else 1

    result = {}
    for word in words:
        result[word] = amap[word] if word in amap else 0
    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")