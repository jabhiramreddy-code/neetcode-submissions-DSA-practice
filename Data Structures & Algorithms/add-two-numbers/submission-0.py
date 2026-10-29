# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l = ListNode()
        ans = l
        while l1 != None and l2 != None:
            temp = l1.val + l2.val + carry
            if temp > 9:
                carry = 1
                temp %= 10
            else:
                carry = 0
            l.next = ListNode(temp)
            l = l.next
            l1 = l1.next
            l2 = l2.next
        last = None
        if l1 != None:
            last = l1
        elif l2 != None:
            last = l2
        if last != None:
            while last != None:
                temp = last.val + carry
                if temp > 9:
                    carry = 1
                    temp %= 10
                else:
                    carry = 0
                l.next = ListNode(temp)
                l = l.next
                last = last.next
        if carry:
            l.next = ListNode(1)
        return ans.next
            

        