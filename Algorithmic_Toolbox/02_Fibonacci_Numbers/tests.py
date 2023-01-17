import unittest
import time
import tracemalloc
import random
from assignment import Fibonacci


class TestFibonacci(unittest.TestCase):


    # Constraint: 0 <= n <= 45
    def test_first_thirteen(self):
        sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for i, val in enumerate(sequence):
            self.assertEqual(val, Fibonacci(i))


    def test_first_thirteen_with_time(self):
        sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for i, val in enumerate(sequence):
            start = time.process_time()
            self.assertEqual(val, Fibonacci(i))
            end = time.process_time()
            self.assertTrue(end-start < 5)


    # def test_first_thirteen_mem(self):
    #     sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    #     for i, val in enumerate(sequence):
    #         tracemalloc.start()
    #         self.assertEqual(val, Fibonacci(i))
    #         tracemalloc.stop()


    def test_last_with_time(self):
        start = time.process_time()
        self.assertEqual(1134903170, Fibonacci(45))
        end = time.process_time()
        self.assertTrue(end-start < 5)


if __name__ == '__main__':
    unittest.main()
