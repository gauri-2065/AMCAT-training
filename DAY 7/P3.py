# Roy and Profile Picture
def checkDim():
    L = int(input("Enter max dimension: "))
    N = int(input("Enter number of images: "))
    
    for i in range(0, N):
        W, H = map(int, input("Enter two values separated by spaces: ").split())
        
        if W < L or H < L:
            print("UPLOAD ANOTHER")
        elif W >= L and H >= L:
            if W == H:
                print("ACCEPTED")
            else:
                print("CROP IT")

checkDim()