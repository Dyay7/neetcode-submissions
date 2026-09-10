class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x-arr[l]) <= abs(x-arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]

    def findClosestElements(self, arr, k, x):
        lo = -1
        hi = len(arr) - k

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            #False → "this window starts too far left; move right"
            #True  → "we've moved far enough right; don't go farther"

            if x - arr[mid] <= arr[mid + k] - x:
                hi = mid
            else:
                lo = mid

        return arr[hi:hi + k]


