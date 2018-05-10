import player
import copy

def calculate_possibility(p, depth):
    if depth == 3:
        return 0
    if p.is_game_finished():
        #p.print_board()
        return 0

    possibility = 0
    for i in range(18):
        for x,y in p.get_avalable_locations(i, (True, True, True)):
            possibility += 1
            p_copy = copy.deepcopy(p)
            p_copy.accept_roll(i, x, y)
            possibility += calculate_possibility(p_copy, depth+1)
    return possibility


if __name__ == '__main__':
    p = player.Player()
    print(calculate_possibility(p, 0))
