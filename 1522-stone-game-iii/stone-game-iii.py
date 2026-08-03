class Solution:
    # def solve(self, stoneValue, i, dp):
    #     if i >= len(stoneValue):
    #         return 0
    #     if dp[i] != float('-inf') :
    #         return dp[i]
    #     take1 = stoneValue[i] - self.solve(stoneValue, i+1, dp)
    #     take2, take3 = float('-inf'), float('-inf')
    #     if i + 1 < len(stoneValue):
    #         take2 = stoneValue[i] + stoneValue[i+1] - self.solve(stoneValue, i+2, dp)
    #     if i + 2 < len(stoneValue):
    #         take3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - self.solve(stoneValue, i+3, dp)
    #     dp[i] = max(take1, take2, take3)
    #     return dp[i]
    # def stoneGameIII(self, stoneValue: List[int]) -> str:
    #     dp = [float('-inf') for i in range(len(stoneValue))]
    #     ans = self.solve(stoneValue, 0, dp)
    #     if ans == 0:
    #         return 'Tie'
    #     if ans > 0:
    #         return 'Alice'
    #     return 'Bob'

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 4)
        for i in range(n - 1, -1, -1):
            take1 = stoneValue[i] - dp[i + 1]
            take2 = float('-inf')
            if i + 1 < n:
                take2 = stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
            take3 = float('-inf')
            if i + 2 < n:
                take3 = (stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3])
            dp[i] = max(take1, take2, take3)
        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        return "Bob"