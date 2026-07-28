class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length = len(s) // 2
        Uni = 97
        dictionary = defaultdict(int)
        for i in range(length):
            dictionary[ord(s[i]) - 97] += 1
        res = ""
        for i in range(0, 26):
            res = res + dictionary[i]*chr(i+97)
        if len(s) % 2 :
            return res + s[length] + res[::-1]
        return res + res[::-1] 