# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNextNumber(self, head, val):
        while head and head.val == val:
            head = head.next
        return head
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = head
        res = top
        headed = True
        while head and head.next:
            if head.val == head.next.val:
                if headed:
                    top = self.getNextNumber(head, head.val)
                    res = top
                    head = top
                else:
                    top.next = self.getNextNumber(head, head.val)
                    head = top.next
            else:
                head = head.next
                if not headed:
                    top = top.next
                headed = False
        return res