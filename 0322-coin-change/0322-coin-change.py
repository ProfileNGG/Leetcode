class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        lst=[math.inf] * (amount+1)# 각 금액까지 만드는데 동전이 최소로 얼마나 드는지 저장하는 리스트(무한대로)
        lst[0]=0 #0원은 동전 안드니까 0으로 설정
        
        for coin in coins:
            for i in range(coin, amount+1): #코인에서 어마운트+1 까지의 범위를 반복하면서 갯수 계산
                #if i-coin>=0: #원래 있던 코드인데 불필요한 것 같아서 일단 주석처리 함
                lst[i]=min(lst[i], lst[i-coin]+1)#각 금액 i 가 가질  수 있는 최소의 동전갯수 저장
        
        return -1 if lst[-1]==math.inf else lst[-1]#lst[-1]은 리스트의 마지막 값을 반환하는 것, 그러므로 어마운트의 동전갯수 리턴