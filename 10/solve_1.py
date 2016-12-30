"""Find the robot handling value-61 microchips and value-17 microchips."""


from analyze_flow import find_node, load_description, parse_description, step


def main():
    """Load a description of the flow of microchips
    between robots (nodes) and find the robot handling
    value-61 and value-17 microchips.
    """
    description = load_description()
    nodes, outputs, edges = parse_description(description)
    while not find_node(nodes, '61', '17'):
        nodes, outputs, edges = step(nodes, outputs, edges)
    print(find_node(nodes, '61', '17'))


if __name__ == '__main__':
    main()
