class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n = length of the array
        # res = the best (maximum) product seen so far
        # We start with nums[0] because the answer must include at least one element
        n, res = len(nums), nums[0]

        # prefix and suffix will store running products
        # They start at 0 so that (prefix or 1) resets them to 1 on the first multiplication
        prefix = suffix = 0

        # We sweep from both ends at the same time:
        # - prefix goes left → right
        # - suffix goes right → left
        for i in range(n):

            # Build the prefix product.
            # If prefix == 0 (either at start or after hitting a zero),
            # (prefix or 1) becomes 1, so multiplication restarts cleanly.
            prefix = nums[i] * (prefix or 1)

            # Build the suffix product.
            # Same logic, but from the right side of the array.
            suffix = nums[n - 1 - i] * (suffix or 1)

            # Update the result with the best product seen so far.
            # We check both prefix and suffix because the maximum product subarray
            # might start from the left or from the right (especially with negatives).
            res = max(res, prefix, suffix)

        # Return the maximum product found.
        return res
