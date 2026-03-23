def searchValue(mylist):
    sum = 0
    for i in range(len(mylist)):
        sum+=mylist[i]
    return sum

mylist = [4,3,5,6,7,8,3,4,1]
res = searchValue(mylist)
print("Sum of the array: ",res)



# import numpy as np

# arr = np.array('i', [1,2,3,4,5,6,7,8,9,10])
# sum = 0
# for i in arr:
#     sum+=i
# print(sum)
