# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # treat it like normal addition, carry forward the balance after each operation
        # result needs to be reversed, so we can append to the end of a list as we go
        ans = []
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            num = val1 + val2 + carry
            digit = num % 10
            carry = num // 10
            ans.append(digit)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        dummy = ListNode(0)
        curr = dummy
        for num in ans:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
