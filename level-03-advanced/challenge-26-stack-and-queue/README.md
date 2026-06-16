# Challenge 26: Stack and Queue

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 60 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- The Stack data structure (Last In, First Out — LIFO)
- The Queue data structure (First In, First Out — FIFO)
- How to implement abstract data types using Python classes
- When to use a stack vs. a queue in real applications

---

## Problem Description

**Stack:** Like a stack of plates. You add to the top and take from the top. The last item placed is the first one removed. (LIFO)

**Queue:** Like a queue of people. You join at the back and leave from the front. The first one in is the first one out. (FIFO)

You will implement both data structures from scratch using Python classes.

---

## Requirements

### Stack class
- [ ] `push(item)` — add item to the top
- [ ] `pop()` — remove and return top item; raise `IndexError` if empty
- [ ] `peek()` — return top item without removing; raise `IndexError` if empty
- [ ] `is_empty()` — return `True` if stack has no items
- [ ] `size()` — return number of items in the stack

### Queue class
- [ ] `enqueue(item)` — add item to the back
- [ ] `dequeue()` — remove and return front item; raise `IndexError` if empty
- [ ] `front()` — return front item without removing; raise `IndexError` if empty
- [ ] `is_empty()` — return `True` if queue has no items
- [ ] `size()` — return number of items in the queue

---

## Expected Behavior

```python
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()    # Returns: 3  (last in, first out)
stack.peek()   # Returns: 2
stack.size()   # Returns: 2
stack.is_empty()  # Returns: False

queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.dequeue()  # Returns: "a"  (first in, first out)
queue.front()    # Returns: "b"
queue.size()     # Returns: 2
```

---

## Hints

> **Hint 1:** Both can be implemented using a Python list internally (`self._items = []`).

> **Hint 2:** Stack uses `self._items.append(item)` for push and `self._items.pop()` for pop.

> **Hint 3:** Queue uses `self._items.append(item)` for enqueue and `self._items.pop(0)` for dequeue (remove from front).

> **Hint 4:** For `peek()` and `front()`: check `if self.is_empty(): raise IndexError(...)` first.

> **Hint 5:** `size()` is just `len(self._items)`.

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-26-stack-and-queue
pytest tests/ -v
```
