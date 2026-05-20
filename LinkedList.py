# Step 1 — Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # points to nothing by default

# Step 2 — Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None   # empty list starts with no head

    # ── INSERT AT END ──────────────────────────────
    def append(self, data):
        new_node = Node(data)

        if self.head is None:       # list is empty
            self.head = new_node
            return

        current = self.head
        while current.next:         # walk to last node
            current = current.next
        current.next = new_node     # attach new node at end

    # ── PRINT THE LIST ─────────────────────────────
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" → ".join(elements) + " → None")

    # ── INSERT AT BEGINNING ────────────────────────
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head   # new node points to old head
        self.head = new_node        # new node becomes new head

    # ── DELETE A VALUE ─────────────────────────────
    def delete(self, data):
        if not self.head:
            return

        # If head itself needs to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # skip the node
                return
            current = current.next

    # ── SEARCH ─────────────────────────────────────
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    # ── LENGTH ─────────────────────────────────────
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# ── TEST IT ────────────────────────────────────────
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.display()          # 10 → 20 → 30 → 40 → None

ll.prepend(5)
ll.display()          # 5 → 10 → 20 → 30 → 40 → None

ll.delete(20)
ll.display()          # 5 → 10 → 30 → 40 → None

print(ll.search(30))  # 2
print(ll.length())    # 4
