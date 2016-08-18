def Fibonaci(n):
    if n <= 1:
        return n
    else:
        return Fibonaci(n-1)+Fibonaci(n-2)
def Fibonaci_fast(n):
     
    Fib = {}
    if n <= 1:
        return n
    Fib[0] = 0   
    Fib[1] = 1 
    for i in range(2,n+1):
        Fib[i] = Fib[i-1]+Fib[i-2]
    return Fib[i]
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