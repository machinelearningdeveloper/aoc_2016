import re


def load_directions(filename):
    """Load directions from a file."""
    with open(filename) as f:
        return [direction.strip().strip(',') for direction
                in f.readline().strip().split()]


def turn(orientation, direction):
    """Given an orientation on the compass
    and a direction ("L" or "R"), return a
    a new orientation after turning 90 deg
    in the specified direction."""
    compass = ['N', 'E', 'S', 'W']
    if orientation not in compass:
        raise ValueError('orientation must be N, E, S, or W')
    if direction not in ['R', 'L']:
        raise ValueError('direction must be R or L')
    i = (compass.index(orientation) + (1 if direction == 'R' else -1)) % len(compass)
    return compass[i]


def follow_directions(starting_point, starting_orientation, *directions):
    """Given a starting point, starting orientation
    and a list of directions of the form DN, where D
    is R (right) or L (left) and N is an integer,
    return the ending point and orientation."""
    point = starting_point
    orientation = starting_orientation
    for step in directions:
       m = re.match(r'(?P<direction>R|L)(?P<n>\d+)', step)
       if not m:
            raise ValueError('each step must be in the form (L|R)[0-9]+')
       orientation = turn(orientation, m.group('direction'))
       x = y = 0
       if orientation == 'E':
           x = 1
       elif orientation == 'W':
           x = -1
       if orientation == 'N':
           y = 1
       elif orientation == 'S':
           y = -1
       move = int(m.group('n'))
       point = (point[0] + x * move, point[1] + y * move) 
    return (point, orientation)
