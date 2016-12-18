import re


def extract_checksum(room):
    """Given a room identifier of the form:

        'aaa-bbb-cc-d-e-123[abcde]'

    Return the part in square braces:

        'abcde'
    """
    m = re.search(r'\[(?P<checksum>[a-z]{5})\]$', room)
    return m.group('checksum') if m else None


def create_checksum(room):
    """Given a room identifier of the form:

        'aaa-bbb-cc-d-e-123[abcde]'

    Create and return a checksum:

        'abcde'

    The checksum consists of the five most-frequent letters
    in the room identifier, not including the putative already-
    computed checksum appearing in square brackets at the end
    of the room identifier, in alphabetical order.  Ties are
    to be broken in alphabetical order.
    """
    m = re.search(r'(?P<name>[a-z]+)', room.replace('-', ''))
    name = ''
    if m:
        name = m.group('name')
    counts = dict()
    for letter in name:
        count, _ = counts.setdefault(letter, (0, letter))
        counts[letter] = (count - 1, letter)
    return ''.join(sorted(counts, key=counts.get)[:5])


def extract_sector_id(room):
    """Given a room identifier of the form:

        'aaa-bbb-cc-d-e-123[abcde]'

    Return the sector id:

        '123'
    """
    m = re.search(r'(?P<sector_id>\d+)', room)
    return m.group('sector_id') if m else None


def is_valid_checksum(room):
    """Given a room identifier of the form:

        'aaa-bb-cc-d-e-123[abcde]'

    Return whether the checksum, 'abcde', is valid, i.e.,
    whether it represents the five most-frequent letters
    in the rest of the room identifier, in alphabetical order.
    """
    return create_checksum(room) == extract_checksum(room)


def sum_sector_ids(rooms):
    """Given a list of room identifiers of the form:

    'aaa-bb-cc-d-e-123[abcde]'

    Return the sum of the sector ids.  In this example
    the sector id is '123'.
    """
    return sum([int(extract_sector_id(room))
                for room in rooms
                if is_valid_checksum(room)])


def load_room_identifiers():
    """Return a list of room identifiers,
    loaded from a text file named rooms.txt."""
