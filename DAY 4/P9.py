#nested loop

n = int(input("Enter the number of rows: "))

for i in range(1,n+1):   #rows
    for j in range(1,i+1):  #Columns
        print(i, end=" ")
    print()
