common_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(0,12):
    print("平年","%d"%(i+1),"月有""%d"%common_year[i])
    if i == 1:
        common_year[1]=28
        print("润年", "%d" % (i + 1), "月有""%d" % common_year[i])
    else:
        print("润年", "%d" % (i + 1), "月有""%d" % common_year[i])