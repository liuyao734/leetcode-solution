class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()  #创建了一个空集合seen,用来存储已经访问过的节点
        while head: #创建一个循环体，只要头节点head不为空则一直执行
            if head in seen:#如果当前节点head已经在seen集合中，意味着链表中存在环
                return True
            seen.add(head)
            head = head.next #将头节点移动到下一节点，继续遍历链表
        return False#如果遍历完整个链表都没有发现环，那么返回False