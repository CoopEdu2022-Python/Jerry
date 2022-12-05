def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    count = 0
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        count+=1
        flowerbed[0] = 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        count+=1
        flowerbed[-1] = 1

    for _ in range(len(flowerbed)-2):
        if flowerbed[_] + flowerbed[1 + _] + flowerbed[2 + _] == 0:
            count += 1
            flowerbed[1+_] = 1
    return count >= n

print(can_place_flowers([1,0,0,0,1],2))
