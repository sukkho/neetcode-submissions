class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} #dictionary

        for num in nums:
            frequency[num] = frequency.get(num,0) + 1 # fetch num value, default value is 0
        
        #sort elements by their frequency count (highest to lowest)
        sorted_elements = sorted(frequency.keys(), key = frequency.get, reverse = True)
        return sorted_elements[:k] # return first k elements



        