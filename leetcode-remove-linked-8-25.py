class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)  #创建一个哑巴节dummy,它的next属性指向头节点head。
        while cur.next:  #循环直到cur.next为None,即遍历整个链表
            if cur.next.val == val:  #如果cur.next指向的节点值等于val,则将cur.next指向该节点的下一个节点,然后删除当前节点;
                cur.next = cur.next.next
            else:
                cur = cur.next  #如果cur.next不等于val,则将cur移动到下一个节点
        return dummy.next  #返回哑节点dummy.next,他指向了删除所有的val值节点后的链表的头节点;