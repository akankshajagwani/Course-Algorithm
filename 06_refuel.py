# greedy algo
def MinRefills(x,n,L):
    #n - no of gas stations between A and B
    #L - Min distance car can travel with full tank,L=300
    #x - list of distance of gas stations from A x[0]-A, x[1]-200, x[2]-450,x[n+1]-B
    MinNoRefills = 0
    curPnt = 0
    lastRefill = 0
    
    while curPnt <= n:
        lastRefill = curPnt
        print "lastRefill: ",x[lastRefill]
        while curPnt <= n and x[curPnt+1]-x[lastRefill] <= L:
            curPnt = curPnt+1
        if curPnt == lastRefill:
            print "IMPOSSIBLE"
            break
        if curPnt <= n:
            MinNoRefills = MinNoRefills + 1
    return MinNoRefills

    
 
Refills = MinRefills([0,100,345,550,750,1150], 4, 700)
print Refills
import random
import time   
testCaseNo = 0        
while True:
    testCaseNo = testCaseNo+1
    if testCaseNo > 10:
        exit()
    else:
        n = random.randint(1, 21)
        print "testCaseNo: %d ,n: %d" %(testCaseNo,n)
        r = range(1,1500)
        x = random.sample(r, n+2)
        x.sort()
        L = random.randint(1, 500)
        print "x: ",x,"L: ",L
        ticks_1 =  time.time()
        result_1 = MinRefills(x,n,L)
        ticks_2 =  time.time()
        
        print "result_1: %d " %(result_1)
        print "time_1: %f  " %(ticks_2-ticks_1)
