# 定义一个函数 perms(l)，参数为长度为 5 且只包含不重复元素的列表，返回所有的排列
# 思考：如果长度不固定，应该怎么做？
# tip：善用搜索 —— 开发者的基本能力之一
def perms(l: list) -> list:
    x = 0
    for a in l:
        for b in l:
            for c in l:
                for d in l:
                    for e in l:
                        if a != b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                            print(str(a)+str(b)+str(c)+str(d)+str(e))
                            x += 1
                            print(x)



perms([1,2,3,4,5])
# import copy
#
# # 用一个全局变量记录每次递归得到的结果
# All_permutation = []
#
#
# # 递归函数,arr表示当前的排列,如[1,2,3,4],next表示当前排列中前next个数已经确定,需要从next+1的位置开始交换
# # 注意列表下标从0开始,next表示的是下标
# # 如next=1时,说明第一个数确定为1,然后从第二个数开始直到列表的结尾,每个数都要与第二个数进行一次交换
# def allPermutation(arr, next):
#     # 当next=len(arr)-1时,此时只剩下一个数要排列,直接就是结果
#     if next == len(arr) - 1:
#         global All_permutation
#         All_permutation.append(arr)
#     else:
#         # 从第next+1个数开始,每个数与第next+1的数进行一次交换(包括自己)
#         for i in range(next, len(arr)):
#             # 深拷贝,避免影响到原来的排列情况
#             update_permutation = copy.deepcopy(arr)
#             update_permutation[i], update_permutation[next] = update_permutation[next], update_permutation[i]
#             allPermutation(update_permutation, next + 1)
#
#
# allPermutation([1, 2, 3, 4, 5], 0)
# print(All_permutation)
