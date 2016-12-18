def initialize_screen(width, height):
    """Create a screen having width x height pixels."""
    rows = ['.' * width] * height
    return '\n'.join(rows)

def transpose(matrix):
    """Transpose a list of lists."""
    return [list(t) for t in zip(*matrix)]


def rotate(elements, rotation):
    """Rotate list of elements by rotation places."""
    length = len(elements)
    rotated = [None] * length
    for i in range(length):
        j = (i + rotation) % length
        rotated[j] = elements[i]
    return rotated


def rotate_column(screen, index, rotation):
    """Rotate the column at index by rotation places."""
    exploded = explode(screen)
    transposed = transpose(exploded)
    transposed[index] = rotate(transposed[index], rotation)
    return implode(transpose(transposed))


def rotate_row(screen, index, rotation):
    """Rotate the row at index by rotation places."""
    exploded = explode(screen)
    exploded[index] = rotate(exploded[index], rotation)
    return implode(exploded)


def redraw_screen(screen, command):
    """Return a new screen by transforming the current
    screen according to a command."""
    cmd_and_args = parse_command(command)
    cmd = cmd_and_args[0]
    args = cmd_and_args[1:]
    return cmd(screen, *args)


def parse_command(command):
    """Return the parsed command, either rect
    or rotate, plus arguments."""
    rect_pattern = 'rect '
    rotate_row_pattern = 'rotate row y='
    rotate_column_pattern = 'rotate column x='
    if command.startswith(rect_pattern):
        arg_str = command.replace(rect_pattern, '')
        width, height = arg_str.split('x')
        return rect, int(width), int(height)
    elif command.startswith(rotate_row_pattern):
        arg_str = command.replace(rotate_row_pattern, '')
        index, _, rotation = arg_str.split()
        return rotate_row, int(index), int(rotation)
    elif command.startswith(rotate_column_pattern):
        arg_str = command.replace(rotate_column_pattern, '')
        index, _, rotation = arg_str.split()
        return rotate_column, int(index), int(rotation)
    raise ValueError('unknown command')


def rect(screen, width, height):
    """Turn on the width x height rectangle of
    pixels starting at 0, 0 (upper right corner)."""
    exploded = explode(screen)
    for j in range(width):
        for i in range(height):
            exploded[i][j] = '#'
    return implode(exploded) 
    

def load_instructions():
    """Load screen-drawing instructions."""
    with open('instructions.txt') as f:
        return [instruction.strip() for instruction in f]


def explode(screen):
    """Convert a string representing a screen
    display into a list of lists."""
    return [list(row) for row in screen.split('\n')]


def implode(exploded):
    """Convert a list of lists representing a
    screen display into a string."""
    return '\n'.join([''.join(row) for row in exploded])
