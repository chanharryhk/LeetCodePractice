
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rabbit = turtle = head
        
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            turtle = turtle.next

        rev = None
        while turtle:
            temp = turtle.next
            turtle.next = rev
            rev = turtle
            turtle = temp
        
        
        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
            
        return True
            