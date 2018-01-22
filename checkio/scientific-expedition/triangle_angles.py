'''
https://py.checkio.org/mission/triangle-angles/
这题没什么难度，就是余弦定理和python一些math函数
cosA=(b^2＋c^2－a^2)/2bc； cosB=(a^2＋c^2－b^2)/2ac； cosC=(a^2＋b^2－c^2)/2ab
math.acos, math.degrees, round
'''
def checkio(a, b, c):
    import math
    #replace this for solution
    if a + b <= c or a + c <= b or b + c= < a:
        return [0, 0, 0]
    cosa = (b*b + c*c - a*a)/(2*b*c)
    cosb = (a*a + c*c - b*b)/(2*a*c)
    cosc = (a*a + b*b - c*c)/(2*a*b)
    anglea = round(math.degrees(math.acos(cosa)))
    angleb = round(math.degrees(math.acos(cosb)))
    anglec = round(math.degrees(math.acos(cosc)))
    return sorted([anglea, angleb, anglec])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"