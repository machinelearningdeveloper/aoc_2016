"""Test whether putative triangles, specified as triples of side lengths,
in fact are possible."""


def load_triangles(filename):
    """Load triangles from filename."""
    triangles = []
    with open(filename) as f:
        for line in f:
           if line.strip():
               triangles.append(tuple([int(side) for side in line.split()]))
    return triangles


def is_possible(*sides):
    """The sum of the lengths of every pair of sides in a, b, c
    must be larger than the length of the remaining side,
    or the putative triangle is impossible."""
    for a in [0, 1]:
        for b in range(a + 1, 3):
            if a == 0:
                c = 1 if b == 2 else 2
            elif a == 1:
                c = 0
            if sum([sides[a], sides[b]]) <= sides[c]:
                return False
    return True
