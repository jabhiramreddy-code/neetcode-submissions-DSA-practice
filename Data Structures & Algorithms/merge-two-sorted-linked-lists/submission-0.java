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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode res= new ListNode();
        ListNode ans = res;
        ListNode temp1 = list1;
        ListNode temp2 = list2;
        ListNode temp = null;
        if(temp1==null && temp2==null)return null;
        while(temp1!=null && temp2 !=null){
            if(temp1.val<=temp2.val){
                temp=temp1;
                temp1=temp1.next;
                temp.next=null;
                res.next=temp;
                res=res.next;
            }
            else{
                temp=temp2;
                temp2=temp2.next;
                temp.next=null;
                res.next=temp;
                res=res.next;
            }
        }
        if(temp1==null && temp2!=null){
            res.next=temp2;
        }
        else if(temp1!=null && temp2==null){
            res.next=temp1;
        }
        return ans.next;
    }
}