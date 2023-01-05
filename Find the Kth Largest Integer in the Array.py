class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        maxnum=[-int(i) for i in nums]
        heapq.heapify(maxnum)
        while k>1:
            heapq.heappop(maxnum)
            k-=1
        return str(-maxnum[0])
