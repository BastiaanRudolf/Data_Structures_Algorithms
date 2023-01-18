def pisano(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if (prev == 0 and curr == 1):
            return i + 1


def Fibonacci(n):
    m = 10
    n = n % pisano(m)
    previous, current = 0, 1
    arr = [0,1]

    if n <= 1:
        return arr[n]
    else:
        for i in range(n-1):
            previous, current = current, previous + current
            arr.append(current)
        return (sum(arr) % m)


if __name__ == '__main__':
    idx = int(input())
    print(Fibonacci(idx))