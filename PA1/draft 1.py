plant_place = [[[],[],[]],[],[]]
def showing_system(a):
    safe_list = []
    while 1:
        if 1 in a == True:
            plant_place[1][1]=  "o"
        elif 2 in a == True:
            plant_place[1][2] = "o"
        elif 3 in a == True:
            plant_place[1][3] = "o"
        elif 4 in a == True:
            plant_place[2][1] = "o"
        elif 5 in a == True:
            plant_place[2][2] = "o"
        elif 6 in a == True:
            plant_place[2][3] = "o"
        elif 7 in a == True:
            plant_place[3][1] = "o"
        elif 8 in a == True:
            plant_place[3][2] = "o"
        elif 9 in a == True:
            plant_place[3][3] = "o"
            return a

def showing_system(b):
    safe_list = []
    while 1:
        if 1 in b == True:
            plant_place[1][1]=  "x"
        elif 2 in b == True:
            plant_place[1][2] = "x"
        elif 3 in b == True:
            plant_place[1][3] = "x"
        elif 4 in b == True:
            plant_place[2][1] = "x"
        elif 5 in b == True:
            plant_place[2][2] = "x"
        elif 6 in b == True:
            plant_place[2][3] = "x"
        elif 7 in b == True:
            plant_place[3][1] = "x"
        elif 8 in b == True:
            plant_place[3][2] = "x"
        elif 9 in b == True:
            plant_place[3][3] = "x"
            return b
while 1:
    x = input(int("输入位置1-9"))

