class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x^y).bit_count()
        # print(result)
        # count = 0
        # for i in range(2,len(result)):
        #     if result[i] == '1':
        #         count += 1
        
        # return count