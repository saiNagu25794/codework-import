
def get_the_result(n, k):
    # starts with 0, 1
    a = 0
    b = 1
    position = 2

    while True:
        c = a + b
        a = b
        b = c
        if b % k == 0:
            return (position * n)
            break
        position += 1



if __name__ == "__main__":
    n = 5
    k = 4
    result = get_the_result(n, k)
    print(result)