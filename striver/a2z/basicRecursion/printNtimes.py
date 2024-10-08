class Solution:
    def printGfg(self, n):
        if n == 0:
            return
        else:
            print('Kai', end=' ')
            self.printGfg(n-1)

hud = Solution()
hud.printGfg(19)