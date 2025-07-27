class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self):
        while True:
            # Create new node
            new_node = Node(int(input("Enter data: ")))
            
            # If list is empty, make new node the head
            if self.head is None:
                self.head = new_node
                temp = self.head
            else:
                # Add to end of list
                temp.next = new_node
                temp = new_node
            
            # Ask if user wants to continue
            choice = int(input("Do you want to continue (0, 1)? "))
            if choice == 0:
                break
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Usage example
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node()
    print("Linked List contents:")
    ll.display()