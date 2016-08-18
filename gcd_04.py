#uses python2
#gcd(a,b) =gcd(b,a') where a' is the remainder of a/b
# gcd(a,0) = a

def gcd_fast(a,b):
    if b is 0:
        return a
    else:
        remainder = a%b
        return gcd_fast(b,remainder)
def gcd(a,b):
    result = 1
    if b is 0:
        return a
    else:
        for i in range(2, min(a, b) + 1):
            if (a%i is 0) and (b%i is 0) :
                result = i
        return result
import random
import time   
# testCaseNo = 0        
# while True:
    # testCaseNo = testCaseNo+1
    # if testCaseNo > 10:
        # result_1 = gcd_fast(3918848,1653264)
        # print result_1
        # result_2 =  gcd(3918848,1653264)
        # print result_2
        # result_3 = gcd_fast(28851538, 1183019)
        # print result_3
        # exit()
    # else:
        # a = random.randint(1, 5000)
        # b = random.randint(1, 5000)
        # print "a:%d, b:%d "%(a,b)
        # ticks_1 =  time.time()
        # result_1 = gcd_fast(a,b)
        # ticks_2 =  time.time()
        # result_2 =  gcd(a,b)
        # ticks_3 =  time.time()
        # print "result_1: %d , result_2: %d" %(result_1,result_2)
        # print "time_1: %f , and time_2: %f" %(ticks_2-ticks_1, ticks_3-ticks_2)