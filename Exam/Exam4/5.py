def cuntlast(s):
    s = str(s)
    return len(s.rpartition(" ")[-1])
print(cuntlast("I alal gcjvkj"))