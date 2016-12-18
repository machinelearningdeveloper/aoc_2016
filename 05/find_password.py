from hashlib import md5


def find_password(seed, complex=False):
    """Return an eight-character password.

    If not complex:

    Search for characters in the password by incrementing
    an integer, appending its string representation to the
    seed, generating a hex digest of the MD5 hash of the
    combined value, and selecting the sixth character
    of the result if it begins with five zeroes.

    If complex:

    Search for digests as before, but instead of filling
    the password from the left, use the sixth character
    as a pointer into the password and the seventh character
    as the actual password character.
    """
    i = 0
    password = ['_'] * 8
    while any([char == '_' for char in password]):
        digest = md5((seed + str(i)).encode()).hexdigest()
        if digest.startswith('00000'):
            if complex:
                ptr = digest[5]
                if ptr.isdigit():
                    ptr = int(ptr)
                    if ptr < len(password) and password[ptr] == '_':
                        password[ptr] = digest[6]
            else:
                ptr = password.index('_')
                password[ptr] = digest[5]
            print(' '.join(password), end='\r')
        i += 1
    print()
    return ''.join(password)
