import sys
import random
from assignment import solution

def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def solve(dataset):
    return max_pairwise_product_compact(dataset)


def generate(length):
    n = random.randint(2,length)
    return [random.randint(0,200000) for i in range(n)]

if __name__ == '__main__':
    # Test
    dataset = generate(10)
    print(f"""n = {len(dataset)}, max = {max(dataset)}""")

    one = max_pairwise_product_naive(dataset)
    two = solution(dataset)

    if one == two:
        print('OK')
    else:
        print(f"Wrong answer! 1: {one} 2: {two}")