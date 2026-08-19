class Node:
    """Represents an individual node in a Doubly Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Forward pointer
        self.prev = None  # Backward pointer


class DoublyLinkedList:
    """Custom Doubly Linked List data structure."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, data):
        """Inserts a new node at the head maintaining both pointers."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.size += 1
        print(f"Inserted '{data}' at head.")

    def insert_at_tail(self, data):
        """Inserts a new node at the tail maintaining both pointers."""
        new_node = Node(data)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1
        print(f"Inserted '{data}' at tail.")

    def insert_at_index(self, index, data):
        """Inserts a node at a specified index with forward/backward re-linking."""
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
        
        # Traverse to target insertion index
        for _ in range(index):
            current = current.next

        # Link new node between (current.prev) and (current)
        previous_node = current.prev
        
        new_node.next = current
        new_node.prev = previous_node
        previous_node.next = new_node
        current.prev = new_node

        self.size += 1
        print(f"Inserted '{data}' at index {index}.")
        return True

    def delete_by_value(self, key):
        """Deletes the first node matching key and properly re-links neighbor pointers."""
        if self.head is None:
            print(f"Error: List is empty. Cannot delete '{key}'.")
            return False

        current = self.head

        # Search for target key
        while current and current.data != key:
            current = current.next

        if current is None:
            print(f"Key '{key}' not found in the list.")
            return False

        # Case 1: Deleting the Head node
        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # List is now empty

        # Case 2: Deleting the Tail node
        elif current == self.tail:
            self.tail = current.prev
            self.tail.next = None

        # Case 3: Deleting a Middle node
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

        self.size -= 1
        print(f"Successfully deleted node with key '{key}'.")
        return True

    def display_forward(self):
        """Traverses and prints from head to tail."""
        if self.head is None:
            print("Forward Traversal: Head -> None")
            return

        current = self.head
        nodes = []
        while current:
            nodes.append(f"[{current.data}]")
            current = current.next

        print("Forward Traversal:  Head <-> " + " <-> ".join(nodes) + " <-> Tail")

    def display_reverse(self):
        """Reverse traversal printing nodes from tail back to head."""
        if self.tail is None:
            print("Reverse Traversal: Tail -> None")
            return

        current = self.tail
        nodes = []
        while current:
            nodes.append(f"[{current.data}]")
            current = current.prev  # Follow backward pointers

        print("Reverse Traversal:  Tail <-> " + " <-> ".join(nodes) + " <-> Head")


def main():
    dll = DoublyLinkedList()

    print("=========================================================")
    print("DOUBLY LINKED LIST (DLL) DEMONSTRATION")
    print("=========================================================\n")

    # 1. Insertion Operations
    print("--- 1. Testing Insertion & Pointer Creation ---")
    dll.insert_at_head(20)
    dll.insert_at_head(10)
    dll.insert_at_tail(40)
    dll.insert_at_index(2, 30)  # Insert 30 at index 2
    dll.insert_at_tail(50)

    # 2. Traversal Demonstrations
    print("\n--- 2. Forward & Reverse Traversals ---")
    dll.display_forward()
    dll.display_reverse()

    # 3. Deletion Operations (Re-linking Pointers)
    print("\n--- 3. Testing Deletion & Pointer Re-linking ---")
    dll.delete_by_value(10)  # Delete Head
    dll.display_forward()

    dll.delete_by_value(30)  # Delete Middle
    dll.display_forward()

    dll.delete_by_value(50)  # Delete Tail
    dll.display_forward()

    # 4. Final Reverse Traversal Verification
    print("\n--- 4. Verification via Reverse Traversal ---")
    dll.display_reverse()


if __name__ == "__main__":
    main()
