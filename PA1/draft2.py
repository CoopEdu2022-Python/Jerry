list_white,list_black =[1,2,3],[4,5]
def checkerboard_print(list_number = [1,2,3,4,5,6,7,8,9]):


    for _ in range(0,3):

        for i in range(0,3):
            print("| "," ",end="|",sep="%s"% str(list_number[int(3 * _ + i)]))
        if _ == 2:
            break
        else:
            print("\n","——--——--——--——-",sep="")
def judge_checkerboard():
    for _ in range(0,7):


checkerboard_print([1,2,"x",4,5,6,7,8,9])
