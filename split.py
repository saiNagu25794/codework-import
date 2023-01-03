def get_the_result(array, k):

    first_part = array[0 : k]
    second_part = array[k: ]
    result = second_part + first_part
    return result



if __name__ == "__main__":
    array = [12, 10, 5, 6, 52, 36]
    k = 2
    result = get_the_result(array, 2)
    print(result)

