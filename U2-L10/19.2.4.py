def prefix_count(words: list[str], pref: str) -> int:
    a = 0
    for _ in range(0,len(words)):
        if words[_][0:len(pref):1] == pref:
            a += 1
    return a
print(prefix_count(["pay","attention","practice","attend"],"at"))