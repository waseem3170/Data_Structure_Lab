class Node:
    """Represents an individual node in the Singly Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Custom Singly Linked List data structure."""
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, data):
        """Inserts a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print(f"Inserted '{data}' at head.")

    def insert_at_tail(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
        self.size += 1
        print(f"Inserted '{data}' at tail.")

    def insert_at_index(self, index, data):
        """Inserts a new node at a specified 0-based index position."""
        if index < 0 or index > self.size:
            print(f"Error: Index {index} out of bounds (valid range: 0 to {self.size}).")
            return False

        if index == 0:
            self.insert_at_head(data)
            return True
        if index == self.size:
            self.insert_at_tail(data)
            return True

        new_node = Node(data)
        current = self.head
        
        # Traverse to the node right before the insertion point
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1
        print(f"Inserted '{data}' at index {index}.")
        return True

    def delete_by_value(self, key):
        """Deletes the first node containing the matching target data key."""
        if self.head is None:
            print(f"Error: List is empty. Cannot delete '{key}'.")
            return False

        # Case 1: Target is at the head node
        if self.head.data == key:
            self.head = self.head.next
            self.size -= 1
            print(f"Successfully deleted node with key '{key}'.")
            return True

        # Case 2: Target is in the middle or end
        current = self.head
        while current.next and current.next.data != key:
            current = current.next

        if current.next is None:
            print(f"Key '{key}' not found in the list.")
            return False

        # Unlink the target node
        current.next = current.next.next
        self.size -= 1
        print(f"Successfully deleted node with key '{key}'.")
        return True

    def display(self):
        """Forward list traversal printing all live data links."""
        if self.head is None:
            print("List is empty: Head -> None")
            return

        current = self.head
        nodes = []
        while current:
            nodes.append(f"[{current.data}]")
            current = current.next

        print("Head -> " + " -> ".join(nodes) + " -> None")


def main():
    sll = SinglyLinkedList()

    print("=========================================================")
    print("SINGLY LINKED LIST (SLL) DEMONSTRATION")
    print("=========================================================\n")

    # 1. Insertion Demonstrations
    print("--- 1. Testing Insertion Methods ---")
    sll.insert_at_head(10)
    sll.insert_at_head(5)
    sll.insert_at_tail(30)
    sll.insert_at_index(2, 20)  # Insert 20 at index 2
    sll.insert_at_tail(40)
    sll.display()

    # 2. Deletion Demonstrations
    print("\n--- 2. Testing Key Deletion ---")
    sll.delete_by_value(5)   # Deleting Head
    sll.display()

    sll.delete_by_value(20)  # Deleting Middle node
    sll.display()

    sll.delete_by_value(40)  # Deleting Tail node
    sll.display()

    sll.delete_by_value(99)  # Non-existent key
    sll.display()


if __name__ == "__main__":
    main()
