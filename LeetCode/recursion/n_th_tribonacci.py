class Solution:
    def tribonacci(self, n: int) -> int:
        memory = [-1 for i in range(38)]
        memory[0] = 0
        memory[1] = 1
        memory[2] = 1
        for i in range(3,n+1):
            memory[i] = memory[i-1] + memory[i-2] + memory[i-3]
        return memory[n]
        
"""
restraint:  
  n<=37
  The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1
"""
