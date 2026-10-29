"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        s = {}
        temp = head
        ans = prev = Node(0)
        while temp != None:
            l = Node(temp.val)
            prev.next= l
            s[temp] = l
            temp = temp.next
            prev = prev.next
        temp = head
        prev = ans.next
        while temp != None:
            if temp.random != None:
                prev.random = s[temp.random]         
            temp = temp.next
            prev = prev.next
        return ans.next


        

        