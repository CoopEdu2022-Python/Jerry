def largest_perimeter(nums: list) -> int:
    nums.sort()
    if nums[0] + nums[1] <= nums[2]:
        return 0
    else:
        return sum(nums)
print(largest_perimeter([1,2,1]))