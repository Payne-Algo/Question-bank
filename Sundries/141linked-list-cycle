# other
'''
use set Time O(1), Memory O(n)
'''
seen = set()
while head:
    if head in seen: 
        return True
    seen.add(head)
    head = head.next
# better Time O(1), Memory O(1)
if not head or not head.next: return False
# two pointer: slow and fast 
slow, fast = head, head.next
while head and fast and fast.next:
    if slow.next == fast.next: return True
    slow = slow.next
    fast = fast.next.next
return False 