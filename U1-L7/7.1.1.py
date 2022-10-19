# def compa(s1:str,s2:str) -->bool ……这个叫啥来着
def compa(s1,s2):
    return sorted(s1) == sorted(s2)

print(compa("asd","dsa"))