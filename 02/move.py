def load_moves(filename):
    """Load a list of moves from a file,
    ignoring whitespace."""
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]


def encode_moves(moves, use_alternate=False):
    """For each move in moves, find the corresponding
    key on the number pad, stringify the key, and append
    to the code."""
    if use_alternate:
        move = alternate_move
    code = ''
    key = 5
    for move_sequence in moves:
        for direction in move_sequence:
            key = move(key, direction)
        code += str(key)
    return code

def normalize_index(i):
    """Ensure 0 <= i < 2."""
    return max(0, min(2, i))


def move(key, direction):
    """Given an integer key 1-9 and a
    direction U, D, L, or R, return
    the next key as if on a number pad,
    stopping at the edges."""
    number_pad = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    if key not in list(range(1, 10)):
        raise ValueError('key must be 1-9')
    if direction not in ['U', 'D', 'L', 'R']:
        raise ValueError('direction must be U, D, L, or R')
    for i, row in enumerate(number_pad):
        if key in row:
            j = row.index(key)
            break
    if direction == 'U':
        i -= 1
    elif direction == 'D':
        i += 1
    elif direction == 'L':
        j -= 1
    elif direction == 'R':
        j += 1
    return number_pad[normalize_index(i)][normalize_index(j)]

def alternate_move(key, direction):
    """Given a key in 1-9, A-D and a direction
    U, D, L, or R, return the next key in the
    alternate character pad, stopping at the edges."""
    character_pad = [[1],
                     [2, 3, 4],
                     [5, 6, 7, 8, 9],
                     ['A', 'B', 'C'],
                     ['D']]
    if key not in list(range(1, 10)) + ['A', 'B', 'C', 'D']:
        raise ValueError('key must be in 1-9 or A-D')
    if direction not in ['U', 'D', 'L', 'R']:
        raise ValueError('direction must be U, D, L, or R')
    for i, row in enumerate(character_pad):
        if key in row:
            j = row.index(key)
            max_j = len(row) - 1
            break
    if direction == 'U':
        # only possible if i == j == 1
        # or i == 2 and 1 <= j <= 3
        # or i == 3 or i == 4
        if i == j == 1:
            i = 0
            j = 0
        elif i == 2 and 1 <= j <= 3:
            i = 1
            j -= 1
        elif i in [3, 4]:
            i -= 1
            j += 1 
    elif direction == 'D':
        # only possible if i == j == 3
        # or i == 2 and 1 <= j <= 3
        # or i == 1 or i == 0
        if i == j == 3:
            i = 4
            j = 0
        elif i == 2 and i <= j <= 3:
            i = 3
            j -= 1
        elif i in [0, 1]:
            i += 1
            j += 1
    elif direction == 'L' and j > 0:
        j -= 1
    elif direction == 'R' and j < len(character_pad[i]) - 1:
        j += 1
    return character_pad[i][j]

