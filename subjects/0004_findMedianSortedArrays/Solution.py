import heapq


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        heapq.heapify(nums1)
        min_size, total, pre = int(len(nums1) / 2), len(nums1), None
        while len(nums1) > min_size:
            pre = heapq.heappop(nums1)
        return float(pre) if total % 2 else float((pre + nums1[0]) / 2)


if __name__ == "__main__":
    nums1 = []
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
