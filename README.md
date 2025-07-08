# Selection Algorithms and Data Structures

## Overview

In this repository, I have implemented and analyzed various **selection algorithms** and **elementary data structures**. The primary focus of this project was to explore **Median of Medians** and **Randomized Quickselect** algorithms for finding the k-th smallest element in an array, and to implement basic data structures such as **arrays**, **stacks**, **queues**, and **linked lists**. The goal was to understand their performance characteristics, including time and space complexity, and identify scenarios where each structure or algorithm is most useful.

---

## Contents

### Part 1: Selection Algorithms

1. **Median of Medians**:
   - A deterministic algorithm for selecting the k-th smallest element in \(O(n)\) time in the worst case.
   
2. **Randomized Quickselect**:
   - A randomized algorithm that, on average, runs in \(O(n)\) time to find the k-th smallest element, with the possibility of \(O(n^2)\) in the worst case.

### Part 2: Elementary Data Structures

1. **Array**:
   - A basic implementation supporting insertion, deletion, and access operations.
   
2. **Stack**:
   - A simple implementation based on the Last-In-First-Out (LIFO) principle, supporting push, pop, peek, and is_empty operations.

3. **Queue**:
   - A basic implementation based on the First-In-First-Out (FIFO) principle, with enqueue, dequeue, peek, and is_empty operations.

4. **Linked List**:
   - A singly linked list implementation supporting insert, delete, and display operations.

---

## How to Run the Code

To run any of the algorithms or data structures, simply clone the repository to your local machine:

git clone https://github.com/nkannekanti38720/Selection-Algorithms-and-Data-Structures.git



Navigate to the respective Python file (e.g., `median_of_medians.py`, `randomized_quickselect.py`, `array.py`, etc.) and run the script using:

python filename.py


You can modify the arrays and parameters in the script to test the functionality with different inputs.

---

## Performance Analysis

- **Median of Medians**: This algorithm guarantees a worst-case time complexity of \(O(n)\), making it reliable for finding the k-th smallest element in a large unsorted array.
- **Randomized Quickselect**: This algorithm performs well in practice with an expected time complexity of \(O(n)\), but it has a \(O(n^2)\) worst-case scenario, especially with poor pivot choices.
  
For the data structures:
- **Arrays** offer fast access but are inefficient for dynamic operations like insertions and deletions.
- **Stacks** and **Queues** are ideal for LIFO and FIFO operations, respectively, and are very efficient for those tasks.
- **Linked Lists** are better suited for dynamic memory management but have slower access times compared to arrays.

---

## Future Improvements

- I plan to optimize the **Queue** implementation to handle large datasets more efficiently.
- Experimenting with **tree-based data structures** like **binary search trees** or **heaps** could be a valuable next step for improving performance in specific scenarios.

---
