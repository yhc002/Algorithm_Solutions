"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.


Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.


Constraints:

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic={}
        l=len(arr)
        for n in arr:
            if n not in dic.keys():
                dic[n]=1
            else:
                dic[n]+=1
        sortedDic={k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}

        count=0
        current=l
        for v in sortedDic.values():
            count+=1
            current-=v
            if current<=l/2:
                break
        
        return count
