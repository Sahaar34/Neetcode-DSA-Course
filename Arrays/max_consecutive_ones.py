# Leetcode 485 Max Consecutive Ones 
# Difficulty: Easy 

# Problem Description:
# Given a binary array nums, return the maximum number of consecutive 1s in the array.
# A binary array contains only 0s and 1s.



def findMaxConsecutiveOnes(nums: list[int]) -> int:
    count_rn = 0
    max_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count_rn += 1

            if count_rn > max_count:
                max_count = count_rn


        else:
            count_rn = 0
    return max_count 


# Test Cases:
nums1 = [1, 1, 0, 1, 1, 1]  # 3
nums2 = [1, 0, 1, 1, 0, 1]  # 2

print(findMaxConsecutiveOnes(nums1))

print(findMaxConsecutiveOnes(nums2))

# Time Complexity: O(n) I traverse the array once 
# Space Complexity: O(1) Im only using two variables 


# Side Notes:
# This function finds the longest consecutive sequence of 1s 
# by scanning the list once. It resets the current streak when it sees a 0.

# count_rn tracks the current streak, while max_count stores the largest streak found.
# The time compexity is O(n) and the space complexitty is O(1)