'''
https://py.checkio.org/mission/restricted-sum/
一开始没有思路，google了一下才想到要用递归
'''
def s(data, index, total):
    if (index == len(data)):
        return total
    else:
        return s(data, index+1, total+data[index])

def checkio(data):
    return s(data, 0, 0)