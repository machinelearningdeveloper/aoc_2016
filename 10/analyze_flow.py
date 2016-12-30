def load_description():
    """Load description of a flow in a network
    from a file named description.txt.
    """
    with open('description.txt') as description:
        return [line.strip() for line in description]


def parse_description(description):
    """Parse a description of a flow.

    Parameters
    ----------
    description : str
        a set of lines desc

    Returns
    -------
    nodes : dict
        each key is a node name
        each value is a 2-tuple containing
        up to two values flowing through
        the node
    outputs : dict
        each key is an output name
        each value is the tuple of values
        at that output name
    edges : dict
        each key is a node name
        each value is a 2-tuple of 2-tuples:
        
            ((low_dictionary, low_node_name),
             (high_dictionary, high_node_name))

        the low dictionary and low node name pair denotes
        where the low value in the node named in the key
        goes, while the high dictionary and high node name
        specify where the high value goes
    """
    nodes = dict()
    outputs = dict()
    edges = dict()
    for line in description:
        components = line.strip().split()
        if not len(components): continue
        sentinel = components[0]
        if sentinel == 'value':
            _, value, _, _, _, node_name = components
            node = nodes.get(node_name, tuple())
            nodes[node_name] = node + (value, )
        else:
            (_, node_name, _, _, _, low_dictionary_name, low_node_name,
             _, _, _, high_dictionary_name, high_node_name) = components
            low_dictionary = \
                nodes if low_dictionary_name == 'bot' else outputs
            high_dictionary = \
                nodes if high_dictionary_name == 'bot' else outputs
            edges[node_name] = ((low_dictionary, low_node_name),
                                (high_dictionary, high_node_name))
    return nodes, outputs, edges


def step(nodes, outputs, edges):
    """Return updated state in the form of a collection
    of nodes, a collection of outputs, and a collection
    of edges, given a collection of nodes, a collection
    of outputs, and a collection of edges.

    A node only propagates values if it has two values.

    Parameters
    ----------
    nodes : dict
        each key is a node name
        each value is a 2-tuple containing
        up to two values flowing through
        the node
    outputs : dict
        each key is an output name
        each value is the tuple of values
        at that output name
    edges : dict
        each key is a node name
        each value is a 2-tuple of 2-tuples:
        
            ((low_dictionary, low_node_name),
             (high_dictionary, high_node_name))

        the low dictionary and low node name pair denotes
        where the low value in the node named in the key
        goes, while the high dictionary and high node name
        specify where the high value goes

    Returns
    -------
    nodes : dict
        nodes, transformed by propagated flows
    outputs : dict
        outputs, transformed by propagated flows
    edges : dict
        edges passed into the function
    """
    flowed = []
    for node_name in nodes.copy():
        if node_name in flowed:
            continue
        if len(nodes[node_name]) == 2:
            if node_name in flowed:
                continue
            node = [int(value) for value in nodes[node_name]]
            low_value, high_value = min(node), max(node)
            low_flow, high_flow = edges[node_name] 
            low_dictionary, low_node_name = low_flow
            high_dictionary, high_node_name = high_flow
            low_node = low_dictionary.get(low_node_name, tuple())
            high_node = high_dictionary.get(high_node_name, tuple())
            low_dictionary[low_node_name] = low_node + (str(low_value),)
            high_dictionary[high_node_name] = high_node + (str(high_value),)
            nodes[node_name] = tuple()
            if low_dictionary is nodes:
                flowed.append(low_node_name)
            if high_dictionary is nodes:
                flowed.append(high_node_name)
    return nodes, outputs, edges


def find_node(nodes, *values):
    """Find the node having all of the search values.

    Parameters
    ----------
    nodes : dict
        each key is a node name
        each value is a 2-tuple containing
        up to two values flowing through
        the node
    values : *args
        every value in values must be in the 
        returned node

    Returns
    -------
    node : dict
        one-element dictionary of the form
        { node_name: search_values }
        representing the node found
        or None if no such node exists
    """
    search_vals= tuple(sorted(values))
    for node_name, node_vals in nodes.items():
        if search_vals == tuple(sorted(node_vals)):
            return {node_name: node_vals}
    return None
