from message import load_messages, recover_message


def main():
    """Recover the error-corrected message in messages
    loaded from messages.txt.
    """
    messages = load_messages()
    print(recover_message(messages, least_frequent=True))


if __name__ == '__main__':
    main()
