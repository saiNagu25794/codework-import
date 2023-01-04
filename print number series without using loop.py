

def PrintNumber(N, original, k, flag):

    #print the number
    print(N, end = " ")

    #checking the num negative or not
    #if lessthan 0 changing the flag value

    if N <= 0:
        if flag == 0:
            flag = 1
        else:
            flag = 0


    if (N == original) and not(flag):
        return

    if flag == True:
        PrintNumber(N - k, original, k, flag)
        return

    if not(flag):
        PrintNumber(N + k, original, k, flag)
        return






#Givens Two number N and K, our task is to subtract a number K from N until number(N)
# is greater than zero, once the N becomes negative or zero then we start adding K until
# that number become the original number(N). Note : Not allow to use any loop
if __name__ == "__main__":
    N = 20
    K = 6
    PrintNumber(N, N, K, True)
