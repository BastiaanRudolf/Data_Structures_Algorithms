def lastDigitOfFibonacci(n):
    arr = ['0','1']
    if n <= 1:
        return arr[n]
    else:
        for i in range(1,n):
            lastdigit = str(int(arr[-2]) + int(arr[-1]))[-1]
            arr.append(lastdigit)
        return arr[-1]


if __name__ == '__main__':
    idx = int(input())
    print(lastDigitOfFibonacci(idx))