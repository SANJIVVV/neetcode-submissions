from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        result = count.most_common(k)
        return [num for num, freq in result]