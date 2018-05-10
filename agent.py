import game

class Agent(object):
    def __init__(self):
        self.board = [[0 for x in range(12)] for y in range(3)]
        self.board[0][0] = -5
        self.board[0][1] = -5
        self.board[0][5] = -5
        self.board[1][0] = -5
        self.board[1][6] = -5
        self.board[1][11] = -5
        self.board[2][4] = -5
        self.board[2][10] = -5
        self.board[2][11] = -5

        self.game = game.Game(4)

    def set_game_player(self, player_number):
        self.game = game.Game(player_number)

    # return value:
    # 0 means available
    # 1 means occupied
    # 2 means row conflict
    # 3 means not in order
    # 4 means column conflict
    # 5 means blocked
    def check_location_conflict(self, number, x, y):
        if self.board[y][x] > 0:
            return 1
        if self.board[y][x] < 0:
            return 5
        for cur in range(12):
            if self.board[y][cur] == number:
                return 2
            if cur < x and self.board[y][cur] > number and self.board[y][cur] > 0:
                return 3
            if cur > x and self.board[y][cur] < number and self.board[y][cur] > 0:
                return 3

        if self.board[0][x] == number or self.board[1][x] == number or self.board[2][x] == number:
            return 4
        # ok no conflict
        return 0

    def is_location_ok(self, number, x, y):
        result = self.check_location_conflict(number, x, y)
        # print(result)
        return result == 0

    def get_avalable_location(self, number, color):
        result = []
        for y in range(3):
            if color[y] == False:
                continue
            row_contain = False
            for x in range(12):
                conflict = self.check_location_conflict(number, x, y)
                if conflict == 0:
                    result.append((y,x))
                if conflict == 2:
                    break
        return result
