def hamming_distance(x: int, y: int) -> int:
    count = 0
    x = bin(x)[2::]
    y = bin(y)[2::]

    max_len = max(len(x),len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    print(x)
    print(y)
    for _ in range(max_len):
        if x[_] != y[_]:
            count +=1
    return count
print(hamming_distance(x = 3, y = 1))