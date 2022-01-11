import unittest
from kruskals_algorithm import Graph


class TestKruskalsAlgorithm(unittest.TestCase):
    def setUp(self):
        self.test_graph_1 = Graph()
        self.test_graph_1.add_edge(0, 1, 1)
        self.test_graph_1.add_edge(0, 2, 1)
        self.test_graph_1.add_edge(2, 3, 6)
        self.test_graph_1.add_edge(1, 3, 3)
        self.test_graph_1.add_edge(1, 2, 4)
        self.test_min_span_tree_1 = [[0, 1, 1], [0, 2, 1], [1, 3, 3]]

        self.test_graph_2 = Graph()
        self.test_graph_2.add_edge(0, 3, 4)
        self.test_graph_2.add_edge(2, 1, 1)
        self.test_graph_2.add_edge(0, 2, 2)
        self.test_graph_2.add_edge(1, 3, 1)
        self.test_graph_2.add_edge(1, 0, 2)
        self.test_min_span_tree_2 = [[2, 1, 1], [1, 3, 1], [0, 2, 2]]

    def testKruskalsAlgorithm1(self):
        self.assertListEqual(self.test_min_span_tree_1,
                             self.test_graph_1.kruskals_algorithm())

    def testKruskalsAlgorithm2(self):
        self.assertListEqual(self.test_min_span_tree_2,
                             self.test_graph_2.kruskals_algorithm())
