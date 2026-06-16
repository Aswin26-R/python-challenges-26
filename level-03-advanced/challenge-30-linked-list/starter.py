class Node:
    """
    TODO:
    A single node in the linked list.
    Each node stores a value and a reference to the next node.

    Attributes:
        value — the data stored in this node
        next  — the next Node, or None if this is the last node
    """

    def __init__(self, value):
        # TODO: Store self.value = value and self.next = None
        pass


class LinkedList:
    """
    TODO:
    A singly linked list.

    The list has a self.head attribute pointing to the first Node.
    If the list is empty, self.head is None.
    """

    def __init__(self):
        self.head = None

    def append(self, value):
        """
        TODO:
        Add a new node with value to the END of the list.

        Example:
            ll = LinkedList()
            ll.append(1)
            ll.append(2)
            ll.append(3)
            ll.to_list()  → [1, 2, 3]

        Algorithm:
            new_node = Node(value)
            If list is empty (self.head is None):
                self.head = new_node
            Else:
                Traverse to the last node (where current.next is None)
                Set last_node.next = new_node
        """
        pass

    def prepend(self, value):
        """
        TODO:
        Add a new node with value to the BEGINNING of the list.

        Example:
            ll.append(2); ll.append(3)
            ll.prepend(1)
            ll.to_list()  → [1, 2, 3]

        Algorithm:
            new_node = Node(value)
            new_node.next = self.head   ← new node points to old head
            self.head = new_node        ← new node becomes the head
        """
        pass

    def delete(self, value):
        """
        TODO:
        Remove the FIRST node that has the given value.
        If the value is not found, do nothing.

        Example:
            ll = [1, 2, 3, 2]
            ll.delete(2)
            ll.to_list()  → [1, 3, 2]  (only first 2 removed)

        Algorithm:
            Handle case where head has the value:
                self.head = self.head.next

            Otherwise, traverse with prev and current:
                prev = self.head
                current = self.head.next
                while current is not None:
                    if current.value == value:
                        prev.next = current.next  ← skip over current
                        return
                    prev = current
                    current = current.next
        """
        pass

    def contains(self, value):
        """
        TODO:
        Return True if the list contains a node with the given value, False otherwise.

        Example:
            ll = [1, 2, 3]
            ll.contains(2)   → True
            ll.contains(99)  → False

        Hint: Traverse the list and check each node's value.
        """
        pass

    def to_list(self):
        """
        TODO:
        Return all values in the linked list as a regular Python list.

        Example:
            ll = [1, 2, 3]
            ll.to_list()  → [1, 2, 3]

        Hint:
            result = []
            current = self.head
            while current is not None:
                result.append(current.value)
                current = current.next
            return result
        """
        pass

    def length(self):
        """
        TODO:
        Return the number of nodes in the list.

        Hint: Traverse and count, or use len(self.to_list()).
        """
        pass

    def reverse(self):
        """
        TODO:
        Reverse the order of nodes IN PLACE.
        The head becomes the tail and vice versa.

        Example:
            ll = [1, 2, 3]
            ll.reverse()
            ll.to_list()  → [3, 2, 1]

        Algorithm (three-pointer technique):
            prev = None
            current = self.head

            while current is not None:
                next_node = current.next   ← save next before we overwrite it
                current.next = prev        ← reverse the pointer
                prev = current             ← move prev forward
                current = next_node        ← move current forward

            self.head = prev   ← prev is now the new head
        """
        pass
