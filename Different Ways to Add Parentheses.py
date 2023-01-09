def get_the_result(expression):
    if expression.isnumeric():
        return [int(expression)]


    res = []
    for i, char in enumerate(expression):

        if char in ['+', '-', '*']:
            left = get_the_result(expression[:i])
            right = get_the_result(expression[i + 1:])

            for le in left:
                for ri in right:
                    if char == '+':
                        res.append(le + ri)
                    elif char == '-':
                        res.append(le - ri)
                    else:  # char == '*'
                        res.append(le * ri)
    return res


if __name__ == "__main__":
    expression = "2-1-1"
    print(get_the_result(expression))