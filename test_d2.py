import unittest
import aoc_checksum

results = [{'input':'''5 1 9 5
    7 5 3 
    2 4 6 8
    ''', 'output':18},
            ]
results_2 = [{'input':'''5 9 2 8
    9 4 7 3
    3 8 6 5
    ''', 'output':9},
    ]

class CheckSumTest(unittest.TestCase):
    def test_results(self):
        print('results are {}'.format(results))
        for r in results:
            print('Checking \n[{}]\n checksums {}'.format(r['input'], r['output']))
            self.assertEqual(aoc_checksum.aoc_checksum(r['input']), r['output'])

    def test_chksm_2(self):
        print('results are {}'.format(results_2))
        for r in results_2:
            print('Checking \n[{}]\n checksums {}'.format(r['input'], r['output']))
            self.assertEqual(aoc_checksum.aoc_checksum_2(r['input']), r['output'])

if __name__ == '__main__':
    print('hello world')
    unittest.main()

