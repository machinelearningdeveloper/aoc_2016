"""Report the manhattan distance between a starting point and an ending point,
given a set of directions to follow to move between the two points."""


from distance import get_distance
from directions import load_directions, follow_directions


def main():
    directions = load_directions('directions.txt')
    starting_point = (0, 0)
    starting_orientation = 'N'
    ending_point, _ = follow_directions(starting_point, starting_orientation, *directions)
    print(get_distance(starting_point, ending_point))


if __name__ == '__main__':
    main()
