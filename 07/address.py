from collections import Counter
import re


def has_reflection(sequences):
    """Does any sequence in sequences have a reflection?

    A reflection is a four-character sequence that is the
    same backward as forward and consists of two different
    characters.
    """
    for sequence in sequences:
        for i in range(len(sequence) - 3):
            subseq = sequence[i:i + 4]
            if (len(Counter(subseq)) == 2) and (subseq == subseq[-1::-1]):
                return True
    return False


def is_compatible(address, protocol=1):
    """Return whether address is compatible with protocol.


    Protocol 1:

    Address has at least one four-character sequence occurring
    outside of square brackets that is the same backward and
    forward and has two different characters, and lacks any
    such sequence inside of square brackets.

    Protocol 2:

    Address has at least one three-character sequence occurring
    outside of square brackets where the two outer characters
    differ from the inner character.  The address must also have
    three-character sequence inside of square brackets matching
    the inverse of the pattern found outside of square brackets.
    """
    bracketed = [word.strip('[]') for word
                 in re.findall('\[[^\]]*\]', address)]
    not_bracketed = re.split('\[[^\]]*?\]', address)
    if protocol == 1:
        if has_reflection(bracketed):
            return False
        return has_reflection(not_bracketed)
    elif protocol == 2:
        patterns = extract_protocol_patterns(bracketed)
        for pattern in patterns:
            inverse_pattern = pattern[1] + pattern[0] + pattern[1]
            if any([inverse_pattern in word for word in not_bracketed]):
                return True
        return False
    else:
        raise ValueError('unknown protocol')   


def extract_protocol_patterns(sequences):
    """Return all three-character patterns of the form 'aba'."""
    patterns = []
    for sequence in sequences:
        length = len(sequence)
        start, mid, end = (range(length - 2),
                           range(1, length - 1),
                           range(2, length))
        for i, j, k in zip(start, mid, end):
            if sequence[i] != sequence[j] and sequence[i] == sequence[k]:
                patterns.append(sequence[i] + sequence[j] + sequence[k])
    return patterns


def load_addresses():
    """Load a list of addresses from a file."""
    with open('addresses.txt') as f:
        return [address.strip() for address in f.readlines()]
