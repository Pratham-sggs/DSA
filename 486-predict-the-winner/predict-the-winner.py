class Solution:
    def solve(self, i, j, nums):
        if i > j :
            return 0
        takeLeft = nums[i] - self.solve(i+1, j, nums)
        takeRight = nums[j] - self.solve(i, j-1, nums)
        return max(takeLeft, takeRight)

    def predictTheWinner(self, nums: List[int]) -> bool:
        res = self.solve(0, len(nums)-1, nums)
        return True if res >=0 else False
        