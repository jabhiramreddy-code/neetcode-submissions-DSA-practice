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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==0)return null;
        ListNode res=lists[0];
        for(int i=1;i<lists.length;i++){
            res=mergeTwo(res,lists[i]);
            
        }
        return res;
    }
    public ListNode mergeTwo(ListNode res,ListNode l){
        ListNode temp=new ListNode();
        ListNode ans=temp;
        while(res!=null && l!=null){
            if(res.val<=l.val){
                temp.next=res;
                res=res.next;
            }
            else{
                temp.next=l;
                l=l.next;
            }
            temp=temp.next;
        }
        if(res!=null){
            temp.next=res;
        }
        else if (l!=null)
            temp.next=l;

        return ans.next;

    }
}
