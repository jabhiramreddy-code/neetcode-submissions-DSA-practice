# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        n = temp
        n = n.next
        prev = head
        while prev != None:
            temp = prev
            prev = prev.next
            temp.next = n
            n = temp
        return n

        