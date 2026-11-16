# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev(self, head1):
        n = None
        while head1 != None:
            temp = head1
            head1 = head1.next
            temp.next = n
            n = temp
        return n
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = head
        last = False
        while temp != None:
            prev = ListNode()
            prev.next = temp
            temp1 = temp
            x = 0
            while temp != None and x < k:
                temp = temp.next
                prev = prev.next
                x += 1;
            prev.next = None
            if x != k:
                last=True
            arr.append(temp1)
        r = len(arr)
        if last:
            r -= 1
        for i in range(r):
            arr[i] = self.rev(arr[i])
        
        for i in range(len(arr)-1):
            temp=arr[i]
            while temp.next != None:
                temp = temp.next
            temp.next = arr[i+1]
        return arr[0]
                

            