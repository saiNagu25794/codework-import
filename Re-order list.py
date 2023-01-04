def re_order_list(head):
    list_a = []
    for i in range(1, len(head) // 2 + 1):
        list_a.append(head[i - 1])
        list_a.append(head[-i])
    if len(head) % 2 == 0:
        return list_a
    else:
        index = len(head) // 2
        list_a.append(head[index])
        return list_a


# Re_order List
if __name__ == "__main__":
    head = [1, 2, 3, 4, 5, 6, 7]
    reorded_list = re_order_list(head)
    print(reorded_list)








