def largest_perimeter(nums: list) -> int:

    for i in range(len(nums)-2):
        nums.sort(reverse=True)
        if nums[0] + nums[1] > nums[2]:
            return nums[0]+nums[1]+nums[2]
        else:
            nums.pop(nums[1])

print(largest_perimeter([2,1,5,6,9,10,13,7,7,3,2,5,4]))