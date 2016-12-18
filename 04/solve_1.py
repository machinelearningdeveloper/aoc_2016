from room import load_rooms, sum_sector_ids

def main():
    """Load a list of room identifiers from text file
    and calculate the sum of the sector ids for the
    valid room identifiers."""
    rooms = load_rooms()
    print(sum_sector_ids(rooms))


if __name__ == '__main__':
    main()
    
