"""Given a starting point, starting orientation, and a list of directions report
the distance between the starting point and the first point visited twice."""


from directions import load_directions, follow_directions, expand_path
from distance import get_distance


def main():
    directions = load_directions('directions.txt')
    starting_point = point = (0, 0)
    orientation = 'N'
    visited = []
    for step in directions:
        next_point, orientation = follow_directions(point, orientation, step)
        expanded = expand_path(point, next_point)
        for intermediate_point in expanded[1:]:
            if intermediate_point in visited:
                print(get_distance(starting_point, intermediate_point))
                return
            else:
                visited.append(intermediate_point)
        point = next_point
    print('No points visited twice.')


if __name__ == '__main__':
    main()
