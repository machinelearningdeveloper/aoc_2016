from move import load_moves, encode_moves


def main():
    """
    Given a character pad, a starting position of five (5),
    and a list of directions encoded as strings, print the
    characters corresponding to the directions.

    Example:
        A file contains the following set of moves:

            ULL
            RRDDD
            LURDL
            UUUUD

        The corresponding code is:

            5DB3

    """
    moves = load_moves('moves.txt')
    code = encode_moves(moves, use_alternate=True)
    print(code)


if __name__ == '__main__':
    main()
