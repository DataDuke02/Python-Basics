def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next    # save next before we overwrite
        current.next = prev         # reverse the arrow
        prev = current              # move prev forward
        current = next_node         # move current forward

    return prev   # prev is now the new head
