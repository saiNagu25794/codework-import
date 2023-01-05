def get_product_array(nums):
    product_list = []
    for i in range(len(nums)):
        product = 1
        for num in nums:
            if nums[i] == num:
                continue
            else:
                product *= num
        product_list.append(product)
    print(product_list)


#Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].

if __name__ == "__main__":
    nums = [-1, -1, 0, -3, -3]
    get_product_array(nums)