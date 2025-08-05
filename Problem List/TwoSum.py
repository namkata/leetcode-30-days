from typing import List
"""
En:
Give an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
---
Vi:
Cho một mảng số nguyên nums và một số nguyên target, trả về chỉ số của hai số nào đó trong mảng sao cho tổng của chúng bằng target.
Bạn có thể giả định rằng mỗi đầu vào sẽ có chính xác một giải pháp, và bạn không thể sử dụng cùng một phần tử twice.
Bạn có thể trả về đáp án theo bất kỳ thứ tự nào.
---
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

f"""
Solutions:
nums = [2, 7, 11, 15], target = 9

- Tìm index trong nums sao cho nums[index] + nums[index2] = target
=> Vòng lặp 0 -> len(nums)
=> Tạo dict lưu lại giá trị của nums[index] và index của nó
ví dụ: num_maps = { 2: 0, 7: 1, 11: 2, 15: 3}
Khi tao loop mảng nums, ta kiểm tra xem nếu lấy target - giá trị index đó thì có tìm thấy giá trị đó trong num_maps không?
-> Ví dụ: 9 - nums[0] = 7, kiểm tra 7 có tồn tại ở trong num_maps không?
-> Có, thì ta trả về index của 7 trong num_maps và index của nums[0]
-> Vậy là ta đã tìm thấy hai số trong mảng nums sao cho tổng của chúng bằng target
Vậy ta lưu lại [num_map[target - nums[i]], i]

=> Ưu điểm thì nhanh hơn cách truyền thống 
- Cách truyền thống, sử dụng mạng i and j
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
=> Nhược điểm: Time complexity là O(n^2) 
=> Cách này không tối ưu, vì chúng ta phải loop qua mảng nums 2 lần
=> Cách này không sử dụng được trong trường hợp mảng nums có nhiều hơn 2 phần tử

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Init dict
        num_map = {}
        # Loop through nums
        for i in range(len(nums)):
            # Check if target - nums[i] is in num_map
            # E.g: target=9, nums[i]=1, then check if 8 is in num_map
            if target - nums[i] in num_map:
                # E.g: num_map[8]=1
                return [num_map[target - nums[i]], i]
            # Add nums[i] to num_map
            # E.g: num_map[1]=2
            num_map[nums[i]] = i
        # Return empty list if no solution
        return []

# Example
# nums = [2, 7, 11, 15]
# target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Test
# nums = [2, 7, 11, 15]
# target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Running:
nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
