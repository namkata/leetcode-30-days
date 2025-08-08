"""
English:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Vietnamese:
Cho một số nguyên 32 bit có dấu x, trả về x với các chữ số đảo ngược. Nếu đảo ngược x dẫn đến giá trị vượt ra ngoài phạm vi số nguyên 32 bit có dấu [-231, 231 - 1], thì trả về 0.
Lưu ý:
- Giả sử môi trường không cho phép bạn lưu trữ số nguyên 64 bit (có dấu hoặc không có dấu).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

"""
Cách giải:
- Bước 1: Kiểm tra nếu x là 0, trả về 0.
- Bước 2: Kiểm tra nếu x là số âm, đặt sign = -1, x = -x, ngược lại đặt sign = 1.
- Bước 3: Duyệt qua từng chữ số trong x, đặt chữ số vào hàng tương ứng trong rows.
- Bước 4: Ghép nối các hàng trong rows thành một chuỗi và trả về.
"""

class Solution:
    def reverse(self, x: int) -> int:
        # Nếu x là 0, trả về 0
        if x == 0:
            return 0
        
        # Kiểm tra nếu x là số âm, đặt sign = -1, x = -x, ngược lại đặt sign = 1
        sign = -1 if x < 0 else 1
        # Lấy giá trị tuyệt đối của x, abs(x) = 123
        x = abs(x)
        # Tạo một mảng rows để lưu trữ các chữ số
        rows = []
        
        # Duyệt qua từng chữ số trong x, đặt chữ số vào hàng tương ứng trong rows
        while x > 0:
            # Lấy chữ số cuối cùng của x, x % 10 = 3
            # Thêm chữ số này vào hàng cuối cùng của rows
            rows.append(x % 10)
            # Loại bỏ chữ số cuối cùng của x, x = 12
            x //= 10
        
        # Ghép nối các hàng trong rows thành một chuỗi, output: "321"
        # Chuyển chuỗi này thành số nguyên, output: 321
        # Nhân với sign, output: 321 * -1 = -321
        res = int(''.join(map(str, rows))) * sign
        
        # Kiểm tra nếu res vượt ra ngoài phạm vi số nguyên 32 bit có dấu [-231, 231 - 1], thì trả về 0
        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res
    
    # Wrong: x = 1534236469
    # Output: 0
    # Expected: 0
    # 1045/1045
    def reverse2(self, x: int) -> int:
        if x == 0:
            return 0
        a = str(x)
        c = ""
        e = ""
        if a[0] == "-":
            c = a[1:]
            e = "-"
        if c:
            d = c[::-1]
        else:
            d = a[::-1]
        g = str(e+d)
        abc = int(g)
        if abc < -2**31 or abc > 2**31 - 1:
            return 0
        return abc


x = -123
solution = Solution()
print(solution.reverse(x))
print(solution.reverse2(x))