from board import Board
from copy import deepcopy


class Game:
    """ Representation of tic-tac-toe game between human and computer."""

    def __init__(self):
        self.board = Board()


    def computer_make_move(self):
        if not self.board.has_winner():
            board1 = deepcopy(self.board)
            board1.make_random_move()
            board2 = deepcopy(self.board)
            board2.make_random_move()
            score1 = board1.count_score()
            score2 = board2.count_score()
        if score1 > score2:
            self.board = board1
        else:
            self.board = board2


    def human_make_move(self, position):
        if not self.board.has_winner():
            position = eval(position)
            self.board.make_move(position)


    def check_move(self, m):
        try:
            m = eval(m)
            if type(m) != tuple:
                raise TypeError
            elif type(m[0]) != int or type(m[1]) != int:
                raise TypeError
            elif len(m) != 2:
                raise Exception
            elif self.board.cells[m[0]][m[1]] != Board.EMPTY:
                raise Exception
            else:
                if not (0 <= m[0] <= 2) and (0 <= m[1] <= 2):
                    raise Exception
        except (AssertionError, TypeError, NameError, SyntaxError, Exception):
            return False
        else:
            return True


    def start(self):
        while not self.board.has_winner():
            move = input('Enter move (f.e. 1,1): ')
            if self.check_move(move):
                self.human_make_move(move)
                self.computer_make_move()
                print(self.board)
            else:
                print('Invalid move! Enter one more time!')


if __name__ == '__main__':
    game = Game()
    game.start()
