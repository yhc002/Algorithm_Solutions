def partitionLabels(self, S: str) -> List[int]:
  answer=[]
  cIdx={}
  for i in range(0,len(S)):
      if S[i] not in cIdx:
          cIdx[S[i]]=[i,i]
      else:
          cIdx[S[i]][1]=i
  check=0
  while check<len(S):
      end=cIdx[S[check]][1]
      for i in range(cIdx[S[check]][1]+1,len(S)):
          if cIdx[S[i]][0]<end:
              end=cIdx[S[i]][1]
      answer.append(end-check+1)
      check=end+1
  return answer
