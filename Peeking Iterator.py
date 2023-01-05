


def peekingIterator(list_a, inputList):
    result_list = []
    index = 0
    for item in inputList:

        if item == "next":
            result_list.append(list_a[index])
            index += 1
        if item == "peek":
            result_list.append(list_a[index])
        if item == "hasNext":
            if index == len(list_a):
                result_list.append(False)
            else:
                result_list.append(True)
    return(result_list)


#list: [1,2,3].

#Call next() gets you 1, the first element in the list. Now you call
#peek() and it returns 2, the next element. Calling next() after that
#still return 2.  You call next() the final time and it returns 3, the
#last element.  Calling hasNext() after that should return false.

if __name__ == "__main__":
    input = [ "next", "peek", "next", "next", "hasNext"]

    print(peekingIterator([1, 2, 3], input))