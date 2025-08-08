"""
English:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 
------

Vietnamese:
Dãy ký tự "PAYPALISHIRING" được viết theo hình dạng ziczac với số hàng cho trước như sau: 
(bạn có thể muốn hiển thị hình dạng này trong một font cố định để dễ đọc)

"""

"""
Cách giải:
- Bước 1: Kiểm tra nếu numRows là 1, trả về s.
- Bước 2: Tạo một mảng 2 chiều rows có kích thước numRows.
- Bước 3: Duyệt qua từng ký tự trong s, đặt ký tự vào hàng tương ứng trong rows.
- Bước 4: Ghép nối các hàng trong rows thành một chuỗi và trả về.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * numRows # Tạo một mảng 2 chiều rows có kích thước numRows, output: ['', '', ''] with numRows = 3
        cur_row = 0 # Bắt đầu từ hàng đầu tiên
        going_down = False # Duyệt theo chiều xuôi
        
        for char in s: # Duyệt qua từng ký tự trong s
            rows[cur_row] += char # Thêm ký tự vào hàng tương ứng
            if cur_row == 0 or cur_row == numRows - 1: # Nếu đến hàng đầu tiên hoặc hàng cuối cùng
                going_down = not going_down # Đổi chiều duyệt
            cur_row += (1 if going_down else -1) # Duyệt theo chiều xuôi hoặc ngược
            
        return ''.join(rows)
    
s = "PAYPALISHIRING"
numRows = 3
solution = Solution()
print(solution.convert(s, numRows)) # "PAHNAPLSIIGYIR"