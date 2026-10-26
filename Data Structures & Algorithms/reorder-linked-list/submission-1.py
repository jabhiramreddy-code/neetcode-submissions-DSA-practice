# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reversList(self, rev):
        n = None
        while rev != None:
            temp = rev
            rev = rev.next
            temp.next = n
            n = temp
        temp = n
        # while temp != None:
        #     print(temp.val)
        #     temp = temp.next
        return n
        


    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = l2 = head
        while l2.next != None and l2.next.next != None:
            l1 = l1.next
            l2 = l2.next.next
        rev = l1.next
        l1.next = None
        rev = self.reversList(rev)
        l1 = head
        while l1 != None and rev != None:
            prev = l1.next
            l1.next = rev
            rev = rev.next
            l1.next.next = prev
            l1 =  l1.next.next


        