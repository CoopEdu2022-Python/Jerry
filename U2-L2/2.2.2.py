# 2.2.2 思考学校生活中有没有逻辑嵌套的场景，仿照 #2.2.1（变量赋值、打印等），实现代码逻辑
paper = int(input("我有几张打印纸？"))
if paper != 0 :
    paper_consume = int(input("我要打印几份啊"))
    if paper < paper_consume :
        print("还需要找""%d""份" % (paper_consume-paper))
    else:
        print("那没事了")
else:
    print("去找找")