class Solution:
    def solve(self, n, i, dp):
        if i > n:
            return 0
        if i == n:
            return 1
        if dp[i] != -1:
            return dp[i]
        climb1 = self.solve(n, i+1, dp)
        climb2 = self.solve(n, i+2, dp)
        dp[i] = climb1 + climb2
        return dp[i]
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n)]
        return self.solve(n, 0, dp)
        