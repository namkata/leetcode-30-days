"""
English:
Give an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
------
Vietnamese:
Cho một mảng nums, viết hàm để di chuyển tất cả các số 0 về cuối mảng mà vẫn giữ nguyên thứ tự của các phần tử khác không phải là 0.
Lưu ý rằng bạn phải thực hiện thao tác này trong-place mà không phải tạo ra một bản sao của mảng.
Ví dụ 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Ví dụ 2:
Input: nums = [0]
Output: [0]
"""
"""
Cách giải:
- Duyệt mảng nums, nếu phần tử tại vị trí i là 0, thì di chuyển tất cả các phần tử sau đó về trước mảng.
- Đoạn code sau đây là một cách giải thích cho cách trên:

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Duyệt mảng nums
        for i in range(len(nums)):
            # Nếu phần tử tại vị trí i là 0
            if nums[i] == 0:
                # Di chuyển tất cả các phần tử sau đó về trước mảng
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                # Đặt phần tử 0 tại vị trí i thành 0
                nums[i] = 0
        return nums
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Duyệt mảng nums
        insert_pos = 0
        # Duyệt mảng nums
        for num in nums:
            # Nếu phần tử tại vị trí i là 0
            if num != 0:
                # Di chuyển tất cả các phần tử sau đó về trước mảng
                nums[insert_pos] = num
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
        return nums



nums = [0,1,0,3,12]
s = Solution()
print(s.moveZeroes(nums))
# Output: [1,3,12,0,0]
