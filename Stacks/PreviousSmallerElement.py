def previous_smaller_element(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)-1,-1,-1):
        while stack and nums[i] < nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    while stack:
        result[stack.pop()] = -1
    return result

# Example usage
print(previous_smaller_element([4, 8, 5, 2, 25]))
