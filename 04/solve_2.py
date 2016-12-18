from room import (decrypt, extract_sector_id,
                  is_valid_checksum, load_rooms)


def main():
    """Load rooms from room.txt and print the decrypted
    names and sector ids of the validly-named rooms."""
    for room in load_rooms():
        if is_valid_checksum(room):
            print(decrypt(room), extract_sector_id(room))


if __name__ == '__main__':
    main()
