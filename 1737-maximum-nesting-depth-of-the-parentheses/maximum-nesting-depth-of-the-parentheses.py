class Solution:
    def maxDepth(self, s: str) -> int:
        length = 0
        res = 0
        for i in s:
            if i == '(':
                length += 1
                res = max(length, res)
            elif i == ')':
                length -= 1
        return res