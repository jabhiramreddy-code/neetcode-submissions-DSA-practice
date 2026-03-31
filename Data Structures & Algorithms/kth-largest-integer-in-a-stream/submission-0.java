class KthLargest {
    List<Integer> l=new ArrayList<>();
    int k;
    public KthLargest(int k, int[] nums) {
        this.k=k;
        for(int n:nums){
            l.add(n);
        }
    }
    
    public int add(int val) {
        l.add(val);
        Collections.sort(l);
        return l.get(l.size()-k);
    }
}
