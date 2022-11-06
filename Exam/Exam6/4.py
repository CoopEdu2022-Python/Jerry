# 定义一个函数 max_sec_average(l, n)，参数为纯数字列表 l 和正整数 n，返回 l 中连续 n 个数的最大平均值
# len(l) >= n，结算结果不需要处理精度
def max_sec_average(nums: list, k: int) -> float:
    if len(nums) >= k:
        x = len(nums) - k
        list_for_end = []
        for i in range(0,x):
            list_for_one = []
            for _ in range(0,k):
                list_for_one.append(nums[i+_])
            list_for_end.append(sum(list_for_one))

        return float(max(list_for_end)/k)


    else:
        return False
print(max_sec_average([1,12,-5,-6,50,3], 4))