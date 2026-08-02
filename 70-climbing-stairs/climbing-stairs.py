class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,0]
        for i in range(n-1, -1, -1):
            dp[0], dp[1] = dp[1], dp[0]
            dp[0] = dp[0] + dp[1]
        return dp[0]
        