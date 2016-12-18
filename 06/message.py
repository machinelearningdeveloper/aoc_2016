from collections import Counter

def recover_message(messages, least_frequent=False):
    """For each position in the recovered message,
    find the most- (least-) frequently-occurring
    character in the same position in the set of
    raw messages.
    """
    i = len(messages) if least_frequent else 1
    return ''.join([Counter(seq).most_common(i)[-1][0]
                    for seq in zip(*messages)])


def load_messages():
    with open('messages.txt') as f:
        return [message.strip() for message in f.readlines()]
