'''
https://py.checkio.org/mission/min-max/
重新实现了built-in的min和max函数，关键点有以下几条
1，在没有key的时候，给key一个默认值lambda x:x，这样可以不用检查key是否为None
2，对于*args，要检查args长度，如果长度为1，那传入的可能是str, list, tuple等，要处理一下
3，本来result直接取args[0]的，但是generator没有下标，会报错
'''
def min(*args, **kwargs):
    key = kwargs.get("key", lambda x : x)
    args = args[0] if len(args) == 1 else args
    result = None
    for x in args:
        result = x if result is None or key(x) < key(result) else result
    
    return result


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x : x)
    args = args[0] if len(args) == 1 else args
    result = None
    for x in args:
        result = x if result is None or key(x) > key(result) else result
    
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert min(abs(i) for i in range(-10, 10)) == 0, "generator object"
    assert max(abs(i) for i in range(-10, 10)) == 10, "generator object"
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max(1, 2, 0, 3, 4) == 4, "Simple case max 2"
    assert min([1, 2, 0, 3, 4]) == 0, "From a list 1"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list 2"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0], [5,0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")