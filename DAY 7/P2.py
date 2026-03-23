def totalDistance(n, arr):
    sum = 0
    for i in range(0,n-1):
        # if(i!=n):
            sum += abs(arr[i] - arr[i+1]) 
        
    return print(sum)


n = 5
arr = [10,11,7,12,14]
totalDistance(n,arr)