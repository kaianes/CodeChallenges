'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''

#Solution

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        positionNumber = m  # Start after the initial m elements

        # Iterate over each element in nums2
        for j in range(n):
            value_nums2 = nums2[j]
            index_to_insert = positionNumber  # Assume insertion is after current nums1 elements
            
            # Find the position in nums1 where nums2[j] should be inserted
            for i in range(positionNumber):
                if nums1[i] > value_nums2:
                    index_to_insert = i
                    break

            # Insert the element from nums2 at the correct position in nums1
            nums1[index_to_insert:index_to_insert] = [value_nums2]
            positionNumber += 1  # Increase the effective length of nums1
            nums1.pop()  # Remove the last element to maintain correct length

