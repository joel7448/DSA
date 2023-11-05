def PreviousGreaterElement( nums ):
    stack = [0]
    res = [-1] * len(nums)
    for i in range(len(nums)-1 , -1, -1 ):
        while stack and nums[stack[-1]] <= nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    while stack:
        res[stack.pop()] = -1
    return res



