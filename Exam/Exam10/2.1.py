def find_lus_length(a: str, b: str) -> int:
    if a == b:
        return -1
    if len(a) == len(b):
        return len(a)
    else:
        return max(len(a),len(b))
print(find_lus_length(a = "aaa", b = "aaa"))