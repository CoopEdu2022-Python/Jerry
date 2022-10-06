plant_place = [["口","口","口"],["口","口","口"],["口","口","口"]]
a = []
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
        if 1 in b == True:
            plant_place[0][0]=  "x"
        elif 2 in b == True:
            plant_place[0][1] = "x"
        elif 3 in b == True:
            plant_place[0][2] = "x"
        elif 4 in b == True:
            plant_place[1][0] = "x"
        elif 5 in b == True:
            plant_place[1][1] = "x"
        elif 6 in b == True:
            plant_place[1][2] = "x"
        elif 7 in b == True:
            plant_place[2][0] = "x"
        elif 8 in b == True:
            plant_place[2][1] = "x"
        elif 9 in b == True:
            plant_place[2][2] = "x"
            return b
def composition():
    for i in range(0,3):
        for cunt in range(0,3):
            print(plant_place[i][cunt],end="   ")
        print("\n")

x = int(input("输入位置1-9"))
showing_systema(x)
print(plant_place)
composition()


