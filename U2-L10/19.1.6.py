# 定义一个函数 triangle(a, b, c)，判断三个参数是否能构成一个三角形
# 如果不能则抛出异常 IllegalArgumentException，显示异常信息 'a, b, c 不能构成三角形'
# 如果可以构成，打印三角形三个边长
# 在方法中得到命令行输入的三个整数，调用此方法，并捕获异
# 常
class IllegalArgumentException(Exception):
    pass
def largest_perimeter(nums: list) -> int:

    nums.sort(reverse=False)
    print(nums)
    if nums[0] + nums[1] > nums[2]:
        return nums
    else:
        raise IllegalArgumentException
try:
    print(largest_perimeter([2,9,4]))
except IllegalArgumentException:
    print("不可")