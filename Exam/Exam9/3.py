from typing import Tuple, List


def largest_altitude(gain: list[int]) -> tuple[list[int], int]:
    altitude = [0]
    altitude_n = 0
    for _ in range(len(gain)):
        altitude_n += gain[_]
        altitude.append(altitude_n)
    return (altitude,max(altitude))
print(largest_altitude([-4,-3,-2,-1,4,3,2]))