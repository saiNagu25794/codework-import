
def get_the_substraction(a, b):
    subMatrix = []
    length = len(a)
    substraction = []
    for i in range(length):
        sub = []
        for j in range(len(a[0])):
            sub.append(a[i][j] - b[i][j])
        substraction.append(sub)
    return(substraction)

def get_the_addition(a, b):
    addMatrix = []
    length = len(a)
    addition = []
    for i in range(length):
        add = []
        for j in range(len(a[0])):
            add.append(a[i][j] + b[i][j])
        addition.append(add)
    return(addition)


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[4, 5], [6, 7]]

    addition = get_the_addition(a, b)
    substraction = get_the_substraction(a, b)

    print(addition)
    print(substraction)