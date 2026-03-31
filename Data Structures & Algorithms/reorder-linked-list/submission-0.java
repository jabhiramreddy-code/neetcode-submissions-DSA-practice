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
    public void reorderList(ListNode head) {
        int n=0;
        ListNode temp=head.next;
        ListNode res=head;
        ListNode firstHalf= head;
        
        while(temp!=null && temp.next!=null){
            temp=temp.next.next;
            firstHalf=firstHalf.next;
        }
        ListNode secondHalf=firstHalf.next;
        firstHalf.next=null;
        ListNode rev=null;
        while(secondHalf!=null){
            ListNode tempS=secondHalf;
            secondHalf=secondHalf.next;
            tempS.next=rev;
            rev=tempS;
        }

        temp=head;
        while(temp!=null && rev!=null){
            ListNode tempP=temp.next;
            temp.next=rev;
            rev=rev.next;
            temp.next.next=tempP;
            temp=temp.next.next;
        }
        
    //    System.out.println(rev.val);

    }
}
