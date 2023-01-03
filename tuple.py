
def get_the_result(test_list):
    x = []

    for i in test_list:
        if i[0] not in x:
            x.append(i[0])
    result = []
    for i in x:
        common = []
        common.append(i)
        for j in test_list:
            if i == j[0]:
                common.append(j[1])
        result.append(common)
    return result


if __name__ == "__main__":
    test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
    result = get_the_result(test_list)
    print(result)