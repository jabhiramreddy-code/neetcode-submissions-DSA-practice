class Solution {
    public String minWindow(String s, String t) {
        Map<Character,Integer> count = new HashMap<>();
        Map<Character,Integer> window = new HashMap<>();
        for(int i=0;i<t.length();i++){
            count.put(t.charAt(i),count.getOrDefault(t.charAt(i),0)+1);
        }
        int have=0,tn=t.length(),sn=s.length();
        int i=0,min=sn+1,start=-1,end=-1;
        for(int j=0;j<sn;j++){
            window.put(s.charAt(j),window.getOrDefault(s.charAt(j),0)+1);
            if(window.get(s.charAt(j))==count.get(s.charAt(j))){
                have++;
            }
            while(have==count.size()){
                if(min>(j-i+1)){
                    min=j-i+1;
                    start=i;
                    end=j;
                }
                window.put(s.charAt(i),window.get(s.charAt(i))-1);
                if(count.containsKey(s.charAt(i)) && window.get(s.charAt(i))<count.get(s.charAt(i)))
                have--;
                i++;
            }
                System.out.println(have+" s "+i+" "+j);
        }
        if(min==sn+1)return "";
        return s.substring(start,end+1);
    }
}
