# import pandas as pd
# s = pd.Series([1, 3, 5])
# print(s)
#
# from MyModule import Animal
# lion = Animal("georges")
# lion.printName()


#ex

med={1,3,8,10}


def median(lst):
    lst = sort(lst)
    if len(lst) % 2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return lst[((len(lst)+1)/2)]

print(median(med))
