# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, node, dp):
        if not node:
            return 0
        if node in dp:
            return dp[node]
        take = node.val
        if node.left:
            take += self.solve(node.left.left, dp) + self.solve(node.left.right, dp)
        if node.right:
            take += self.solve(node.right.left, dp) + self.solve(node.right.right, dp)
        not_take = self.solve(node.left, dp) + self.solve(node.right, dp)
        dp[node] = max(take, not_take)
        return dp[node]

    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        return self.solve(root, dp)