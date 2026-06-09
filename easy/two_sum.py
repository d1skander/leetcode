#python3 easy/two_sum.py
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.numbers: List[int] = nums
        self.target: int  = target
        for i in range(len(self.numbers)):
            for x in range(i + 1, len(self.numbers)):
                if self.numbers[i] + self.numbers[x] == self.target:
                    return [i, x]


nums = [10, 2, 8, 15]
target = 17
two_sum = Solution()
result = two_sum.twoSum(nums=nums, target=target)
print(result)