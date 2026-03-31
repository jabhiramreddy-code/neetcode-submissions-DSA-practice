class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);
            if(c==')' || c== '}' || c ==']'){
                if(stack.isEmpty())return false;
                if(c==')' && stack.peek()=='(')stack.pop();
                else if(c=='}' && stack.peek()=='{')stack.pop();
                else if(c==']' && stack.peek()=='[')stack.pop();
                else
                return false;
            }
            else{
                stack.push(c);
            }

        }
        if(stack.isEmpty())
        return true;
        return false;
    }
}
