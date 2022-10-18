b = [["I",1],['V',5],['X', 10],['L', 50],['C', 100],['D',500],['M',1000]]


def romanToInt(d):

    r = []

    for _ in range(0,len(d)):

        if b[-_+1] > b[-_]:
            a = b[-_+1] - b[-_]
        else:r.append(b[-_])
        r.append(a)

    return sum(r)
romanToInt("VI")