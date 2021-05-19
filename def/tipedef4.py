def perim(p):
    return p * 4


def area(s):
    return (s + s)**2




p = int(input('Enter sides of square: '))
x= perim(p)
s = area(p)




print('perim:', x)
print('area:', s)
