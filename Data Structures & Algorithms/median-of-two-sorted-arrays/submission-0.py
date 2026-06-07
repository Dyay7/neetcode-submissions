class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary‑search the smaller array
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        m, n = len(A), len(B)
        total = m + n
        half = (total + 1) // 2

        # Edge case: A is empty → median comes entirely from B
        if m == 0:
            if n % 2 == 1:
                return float(B[half - 1])
            return (B[half - 1] + B[half]) / 2.0

        # Binary search on A using the minimization template
        left, right = -1, m

        while left + 1 < right:
            i = left + (right - left) // 2
            j = half - i

            # Partition boundaries
            aLeft  = float('-inf') if i == 0 else A[i - 1]
            aRight = float('inf')  if i == m else A[i]
            bLeft  = float('-inf') if j == 0 else B[j - 1]
            bRight = float('inf')  if j == n else B[j]

            # Correct partition found
            if aLeft <= bRight and bLeft <= aRight:
                return compute_median(aLeft, aRight, bLeft, bRight, total)

            # Move search window
            if aLeft > bRight:
                right = i
            else:
                left = i

        # Final check using right index
        i = right
        j = half - i

        aLeft  = float('-inf') if i == 0 else A[i - 1]
        aRight = float('inf')  if i == m else A[i]
        bLeft  = float('-inf') if j == 0 else B[j - 1]
        bRight = float('inf')  if j == n else B[j]

        return compute_median(aLeft, aRight, bLeft, bRight, total)


def compute_median(aLeft, aRight, bLeft, bRight, total):
    # if it is even we need to calculate it if it is odd we take the element in the middle
    if total % 2 == 1:
        return float(max(aLeft, bLeft))
    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2.0