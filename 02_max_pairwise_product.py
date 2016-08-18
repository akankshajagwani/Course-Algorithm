# Uses python2
import random
import time
import sys
def IsInteger(str):
    try:
        d =int(str)
        return d
    except:
        print "Entry is not int type"
        exit ()
def CheckRange(num, minValue, maxValue):
    if num < minValue or  num > maxValue:
        print "Entry: %d is not in range. It should be >= %d and <= %d" %(num,minValue,maxValue)
def Method_1(r):
    r.sort(reverse=True)
    return r[0]*r[1]
    
def Method_2(a):
    result_2 = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result_2:
                result_2 = a[i]*a[j]
    return result_2

testCaseNo = 0 
x = 200000
y = 100000      
while True:
    testCaseNo = testCaseNo+1
    if testCaseNo > 10:
        exit()
    n = random.randint(2, x)
    print "testCaseNo: %d ,n: %d" %(testCaseNo,n)
    r = range(1,y+1)
    if n > y:
        print "here"
        r = random.sample(r, y) 
        r = r + random.sample(r, n-y)
    else: 
        r = random.sample(r, n) 
    assert(len(r) == n)
    #Method_1
    ticks_1 =  time.time()
    result_1 = Method_1(r)
    ticks_2 =  time.time()
    #Method_2
    result_2 = 0
    result_2 = Method_2(r)
    ticks_3 =  time.time()
    print "result_1: %d , result_2: %d" %(result_1,result_2)
    print "time_1: %f , and time_2: %f" %(ticks_2-ticks_1, ticks_3-ticks_2)
    


str = raw_input()
a = [int(x) for x in raw_input().split()]
ticks_1 =  time.time()
n = IsInteger(str)
CheckRange(n,2,200000)
for i in a:
    CheckRange(i,0,100000)
assert(n > 1)
assert(len(a) == n)

a.sort(reverse=True)
result = a[0]*a[1]
# result = 0

# for i in range(0, n):
    # for j in range(i+1, n):
        # if a[i]*a[j] > result:
            # result = a[i]*a[j]

print(result)

ticks_2 =  time.time()
print "time taken: ",ticks_2-ticks_1
print(type(result))
print sys.maxint
print 2**31
print sys.maxint
print type(sys.maxint)
print type(sys.maxint+1)
