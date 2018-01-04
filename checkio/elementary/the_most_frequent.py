'''
https://py.checkio.org/mission/the-most-frequent/
先聚合成dict再for循环是最原始的写法了
看了别人的答案，应该是考察list的count函数和利用list comprehension生成dict
还有使用max直接对dict进行排序，python内置的函数都很强大
'''
def most_frequent(data):
    d = {data.count(e): e for e in data}
    return d[max(d)]

def most_frequent_2(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    amap = {}
    for word in data:
        amap[word] = amap[word] + 1 if word in amap else 1
    maxcount = 0
    result = ''
    for k in amap:
        if amap[k] > maxcount:
            result = k 
            maxcount = amap[k]
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')