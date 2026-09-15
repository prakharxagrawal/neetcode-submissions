class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        i = 0
        while i < len(nums):
            hash_map[nums[i]] = 0
            i+=1
        i = 0
        while i < len(nums):
            hash_map[nums[i]]+=1
            i+=1
        i = 0
        while i < len(nums):
            if hash_map[nums[i]] > 1:
                b=True
                return b
            i+=1
        return False