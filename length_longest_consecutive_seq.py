from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # build a count dictionary. Could also use Counter
        count = defaultdict(int)
        for num in nums:
            if num not in count:
                count[num] += 1

        max_streak = 1

        for num in count:
            if num-1 not in count: # only compute the streak starting from this number if prev number not present
                curr_num = num
                while curr_num + 1 in count:
                    count[num] += 1
                    curr_num = curr_num + 1

                max_streak = max(count[num], max_streak)

        return max_streak
