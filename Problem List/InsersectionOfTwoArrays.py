"""
En:
Give two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
---------
Vi:
Cho hai mảng số nguyên nums1 và nums2, trả về một mảng chứa các phần tử chung của hai mảng. 
Mỗi phần tử trong kết quả phải là duy nhất và bạn có thể trả về kết quả theo bất kỳ thứ tự nào.
Ví dụ 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Ví dụ 2:
"""
f"""
Solutions:
- Cho 2 mảng: nums1, nums2
[] List số chung ở 2 mảng
-> Set để lấy các phẩn tử
-> Kiểm tra Set nums1 và Set nums2 -> Found số chung -> Add vào List số chung

Cách khác:
- Sắp xếp 2 mảng
- Dùng 2 con trỏ
- Nếu 2 con trỏ trùng nhau -> Add vào List số chung
- Nếu 2 con trỏ khác nhau -> Di chuyển con trỏ nào nhỏ hơn
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Tại sao phải dùng & ở đây
        # Vì & là phép giao của 2 tập hợp, trong trường hợp này là 2 mảng
        # Vì mảng có thể có các phần tử trùng nhau, nên phải dùng set để loại bỏ các phần tử trùng nhau
        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] not in res:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res 

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))
print(Solution().intersection2(nums1, nums2))