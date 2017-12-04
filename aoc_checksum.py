import unittest
import aoc_checksum

results = [{'input':'''5 1 9 5 7 5 3 2 4 6 8''', 'output':18},
            ]
class CheckSumTest(unittest.TestCase):
    def test_results(self):
        print('results are {}'.format(results))
        for r in results:
            print('Checking {} checksums {}'.format(r['input'], r['offset'], r['output']))
            self.assertEqual(aoc_checksum.checksum(r['input'], r['output']))

if __name__ == '__main__':
    print('hello world')
    unittest.main()

