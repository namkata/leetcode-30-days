"""
English:
Give an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.  
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
---------
Vietnamese:
Cho một mảng nums có kích thước n, trả về phần tử xuất hiện nhiều hơn ⌊n / 2⌋ lần. 
Bạn có thể giả sử rằng phần tử xuất hiện nhiều hơn ⌊n / 2⌋ lần luôn tồn tại trong mảng.
Ví dụ 1:
Input: nums = [3,2,3]
Output: 3
Ví dụ 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2 
"""
"""
Solutions:

"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Tạo một dict để lưu số lần xuất hiện của từng phần tử
        num_map = {}
        # Duyệt qua từng phần tử trong mảng
        for num in nums:
            # Kiểm tra xem phần tử đó đã có trong dict chưa
            if num in num_map:
                # Nếu có, tăng số lần xuất hiện lên 1
                num_map[num] += 1
            else:
                # Nếu không, thêm phần tử đó vào dict với số lần xuất hiện là 1
                num_map[num] = 1
        # Kiểm tra xem phần tử đó có phải là phần tử xuất hiện nhiều hơn n/2 lần không
        if num_map[num] > len(nums) // 2:
            # Nếu có, trả về phần tử đó
            return num
        # Nếu không, trả về -1
        return -1
    
    def majorityElement2(self, nums: List[int]) -> int:
        # Sắp xếp mảng
        nums.sort()
        # Trả về phần tử ở giữa mảng
        return nums[len(nums) // 2]
    
    def majorityElement3(self, nums: List[int]) -> int:
        # Tạo một biến để lưu phần tử xuất hiện nhiều hơn n/2 lần
        majority = None
        # Tạo một biến để lưu số lần xuất hiện của phần tử đó
        count = 0
        # Duyệt qua từng phần tử trong mảng
        for num in nums:
            # Kiểm tra xem phần tử đó có phải là phần tử xuất hiện nhiều hơn n/2 lần không
            if count == 0:
                # Nếu là phần tử đầu tiên, gán phần tử đó cho majority
                majority = num
            # Kiểm tra xem phần tử đó có phải là phần tử xuất hiện nhiều hơn n/2 lần không
            if num == majority:
                # Nếu có, tăng số lần xuất hiện lên 1
                count += 1
            else:
                # Nếu không, giảm số lần xuất hiện đi 1
                count -= 1
        # Trả về phần tử xuất hiện nhiều hơn n/2 lần
        return majority

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
print(Solution().majorityElement2(nums))
print(Solution().majorityElement3(nums))
# Output: 2
