def minFallingPathSum(self, A: List[List[int]]) -> int:
  minVal=[A[0]]
  for i in range(1,len(A)):
      row=[]
      for j in range(0,len(A[0])):
          if j==0:
              row.append(A[i][j]+min(minVal[i-1][j],minVal[i-1][j+1]))
          elif j<len(A[0])-1:
              row.append(A[i][j]+min(minVal[i-1][j-1],minVal[i-1][j],minVal[i-1][j+1]))
          else:
              row.append(A[i][j]+min(minVal[i-1][j-1],minVal[i-1][j]))
      minVal.append(row)
  return min(minVal[len(A)-1])
