def find_shortest_subarray(nums: list[int]) -> int:
    a = list(set(nums))
    x = []
    save = []
    maxl = []
    for c in range(len(a)):
        save.append(nums.count(a[c]))
    for findc in range(len(save)):
        if save[findc] == max(save):
            maxl.append(findc)
    for i in range(len(a)):
        for _ in range(len(nums)):
            if nums[len(nums)-_-1] == a[i]:
                t = _
                break
        for b in range(len(nums)):
            if nums[b] == a[i]:
                h = b
                break
        x.append(len(nums)-t-h)
    minl = []
    for g in range(len(maxl)):
        minl.append(x[maxl[g]])
    return (min(minl))


print(find_shortest_subarray([1,2,5,2,3,1]))