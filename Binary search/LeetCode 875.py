class Solution:
    def totalBananasEaten(self,piles,h,mid):
        TimeTaken = 0
        for i in piles:
            TimeTaken += math.ceil( i / mid )
        if h >= TimeTaken:
            return True
        return False
        
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        start , end = 1 , max(piles)
        while start < end:
            mid = ( start + end )//2
            if self.totalBananasEaten( piles , h , mid ):
                end = mid 
            else:
                start = mid + 1
        return start