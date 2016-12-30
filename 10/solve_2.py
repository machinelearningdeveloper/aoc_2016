"""Multiply together the values of the chips in outputs 0-2."""

from analyze_flow import load_description, parse_description, step

def main():
    """Load the description of flows of chips
    between robots (nodes) and outputs and
    report the product of the chip values in
    outputs numbered 0, 1, and 2.
    """
    description = load_description()
    nodes, outputs, edges = parse_description(description)
    while ('0' not in outputs
           or '1' not in outputs
           or '2' not in outputs):
        nodes, outputs, edges = step(nodes, outputs, edges)
    product = 1
    for output_name in outputs:
        if output_name in ['0', '1', '2']:
            product *= int(outputs[output_name][0])
    print(product)


if __name__ == '__main__':
    main()
