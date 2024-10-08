class Solution:    
    #Complete this function
    def printNos(self,n):
        if n == 0:
            return
        else:
            self.printNos(n-1)
            print(n, end=' ')
sol = Solution()
sol.printNos(100) # 1 2 3 4 5 6 7 8 9 10