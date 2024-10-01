# Definition for singly-linked list.
#Input: head = [1,1,2,3,3]
#Output: [1,2,3]


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head