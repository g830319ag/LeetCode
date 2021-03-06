#### 13. Roman to Integer ####
class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        output = 0
        for idx in range(len(s)):
            if idx>0 and sym[s[idx]]>sym[s[idx-1]]:
                output += sym[s[idx]] - 2*sym[s[idx-1]]
            else:
                output += sym[s[idx]]
        return output
