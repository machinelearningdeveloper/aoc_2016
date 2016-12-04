from distance import get_distance
import random

def generate_points(n):
    """Generate a list of points at randomly-
    selected coordinates.

    Parameters
    ----------
    n : int
        number of points to generate

    Returns
    -------
    points : list
        list of randomly-selected points
    """
    return [(random.randint(-20, 20), random.randint(-20, 20))
            for _ in range(n)]


def test_get_distance():
    points = generate_points(5)
    for a in points:
        for b in points:
            distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
            assert get_distance(a, b) == distance, \
                 "get_distance({a}, {b}) != {distance}".format(a=a, b=b, distance=distance)

test_get_distance()
print("All tests passed.")
