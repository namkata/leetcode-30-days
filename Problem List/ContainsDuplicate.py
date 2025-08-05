"""
En:
Give an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
--------
Vi:
Cho một mảng số nguyên nums, trả về true nếu bất kỳ giá trị nào xuất hiện ít nhất hai lần trong mảng, và trả về false nếu mọi phần tử đều khác nhau.
Ví dụ 1:
Input: nums = [1,2,3,1]
Output: true
Ví dụ 2:
Input: nums = [1,2,3,4]
Output: false
Ví dụ 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

"""
Solutions:
True: If any value appears at least twice in the array (Bất kì số nào xuất hiện ít nhất 2 lần trong mảng)
False: If every element is distinct (Mọi phần tử đều khác nhau)
Cách 1:
-> So sánh độ dài của mảng và độ dài của set của mảng
-> Nếu 2 độ dài khác nhau, thì có ít nhất 1 số xuất hiện ít nhất 2 lần trong mảng

Ưu điểm:
- Dễ implement
- Cung cấp độ chính xác

Nhược điểm:
- Nếu mảng có nhiều phần tử, thì có thể tốn nhiều thời gian

Cách 2:
-> Sử dụng hàm count()
-> Đếm số lần xuất hiện của từng phần tử trong mảng
-> Nếu có phần tử nào xuất hiện ít nhất 2 lần, thì trả về true
-> Ngược lại, trả về false

Ưu điểm:
- Dễ implement
- Cung cấp độ chính xác

Nhược điểm:
- Nếu mảng có nhiều phần tử, thì có thể tốn nhiều thời gian

Cách 3:
-> Sử dụng hàm sort()
-> Sắp xếp mảng theo thứ tự tăng dần
-> So sánh từng phần tử liền kề
-> Nếu 2 phần tử liền kề giống nhau, thì trả về true
-> Ngược lại, trả về false

Ưu điểm:
- Dễ implement
- Cung cấp độ chính xác

Nhược điểm:
- Nếu mảng có nhiều phần tử, thì có thể tốn nhiều thời gian

"""

from typing import List, Counter

class Solution:
    # Correct
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
    # Correct
    def containsDuplicate2(self, nums: List[int]) -> bool:
       counter = Counter(nums)
       for num in counter:
           if counter[num] > 1:
               return True
       return False
    
    # Correct
    def containsDuplicate3(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))
print(solution.containsDuplicate2(nums))
print(solution.containsDuplicate3(nums))
