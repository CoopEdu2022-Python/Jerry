
def alt(s):
    list = []
    s = str(s)
    s=s.replace('IV','4 ')
    s=s.replace('IX','9 ')
    s=s.replace('XL','40 ')
    s=s.replace('XC','90 ')
    s=s.replace('CD','400 ')
    s=s.replace('CM','900 ')

    s=s.replace('I','1 ')
    s=s.replace('V','5 ')
    s=s.replace('X','10 ')
    s=s.replace('L','50 ')
    s=s.replace('C','100 ')
    s=s.replace('D','500 ')
    s=s.replace('M','1000 ')
    end = s.split()


    for _ in range(len(end)):
        s = int(end[_])
        list.append(s)

    a = sum(list)
    return a
print(alt("MCMXCIV"))

