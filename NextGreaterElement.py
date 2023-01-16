class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if not nums1 or not nums2:
            return []
        my={}
        stack=[nums2[0]]
        for i in range(1,len(nums2)):
            while (stack and nums2[i]> stack[-1]):
                my[stack.pop()]=nums2[i]
            stack.append(nums2[i])
        for key in stack:
            my[key]=-1
        return [my[key] for key in nums1]

