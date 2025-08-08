"""
English:
Give a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

-------
Vietnamse:
Cho một chuỗi s, trả về chuỗi con palindromic dài nhất trong s.

"""

"""
Solutions:
- Solution 1:
    + Bước 1: Kiểm tra xem chuỗi s có phải chuỗi palindromic hay không.
    + Bước 2: Nếu chuỗi s là chuỗi palindromic, trả về chuỗi s.
    + Bước 3: Nếu chuỗi s không phải chuỗi palindromic, kiểm tra từng ký tự trong chuỗi s.
    + Bước 4: Nếu ký tự tại vị trí i là ký tự palindromic, kiểm tra xem chuỗi con từ vị trí i đến vị trí j có phải chuỗi palindromic hay không.
    + Bước 5: Nếu chuỗi con từ vị trí i đến vị trí j là chuỗi palindromic, kiểm tra xem độ dài của chuỗi con này có lớn hơn độ dài của chuỗi con palindromic trước đó hay không.
    + Bước 6: Nếu chuỗi con từ vị trí i đến vị trí j là chuỗi palindromic và độ dài của chuỗi con này lớn hơn độ dài của chuỗi con palindromic trước đó, cập nhật chuỗi con palindromic trước đó.
    + Bước 7: Trả về chuỗi con palindromic trước đó.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Kiểm tra chuỗi s: ví dụ aba với chuôi ngược lại cũng là aba, vậy aba là chuỗi palindromic
        if s == s[::-1]:
            return s
        
        # Kiểm tra từng ký tự trong chuỗi s
        n = len(s)
        max_len = 0
        max_str = ""
        # Duyệt qua từng ký tự trong chuỗi s
        for i in range(n):
            # Duyệt qua từng ký tự sau ký tự i
            for j in range(i+1, n+1): # j là vị trí sau i, nếu i = 0, j sẽ chạy từ 1 đến n
                # Kiểm tra xem chuỗi con từ i đến j có phải chuỗi palindromic hay không. Ví dụ: s[i:j] = "aba"
                if s[i:j] == s[i:j][::-1]:
                    # Nếu chuỗi con từ i đến j là chuỗi palindromic và độ dài của chuỗi con này lớn hơn độ dài của chuỗi con palindromic trước đó
                    if j-i > max_len: # j-i là độ dài của chuỗi con từ i đến j
                        # Cập nhật độ dài của chuỗi con palindromic trước đó
                        max_len = j-i # j-i là độ dài của chuỗi con từ i đến j
                        # Cập nhật chuỗi con palindromic trước đó
                        max_str = s[i:j] # s[i:j] là chuỗi con từ i đến j
        return max_str

s = "babad"
solution = Solution()
print(solution.longestPalindrome(s)) # "bab"

s = "cbbd"
solution = Solution()
print(solution.longestPalindrome(s)) # "bb"

s = "a"
solution = Solution()
print(solution.longestPalindrome(s)) # "a"
