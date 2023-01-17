import unittest
import time
import tracemalloc
import random
from assignment import lastDigitOfFibonacci


class TestFibonacci(unittest.TestCase):


    # Constraint: 0 <= n <= 10^6
    def test_first_thirteen(self):
        sequence = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4]
        for i, val in enumerate(sequence):
            self.assertEqual(str(val), lastDigitOfFibonacci(i))


    def test_first_thirteen_with_time(self):
        sequence = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4]
        for i, val in enumerate(sequence):
            start = time.process_time()
            self.assertEqual(str(val), lastDigitOfFibonacci(i))
            end = time.process_time()
            self.assertTrue(end-start < 5)


    def test_last_with_time(self):
        start = time.process_time()
        self.assertEqual('0', lastDigitOfFibonacci(45))
        end = time.process_time()
        self.assertTrue(end-start < 5)


if __name__ == '__main__':
    unittest.main()
