# coding: utf-8

import math, random

perfect_board = '''
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179'''.replace('\n', '')

perfect_board_2 = '''
123456789
456789123
789123456
234567891
567891234
891234567
345678912
678912345
912345678'''.replace('\n', '')

def sudoku_solution(blocks_per_row=3):
    N = blocks_per_row
    NN = N * N  # row_len
    return '\n'.join(''.join(str((i * N + i / N + j) % NN + 1)
            for j in xrange(NN)) for i in xrange(NN))

class Sudoku(object):
    def __init__(self, board=None):
        self.board = board or self._random_board_with_valid_rows()
        self._row_len = rl = int(math.sqrt(len(self.board)))  # 9 for normal Sudoku
        assert rl * rl == len(self.board), 'Invalid board length'
        self._blocks_per_row = br = int(math.sqrt(self._row_len))  # 3 for normal Sudoku
        assert br * br == self._row_len, 'Invalid board length'
        self._valid_str = ''.join(str(i) for i in xrange(1, rl+1))
        #print('vs', self._valid_str)

    @classmethod
    def _random_board(cls):
        board = [x for x in ''.join(str(i) * 9 for i in xrange(1, 10))]
        random.shuffle(board)
        return ''.join(board)

    @classmethod
    def _random_board_with_valid_rows(cls):
        def _random_valid_row():
            row = [str(i) for i in xrange(1, 10)]
            random.shuffle(row)
            return ''.join(row)
        return ''.join(_random_valid_row() for i in xrange(9))

    def _valid_group(self, line):
        return ''.join(sorted(line)) == self._valid_str

    def _valid_rows(self):
        return all(self._valid_group(row) for row in self._matrix)  #.splitlines())

    def _valid_cols(self):
        rotated = zip(*self._matrix)
        return all(self._valid_group(row) for row in rotated)

    def _valid_squares(self):
        the_matrix = list(self._matrix)
        rl, br = self._row_len, self._blocks_per_row  # 9, 3 for normal Sudoku
        for i in xrange(0, rl, br):
            for j in xrange(0, rl, br):
                if not self._valid_group(''.join(the_matrix[i+k][j:j+br] for k in xrange(br))):
                    return False
        return True

    def winning_board(self):
        return self._valid_rows() and self._valid_cols() and self._valid_squares()

    @property
    def _matrix(self):
        rl = self._row_len
        return (self.board[i*rl:(i+1)*rl] for i in xrange(rl))

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, self.board)

    def _border_line(self):
        br = self._blocks_per_row
        return ('=' * (br * 2 + 1)).join('+' * (br + 1))

    def _get_fmt(self, i):
        return '{}' if i % self._blocks_per_row else '+ {}'

    def _sudoku_line(self, i, line):
        s = '' if i % self._blocks_per_row else self._border_line() + '\n'
        return s + ' '.join(self._get_fmt(i).format(x if x != '0' else '_')
            for i, x in enumerate(line)) + ' +'

    def __str__(self):
        return '\n'.join(('\n'.join(self._sudoku_line(i, line) for i, line
            in enumerate(self._matrix)), self._border_line()))
            #in enumerate(self._matrix.splitlines())), self._border_line()))

#print(Sudoku.random_board())
#print(Sudoku.random_board())
#print(Sudoku.random_board())
print('=' * 91)
fmt = '{}\n{}\n{}\nWinning Board: {}'
#            1234123412341234
s = Sudoku(perfect_board)
print(fmt.format(repr(s), s, '\n'.join(s._matrix), s.winning_board()))
print('')
s = Sudoku(perfect_board_2)
print(fmt.format(repr(s), s, '\n'.join(s._matrix), s.winning_board()))
print('')
s = Sudoku('1234341243212143')
print(fmt.format(repr(s), s, '\n'.join(s._matrix), s.winning_board()))
print('')
'''
s = Sudoku()
print(fmt.format(repr(s), s, s._matrix, s.winning_board()))
print('')
'''
s = Sudoku()
print(fmt.format(repr(s), s, '\n'.join(s._matrix), s.winning_board()))
print('')
#print('a')
#print(Sudoku('12341234123412345'))
#exit('Done.') # ===============================================================

for i in xrange(1000000):
    s = Sudoku()
    #assert s._valid_rows()
    if not i % 5000:
        print(i)
    if s.winning_board():
        print('\n'.join(i, s, s.winning_board()))
print('Done.')
