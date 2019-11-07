def maxProfit(self, prices):
  """
  :type prices: List[int]
  :rtype: int
  """
  profit=0
  if len(prices)==0:
      return profit
  maxPrice=prices[0]
  minPrice=prices[0]
  
  for i in range(1,len(prices)):
      if prices[i]<minPrice:
          if profit<maxPrice-minPrice:
              profit=maxPrice-minPrice
          minPrice=prices[i]
          maxPrice=prices[i]
      elif prices[i]>maxPrice:
          maxPrice=prices[i]
  if profit<maxPrice-minPrice:
      profit=maxPrice-minPrice
  return profit
