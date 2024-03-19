from heapq import *

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_1 = {}
        index_tuple = []
        min_heap = []
        result = []
        
        for i in range(len(list1)):
            dict_1[list1[i]] = i
        
        for i in range(len(list2)):
            if list2[i] in dict_1:
                index_tuple.append((list2[i], dict_1[list2[i]] + i))

        for i in range(len(index_tuple)):
            heappush(min_heap, index_tuple[i][1])

        min_index = 0
        while min_heap:
            min_index = heappop(min_heap)
            break

        for i in range(len(index_tuple)):
            if index_tuple[i][1] == min_index:
                result.append(index_tuple[i][0])
        
        return result
