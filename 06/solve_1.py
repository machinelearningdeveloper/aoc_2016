from message import load_messages, recover_message


def main():
    """Load messages and find the error-corrected message."""
    messages = load_messages()
    print(recover_message(messages))


if __name__ == '__main__':
    main()
