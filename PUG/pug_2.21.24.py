#USING BINARY SEARCH TO SEE IF TARGET NUMBER IS PART OF THE LIST

#given an array of integers nums which is sorted in ascending order, and an integer target function to search target in nums. If target exists, then return its index. Otherwise, return -1
# write algorithm

#Write an algorithm with O(log n) runtime complexity

# 1 way to approach it - but not efficient b/c have to go through the entire list - THEORETICAL PLAN
# def binary_search(nums, target):
#     for current_index, number in enumerate (nums):
#         if number == target:
#             return current index

#         return -1

#More efficient way - PLAN
#DECLARE FUNCTION and it takes 2 parameters (nums & target)

#SPLIT THE LIST SO YOU DON'T HAVE LOOP THROUGH EACH ONE - when you split, assume that list is sorted
#Look at the middle and see if that is the target - if it is, you can eliminate 1/2 of th list
#Example: 500s, want to see if 100 is there. Split list, pick a # - say 94. 
#100>94 = skip the first half of the list b/c 100 is not on that side
#Now that you have the right side of the list, split that in half again to see if you find the target #



#DECLARE FUNCTION and it takes 2 parameters (nums & target)
def binary_search(nums, target):
    left = 0  #this is the 1st position in the array (left side of list)
    right = len(nums) - 1 #this is the last position in the array - array length - 1 (right side of list)
    midpt = (left + right)//2  #this is how to get the midpoint of the list - // = floor divide function that rounds down the value so you don't get an odd # that's a float
    #if the midpoint is an odd # - then it will convert to a float b/c array only has discrete, whole integers
    while left <= right:  #need this b/c if the target # is not in the list, then the list will split and split until there is on1y 1 element/index. if left/right are the same index, then stop code 
        if nums[midpt] == target:  #if the element/index = target value, then return midpoint
            return midpt
        elif nums[midpt] < target: #else if the element/index < target value, then search the right 1/2 of the list by moving the left side of the list up to the midpoint
            left = midpt + 1  # have a new left value - shift left pointer up 
        else: #implied if nums[midpt] > target
            right = midpt - 1  # have a new right value - shift right pointer down
        midpt = (left + right) // 2  #repeat this formula so that you find the new midpoint 
    return -1 #will return -1 if the target value is not in the list


nums = [1,2,3,5,6,7,9]
print(binary_search(nums, 7))  #insert the nums and 7(target) argument
        
        
            
 
