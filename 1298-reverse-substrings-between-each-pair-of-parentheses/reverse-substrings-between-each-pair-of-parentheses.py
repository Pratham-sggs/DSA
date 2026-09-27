class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        answer = ''
        for i in s :
            if i == '(':
                stack.append('(')
            elif i == ')':
                k = stack.pop()
                while k != '(':
                    answer += k
                    k = stack.pop()
                stack.append(answer[::-1])
                answer = ''
            else:
                stack.append(i)
        print(stack)
        if len(stack) > 1 :
            result = ''
            while stack:
                result += stack.pop()
            return result[::-1]
        return stack[0][::-1]