"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    
    last_value = head.val

    prev = head
    current = head.next

    while current:  
        # print("current ",current.val)      
        if current.val == last_value:
            prev.next = current.next
        else:
            last_value = current.val
            prev = current 
        current = current.next
    
    return head    
    

def main():
    node7 = ListNode(16)
    node6 = ListNode(15, node7)
    node5 = ListNode(14, node6)
    node4 = ListNode(6, node5)
    node3 = ListNode(6, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    list1 = node1
    
    # node7 = ListNode(7)
    # node6 = ListNode(7, node7)
    # node5 = ListNode(7, node6)
    # node4 = ListNode(7, node5)
    # node3 = ListNode(7, node4)
    # node2 = ListNode(7, node3)
    # node1 = ListNode(7, node2)
    # list1 = node1
    
    # node4 = ListNode(1)
    # node3 = ListNode(2, node4)
    # node2 = ListNode(2, node3)
    # node1 = ListNode(1, node2)
    # list1 = node1
    list1 = delete_duplicates(list1)
    while list1:
        print(list1.val)
        list1 = list1.next
    

if __name__ == '__main__':
    main()