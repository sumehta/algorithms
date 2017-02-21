from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff = {}
        for i,num in enumerate(nums):
            if num in buff.keys():
                return sorted([i, buff[num]])
            else:
                buff[target-num] = i

        return []

if __name__ == '__main__':

    s = Solution()
    print s.twoSum([3,2,4], 6)
