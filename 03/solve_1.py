"""Report the number of putative triangles that are, in fact, possible."""


from triangle import load_triangles, is_possible


def main():
    """Report the number of possible triangles in
    a file defining triangles by side length."""
    triangles = load_triangles('triangles.txt')
    print(sum([is_possible(*triangle) for triangle in triangles]))


if __name__ == '__main__':
    main()
