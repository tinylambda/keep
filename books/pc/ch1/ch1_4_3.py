import heapq

if __name__ == "__main__":
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    print(heap)

    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
