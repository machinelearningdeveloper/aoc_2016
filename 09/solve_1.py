from message import load_data, read_data


def main():
    """Load some compressed data, read it,
    and report the decompressed length.
    """
    data = load_data()
    decompressed = read_data(data)
    print(decompressed)
    print(len(decompressed))


if __name__ == '__main__':
    main()
