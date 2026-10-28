# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=1
        temp = head
        prev = ListNode()
        prev.next = head
        size = 0
        while temp != None:
            size += 1
            temp = temp.next
        temp = head
        n = size - n + 1
        if n == 1:
            return head.next
        while temp != None:
            if i == n-1:
                if temp.next != None:
                    temp.next = temp.next.next
                else:
                    prev.next = None
            i += 1
            temp = temp.next
            prev = prev.next
        return head
        