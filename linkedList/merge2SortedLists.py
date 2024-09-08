#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = current = ListNode(0) # type: ignore
        while l1 and l2:
            if l1.val < l2.val:
                current.next =l1
                l1=l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next =l1 or l2
        return dummy.next
        
#dummy.next points to the start of the merged list.

#current points to the end of the merged list after merging.

#Returning dummy.next ensures that the merged list starts with the first real node and not the dummy node.

