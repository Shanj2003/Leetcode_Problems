class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        for i in range(n):
            nums1[i+m]=nums2[i]
    
        nums1.sort()
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
merge(nums1,m,nums2,n)
