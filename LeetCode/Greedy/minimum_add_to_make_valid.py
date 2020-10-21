"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.


Note:

S.length <= 1000
S only consists of '(' and ')' characters.
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        par=0
        count=0
        for char in S:
            if char=='(':
                par+=1
            if char==')':
                par-=1
            if par<0:
                count+=1
                par=0
        return count+par
