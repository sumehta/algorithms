def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        L = len(nums)
        for pos in range(L-2):
            if pos > 0 and nums[pos] == nums[pos-1]: # nums at two consecutive positions are the same continue continue else will lead to duplicates
                continue

            target = -nums[pos]

            i, j = pos+1, L-1

            while i < j:
                total = nums[i] + nums[j]
                if total < target:
                    i += 1
                elif total > target:
                    j -= 1
                else:
                    print([-target, nums[i], nums[j]])
                    ans.append([-target, nums[i], nums[j]])
                    i+=1
                    j-=1
                    while (nums[i] == nums[i-1]) and (i < L-1):  # increment the pointer if consecutive numbers same
                        i+=1
                    while (nums[j] == nums[j+1]) and (j > 1): # decrement the pointer if consecutive numbers same
                        j-=1

        return ans
