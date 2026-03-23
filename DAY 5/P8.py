mylist =  [4,2,7,8,5,4,1]

def searchValue(target):
    for i in range(len(mylist)):
        print(mylist[i])

        if mylist[i] == target:
            return print("Target ", target, " was found at index.",i)

    return print("The target was not found!")

target = 7
searchValue(target)

target = 10
searchValue(target)