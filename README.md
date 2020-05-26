**LeetCode**

1.[Two Sum](https://leetcode.com/problems/two-sum/?tab=Description)

Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

A simple solution is to sort the array. Keep two pointers to start and end of the array, increment and decrement the pointers respectively according to if the sum of the elements pointed is lesser or smaller than the target. If the pointers cross before the target is reached required elements don't exist. A simple time complexity analysis of this program will tell you that the time complexity is O(nlgn).

Can we do it O(n) by using extra space? Sure, here is the intuition. We obviously want to get away with sorting. Let's
traverse through the array. We must somehow keep track of the difference between the target and the current element. So while traversing first check if the difference between the target and the current element exists in the buffer if not store the current element as a key and it's index as value. If we encounter that the difference between the target and the current element is in the buffer that means we already encountered an array element that when paired with the current element would give us the target. We know the index of the current element and we have stored the index of the difference in the buffer. Return both indices. In the worst case this approach will occupy O(n) space and take O(n) time.

2.LinkedList

Defines a python LinkedList class as an iterator object.

Iterator objects in python conform to the iterator protocol, which basically means they provide two methods: `__iter__()` and  `next()`. The `__iter__` returns the iterator object and is implicitly called at the start of loops. The next() method returns the next value and is implicitly called at each loop increment.  next() raises a StopIteration exception when there are no more value to return, which is implicitly captured by looping constructs to stop iterating.

3. [3Sum](https://leetcode.com/problems/3sum/)

Key ideas - In an array sorted in the ascending order, with a target chosen while iterating from left to right, if target+a+b=0, this condition must hold true then a>target and b>target and target<0.

Based on this idea, first sort the array, fix a target while iterating and solve the two sum problem using two pointers for all elements greater than target, that is target position onwards.

Couple of optimizations -
1) While iterating the sorted array, if consecutive targets are the same, skip the computation the 2nd time, because it will lead to the same tuples.
2) While solving the 2sum problem if consecutive numbers at left position are equal increment the left pointer and if consecutive numbers at the right position are equal decrement the right pointer. This is because same numbers will lead to same answer pairs.

4. [3SumClosest](https://leetcode.com/problems/3sum-closest/submissions/)

Key ideas - Sort the array. Iterating from left to right fix numbers. For the rest of the array, check sum of all pairs along with the fixed number using left and right pointers. If the sum current sum is greater than target, since the array is sorted decrease the sum by decrementing the left pointer. If the current sum is less than the target, since the array is sorted, increase the sum by incrementing the left pointer. Keep track of the sum closest to the target by using an extra variable.
