class Solution:
    def copyRandomList(self, head:"Node") -> 'Node':
        dummy = Node(-1)
        dummy.next = head
        cur = head

        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = head

        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = dummy
        new = head

        while old:
            cur.next = old.next
            cur = old
            old = cur.next
        return dummy.next

if __name__ == "__main__":





