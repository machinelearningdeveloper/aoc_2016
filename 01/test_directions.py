from directions import load_directions, turn, follow_directions


def test_load_directions():
    with open("directions.txt") as f:
        directions = [direction.strip(',')
                      for direction
                      in f.readline().strip().split()]
    assert load_directions("directions.txt") == directions, \
        "Failed to load directions from directions.txt."


def test_turn():
    assert turn('N', 'R') == 'E'
    assert turn('N', 'L') == 'W'
    assert turn('E', 'R') == 'S'
    assert turn('E', 'L') == 'N'
    assert turn('S', 'R') == 'W'
    assert turn('S', 'L') == 'E'
    assert turn('W', 'R') == 'N'
    assert turn('W', 'L') == 'S'


def test_follow_directions():
    starting_point = (0, 0)
    starting_orientation = 'N'
    directions = ['R2', 'L3', 'R1']
    ending_point = (3, 3)
    ending_orientation = 'E'
    assert (follow_directions(starting_point, starting_orientation, *directions)
            == (ending_point, ending_orientation))


test_load_directions()
test_turn()
test_follow_directions()
print("All tests passed.")
