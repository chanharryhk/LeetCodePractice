# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        
        rabbit = turtle = pre
        while rabbit.next:
            if n:
                n -= 1
            else:
                turtle = turtle.next
            rabbit = rabbit.next
        
        turtle.next = turtle.next.next
        return pre.next