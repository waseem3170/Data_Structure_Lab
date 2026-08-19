import sys

class ArrayDatabase:
    def __init__(self, capacity=100):
        # Initialize internal storage with a fixed capacity
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0  # Tracks actual number of elements stored

    def insert_at(self, index, value):
        """Inserts value at specified index, shifting trailing elements right."""
        if self.size >= self.capacity:
            print("Error: Array capacity full. Cannot insert.")
            return False

        if index < 0 or index > self.size:
            print(f"Error: Invalid index. Must be between 0 and {self.size}.")
            return False

        # Shift elements to the right from the end down to the target index
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1
        print(f"Successfully inserted {value} at index {index}.")
        return True

    def delete_at(self, index):
        """Deletes element at specified index, shifting trailing elements left."""
        if self.size == 0:
            print("Error: Array is empty. Nothing to delete.")
            return False

        if index < 0 or index >= self.size:
            print(f"Error: Invalid index. Must be between 0 and {self.size - 1}.")
            return False

        removed_value = self.data[index]

        # Shift elements to the left from target index up to size - 1
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None  # Clear trailing entry
        self.size -= 1
        print(f"Successfully deleted {removed_value} from index {index}.")
        return True

    def search_sequential(self, target):
        """Performs linear search to find first index match for target."""
        for i in range(self.size):
            if self.data[i] == target:
                return i
        return -1

    def display(self):
        """Displays current elements and active size."""
        current_elements = self.data[:self.size]
        print(f"\nCurrent Array (Size: {self.size}/{self.capacity}): {current_elements}")


def main():
    db = ArrayDatabase(capacity=100)

    while True:
        db.display()
        print("\n--- Structural Actions Menu ---")
        print("1. Insert Element")
        print("2. Delete Element")
        print("3. Sequential Search")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            try:
                val = float(input("Enter numeric value to insert: "))
                idx = int(input(f"Enter target index (0 to {db.size}): "))
                db.insert_at(idx, val)
            except ValueError:
                print("Error: Invalid numeric input.")

        elif choice == '2':
            if db.size == 0:
                print("Array is empty.")
                continue
            try:
                idx = int(input(f"Enter target index to delete (0 to {db.size - 1}): "))
                db.delete_at(idx)
            except ValueError:
                print("Error: Invalid index input.")

        elif choice == '3':
            if db.size == 0:
                print("Array is empty.")
                continue
            try:
                target = float(input("Enter numeric value to search: "))
                found_index = db.search_sequential(target)
                if found_index != -1:
                    print(f"Match found! Value {target} first occurs at index {found_index}.")
                else:
                    print(f"Value {target} not found in the array.")
            except ValueError:
                print("Error: Invalid numeric input.")

        elif choice == '4':
            print("Exiting application.")
            sys.exit(0)

        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
