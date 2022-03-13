
import math


def FindSchedule(l,k,s):

    n = len(l)
    newL=[]
    
    if(n>=4):
        if(l[0]+2*l[1]+l[len(l)-1] <= 2*l[0]+l[len(l)-2]+l[len(l)-1]):
            #case 1
            s += "+{"+str(l[0])+","+str(l[1])+"}-"+str(l[0])+"+{"+str(l[len(l)-1])+","+str(l[len(l)-2])+"}-"+str(l[1])
        else:
            #case 2
            s += "+{"+str(l[0])+","+str(l[len(l)-1])+"}-"+str(l[0])+"+{"+str(l[0])+""+str(l[len(l)-2])+"}-"+str(l[0])

    elif(n==3):
        s+="+{"+str(l[0])+","+str(l[2])+"}-"+str(l[0])+"+{"+str(l[0])+","+str(l[1])+"}"
        return s
    elif(n==2):
        s+="+{"+str(l[0])+","+str(l[1])+"}"
        return s
    return FindSchedule(l[:-2],k,s)
        
    
def CrossingTheBridge(l):
    order = []
    c = []
    l.sort()
    n = len(l)
    ck = 0
    if(n<=2):
        print(l)
        return max(l)
    for k in range(0, math.floor((n/2)-1)+1):
        order.append([])
        ck = (n-2-k)*l[0] + (2*k+1)*l[1]
        for i in range(0,n-2-k):
            order[k].append(l[0])
        for i in range(0,2*k+1):
            order[k].append(l[1])

        for i in range(3,n+1):
            ck+=l[i-1]
            order[k].append(l[i-1])

        for i in range(1,k+1):
            ck-=l[(n+1-2*i)-1]
            order[k].append(-l[(n+1-2*i)-1])

        c.append(ck)



    x = c.index(min(c))

    print(FindSchedule(l,x,"Schedule: "))
    print(min(c))

CrossingTheBridge([1,2,5]) # 8
CrossingTheBridge([1,2,5,10]) # 17
CrossingTheBridge([1,2,3,4,5]) # 16
CrossingTheBridge([1,1,2,3,4]) # 11
CrossingTheBridge([1,2,3,5,8]) # 19
CrossingTheBridge([1,3,4,5,9,15]) # 36
CrossingTheBridge([2,4,5,6,10,16]) # 45
CrossingTheBridge([1,3,8,11,15,17]) # 45
CrossingTheBridge([1,1,9,11,17,19]) # 37
CrossingTheBridge([1,2,2,3,3,3,4,4,4,4]) # 35
CrossingTheBridge([1,4,5,5,5,5,6,6,6,7]) # 57
CrossingTheBridge([1,2,5,5,5,5,6,6,6,7]) # 45
CrossingTheBridge([1,2,2,3,3,3,4,4,4,4,5]) # 41


