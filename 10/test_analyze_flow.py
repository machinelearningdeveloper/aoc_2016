import operator
import unittest

from analyze_flow import (load_description, parse_description, step, find_node)


class TestAnalyzeFlow(unittest.TestCase):
    def setUp(self):
        self.description = \
            """bot 90 gives low to bot 7 and high to bot 113
            value 43 goes to bot 90
            value 17 goes to bot 90
            value 1 goes to bot 113
            bot 113 gives low to bot 30 and high to output 7""".split('\n')
        self.nodes_a = {'90': ('43', '17'), '113': ('1',)}
        self.nodes_b = {'90': tuple(), '7': ('17',), '113': ('1', '43')}
        self.nodes_c = {'90': tuple(), '7': ('17',), '113': tuple(),
                        '30': ('1',)}
        self.outputs_a = dict()
        self.outputs_b = dict()
        self.outputs_c = {'7': ('43', )}
        self.edges = {'90': ((self.nodes_a, '7'), (self.nodes_a, '113')),
                      '113': ((self.nodes_a, '30'), (self.outputs_a, '7'))}

    def test_load_description(self):
        assert len(load_description())

    def test_parse_description(self):
        nodes, outputs, edges = parse_description(self.description)
        assert nodes is not outputs
        assert nodes == self.nodes_a
        assert outputs == self.outputs_a
        assert edges == self.edges

    def test_step(self):
        nodes, outputs, edges = \
            step(self.nodes_a, self.outputs_a, self.edges)
        assert nodes is not outputs
        assert nodes == self.nodes_b
        assert outputs == self.outputs_b
        assert edges == self.edges
        nodes, outputs, edges = step(nodes, outputs, edges)
        assert nodes == self.nodes_c
        assert outputs == self.outputs_c
        assert edges == self.edges

    def test_find_node(self):
        assert find_node(self.nodes_a, '1') \
            == {'113': self.nodes_a['113']}
        assert find_node(self.nodes_a, '17', '43') \
            == {'90': self.nodes_a['90']}
        assert find_node(self.nodes_a, '100', '99') is None 
