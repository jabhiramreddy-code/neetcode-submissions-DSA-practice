/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode checkHead= head;
        while(head!=null){
            if(checkHead.next==null)return false;
            else if(checkHead.next.next==null)return false;
            else if(head.next == checkHead.next.next) return true;
            head = head.next;
            checkHead=checkHead.next.next;
        }
        return false;
    }
}
