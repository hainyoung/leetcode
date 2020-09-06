# 31 Top K Frequent Elements

# Given a non-empty array of inteers, return the k most frequent elements
# input : [1, 1, 1, 2, 2, 3], k = 2
# output : [1, 2]

from typing import List
import collections
import heapq

def topKFrequent_1(nums: List[int], k: int):
    result = []
    for num, cnt in collections.Counter(nums).most_common(k):
        result.append(num)
    return result
    
   

   
def topKFrequent_2(nums: List[int], k: int):
     return list(zip(*collections.Counter(nums).most_common(k)))[0]




def topKFrequent_3(nums: List[int], k: int):
    freqs = collections.Counter(nums)
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        heapq.heqppop(freqs_heap[1])