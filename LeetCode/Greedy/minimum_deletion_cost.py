"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

Constraints:

  s.length == cost.length
  1 <= s.length, cost.length <= 10^5
  1 <= cost[i] <= 10^4
  s contains only lowercase English letters.
"""

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        idx=1
        prev=0
        total=0
        old_min=cost[0]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                if cost[i]>old_min:
                    total+=old_min
                    old_min=cost[i]
                else:
                    total+=cost[i]
            else:
                prev=s[i]
                old_min=cost[i]
        return total
