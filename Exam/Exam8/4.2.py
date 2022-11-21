def array_sign(nums: list[int]) -> int:
    count = 0
    for _ in range(len(nums)):
        if 0 == nums[_]:
            return 0
        if nums[_]<0:
            count += 1
    if count % 2 == 0:
        return 1
    else:
        return -1
print(array_sign([-1,1,-1,1,-1]))