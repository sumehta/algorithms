class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        i, j = 0, 0  # i -> slow pointer, j -> fast pointer

        for j in range(len(nums)):
            if nums[j] != val:  # when j points to a valid element, push it to the front (i)
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return i
