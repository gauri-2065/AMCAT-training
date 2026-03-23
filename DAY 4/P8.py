#nested loop

n = int(input("Enter the number of rows: "))

for i in range(1,n+1):   #rows
    for j in range(1,n+1):  #Columns
        print(chr(64+i), end=" ")
    print()
