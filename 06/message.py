from collections import Counter

def recover_message(messages):
    """For each position in the recovered message,
    find the most-frequently-occurring character
    in the same position in the set of raw messages.
    """
    return ''.join([Counter(seq).most_common(1)[0][0]
                    for seq in zip(*messages)])


def load_messages():
    with open('messages.txt') as f:
        return [message.strip() for message in f.readlines()]
