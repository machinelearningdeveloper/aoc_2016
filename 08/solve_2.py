from collections import Counter

from screen import initialize_screen, load_instructions, redraw_screen


def main():
    """Initialize a screen, load instructions,
    and print the final screen after following
    all instructions for redrawing the screen.
    """
    screen = initialize_screen(50, 6)
    instructions = load_instructions()
    for command in instructions:
        screen = redraw_screen(screen, command)
    print(screen)


if __name__ == '__main__':
    main()
