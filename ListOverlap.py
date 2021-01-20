'''
Overlap 2 list to find elements that are common between the list
Try to write as comprehensive as possible
lv2: try if there is 2 same number in one of the list
'''

a = [1,2,3,4,5,6,7,8,9]
b = [1,7,3,3,5,33,11,33,6,3,7,77]


def fuselst(lsta,lstb):
    fuselst_og = [i for i in lstb if i in lsta]
    fuselst = []
    for x in fuselst_og:
        if x not in fuselst:
            fuselst.append(x)
    fuselst.sort(reverse=False)
    return fuselst
print(fuselst(a,b))