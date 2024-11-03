#

import unittest
from dictionary import get_p_distance, get_p_distance_matrix

class TestPDistanceFunctions(unittest.TestCase):
    def test_p_distance(self):
        result = get_p_distance("TTCCTTT", "ATTTCGT")
        self.assertAlmostEqual(result, 0,4)

    def test_p_distance_matrix(self):
        dna_list = [
            "TTCCTTT",
            "ATTTCGT",
            "GTATTCA",
            "TTATTCA"
        ]
        result = get_p_distance_matrix(dna_list)
        expected = [
            [0.0, 0.4, 0.4, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.4, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        for i in range(len(dna_list)):
            for j in range(len(dna_list)):
                self.assertAlmostEqual(result[i][j], expected[i][j])

if __name__ == '__main__':
    unittest.main()