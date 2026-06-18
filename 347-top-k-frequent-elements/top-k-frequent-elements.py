class Solution(object):
    def topKFrequent(self, nums, k):
        #Storing the frequencies in the freq of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1


        #creating buckets which will have frequencies maping numbers
        buckets = [[] for _ in range (len (nums) +1)]

        for num, count in freq.items():
            buckets[count].append(num)


        #extraction of k element 
        result = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
