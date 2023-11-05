def NextGreaterElement( self , nums ):
    # Monotonically increasing stack
    stack = [ 0 ]
    res = [-1] *len(nums)
    for i in range( 1 , len(nums) ):
        while stack and nums[stack[-1]] <= nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    while stack:
        res[stack.pop()] = -1
    return res



