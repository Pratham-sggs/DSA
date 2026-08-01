class Solution:
    def solve(self, i, j, nums, dp):
        if i > j :
            return 0
        if dp[i][j] != float('inf'):
            return dp[i][j]
        takeLeft = nums[i] - self.solve(i+1, j, nums, dp)
        takeRight = nums[j] - self.solve(i, j-1, nums, dp)
        dp[i][j] = max(takeLeft, takeRight)
        return dp[i][j]

    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = [[float('inf') for j in range(len(nums))] for i in range(len(nums))]
        res = self.solve(0, len(nums)-1, nums, dp)
        return True if res >=0 else False
        