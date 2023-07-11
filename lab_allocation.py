def lab_allocation(x,y,z,n):
    if(n<=x):
        return "L1"
    elif(n<=y):
        return "L2"
    else:
        return "L3"
    
x,y,z,n=map(int,input().split())
print(lab_allocation(x,y,z,n))