list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def checkerboard_print(list_number):
    for _ in range(0, 3):

        for i in range(0, 3):
            print("| ", " ", end="|", sep="%s" % str(list_number[int(3 * _ + i)]))
        if _ == 2:
            break
        else:
            print("\n", "——--——--——--——-", sep="")
def judge_checkerboard(list_number):
    for _ in range(0, 7):
        location = int(input("下在哪里"))
        if location == list_number[location+1]:
            if _ // 2 == 1:
                list_number[location + 1] = "x"
            else:
                list_number[location + 1] = "o"



checkerboard_print([1, 2, "x", 4, 5, 6, 7, 8, 9])
