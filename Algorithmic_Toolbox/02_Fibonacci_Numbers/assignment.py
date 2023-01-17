def Fibonacci(n):
    arr = [0,1]
    if n <= 1:
        return arr[n]
    else:
        for i in range(1,n):
            arr.append(arr[-2] + arr[-1])
        return arr[-1]


if __name__ == '__main__':
    idx = int(input())
    print(Fibonacci(idx))