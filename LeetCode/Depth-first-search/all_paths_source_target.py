"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

example1
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    #solution1: using iteration
        stack=[[0]]
        goal=len(graph)-1
        allPath=[]
        while len(stack)>0:
            newStack=[]
            for path in stack:
                if path[-1]==goal:
                    allPath.append(path)
                else:
                    for node in graph[path[-1]]:
                        newStack.append(path+[node])
            stack=newStack
        return allPath
        
     #solution2: using recursion   
        self.allPath=[]
        def find(path):
            for node in graph[path[-1]]:
                if node==len(graph)-1:
                    self.allPath.append(path+[node])
                find(path+[node])
        find([0])
        return self.allPath
