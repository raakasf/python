import heapq
heap = [1, 3, 2, 4, 5]
heapq.heapify(heap)
popped = heapq.heappop(heap)
print(popped)
