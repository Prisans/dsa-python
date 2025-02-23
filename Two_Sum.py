# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Solution -1


nums = [1,4,7]

# def two_sum(list,target):
#     for x, val1 in enumerate(list):
#         y=x+1
#         for y, val2 in enumerate(list):                       <------------My approach and it worked.
#             if x<len(list):
#                 if list[x]+list[y]==target:
#                     return x,y
#             else:
#                 return -1
# ans = two_sum(nums,11)
# print(ans)


# Solution - 2

# def twoSum(nums, target):
#     num_map = {}  # Dictionary to store numbers and their indices
    
#     for i, num in enumerate(nums):  # Loop through the array
#         complement = target - num  # Calculate the complement
        
#         if complement in num_map:  # Check if complement exists in dictionary
#             return [num_map[complement], i]  # Return indices of the two numbers
        
#         num_map[num] = i  # Store the number and its index in dictionary


# Iteration	num	complement = target - num	num_map Before	if complement in num_map?	Action
# 1st (i=0)	2	9 - 2 = 7	{} (empty)	❌ No	Store {2: 0} in num_map
# 2nd (i=1)	7	9 - 7 = 2	{2: 0}	✅ Yes, 2 exists!	Return [0, 1]
