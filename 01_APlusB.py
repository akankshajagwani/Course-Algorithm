# Uses python2

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
        exit()
# Taking inputs     
str_numbers = raw_input()
lst_num = str_numbers.split()
n_a = IsInteger(lst_num[0])
CheckRange(n_a,0,9)
n_b = IsInteger(lst_num[1])
CheckRange(n_b,0,9)

#Output
sum = n_a+n_b
print sum