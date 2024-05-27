class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums1)):
            index_num = nums2.index(nums1[i])
            for j in range(index_num,len(nums2)):
                if nums1[i] < nums2[j]:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)
        return result
obj = Solution()
print(obj.nextGreaterElement([4,1,2],[1,3,4,2]))