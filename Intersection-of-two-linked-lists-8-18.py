class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB #初始化两个节点
        while A != B: #当满足A != B时，一直运行
            A = A.next if A else headB  #如果A的节点不为空，则运行下一个节点，如果为空，则指向B的头节点；
            B = B.next if B else headA #上同
        return A