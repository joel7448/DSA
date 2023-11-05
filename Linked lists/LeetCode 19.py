def RemoveNthNodeFromEnd( head , n):
    left , right = head , head
    for i in range(n):
        right = right.next

    if not right:
        head.next

    while right.next:
        left = left.next
        right = right.next
    left.next = left.next.next 
     
    return head