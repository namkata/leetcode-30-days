"""
English:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

------
Vietnamese:
Cho hai mảng nums1 và nums2 có kích thước m và n , trả về trung vị của hai mảng đã sắp xếp.

Tổng quan độ phức tạp thuật toán:
- Time complexity: O(log (m+n))
- Space complexity: O(1)

"""
"""
Solutions:
- Solution 1:
    + Bước 1: Kết hợp hai mảng nums1 và nums2 thành một mảng mới nums.
    + Bước 2: Sắp xếp mảng nums theo thứ tự tăng dần.
    + Bước 3: Tính toán vị trí trung vị của mảng nums.
    + Bước 4: Trả về giá trị tại vị trí trung vị.
"""
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        
        nums.sort() # Sap xep lai

        n = len(nums) # Lay do dai cua mang, chia doi su dung integer division để làm tròn sau khi chia
        if n % 2 == 0: # Nếu độ dài của mảng là chắn 
            return (nums[n//2 - 1] + nums[n//2]) / 2 # Trả về giá trị trung bình ở giữa, ví dụ: (2+3)/2=2.5
        else:
            return nums[n//2]

nums1 = [1,3]
nums2 = [2]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
