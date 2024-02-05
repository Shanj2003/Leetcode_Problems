class Solution(object):
    def removeElement(self, nums, val):
       
        
            i=len(nums)-1
            while i>=0:
                if nums[i] == val:
                    nums.pop(i)
                i -=1    
            return len(nums)
  
