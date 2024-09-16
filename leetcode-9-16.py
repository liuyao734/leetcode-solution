 Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            tmp = cur.next  #暂存后继节点
            cur.next = pre   #修改next 引用指向
            pre = cur     # pre暂存cur
            cur = tmp     #cur访问下一节点
        return pre
    