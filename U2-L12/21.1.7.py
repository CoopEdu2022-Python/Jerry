def change_name(papername,name):
    file = open(papername,"r+")
    file.writelines(name)
    file.close()
change_name("dldkj.txt","aaaaa")
change_name("qpeuwr.txt","aaaaa")
change_name("zmcxbvn.txt","aaaaa")

