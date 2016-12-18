from find_password import find_password


def main():
    """Print the eight-character password seeded
    by the given door id.
    """
    door_id = 'ffykfhsq'
    print(find_password(door_id, length=8))


if __name__ == '__main__':
    main()
