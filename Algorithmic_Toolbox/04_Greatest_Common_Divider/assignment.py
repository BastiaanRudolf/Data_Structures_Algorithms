def EuclidGCD(a, b):
    if b == 0:
        return a
    else:
        return EuclidGCD(b, a%b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(EuclidGCD(a, b))
