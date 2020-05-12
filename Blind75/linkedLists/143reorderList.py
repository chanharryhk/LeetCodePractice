# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        rabbit, turtle = head.next, head
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            
        second = turtle.next
        turtle.next = None
        
        rev = None
        while second:
            temp = second.next
            second.next = rev
            rev = second
            second = temp
        
        ans = tempAns = ListNode(0)
        count = 0
        while head or rev:
            if count % 2 == 0:
                ans.next = head
                head = head.next
                ans = ans.next
            else:
                ans.next = rev
                rev = rev.next
                ans = ans.next
            count += 1

        return ans.next