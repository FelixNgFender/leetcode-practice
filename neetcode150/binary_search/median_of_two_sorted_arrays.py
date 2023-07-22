def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    m, n = len(nums1), len(nums2)
    # search space is the shorter array (nums1)
    lo, hi = 0, m - 1

    while True:
        partitionA = (lo + hi) // 2  # end of partition
        partitionB = (m + n) // 2 - partitionA - 2
        # we find the correct partition when all left elements
        # are smaller than the ones on the right
        # nums1 and nums2 are already sorted -> no need to check
        # if nums1[partitionA] < nums1[partitionA + 1]
        # only cross check edge elements
        maxLeftA = nums1[partitionA] if partitionA >= 0 else float("-inf")
        minRightA = nums1[partitionA + 1] if partitionA + 1 < m else float("inf")
        maxLeftB = nums2[partitionB] if partitionB >= 0 else float("-inf")
        minRightB = nums2[partitionB + 1] if partitionB + 1 < n else float("inf")

        # found the correct partition
        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if (m + n) % 2 == 0:
                # average of max left and min right
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                # min of right partition
                return min(minRightA, minRightB)
        elif maxLeftB > minRightA:
            lo = partitionA + 1
        else:
            hi = partitionA - 1


nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))
