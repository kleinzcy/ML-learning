"""
一次遍历，用两个指针，left与right相隔n,当right.next为None的时候，left.next就是要删除的指针。 这里有两个特例，
[1]1，删除的元素是最后一个元素，那么left.next.next不存在，所以要判断left.next是否为None。
另一个【1,2】2，删除元素是头元素，这也是为什么left的初始值为None，如果初始值是head的话，那么就难以处理这个问题，
所以在最后删除节点的时候判断left是否为None。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        right = head
        left = None
        current = 0
        
        while(right.next!=None):
            right = right.next
            current += 1
            if current > n:
                left = left.next
            elif current==n:
                left = head
        
        if left==None:
            return head.next
        elif left.next == None:
            return []
        else:
            left.next = left.next.next
        
        return head
