class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # might be helpful to know how many bananas there are
        # in total, so sum the piles. if sum < h, k = 1
        # if sum > h, do (sum // h) + 1 -> (10 // 9 = 1) + 1 = 2
        # 

        # from a binary search perspective, we need to find the
        # ends of the array that we are going to shorten in log(n)
        # left pointer can be one and right pointer can be max(piles)
        # from there, we can try to see if the value of k at mid 
        # point gets us through all the piles with any hours left 
        # if there are more hours left then we move left pointer
        # can use floor division to enforce the rule of 1 pile
        # per 1 hour allocation

        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(float(piles[i]) / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            elif hours > h:
                l = k + 1
        
        return res

        