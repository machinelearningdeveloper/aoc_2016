def normalize_index(i):
    """A number pad has three rows and three columns.
    Ensure that an index into the number pad never
    is less than 0 and never exceeds 2."""
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
        j = key in row and row.index(key)
        if j != False:
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
