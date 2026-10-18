# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        stack = []
        New = ListNode(0)
        last = New
        while head:
            node = head
            head = head.next
            node.next = None
            stack.append(node)
            if len(stack) == k:
                while stack:
                    last.next = stack.pop()
                    last = last.next
        temp = None
        while stack:
            node = stack.pop()
            node.next = temp
            temp = node
        last.next = temp
        return New.next