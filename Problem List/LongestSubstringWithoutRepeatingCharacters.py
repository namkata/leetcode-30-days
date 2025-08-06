"""
English:
Give a string s, find the length of the longest substring without repeating characters.

Vietnamese:
Cho một chuỗi s, tìm độ dài của chuỗi con dài nhất không có ký tự lặp lại.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
Cách giải:
Sử dụng set, sau đó counter
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # Lưu trữ các ký tự đã gặp
        left = 0 # Phần tử bên trái của cửa sổ
        max_len = 0 # Độ dài của chuỗi con dài nhất

        # Lọc mảng qua phía phải
        for right in range(len(s)):
            # Kiểm tra xem ký tự tại right có trong set hay không
            while s[right] in seen: # eg: pwwkew, right = 2, left = 0, max_len = 2
                # Nếu có thì xoá ký tự đã lưu ở vị trí left
                seen.remove(s[left]) # eg: pwwkew, left = 0, seen = {p}
                # Cập nhập lại ví trí left thành ví trí right
                left += 1 # eg: pwwkew, left = 1
            # Nếu không có thì thêm ký tự tại right vào set
            seen.add(s[right]) # eg: pwwkew, right = 2, seen = {p, w}   
            # Cập nhập lại độ dài của chuỗi con dài nhất
            max_len = max(max_len, right - left + 1) # eg: pwwkew, right = 2, left = 1, max_len = 2
        return max_len
            

f"""
Quy trình chạy code:
s = "pwwkew"
seen = set(), left = 0, max_len = 0
right = 0; while s[right] not in seen:
    seen.add(s[right]) 
    seen = {p}
    right = 0
    left = 0
    max_len = max(max_len, right - left + 1) // max(0, 0 - 0 + 1) // 1

right = 1, s[right] = "w", while s[right] not in seen:
    seen.add(s[right])
    seen = {p, w}
    right = 1
    left = 0
    max_len = 0
    max_len = max(max_len, right - left + 1) // max(0, 1 - 0 + 1) // 1

right = 2, s[right] = "w", while s[right] in seen:
    seen.remove(s[left]) # seen = {p}
    left += 1

    seen = {p, w}
    left = 1
    right = 2
    max_len = 0
    max_len = max(max_len, right - left + 1) // max(0, 2 - 1 + 1) // 1

right = 3, s[right] = "k", while s[right] not in seen:
    seen.add(s[right])
    seen = {p, w, k}
    right = 3
    left = 1
    max_len = 0
    max_len = max(max_len, right - left + 1) // max(0, 3 - 1 + 1) // 2

right = 4, s[right] = "e", while s[right] not in seen:
    seen.add(s[right])
    seen = {p, w, k, e}
    right = 4
    left = 1
    max_len = 0
    max_len = max(max_len, right - left + 1) // max(0, 4 - 1 + 1) // 3

right = 5, s[right] = "w", while s[right] in seen:
    seen.remove(s[left]) # seen = {p, w, k}
    left += 1
    left = 2
    right = 5
    max_len = 0
    max_len = max(max_len, right - left + 1) // max(0, 5 - 2 + 1) // 3
"""

s = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
