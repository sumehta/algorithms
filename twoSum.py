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
            if target-num in buff.keys():
                return sorted([i, buff[target-num]])
            else:
                buff[num] = i

        return []

    def threeSum(self, nums, target):
        for i,num in enumerate(nums):
            two_sum = self.twoSum(nums[0:nums.index(num)] + nums[nums.index(num)+1:], target-num)
            if two_sum:
                for k,idx in enumerate(two_sum):
                    if idx > nums.index(num):
                        two_sum[k]+=1

                two_sum.append(i)
                return sorted(two_sum)


if __name__ == '__main__':

    s = Solution()
    print s.twoSum([3,2,4], 6)
    print(s.threeSum([1,3,5,7,9,11,13,15], 29))
