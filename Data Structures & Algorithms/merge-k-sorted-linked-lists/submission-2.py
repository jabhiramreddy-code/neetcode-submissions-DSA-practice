# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, head1,head2):
        temp = ListNode()
        node = temp
        while head1 != None and head2 != None:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
                node = node.next
            else:
                node.next = head2
                head2 = head2.next
                node = node.next
        if head1 != None:
            node.next = head1
        elif head2 != None:
            node.next = head2
        return temp.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        print(n)
        if n==0:
            print(n)
            return None
        m = len(lists)
        while m > 1:
            l, r, write = 0, m - 1, 0
            while l < r:
                lists[write] = self.merge(lists[l], lists[r])
                write += 1
                l += 1
                r -= 1
            if l == r:                       # odd middle element, carry it
                lists[write] = lists[l]
                write += 1
            m = write       
        return lists[0]
        