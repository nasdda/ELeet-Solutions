class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        hp = 1

        for x in nums[1:]:
            if x == current:
                hp += 1
                continue
            if hp > 0:
                hp -= 1
            else:
                current = x
                hp = 1
        
        return current
