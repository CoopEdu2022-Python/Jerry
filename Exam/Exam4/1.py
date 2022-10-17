def movenumber(x,list_input=[],direction = "right"):
    if direction == "right":
        return list_input[-x:]+list_input[:-x]
    elif direction == "left":
        return list_input[x:]+list_input[:x]
print(movenumber(2,[1,2,3,4,5,6,7],"left"))
