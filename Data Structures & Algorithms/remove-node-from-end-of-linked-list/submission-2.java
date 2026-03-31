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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length=0;
        ListNode temp=head;
        while(temp!=null){
            length++;
            temp=temp.next;
        }
        if(length==1)return null;
        int removeIndex=length-n;
        temp=head;
        ListNode prev=new ListNode();
        prev.next=head;
        head=prev;
        while(removeIndex>0){
            temp=temp.next;
            prev=prev.next;
            removeIndex--;
        }
        prev.next=temp.next;
        System.out.println(temp.val+" "+prev.val);
        return head.next;
    }
}
