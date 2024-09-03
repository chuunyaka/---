game = [[None, None, None], [None, None, None], [None, None, None]]
game_is_on = True
while game_is_on:
    move = input()
    exec ("game" + move)
    for row in game:
        print(row)

    reference_matrix = [
        game[0],
        game[1],
        game[2],
        [i[0] for i in game],
        [i[1] for i in game],
        [i[2] for i in game],
        [game[0][0], game[1][1], game[2][2]],
        [game[0][2], game[1][1], game[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] != None:
            print("Игра окончена!")
            game_is_on = False
            break