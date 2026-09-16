class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i < j and i < len(s) and j>=0:
            while i < len(s) and not ((ord(s[i]) >=ord('A') and ord(s[i]) <=ord('Z')) or 
                    (ord(s[i]) >=ord('a') and ord(s[i]) <=ord('z')) or 
                    (ord(s[i]) >=ord('0') and ord(s[i]) <=ord('9')))  :
                i += 1
            while j>=0 and not ((ord(s[j]) >=ord('A') and ord(s[j]) <=ord('Z')) or 
                    (ord(s[j]) >=ord('a') and ord(s[j]) <=ord('z')) or 
                    (ord(s[j]) >=ord('0') and ord(s[j]) <=ord('9'))):
                j -= 1
            if i < len(s) and j>=0 and s[i].lower() != s[j].lower():
                return False
            i += 1;
            j -= 1;

        return True