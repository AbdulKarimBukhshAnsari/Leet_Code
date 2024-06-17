class Solution:
  def searchRange(self, nums: list[int], target: int) -> list[int]:
    if target not in nums:
      return [-1, -1]
    start = 0
    end = len(nums) - 1
    mid = int((start + end) / 2)
    while start <= end:
      if nums[mid] == target:
        start_word = end_word = mid  # Initialize both with mid for single occurrence
        i = mid - 1
        while i >= 0 and nums[i] == target:  # Check for elements before mid
          start_word -= 1
          i -= 1
        j = mid + 1
        while j < len(nums) and nums[j] == target:  # Check for elements after mid
          end_word += 1
          j += 1
        return [start_word, end_word]
      elif nums[mid] > target:
        end = mid - 1
      elif nums[mid] < target:
        start = mid + 1
      mid = int((start + end) / 2)
      