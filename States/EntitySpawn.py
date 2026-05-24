import random
import Var

def entitySpawn():
    legal_mine_pos_list = Var.apple_array.copy()
    if [Var.apple_x, Var.apple_y] in legal_mine_pos_list:
        legal_mine_pos_list.remove([Var.apple_x, Var.apple_y]) 

    filter_apple = [apple for apple in Var.apple_array if apple not in Var.snake_body]

    if Var.challenge[1] == 1:
        for not_legal_mine_pos in Var.mineList:
            if not_legal_mine_pos in filter_apple:
                filter_apple.remove(not_legal_mine_pos)

    try:
        apple = random.choice(filter_apple)
        Var.apple_x = apple[0]
        Var.apple_y = apple[1]
        Var.applePoison = random.randint(0, Var.challenge[3])
        Var.appleDirection = random.randint(0,3)

    except IndexError:
        apple = [-100, -100]
    
    if [Var.apple_x, Var.apple_y] in legal_mine_pos_list:
        legal_mine_pos_list.remove([Var.apple_x, Var.apple_y])
    
    for snake_part_of_body in Var.snake_body:
        if (snake_part_of_body in legal_mine_pos_list):
            legal_mine_pos_list.remove(snake_part_of_body)

    if [Var.snake_body[-1][0] + 1, Var.snake_body[-1][1]] in legal_mine_pos_list:
        legal_mine_pos_list.remove([Var.snake_body[-1][0] + 1, Var.snake_body[-1][1]])
    if [Var.snake_body[-1][0] - 1, Var.snake_body[-1][1]] in legal_mine_pos_list:
        legal_mine_pos_list.remove([Var.snake_body[-1][0] - 1, Var.snake_body[-1][1]])
    if [Var.snake_body[-1][0], Var.snake_body[-1][1] + 1] in legal_mine_pos_list:
        legal_mine_pos_list.remove([Var.snake_body[-1][0], Var.snake_body[-1][1] + 1])
    if [Var.snake_body[-1][0], Var.snake_body[-1][1] - 1] in legal_mine_pos_list:
        legal_mine_pos_list.remove([Var.snake_body[-1][0], Var.snake_body[-1][1] - 1])
    for already_shown_mine in Var.mineList:
        if already_shown_mine in legal_mine_pos_list:
            legal_mine_pos_list.remove(already_shown_mine)

    try:
        Var.mineList.append(random.choice(legal_mine_pos_list))
    except IndexError:
        pass
