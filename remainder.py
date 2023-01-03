def get_the_ramainder(num, n):
    remainder = num % n
    return remainder

def get_the_multiply(array):

    multiply = 1
    for num in array:
        multiply *= num
    return multiply






if __name__ == "__main__":
    array = [100, 10, 5, 25, 35, 14]
    n = 11

    multiplication = get_the_multiply(array)
    remainder = get_the_ramainder(multiplication, n)
    print(remainder)





