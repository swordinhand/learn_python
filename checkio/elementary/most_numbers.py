'''
https://py.checkio.org/mission/most-numbers
应该使用x is None来判断x是否是None，如果使用if not x这样的写法来判断，会把0也当成None
'''
def checkio(*args):
    min = max = None
    for i in args:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
    #print("max={0}, min={1}".format(max, min))       
    return max - min  if max is not None else 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    assert almost_equal(checkio(-69,0,0,-0.051,-0.021,-0.81), 69, 3), "0-(-69)=69"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")