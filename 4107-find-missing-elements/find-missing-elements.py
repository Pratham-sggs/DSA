class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = float('inf')
        largest = float('-inf')
        numsSet = set()
        for i in nums:
            smallest = min(smallest, i)
            largest = max(largest, i)
            numsSet.add(i)
        res = []
        for i in range(smallest, largest+1):
            if i not in numsSet:
                res.append(i)
        res.sort()
        return res