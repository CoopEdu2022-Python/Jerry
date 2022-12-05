def min_cost_climbing_stairs(cost: list[int]) -> int:
    for _ in range(0,len(cost)-2):
        cost[_+2] += min(cost[_],cost[_ + 1])
    return min(cost[-1],cost[-2])
print(min_cost_climbing_stairs([10,15,20]))