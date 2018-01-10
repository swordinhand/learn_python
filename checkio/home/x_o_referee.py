'''
https://py.checkio.org/mission/x-o-referee/
最简单的思路就是用循环了
看了别人的代码，还有种思路就是直接把需要比较的三项拼成字符串，放入list，然后检查是否包含'XXX'或者‘OOO’
'''
def checkio(game_result):
    winner = None
    for row in game_result:
        if row == 'OOO': return 'O'
        elif row == "XXX": return "X"
    for i in range(0, 3):
        if game_result[0][i] == game_result[1][i] and game_result[0][i] == game_result[2][i]:
            winner = game_result[0][i]
    if game_result[0][0] == game_result[1][1] and game_result[0][0] == game_result[2][2]:
        winner = game_result[0][0]
    elif game_result[0][2] == game_result[1][1] and game_result[0][2] == game_result[2][0]:
        winner = game_result[0][2]
    winner = 'D' if winner is None  or winner == '.' else winner
    return winner

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"