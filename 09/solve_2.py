from message import load_data, calc_decomp_sz


def main():
    """Load data and calculate the decompressed size
    obtained from applying all nested markers.
    """
    data =  load_data()
    print(calc_decomp_sz(data))


if __name__ == '__main__':
    main()
