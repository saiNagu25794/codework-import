def get_the_modified_array(array):
    array[0] = array[-1]
    array[-1] = array[0]
    return array


if __name__ == "__main__":
    array = [12, 35, 9, 56, 24]

    modified_array = get_the_modified_array(array)
    print(modified_array)
