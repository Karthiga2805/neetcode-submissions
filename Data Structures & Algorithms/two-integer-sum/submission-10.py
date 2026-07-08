class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Set = set()  # Even though this looks efficient(avoids the recalculation and looping for numbers already calculated), it takes more time than the one where you dont use set
        # for i in range(len(nums)):
        #     if nums[i] not in Set:
        #         Set.add(nums[i])
        #         if ((target - nums[i]) in nums[i+1:]):
        #             nums_dup  = nums[i+1:]
        #             index = nums_dup.index(target-nums[i]) + i + 1
        #             return [i,index]          
        # return []
        for i in range(len(nums)):
            if ((target - nums[i]) in nums[i+1:]):
                nums_dup  = nums[i+1:]
                index = nums_dup.index(target-nums[i]) + i + 1
                return [i,index]          
        return []
