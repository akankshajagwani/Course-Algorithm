# n = int(raw_input(''))
# lst_a = raw_input('').split()
# lst_b = raw_input('').split()
def MinDotProduct(lst_a,lst_b):
    lst_A = []
    lst_B = []
    for i in lst_a:
        lst_A.append(int(i))
    for i in lst_b:
        lst_B.append(int(i))
    lst_A.sort()
    lst_B.sort(reverse=True)
    Dotproduct = 0
    for i in range(0,len(lst_A)):
       Dotproduct = Dotproduct +  lst_A[i]*lst_B[i]
    return Dotproduct

import random
import time   
testCaseNo = 0        
while True:
    testCaseNo = testCaseNo+1
    if testCaseNo > 10:
        exit()
    else:
        lst = range(-100000,100000)
        n = random.randint(1, 1000)
      
        lst_a = random.sample(lst, n) 
        lst_b = random.sample(lst, n) 
        print "n: ",n
        ticks_1 =  time.time()
        result_1 = MinDotProduct(lst_a,lst_b)
        ticks_2 =  time.time()
        # result_2 =  0
        # result_2 =  Fibonaci(n)
        # ticks_3 =  time.time()
        print "result_1: %d " %(result_1)
        print "time_1: %f " %(ticks_2-ticks_1)