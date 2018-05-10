import game

class Player(object):
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

        self.failcount = 0

        self.game = game.Game(4)

    def set_game_player_number(self, player_number):
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
            # occupied
            return 1
        if self.board[y][x] < 0:
            # blocked
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

    def get_avalable_locations(self, number, color):
        result = []
        for y in range(3):
            if color[y] == False:
                continue
            row_contain = False
            for x in range(12):
                conflict = self.check_location_conflict(number, x, y)
                if conflict == 0:
                    result.append((x,y))
                if conflict == 2:
                    break
        return result

    def get_score_board(self):
        return self.board

    def accept_roll(self, number, x, y):
        self.board[y][x] = number

    def fail(self):
        self.failcount+=1

    def is_game_finished(self):
        completed_row = 0
        for y in range(3):
            completed_number = 0
            for x in range(12):
                if self.board[y][x] > 0:
                    completed_number+=1
            if completed_number == 9:
                completed_row +=1
        if completed_row == 2 or self.failcount == 4:
            return True
        else:
            return False

    def print_board(self):
        print('board:')
        for y in range(3):
            for x in range(12):
                print(repr(self.board[y][x]).rjust(3), end = '')
            print('')


    def calculate_score(self):
        score = 0
        for y in range(3):
            completed_number = 0
            for x in range(12):
                if self.board[y][x] > 0:
                    completed_number += 1
            if completed_number == 9:
                score += self.board[y][11-y]
                # print("completed row score %d at x %d y %d." % (self.board[y][11-y], 11-y, y))
            else:
                score += completed_number
                # print("row score by count %d at y %d." % (completed_number, y))

        for x, y in ((2,2),(3,0),(7,0),(8,1),(9,2)):
            if self.board[0][x] > 0 and self.board[1][x] > 0 and self.board[2][x] > 0:
                score += self.board[y][x]
                # print("pentagon score %d at x %d y %d." % (self.board[y][x], x, y))

        score -= self.failcount * 5
        # print("deduct score %d." % (-self.failcount * 5))
        return score
