def max_profit(prices: list[int]) -> int:
    x = []
    for _ in range(len(prices)):
        for i in range(len(prices)-_):
             x.append(prices[_+i] - prices[_])

    if max(x) < 0:
        return 0
    else:return max(x)
print(max_profit( [7,6,4,3,1]))