# nums = [4,5,6,7,0,1,2 ,3], target = 2
def Search( self , nums , target ):
    start , end = 0 , len(nums)-1
    while start <= end:
        mid = ( start + end )//2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            # left array potion is sorted
            if target <= nums[mid] and target >= nums[start]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # right portion is sorted
            if nums[mid] <= target and nums[end] >= target:
                start = mid + 1
            else:
                end = mid - 1

    return -1
        
