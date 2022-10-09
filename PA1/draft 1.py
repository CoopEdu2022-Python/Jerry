plant_place = [["口","口","口"],["口","口","口"],["口","口","口"]]
a = []
b = []
def showing_systema(x):
    while 1:
        if 1 == x:
            plant_place[0][0]=  "o"
            return a
        elif 2 == x:
            plant_place[0][1] = "o"
            return a
        elif 3 == x:
            plant_place[0][2] = "o"
            return a
        elif 4 == x:
            plant_place[1][0] = "o"
            return a
        elif 5 == x:
            plant_place[1][1] = "o"
            return a
        elif 6 == x:
            plant_place[1][2] = "o"
            return a
        elif 7 == x:
            plant_place[2][0] = "o"
            return a
        elif 8 == x:
            plant_place[2][1] = "o"
            return a
        elif 9 == x:
            plant_place[2][2] = "o"
            return a
    a.append(x)

def showing_systemb(b):
    while 1:
        if 1 == x:
            plant_place[0][0]=  "x"
            return b
        elif 2 == x:
            plant_place[0][1] = "x"
            return b
        elif 3 == x:
            plant_place[0][2] = "x"
            return b
        elif 4 == x:
            plant_place[1][0] = "x"
            return b
        elif 5 == x:
            plant_place[1][1] = "x"
            return b
        elif 6 == x:
            plant_place[1][2] = "x"
            return b
        elif 7 == x:
            plant_place[2][0] = "x"
            return b
        elif 8 == x:
            plant_place[2][1] = "x"
            return b
        elif 9 == x:
            plant_place[2][2] = "x"
            return b
    b.append(x)
def composition():
    for i in range(0,3):
        for cunt in range(0,3):
            print(plant_place[i][cunt],end="   ")
        print("\n")


while 1 :
    for _ in range(0,2):
        if _ == 0:
            x = int(input("输入位置1-9"))
            showing_systema(x)
            composition()
        else:
            x = int(input("输入位置1-9"))
            showing_systemb(x)
            composition()


