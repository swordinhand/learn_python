'''
https://py.checkio.org/mission/brackets/
看了别人的答案，也没什么pythonic的写法
'''
def checkio(expression):
    adict = {')':'(', ']': '[', '}': '{'}
    lst = []
    for x in expression:
        if x in '([{':
            lst.append(x)
        elif x in ')]}':
            ch = adict.get(x)
            if len(lst) == 0 or ch != lst[-1]: 
                return False
            else:
                del lst[-1]
    return len(lst) == 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"