# -*- coding: utf-8 -*-
"""
TC : O(2^ N) where N is the number of elements in the array
SC : O(1) no extra space
"""

class Solution :    
    narrngement = 0
    def countArrangement(self,n):
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        self.permute(nums, 0)
        return self.narrngement
    
    def permute(self, nums : [], k : int):
        if k == len(nums):
            self.narrngement += 1
        for i in range(k,len(nums)):
            self.swap(nums, i, k);
            if nums[k] % (k + 1) == 0 or (k + 1) % nums[k] == 0:
                self.permute(nums, k + 1)
            self.swap(nums, i, k)
    def swap(self, nums:[],i : int,j : int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
       
    
S = Solution()
print(S.countArrangement(3))
