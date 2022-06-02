"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def remove_elements_from_linked_list(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head is None:
        return None
    
    if head.val == val:
        return remove_elements_from_linked_list(head.next, val)
    
    current = head
    prev = None
    
    while current:  
        # print("current ",current.val)      
        if current.val == val:
            prev.next = current.next
        else:
            prev = current 
        current = current.next
    
    return head    
    

def main():
    # node7 = ListNode(6)
    # node6 = ListNode(5, node7)
    # node5 = ListNode(4, node6)
    # node4 = ListNode(3, node5)
    # node3 = ListNode(6, node4)
    # node2 = ListNode(2, node3)
    # node1 = ListNode(1, node2)
    # list1 = node1
    
    node7 = ListNode(7)
    node6 = ListNode(7, node7)
    node5 = ListNode(7, node6)
    node4 = ListNode(7, node5)
    node3 = ListNode(7, node4)
    node2 = ListNode(7, node3)
    node1 = ListNode(7, node2)
    list1 = node1
    
    # node4 = ListNode(1)
    # node3 = ListNode(2, node4)
    # node2 = ListNode(2, node3)
    # node1 = ListNode(1, node2)
    # list1 = node1
    list1 = remove_elements_from_linked_list(list1, 7)
    while list1:
        print(list1.val)
        list1 = list1.next
    

if __name__ == '__main__':
    main()