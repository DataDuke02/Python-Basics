def merge_sorted_lists(l1, l2):
    dummy = Node(0)       # dummy head makes logic cleaner
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # attach remaining nodes
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next   # skip the dummy node

