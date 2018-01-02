'''
python2是for k, v in data.iteritems()，而python3是for k, v in data.items()
更简单的写法是for k in data
'''
def best_stock(data):
    # your code here
    max = 0
    result = None
    for k in data:
        if data[k] > max:
            result = k
            max = data[k]

    return result

def best_stock_2(data):
    # your code here
    max = 0
    result = None
    for k, v in data.items():
        if v > max:
            result = k
            max = v

    return result


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")