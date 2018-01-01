'''
https://py.checkio.org/mission/second-index/
index在找不到时会抛出ValueError，而find会返回-1
'''
def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    first = text.find(symbol)
    if first >= 0:
        second = text.find(symbol, first + len(symbol))
        return second if second >= 0 else None
    else:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')