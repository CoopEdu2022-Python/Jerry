def movenumber(x,list_input=[],direction = "right"):
    if direction == "right":
        safe = list_input[:x+2:-1]
        list_input = list_input[0:len(list_input) - x]
        newlist = safe + list_input
        return newlist
    elif direction == "left":
        safe_1 = list_input[x-1:0:-1]+[1]
        list_input = list_input[len(list_input)-x-3 :len(list_input)]
        newlist = list_input + safe_1
        return newlist
print(movenumber(2,[1,2,3,4,5,6,7],"left"))
