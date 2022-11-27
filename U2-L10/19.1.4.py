# 定义一个函数，参数为半径 r，计算圆的面积
# 自定义一个异常类 RadiusError，如果半径为负值，抛出 RadiusError
class Erro(Exception):
    pass
class RadiusError(Erro):
    pass
def radiuserror(r):
    r = int(r)
    area = 3.14 * (r**2)
    if r < 0:
        radiusError = Erro("RadiusError")
        raise radiusError
    else:
        return area
print(radiuserror("-7"))
# __main__这个是为啥
