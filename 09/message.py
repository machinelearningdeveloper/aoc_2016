import re

def load_data():
    """Load data from a file."""
    with open('data.txt') as f:
        return ''.join(f)


def parse_marker(marker):
    """Parse a marker out into compressed data length
    and number of times to repeat the compressed data.
    """
    return tuple(int(i) for i in marker.strip('()').split('x'))


def read_data(data):
    """Read data character-by-character,
    inflating any compressed sequences
    encountered along the way.
    """
    ptr = 0
    buffer = ''
    data = re.sub('\s', '', data)
    while ptr < len(data):
        marker_start = data.find('(', ptr)
        if marker_start >= 0:
            buffer = buffer + data[ptr:marker_start]
            marker_end = data.find(')', marker_start) + 1
            compressed_length, repeat = \
                parse_marker(data[marker_start:marker_end])
            ptr = marker_end
            compressed_data = data[ptr:ptr + compressed_length]
            buffer = buffer + compressed_data * repeat
            ptr += compressed_length
        else:
            buffer = buffer + data[ptr:]
            ptr = len(data)
    return buffer


def calc_decomp_sz(data):
    """Calculate--without decompressing--the decompressed
    size of data when all nested markers are applied.
    """
    data = re.sub('\s', '', data)
    decomp_sz = 0
    while len(data):
        marker_start = data.find('(')
        if marker_start >= 0:
            decomp_sz += marker_start
            marker_end = data.index(')') + 1
            comp_len, repeat = parse_marker(data[marker_start:marker_end])
            subseq = data[marker_end:marker_end + comp_len]
            decomp_sz += repeat * calc_decomp_sz(subseq)
            data = data[marker_end + comp_len:]
        else:
            decomp_sz += len(data)
            data = ''
    return decomp_sz
