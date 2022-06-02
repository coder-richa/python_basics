""" 
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False
    
    nodes = set()
    while head.next:
        if head in nodes:
            return True
        nodes.add(head)
        head = head.next
        
    return False     


def main():
    node4 = ListNode(4)
    node3 = ListNode(3)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2
    headNode = node1
    # node4.next =node2
    print(hasCycle(headNode))
    

if __name__ == '__main__':
    main()       