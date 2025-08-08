"""
English:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
The algorithm for myAtoi(string s) is as follows:
1. Whitespaces: Ignore any leading whitespace in the string.
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
---
Vietnamese:
Cài đặt hàm myAtoi(string s), chuyển đổi một chuỗi thành một số nguyên 32-bit có dấu (tương tự như hàm atoi trong C/C++).
Công thức myAtoi(string s) như sau:
1. Bỏ qua khoảng trắng: Bỏ qua bất kỳ khoảng trắng ở đầu chuỗi.
2. Xác định dấu: Xác định dấu bằng cách kiểm tra ký tự tiếp theo là '-' hoặc '+', nếu không có thì mặc định là dấu dương.
3. Chuyển đổi: Đọc số nguyên bằng cách bỏ qua các số 0 ở đầu, dừng khi gặp ký tự không phải số hoặc kết thúc chuỗi. Nếu không đọc được số nào, thì kết quả là 0.
4. Xác định dấu: Xác định dấu bằng cách kiểm tra ký tự tiếp theo là '-' hoặc '+', nếu không có thì mặc định là dấu dương.
Trả về kết quả: Trả về kết quả là số nguyên 32-bit có dấu

"""

"""
Cách giải:
- Bước 1: Kiểm tra nếu chuỗi s rỗng, trả về 0.
- Bước 2: Bỏ qua khoảng trắng ở đầu chuỗi.
- Bước 3: Xác định dấu.
- Bước 4: Chuyển đổi.
- Bước 5: Xác định dấu.
- Bước 6: Trả về kết quả.

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        s = s.strip() # Bỏ qua khoảng trắng ở đầu chuỗi
        if not s:
            return 0
        
        sign = 1 # Dấu mặc định là dương
        if s[0] == '-': # Nếu ký tự đầu tiên là dấu trừ
            sign = -1 # Thì dấu là âm
            s = s[1:] # Bỏ qua ký tự đầu tiên
        elif s[0] == '+': # Nếu ký tự đầu tiên là dấu cộng
            sign = 1 # Thì dấu là dương
            s = s[1:] # Bỏ qua ký tự đầu tiên
        
        result = 0 # Kết quả
        for char in s: # Duyệt qua từng ký tự trong s
            if not char.isdigit(): # Nếu ký tự không phải số
                break # Dừng lại
            
            # Tại sao * 10 vì nó là hàng đơn vị
            result = result * 10 + int(char) # Thêm ký tự vào kết quả
            if sign == 1 and result > 2**31 - 1: # Nếu kết quả vượt quá giới hạn của số nguyên 32-bit có dấu
                return 2**31 - 1 # Trả về giới hạn trên
            elif sign == -1 and result > 2**31: # Nếu kết quả vượt quá giới hạn của số nguyên 32-bit có dấu
                return -2**31 # Trả về giới hạn dưới
        return sign * result # Trả về kết quả

    def myAtoi2(self, s: str) -> int:
        if not s:
            return 0

        s = s.strip() # Bỏ qua khoảng trắng ở đầu chuỗi
        if not s:
            return 0
        
        sign = 1 # Dấu mặc định là dương
        if s[0] == '-': # Nếu ký tự đầu tiên là dấu trừ
            sign = -1 # Thì dấu là âm
            s = s[1:] # Bỏ qua ký tự đầu tiên
        elif s[0] == '+': # Nếu ký tự đầu tiên là dấu cộng
            sign = 1 # Thì dấu là dương
            s = s[1:] # Bỏ qua ký tự đầu tiên
        
        a = ""
        for char in s: # Duyệt qua từng ký tự trong s
            if not char.isdigit(): # Nếu ký tự không phải số
                break # Dừng lại
            
            a += char

            if sign == 1 and int(a) > 2**31 - 1: # Nếu kết quả vượt quá giới hạn của số nguyên 32-bit có dấu
                return 2**31 - 1 # Trả về giới hạn trên
            elif sign == -1 and int(a) > 2**31: # Nếu kết quả vượt quá giới hạn của số nguyên 32-bit có dấu
                return -2**31 # Trả về giới hạn dưới
        
        if not a:
            return 0
        
        return sign * int(a) # Trả về kết quả


x = "   -42"
y = "4193 with words"
z = "words and 987"
print(Solution().myAtoi(x))
print(Solution().myAtoi(y))
print(Solution().myAtoi(z))
print(Solution().myAtoi2(x))
print(Solution().myAtoi2(y))
print(Solution().myAtoi2(z))
