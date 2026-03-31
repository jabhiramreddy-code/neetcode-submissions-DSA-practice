class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> q=new PriorityQueue<>();
        for(int i:stones){
            q.offer(-i);
        }
        while(q.size()>1){
            int f=q.poll();
            int s=q.poll();
            int curr = f-s;
            if(s>f)
            q.offer(curr);
        }
        q.offer(0);
        return  Math.abs(q.peek());
    }
}
