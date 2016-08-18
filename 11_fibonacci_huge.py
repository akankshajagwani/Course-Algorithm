# Uses python2


def Fibonaci_fast(n):
     
    Fib = {}
    if n <= 1:
        return n
    Fib[0] = 0   
    Fib[1] = 1 
    for i in range(2,n+1):
        Fib[i] = Fib[i-1]+Fib[i-2]
    return Fib[i]


input = raw_input(" ").split()
print input
n = 10**int(input[0])
m = 10**int(input[1])
i = 0
lst = []
pattern = []
while i < n:
    result_1 = Fibonaci_fast(i)
    mod = result_1 % m
    lst.append(mod)
    if i > 2 and lst[i-2:i+1] == [0,1,1]:
        pattern = pattern + lst[0:i-2]
        break;
    i = i+1
 
# print "pattern:",len(pattern)
   
if len(pattern) is 0:
    ans = Fibonaci_fast(n) % m
else:
    ans = pattern[n% len(pattern)] 
print ans
exit()
import random
import time   
testCaseNo = 0        
while True:
    testCaseNo = testCaseNo+1
    if testCaseNo > 50:
        exit()
    else:
        lst = range(0,50)
        # n = random.randint(0, 46)
        # n= 327305
        n = testCaseNo-1
        print "n: ",n
        ticks_1 =  time.time()
        result_1 = Fibonaci_fast(n)
        ticks_2 =  time.time()
        result_2 =  0
        # result_2 =  Fibonaci(n)
        ticks_3 =  time.time()
        print "result_1: %d , result_2: %d" %(result_1,result_2)
        print "time_1: %f , and time_2: %f" %(ticks_2-ticks_1, ticks_3-ticks_2)