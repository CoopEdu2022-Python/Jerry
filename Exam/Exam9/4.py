def calculate_tax(brackets: list[list[int]], income: int) -> float:
    a = 0
    for i in range(len(brackets)):
        if i != 0:
            brackets[i][0] = brackets[i][0] - brackets[i-1][0]
    for _ in range(len(brackets)):
        if income - brackets[_][0] >= 0:
            a += brackets[_][0] * 0.01 * brackets[_][1]
            income = income - brackets[_][0]
        elif income - brackets[_][0] == 0:
            a += brackets[_][0] * 0.01 * brackets[_][1]
            income = income - brackets[_][0]
            return a
        else:
            a += income*0.01*brackets[_][1]

            return a
print(calculate_tax([[3,50],[7,10],[12,25]],10))


