def find_duplicate_items(nums: list[int]) -> int:
    for _ in range(0,len(nums)):
        for i in range(0,len(nums)):
            if nums[_] ==nums[i]:
                return nums[_]

print(find_duplicate_items([2,1,2,5,3,2]))