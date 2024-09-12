# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next: #head
            if curr.next.val == val: #head.val == val
                curr.next = curr.next.next #head = head.next
            else:
                curr = curr.next #dummy = head
        return dummy.next
            
        