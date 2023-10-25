class Solution:
    def coinChange(self, coins, amount):        
        lst = [amount+1] * (amount+1)
        lst[0] = 0
        for coin in coins:
            for i in range(coin,amount +1):
                lst[i] = min(lst[i],lst[i-coin]+1)

        return -1 if lst[-1] == (amount + 1) else lst[-1]
            