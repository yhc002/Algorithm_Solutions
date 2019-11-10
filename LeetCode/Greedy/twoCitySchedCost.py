def twoCitySchedCost(self, costs: List[List[int]]) -> int:
  costs.sort(key=lambda c: c[1] - c[0])
  # first N going to city B, second N going to city A
  total = 0;
  n = len(costs)//2
  for i in range(2*n):
      if i < n:
          total += costs[i][1]
      else:
          total += costs[i][0]
  return total
