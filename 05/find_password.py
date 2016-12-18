from hashlib import md5


def find_password(seed, length):
    """Return a password having length characters.

    Search for characters in the password by incrementing
    an integer, appending its string representation to the
    seed, generating a hex digest of the MD5 hash of the
    combined value, and selecting the sixth character
    of the result if it begins with five zeroes.
    """
    i = 0
    password = []
    while len(password) < length:
        digest = md5((seed + str(i)).encode()).hexdigest()
        if digest.startswith('00000'):
            password.append(digest[5])
        i += 1
    return ''.join(password)
