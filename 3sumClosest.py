 def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        L = len(nums)
        closest_so_far = 200000
        ans = 0

        for pos in range(L-2):
            fixed = nums[pos] # fixed number
            i, j = pos+1, L-1
            while i < j: # two sum iteration
                curr_sum = fixed+nums[i]+nums[j]
                if abs(target - curr_sum) < closest_so_far:
                    closest_so_far =  abs(target-curr_sum)
                    ans = curr_sum

                if  curr_sum > target: # if curr sum greater than target decrease the sum
                    j -=1
                    while (nums[j+1] == nums[j]) and j>1:
                        j-=1

                if curr_sum <target: # if curr sum less than target increase the sum
                    i +=1
                    while (nums[i] == nums[i-1]) and i<L-1:
                        i+=1

                if curr_sum == target: # curr sum same as target return the sum
                    return curr_sum
        return ans
