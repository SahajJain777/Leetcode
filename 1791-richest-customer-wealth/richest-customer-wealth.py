class Solution(object):
    def maximumWealth(self, accounts):
        maxsum = 0
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[0])):
                sum = sum + accounts[i][j]
            if(maxsum<sum): maxsum = sum
        return maxsum

        