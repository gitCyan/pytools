from matplotlib import pyplot as plt
from math import ceil

def calc_y(L=5, x=1):
    y = (L**2 - x**2) ** 0.5
    return x, y

def main():
    LL = 15
    strtmp = input("Please input round depth\n(default is 15, press Enter for default, input numbers for specified value under 15)\n:")
    try:
        LL = int(strtmp)
        if LL > 15: LL = 15
    except: LL = 15
    list1 = []
    for i in range(LL+1): 
        xx, yy = calc_y(LL, i)
        xx, yy = round(xx, 0), round(yy, 0)
        #xx, yy = ceil(xx), ceil(yy)
        list1.append((xx, yy))
    plt.plot(list1)
    plt.show()
    print(list1)
    stro = ''
    for i in list1:
        xx, yy = i
        xx, yy = int(xx), int(yy)
        strtmp = hex(xx)
        strtmp = strtmp[2:].rjust(1, '0')
        stro += strtmp
        strtmp = hex(yy)
        strtmp = strtmp[2:].rjust(1, '0')
        stro += strtmp
        stro += '\n'
    print(stro)
    input("press any key to exit ...")
    exit()

if __name__ == "__main__":
    main()