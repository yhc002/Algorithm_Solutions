"""
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.

Constraints:

1 <= numBottles <= 100
2 <= numExchange <= 100
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        total = 0
        while numBottles>0:
            total+=numBottles
            empty+=numBottles
            numBottles=int(empty/numExchange)
            empty=empty%numExchange
        return total
