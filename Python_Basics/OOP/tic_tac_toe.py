game = [[0,0,0],
        [0,0,0],
        [0,0,0],]
def game_board(game_map, player = 0, row = 0, column = 0):
    try:
        if player != 0:
            game_map[row][column] = player
        print('   1  2  3')
        for count,row in enumerate(game_map):
            print(count, row)

        return game_map
    except IndexError as e:
        print('Make sure you entered row or column betn 0 and 2',e)

game = game_board(game, 1, 2, 1)


