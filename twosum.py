
class Solution:
    def twoSum(self,nums:list(int),target:int)->list[int]:
        hash={} #to store val,index
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hash:
                return [hash[diff],i]
            
            hash[i]=n
