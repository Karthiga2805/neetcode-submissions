class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      Count = {}
      for i in nums:
        Count[i] = Count.get(i,0) + 1
      # Count = Counter(nums)  #Whatever is done above is equivalent to this
      sorted_items = sorted(Count.items(),key= lambda x:x[1],reverse = True)

      topKfreq = [key for (key,value) in sorted_items[:k]]
      return topKfreq



