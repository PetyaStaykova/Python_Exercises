nums_as_str = input().split(', ')
nums = [int(i) for i in nums_as_str]
even_nums = [index for index in range(len(nums)) if nums[index] % 2 == 0]
print(even_nums)