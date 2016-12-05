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


def load_triangles_from_cols(filename):
    """Instead of loading one triangle per line,
    load one-third each of three triangles per line."""
    xs = []
    ys = []
    zs = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y, z = [int(side) for side in line.split()]
                xs.append(x)
                ys.append(y)
                zs.append(z)
    return ([(xs[i], xs[i+1], xs[i+2]) for i in range(0, len(xs), 3)]
            + [(ys[i], ys[i+1], ys[i+2]) for i in range(0, len(ys), 3)]
            + [(zs[i], zs[i+1], zs[i+2]) for i in range(0, len(zs), 3)])
                


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
