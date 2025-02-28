s = "ach"
t = "ahbgdc"

def findSequence(s,t):
    count = 0
    for x in s:
        for y in t:
            if x in y:
                count+=1
    
    if count == len(s):                   
        return True
    else:
        return False

ans = findSequence(s,t)
print(ans)

# this solution is true and runs every test cases but there is a catch -> A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# thats why it is not the optimal solution,  but great try.


class Solution(object):
    def isSubsequence(self, s, t):
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        
        if i == len(s):
            return True     # return i == len(s) <- can do also
        else:
            return False
