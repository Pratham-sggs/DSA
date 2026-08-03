class Solution:
    def solve(self, stoneValue, i, dp):
        if i >= len(stoneValue):
            return 0
        if dp[i] != float('-inf') :
            return dp[i]
        take1 = stoneValue[i] - self.solve(stoneValue, i+1, dp)
        take2, take3 = float('-inf'), float('-inf')
        if i + 1 < len(stoneValue):
            take2 = stoneValue[i] + stoneValue[i+1] - self.solve(stoneValue, i+2, dp)
        if i + 2 < len(stoneValue):
            take3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - self.solve(stoneValue, i+3, dp)
        dp[i] = max(take1, take2, take3)
        return dp[i]
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [float('-inf') for i in range(len(stoneValue))]
        ans = self.solve(stoneValue, 0, dp)
        if ans == 0:
            return 'Tie'
        if ans > 0:
            return 'Alice'
        return 'Bob'