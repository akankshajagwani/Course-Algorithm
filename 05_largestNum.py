# greedy algo
def LargetNumFromDigits(lst_digits):
    lst_digits.sort(reverse=True)
    str_1 = ""
    for i in lst_digits:
        str_1 = str_1+str(i)
    
    return str_1
    
# LargetNumFromDigits(raw_input().split())
import random
import time   
testCaseNo = 0        
while True:
    testCaseNo = testCaseNo+1
    if testCaseNo > 10:
        exit()
    else:
        n = random.randint(2, 9)
        print "testCaseNo: %d ,n: %d" %(testCaseNo,n)
        r = range(1,10)
   
        r = random.sample(r, n) 
        print "r: ",r
        ticks_1 =  time.time()
        result_1 = LargetNumFromDigits(r)
        ticks_2 =  time.time()
        
        print "result_1: %s " %(result_1)
        print "time_1: %f  " %(ticks_2-ticks_1)
