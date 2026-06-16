# Challenge 30: Linked List

**Level:** 3 – Advanced Python
**Difficulty:** ⭐⭐⭐ (Advanced)
**Estimated Time:** 70 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What a linked list is and how it differs from a Python list
- How to create and use Node objects
- How to traverse a linked list
- How to insert and delete nodes

---

## Problem Description

A **linked list** is a data structure where each element (node) contains a value and a reference (pointer) to the next node. Unlike Python lists (which store items in contiguous memory), linked lists connect nodes via pointers.

```
[1] → [2] → [3] → [4] → None
```

---

## Requirements

### Node class
- `__init__(value)` — stores value and `next = None`

### LinkedList class
- [ ] `append(value)` — add value to the end
- [ ] `prepend(value)` — add value to the beginning
- [ ] `delete(value)` — remove first node with this value
- [ ] `contains(value)` — return `True` if value exists
- [ ] `to_list()` — return all values as a Python list
- [ ] `length()` — return the number of nodes
- [ ] `reverse()` — reverse the order of nodes in place

---

## Expected Behavior

```python
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.to_list()    # Returns: [1, 2, 3]
ll.length()     # Returns: 3

ll.prepend(0)
ll.to_list()    # Returns: [0, 1, 2, 3]

ll.delete(2)
ll.to_list()    # Returns: [0, 1, 3]

ll.contains(1)  # Returns: True
ll.contains(99) # Returns: False

ll.reverse()
ll.to_list()    # Returns: [3, 1, 0]
```

---

## How Nodes Work

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None   # pointer to the next node

# Building: 1 → 2 → 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
# now node1.next.next.value == 3
```

---

## Traversal Pattern

```python
current = self.head
while current is not None:
    print(current.value)
    current = current.next
```

---

## Hints

> **Hint 1:** `LinkedList` has a `self.head` attribute that points to the first node (or `None` if empty).

> **Hint 2:** `append`: traverse to the last node (where `current.next is None`), then set `current.next = Node(value)`.

> **Hint 3:** `prepend`: create a new node, set `new_node.next = self.head`, then `self.head = new_node`.

> **Hint 4:** `delete`: keep track of the previous node so you can set `prev.next = current.next`.

> **Hint 5:** `reverse`: use three pointers: `prev = None`, `current = self.head`, `next_node`. Update them in each iteration.

---

## How to Run the Tests

```bash
cd level-03-advanced/challenge-30-linked-list
pytest tests/ -v
```
