""" 
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    
    reversed_list_head, reversed_list_node = None, None
    while head:
        if reversed_list_node is None:
            reversed_list_node = ListNode(head.val)
            
        else:
            reversed_list_node = ListNode(head.val,reversed_list_node)
             
        reversed_list_head = reversed_list_node     
        head = head.next
    
    return reversed_list_head    
    

def main():
    # node7 = ListNode(16)
    # node6 = ListNode(15, node7)
    # node5 = ListNode(14, node6)
    # node4 = ListNode(6, node5)
    # node3 = ListNode(6, node4)
    # node2 = ListNode(2, node3)
    # node1 = ListNode(1, node2)
    # list1 = node1
    
    # node7 = ListNode(7)
    # node6 = ListNode(7, node7)
    # node5 = ListNode(7, node6)
    # node4 = ListNode(7, node5)
    # node3 = ListNode(7, node4)
    # node2 = ListNode(7, node3)
    # node1 = ListNode(7, node2)
    # list1 = node1
    
    node4 = ListNode(3)
    node3 = ListNode(2, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    list1 = node1
    list1 = reverse_linked_list(list1)
    while list1:
        print(list1.val)
        list1 = list1.next
    

if __name__ == '__main__':
    main()