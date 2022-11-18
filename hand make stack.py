#栈
class Stack():
    def __init__(self):
        self.all = []
        self.len = 0
    def __str__(self):
        print(self.all[self.len])
    def yazhan(self,x):
        self.all.append(x)
        self.len += 1
    def pop(self):
        print(self.all[self.len])
        self.all.pop(self.len)
        self.len -= 1
    def __len__(self):
        return self.len
    def max_min(self):
        max(self.all)

