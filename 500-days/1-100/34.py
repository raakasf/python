import heapq

heap = [3, 1, 4, 5, 2]
# The heapq module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
# A heap is a binary tree where the parent node is smaller (for a min-heap) or larger (for a max-heap) than its child nodes.
# The heapq module in Python supports min-heaps by default.
heapq.heapify(heap)
heapq.heappush(heap, 6)
print(heap)
