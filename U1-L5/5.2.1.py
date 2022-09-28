# 5.2.1 回忆你在学校吃过的 5 道菜品，并存储在元组 menu 中
# 使用 for 循环将菜单的菜品打印出来
# 尝试修改其中的一个元素，查看错误信息，以注释的形式将错误信息添加在上面一行；然后，将发生错误的代码注释，保证程序能正常运行
# 学校调整了菜单，替换了它提供的其中 2 道菜品。想办法修改菜单，并打印新版本的菜单
mene = ("redfiremeat","water","rice","apple","friffe")
for i in range(0,len(mene)):
    print(mene[i],end=" ")
mene_new = ("redfiremeat","water","rice","bpple","aaaaaaaa")
# 'tuple' object does not support item assignment
# mene[2]="sadwsdw"
mene = mene_new
print("\n")
for i in range(0,len(mene)):
    print(mene[i],end=" ")