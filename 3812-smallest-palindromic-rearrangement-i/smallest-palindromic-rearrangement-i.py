class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length = len(s)//2
        ans = s[:length]
        ans = sorted(ans)
        res = ""
        for i in ans:
            res = res + i
        
        if (len(s)%2):
            return res + s[length] + res[::-1]
        return res + res[::-1]