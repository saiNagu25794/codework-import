def PrintNumber(n, k):
    original = n
    list_num = []
    while n >= 0:
        list_num.append(n)
        n -= k
    while n <= original:
        list_num.append(n)
        n += k
    return list_num

if __name__ == "__main__":
    n = 20
    k = 6
    num_series = PrintNumber(n, k)
    print(*num_series)