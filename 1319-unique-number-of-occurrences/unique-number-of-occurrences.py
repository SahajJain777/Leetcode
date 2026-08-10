class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 1 = 3, 2 = 2, 3 = 1 

        dic = {}
        l = []
        s = set()

        #dic
        for num in arr:
            dic[num] = dic.get(num,0) + 1
        
        #list
        for key,value in dic.items():
            l.append(value)

        
        for i in range(len(l)):
            s.add(l[i])
        
        return len(s) == len(l)

