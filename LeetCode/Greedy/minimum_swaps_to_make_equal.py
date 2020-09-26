"""
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Constraints:

  1 <= s1.length, s2.length <= 1000
  s1, s2 only contain 'x' or 'y'.
"""
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy=0 #s1=x,s2=y
        yx=0 #s1=y,s2=x
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i]=='x':
                    xy+=1
                else:
                    yx+=1
        if xy%2!=yx%2:
            return -1
        return math.ceil(xy/2)+math.ceil(yx/2)
