

def get_the_result(list1, list2):
    set_list = set(list2)
    # print(set_list)
    sorted_list = sorted(set_list)
    # print(sorted_list)
    result = []
    for i in range(len(sorted_list)):
        for j in range(len(list2)):
            if sorted_list[i] == list2[j]:
                result.append(list1[j])
    return result




if __name__ == "__main__":
    list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
    sorted_list = get_the_result(list1, list2)
    print(sorted_list)