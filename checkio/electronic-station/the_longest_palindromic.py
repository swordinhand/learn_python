'''
https://py.checkio.org/mission/the-longest-palindromic/
'''
def longest_palindromic(text):
    result = ''
    for i in range(len(text)):
        ch = text[i]
        j = text.find(ch, i+1)
        while j > 0:
            if text[i:j+1] == text[i:j+1][::-1] and j-i+1 > len(result):
                result = text[i:j+1]
            j = text.find(ch, j+1)
        else:
            if result == '':
                result = text[i]
    return result

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abc") == "a", "No Repeat"