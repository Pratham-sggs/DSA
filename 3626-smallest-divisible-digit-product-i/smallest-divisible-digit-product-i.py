class Solution:
    def digitProduct(self, number):
        ans = 1
        while number > 0:
            ans *= number % 10
            number //= 10
        return ans
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            num = self.digitProduct(n)
            if num % t == 0:
                return n
            n += 1