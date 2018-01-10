'''
https://py.checkio.org/mission/pawn-brotherhood/
这题可能只支持py2，因为提交时报错set没有count方法，查了一下，py2的set没有这个方法，py3的set有
看了别人的解法，基本都不考虑边界情况，直接拼dest1和dest2，还有就是把索引2也当chr对待
还有一种思路就是检查每个兵可以支援哪两个位置，最后统计这些位置有多少在pawns里面
'''
'''
检查每个兵可以支援哪两个位置，最后统计这些位置有多少在pawns里面
'''
def safe_pawns(pawns):
    s = set()
    for x in pawns:
        s.add(chr(ord(x[0])-1) + chr(ord(x[1])+1))
        s.add(chr(ord(x[0])+1) + chr(ord(x[1])+1))
    return len([x for x in s if x in pawns])
'''
下面这两种解法是检查每个兵的支撑位是否在pawns里面
'''
def safe_pawns_2(pawns):
    count = 0
    for x in pawns:
        dest1 = chr(ord(x[0])-1) + chr(ord(x[1])-1)
        dest2 = chr(ord(x[0])+1) + chr(ord(x[1])-1)
        if dest1 in pawns or dest2 in pawns: count += 1
    return count

def safe_pawns_3(pawns):
    count = 0
    for x in pawns:
        if (int(x[1]) == 1):
            continue
        elif (x[0] == 'a'):
            dest = 'b' + str(int(x[1])-1)
            if dest in pawns: count += 1
        elif (x[0] == 'h'):
            dest = 'g' + str(int(x[1])-1)
            if dest in pawns: count += 1
        else:
            dest1 = chr(ord(x[0])-1) + str(int(x[1])-1)
            dest2 = chr(ord(x[0])+1) + str(int(x[1])-1)
            if dest1 in pawns or dest2 in pawns: count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")