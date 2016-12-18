from address import is_compatible, load_addresses


def main():
    """Load addresses and count how many are have
    reflections outside of a bracketed sequence
    and no reflections within a bracketed sequence.
    """
    addresses = load_addresses()
    print(sum([is_compatible(address) for address in addresses]))


if __name__ == '__main__':
    main()
