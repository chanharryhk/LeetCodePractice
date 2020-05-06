# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
#         currNode = head
#         nextNode = None

#         while currNode:
#             tempNext = currNode.next
#             currNode.next = nextNode
#             nextNode = currNode
#             currNode = tempNext
        
#         return nextNode

        def helper(head, next) -> ListNode:
            if head:
                temp = head.next
                head.next = next
                return helper(temp, head)
            else:
                return next
        
        return helper(head, None)
        