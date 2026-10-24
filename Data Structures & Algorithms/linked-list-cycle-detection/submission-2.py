# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        prev = head
        while temp != None and prev != None:
            temp = temp.next
            if prev.next != None:
                prev = prev.next.next
            else:
                return False
            if temp == prev:
                return True
        return False
        