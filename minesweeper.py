import pprint
import random

class Board(object):

    def __repr__(self):
        return pprint.pformat(self.storage)

    def __init__(self, width=10, height=10, num_mines=5):
        self.width, self.height = width, height
        self.storage = [[0 for _ in xrange(width)] for _ in xrange(height)]
        self.is_playing = True
        self.is_solved = False
        self.num_mines = num_mines
        self.create_random_mines()

    def create_random_mines(self):
        for x in xrange(self.num_mines+1):
            row = random.randrange(0, self.height)
            col = random.randrange(0, self.width)
            self.storage[row][col] = 1

    def process_move(self, row, col, type_):

        if type_ == 'F':
            self.process_flag(row, col)
        elif type == 'M':
            self.process_mine(row, col)
        else:
            raise ValueError

    def process_flag(self, row, col):

        self.is_solved = True




def get_move():
    print "place move in format row,col,type: "
    move = raw_input()
    return move.split(',')


def main():
    board = Board()
    print board

    while board.is_playing and not board.is_solved:
        row, col, type_ = get_move()
        board.process_move(row, col, type_)

    if board.is_solved:
        print "well done!"
    else:
        print "failure!"




if __name__ == '__main__':
    main()