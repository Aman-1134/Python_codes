def findMedianSortedArrays(self, nums1, nums2):
    num = sorted(nums1 + nums2)
    l = len(num)

    if l % 2 != 0:
        a = (l - 1) // 2
        median = num[a]
    else:
        a1 = l // 2
        a2 = (l // 2) - 1
        median = (num[a1] + num[a2]) / 2

    return median

l1 = [1, 2]
l2 = [3, 4]
l3 = [3]
ans = findMedianSortedArrays(l1, l2)
print(ans)