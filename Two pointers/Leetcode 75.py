# - Brute force approach 
#  Keep a count of all 0s 1s and 2s
#  accordigly map 0s 1s and 2s with the count of count0s, count1s and count2s
 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count1s , count2s , count0s = 0 , 0 , 0
        res = []
        for num in nums:
            if num == 0:
                count0s += 1
            elif num == 1:
                count1s += 1
            else:
                count2s += 1
        for i in range(count0s):
            res.append(0)
        for i in range(count1s):
            res.append(1)
        for i in range(count2s):
            res.append(2)

#  Better approach 
# - sort your array

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return nums.sorted()
    
# optimal approach
# - Dutch national flag algorithm
#  have low  , mid pointing to startIndex of the array and high on end index
#  when arr[mid] is 0 , swap arr[low] and arr[mid] and increment both by 1
#  when arr[mid] becomes 1 increment your mid pointer by one, no other changes done.
# if arr[mid] becomes 2 , swap arr[high] and arr[mid] decrease your high pointer by one
    

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low , mid , high = 0 , 0 , len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low] , nums[mid] = nums[mid] , nums[low]
                low+=1
                mid+=1
                
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -= 1
        return nums