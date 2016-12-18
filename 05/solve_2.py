from find_password import find_password


def main():
    """Find a password given a seed."""
    door_id = 'ffykfhsq'
    print(find_password(door_id, complex=True))


if __name__ == '__main__':
    main()
