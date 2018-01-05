'''
https://py.checkio.org/mission/most-wanted-letter/
原始思路很简单，先转小写，再遍历，最后取最大的key，再排序
网站上有个解法思路很好，先逆向排序，然后挨个count，count相同就用后面的取代前面的，最后取key最大的
和elementary里面的the_most_frequent那道题很像了
'''
def checkio(text):
    text = text.lower()
    adict = {text.count(ch) : ch for ch in sorted(text, reverse=True) if ch.isalpha()}
    return adict[max(adict)]

def checkio_2(text):
    #replace this for solution
    text = text.lower()
    adict = {}
    for ch in text:
        if ch >= 'a' and ch <= 'z':
            count = text.count(ch)           
            if count not in adict:                
                adict[count] = [ch]
            elif ch not in adict[count]:                
                adict[count].append(ch)
    return sorted(adict[max(adict)])[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
