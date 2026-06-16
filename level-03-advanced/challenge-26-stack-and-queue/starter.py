class Stack:
    """
    TODO:
    Implement a Stack data structure (Last In, First Out — LIFO).

    A stack works like a stack of plates:
    - You can only add (push) to the top
    - You can only remove (pop) from the top
    - The most recently added item comes out first

    Internal storage: use a list called self._items = []

    Methods to implement:
        push(item)   — add item to the top
        pop()        — remove and return the top item
        peek()       — return the top item WITHOUT removing it
        is_empty()   — return True if the stack has no items
        size()       — return the number of items
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        """
        TODO: Add item to the top of the stack.

        Example:
            stack = Stack()
            stack.push(1)
            stack.push(2)
            stack.push(3)
            # stack now has [1, 2, 3], with 3 on top

        Hint: self._items.append(item)
        """
        pass

    def pop(self):
        """
        TODO: Remove and return the top item from the stack.
        If the stack is empty, raise IndexError("Stack is empty").

        Example:
            stack.push(1); stack.push(2)
            stack.pop()  → 2  (most recently added)
            stack.pop()  → 1

        Hint:
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self._items.pop()
        """
        pass

    def peek(self):
        """
        TODO: Return the top item WITHOUT removing it.
        If the stack is empty, raise IndexError("Stack is empty").

        Example:
            stack.push(1); stack.push(2)
            stack.peek()  → 2  (doesn't change the stack)
            stack.size()  → 2  (still 2 items)

        Hint: return self._items[-1]
        """
        pass

    def is_empty(self):
        """
        TODO: Return True if the stack has no items, False otherwise.

        Example:
            stack = Stack()
            stack.is_empty()  → True
            stack.push(1)
            stack.is_empty()  → False

        Hint: return len(self._items) == 0
        """
        pass

    def size(self):
        """
        TODO: Return the number of items currently in the stack.

        Example:
            stack.push(1); stack.push(2)
            stack.size()  → 2

        Hint: return len(self._items)
        """
        pass


class Queue:
    """
    TODO:
    Implement a Queue data structure (First In, First Out — FIFO).

    A queue works like a line of people:
    - You join (enqueue) at the BACK
    - You leave (dequeue) from the FRONT
    - The first one in is the first one out

    Internal storage: use a list called self._items = []

    Methods to implement:
        enqueue(item) — add item to the back
        dequeue()     — remove and return the front item
        front()       — return the front item WITHOUT removing it
        is_empty()    — return True if the queue has no items
        size()        — return the number of items
    """

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """
        TODO: Add item to the BACK of the queue.

        Example:
            queue.enqueue("a")
            queue.enqueue("b")
            # queue: ["a", "b"], "a" is at the front

        Hint: self._items.append(item)
        """
        pass

    def dequeue(self):
        """
        TODO: Remove and return the FRONT item from the queue.
        If the queue is empty, raise IndexError("Queue is empty").

        Example:
            queue.enqueue("a"); queue.enqueue("b")
            queue.dequeue()  → "a"  (first in, first out)
            queue.dequeue()  → "b"

        Hint: return self._items.pop(0)  ← pop from index 0 removes the first item
        """
        pass

    def front(self):
        """
        TODO: Return the FRONT item WITHOUT removing it.
        If the queue is empty, raise IndexError("Queue is empty").

        Hint: return self._items[0]
        """
        pass

    def is_empty(self):
        """
        TODO: Return True if the queue is empty, False otherwise.
        """
        pass

    def size(self):
        """
        TODO: Return the number of items in the queue.
        """
        pass
