def longest_common_prefix(strs: list[str]) -> str:
    l = []
    for _ in range(len(strs)):
        l.append(len(strs[_]))
    for _ in range(min(l)+1):
        for b in range(len(strs)):
            if strs[b][:_] != strs[0][:_]:
                return strs[b][:_-1]

file = open("1 (2).txt",mode="r")
for line in file.readlines():
    _ = line.split(" ")
    lis = []
    for i in range(len(_[0].split(","))):
        lis.append(_[0].split(",")[i])
    if longest_common_prefix(lis) != _[1].strip():
        print("False",lis)
    else:
        print("Correct")
