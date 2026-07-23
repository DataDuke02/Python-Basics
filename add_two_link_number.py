# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to act as the head of the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop while there are still nodes to process or a carry remains
        while l1 or l2 or carry:
            # Get values from current nodes, defaulting to 0 if list is finished
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum and update the carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
            
            # Append the new node to the result list
            current.next = ListNode(new_digit)
            current = current.next
            
            # Advance the list pointers if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
