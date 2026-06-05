# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #well from the head we don't know the length of the list
        #easy solution is just traverse list once to get list length
        #then traverse again and once we hit the spot we want do the cut there
        list_len = 0
        node = head
        while node:
            node = node.next
            list_len += 1

        i = 0
        node = head
        prev_node = None
        while node:
            if i == list_len - n:
                if not prev_node:
                    head = node.next
                else:
                    prev_node.next = node.next 
            i += 1
            prev_node = node
            node = node.next

        

        return head
