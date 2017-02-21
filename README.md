*LeetCode*

1.[Two Sum](https://leetcode.com/problems/two-sum/?tab=Description)

Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

A simple solution is to sort the array. Keep two pointers to start and end of the array, increment and decrement the pointers respectively according to if the sum of the elements pointed is lesser or smaller than the target. If the pointers cross before the target is reached required elements don't exist. A simple time complexity analysis of this program will tell you that the time complexity is O(nlgn).

Can we do it O(n) by using extra space? Sure, here is the intuition. We obviously want to get away with sorting.Let's
traverse through the array. We must somehow keep track of the difference between the target and the current element, its index really, and if this difference exists in the array awesome just return its index and the index of the current. So while traversing store the difference between the target and the current element 
in a dictionary as key and value is the index of the current element. This tells us that the key and element at index value
sum to target. Now if the next element we encounter is already present in the dictionary that means some previous element in
the array + current element equal to target.
