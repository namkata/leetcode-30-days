"""
English:
Give an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Vi:
Cho một mảng số nguyên nums, tìm mảng con có tổng lớn nhất và trả về tổng của nó.
Ví dụ 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Ví dụ 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Ví dụ 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

"""
Cách giải:
nums=[-2,1,-3,4,-1,2,1,-5,4]
Khởi tạo: max_sum, current_sum = phần từ đầu tiên (nums[0]=-2)
Duyệt mảng nums từ phần từ thứ 1:
- Sử dụng max: Nếu num lớn hơn current_sum + num => current_sum = num
- Sử dụng max: Nếu current_sum lớn hơn max_sum => max_sum = current_sum
Trả về max_sum
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Khởi tạo: max_sum, current_sum = phần từ đầu tiên (nums[0]=-2)
        max_sum = nums[0]
        current_sum = nums[0]
        # Duyệt mảng nums từ phần tử thứ 1
        for num in nums[1:]:
            # Sử dụng max: Nếu num lớn hơn current_sum + num => current_sum = num
            current_sum = max(num, current_sum + num)
            # Sử dụng max: Nếu current_sum lớn hơn max_sum => max_sum = current_sum
            max_sum = max(max_sum, current_sum)
        return max_sum
    def maxSubArray2(self, nums: List[int]) -> int:
        # Khởi tạo: max_sum, current_sum = phần tử đầu tiên (nums[0]=-2)
        max_sum = nums[0]
        current_sum = nums[0]
        # Duyệt mảng nums từ phần tử thứ 1
        for num in nums[1:]:
            # Sử dụng max: Nếu num lớn hơn current_sum + num => current_sum = num
            current_sum = max(num, current_sum + num)
            # Sử dụng max: Nếu current_sum lớn hơn max_sum => max_sum = current_sum
            max_sum = max(max_sum, current_sum)
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(nums))
# Output: 6
print(s.maxSubArray2(nums))
# Output: 6