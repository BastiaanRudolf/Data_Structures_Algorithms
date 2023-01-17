def EuclidGCD(a, b):
    if b == 0:
        return a
    else:
        return EuclidGCD(b, a%b)


def LCM(a,b):
    return int((a*b) / EuclidGCD(a, b))

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(LCM(a, b))
