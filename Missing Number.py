//Easy to understand
def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        a=[]
        m=0
        for i in range(length+1):
            a.append(i)
        for i in range(len(a)):
            if a[i] not in nums:
                m=a[i]
        return m

//Optimised code..
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
