# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fl = 0
        while l1:
            fl = fl * 10 + l1.val
            l1 = l1.next
        sl = 0
        while l2:
            sl = sl * 10 + l2.val
            l2 = l2.next
        sl += fl
        st = str(sl)
        head = ListNode(st[0])
        tem = head
        for i in range(1, len(st)):
            tem.next = ListNode(st[i])
            tem = tem.next
        return head