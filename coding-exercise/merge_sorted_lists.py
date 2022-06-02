""" 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    if list1 is None:
        return list2
    
    if list2 is None:
        return list1
    
    merged_head = None
    if list1.val < list2.val:
        merged_head = list1
        merged_head.next = merge_two_lists(list1.next, list2)
    else:
        merged_head = list2
        merged_head.next = merge_two_lists(list1, list2.next)
        
    return merged_head


def main():
    node3 = ListNode(4)
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2
    list1 = node1
    
    node3 = ListNode(4)
    node2 = ListNode(3)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2
    list2 = node1
    
    merged_head = merge_two_lists(list1, list2)
    while merged_head:
        print(merged_head.val)
        merged_head = merged_head.next
    

if __name__ == '__main__':
    main()