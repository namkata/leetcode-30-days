"""
English:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

--------
Vi:
Cho một chuỗi s, trả về true nếu chuỗi đó là chuỗi palindrome, ngược lại trả về false.
Chuỗi palindrome là chuỗi mà khi đảo ngược thứ tự các ký tự trong chuỗi, chuỗi đó vẫn giữ nguyên.
Ví dụ 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Ví dụ 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Ví dụ 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

"""
Cách giải cho tôi:
- Xóa tất cả các ký tự không phải là chữ cái hoặc số
- Chuyển đổi chuỗi thành chữ thường
- Kiểm tra xem chuỗi có phải là palindrome không
Giải thích palindrome là gì:
- Palindrome là chuỗi mà khi đảo ngược thứ tự các ký tự trong chuỗi, chuỗi đó vẫn giữ nguyên.
- Ví dụ: "amanaplanacanalpanama" là một palindrome.
- Ví dụ: "raceacar" không phải là palindrome.
- Ví dụ: " " là một palindrome.
- Ví dụ: "0P" không phải là palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Xóa tất cả các ký tự không phải là chữ cái hoặc số
        s = ''.join(char for char in s if char.isalnum())
        # Chuyển đổi chuỗi thành chữ thường
        s = s.lower()
        # Kiểm tra xem chuỗi có phải là palindrome không
        return s == s[::-1]
    
    def isPalindrome2(self, s: str) -> bool:
        # Xóa tất cả các ký tự không phải là chữ cái hoặc số
        s = ''.join(char for char in s if char.isalnum())
        # Chuyển đổi chuỗi thành chữ thường
        s = s.lower()
        # Kiểm tra xem chuỗi có phải là palindrome không
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))
print(solution.isPalindrome2(s))

s = "race a car"
print(solution.isPalindrome(s))
print(solution.isPalindrome2(s))

s = " "
print(solution.isPalindrome(s))
print(solution.isPalindrome2(s))