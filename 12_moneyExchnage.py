m = int(raw_input(''))
minCoins = 0
minCoins = minCoins + m/10 
# print minCoins
remainder = (m%10)
minCoins = minCoins + remainder/5 + remainder%5
print minCoins