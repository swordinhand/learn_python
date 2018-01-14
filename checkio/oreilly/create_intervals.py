'''
https://py.checkio.org/mission/create-intervals/
最简单的做法就是for循环遍历了
看了别人的solution，有个很奇妙的，记录在下面
&是集合求交集，[[x] * (2 - len({x-1,x+1} & d)) for x in sorted(d)]产生的结果是[[1], [], [], [], [5], [7], [8], [12, 12]]这样的，sum之后变成了[1, 5, 7, 8, 12, 12]
不理解这里sum的用法，试了一下才知道多个list可以直接用+合并， [1,2] + [] + [3, 4] = [1,2,3,4]
'''
f=lambda d: sum([[x] * (2 - len({x-1,x+1} & d)) for x in sorted(d)], [])
create_intervals=lambda d:list(zip(f(d)[::2],f(d)[1::2]))

def create_intervals_2(data):
    """
        Create a list of intervals out of set of ints.
    """
    # your code here
    if len(data) == 0:
        return []
    lst = sorted(list(data))
    result = []
    begin=end=lst[0]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1] + 1:
            end = lst[i]
        else:
            result.append((begin, end))
            begin=end=lst[i]
    result.append((begin, end))
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')