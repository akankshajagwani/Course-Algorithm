
from gcd_04 import gcd 
def lcm(a,b):
    result = 1
    gcd_1 = gcd(a,b)
    result = a*b/gcd_1
    return result
    
print lcm(6,8)
print lcm(28851538, 1183019)