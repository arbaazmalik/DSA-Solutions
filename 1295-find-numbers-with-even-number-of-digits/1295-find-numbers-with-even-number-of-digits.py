class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            r=0
            while num>0:
             num=num//10
             r+=1
            if (r%2==0):
             count+=1
        return count


        