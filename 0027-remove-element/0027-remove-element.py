class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i=0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna