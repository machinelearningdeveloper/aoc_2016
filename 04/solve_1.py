from sum_sector_ids import sum_sector_ids

def main():
    """Load a list of room identifiers from text file
    and calculate the sum of the sector ids for the
    valid room identifiers."""
    with open('rooms.txt') as f:
        rooms = [room.strip() for room in f.readlines()]
    print(sum_sector_ids(rooms))


if __name__ == '__main__':
    main()
    
