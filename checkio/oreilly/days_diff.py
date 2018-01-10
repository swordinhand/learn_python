'''
https://py.checkio.org/mission/days-diff/
datetime的简单使用，使用*date1作为参数算是个技巧吧
'''
from datetime import date
def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    d1 = date(*date1)
    d2 = date(*date2)    
    return abs((d2-d1).days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238