class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r = 0, 1
        m = max(nums)
        while nums[l] != m:
            if nums[l] != nums[r]:
                nums[l+1], nums[r] = nums[r], nums[l+1]
                l+=1
            r+=1
        return l + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna