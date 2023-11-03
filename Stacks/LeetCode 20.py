def isValid(self , s : str) -> bool:
    hashMap = { '}' : '{' , ']' : '[' , ')' : '(' }
    stack = []
    for paranthesis in s:
        if paranthesis not in hashMap:
            stack.append(paranthesis)
            continue
        if not stack or stack[-1] != hashMap[paranthesis]:
            return False
        stack.pop()
    return not stack
