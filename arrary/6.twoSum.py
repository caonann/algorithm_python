from typing import List
'''
https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r] > target:
                r=r-1
            else:
                l=l+1
        return [-1,-1]