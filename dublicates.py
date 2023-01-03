def get_the_dublicates_list(list):
    new_list = []
    dublicates_list = []
    for num in list:
        if num not in new_list:
            new_list.append(num)
        else:
            dublicates_list.append(num)
    return sorted(set(dublicates_list))





if __name__ == "__main__":
    list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
    dublicates_list = get_the_dublicates_list(list)
    print(dublicates_list)