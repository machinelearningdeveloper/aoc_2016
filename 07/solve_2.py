from address import is_compatible, load_addresses


def main():
    """Count the number of addresses compatible with
    the second protocol, i.e., matching 'aba[bab]'.
    """
    addresses = load_addresses()
    print(sum([is_compatible(address, protocol=2) for address in addresses]))


if __name__ == '__main__':
    main()
