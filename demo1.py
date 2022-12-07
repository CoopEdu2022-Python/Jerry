def jurged(x:str):
    stack = []
    ch = []
    len_ = 0
    for _ in range(len(x)):
        stack.append(x[_])
        len_ += 1

    for i in range(len(x)):
        ch.append(stack[len_-1])
        stack.pop(len_-1)
        len_ -= 1
    if list(x) == ch:
        return True
    else:return False
print(jurged("123989023"))