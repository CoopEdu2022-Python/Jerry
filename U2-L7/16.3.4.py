def shuffle_array(nums: list[int]) -> list[int]:
    list_safe = []
    new_list = []
    for _ in range(0,len(nums)//2):
        list_safe.append(nums[_])
    for i in range(0,len(nums)//2):
        new_list.append(list_safe[i])
        new_list.append(nums[i+len(nums)//2])
    return new_list
print(shuffle_array([1,2,3,4,4,3,2,1]))