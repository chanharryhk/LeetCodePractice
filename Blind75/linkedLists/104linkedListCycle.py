# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
#         def helper(turtle, rabbit):
#             if not turtle or not rabbit:
#                 return False
#             if not rabbit.next:
#                 return False
#             if turtle.val == rabbit.val:
#                 return True
#             return helper(turtle.next, rabbit.next.next)
        
#         if head:
#             return helper(head, head.next)
        dict = {}
        curr = head
        while curr:
#           memory address of each of the nodes
            if hex(id(curr)) in dict:
                return True
            dict[hex(id(curr))] = True
            curr = curr.next
        return False