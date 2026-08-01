class Solution:
    def solve(self, start, end, person1, person2, chance, dp, nums):
        if start > end:
            return person1 >= person2
        if chance:
            take = self.solve(start+1, end,  person1+nums[start], person2, False, dp, nums)
            nottake = self.solve(start, end-1,  person1+nums[end], person2, False, dp, nums)
            return take or nottake
        take = self.solve(start+1, end, person1, person2+nums[start], True, dp, nums)
        nottake = self.solve(start, end-1, person1, person2+nums[end], True, dp, nums)
        return take and nottake
    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.solve(0, len(nums)-1, 0, 0, True, {}, nums)
        