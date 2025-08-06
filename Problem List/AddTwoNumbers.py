"""
English:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

--------
Vietnamese:
Cho hai danh sách liên kết không rỗng, mỗi danh sách liên kết đại diện cho một số không âm.
Các chữ số được lưu trữ theo thứ tự ngược lại, và mỗi nút chứa một chữ số.
Thêm hai số và trả về tổng dưới dạng danh sách liên kết.
Bạn có thể giả sử rằng hai số không chứa bất kỳ số 0 đứng đầu nào, ngoại trừ số 0 самого.
Ví dụ 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Ví dụ 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Ví dụ 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998.
"""
"""
Cách giải cho tôi:
- Duyệt qua từng nút của hai danh sách liên kết
- Cộng giá trị của từng nút lại với nhau
- Nếu giá trị cộng lớn hơn 9, thì gán giá trị của nút đó thành giá trị cộng lấy dư
- Nếu giá trị cộng nhỏ hơn 9, thì gán giá trị của nút đó thành giá trị cộng
- Trả về danh sách liên kết kết quả
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Tạo một danh sách liên kết mới
        dummy = ListNode(0)
        # Tạo một con trỏ để duyệt qua danh sách liên kết mới
        curr = dummy # eg: 0
        # Tạo một biến để lưu giá trị nhớ
        carry = 0
        # Duyệt qua từng nút của hai danh sách liên kết
        while l1 or l2 or carry:
            # Lấy giá trị của từng nút
            val1 = l1.val if l1 else 0 # eg: 2
            val2 = l2.val if l2 else 0 # eg: 5
            # Cộng giá trị của từng nút lại với nhau
            val = val1 + val2 + carry # eg: 2 + 5 + 0 = 7, số cuổi là 8 vì carray là 1 do val trước đó là 10//10 = 1
            # Gán giá trị của nút đó thành giá trị cộng lấy dư
            carry = val // 10 # eg: 7 // 10 = 0
            # Gán giá trị của nút đó thành giá trị cộng
            curr.next = ListNode(val % 10) # eg: 7 % 10 = 7 // Dán vào ListNode curr
            # Di chuyển con trỏ đến nút tiếp theo
            curr = curr.next # eg: 7
            # Di chuyển con trỏ đến nút tiếp theo
            l1 = l1.next if l1 else None # eg: 4
            l2 = l2.next if l2 else None # eg: 6
        # Trả về danh sách liên kết kết quả
        return dummy.next # eg: 7 -> 0 -> 8

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Test
s = Solution()
print(s.addTwoNumbers(l1, l2))
# Output: 7 -> 0 -> 8

a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)

b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)

print(a.val)
print(a.next.val)
print(a.next.next.val)

print(b.val)
print(b.next.val)
print(b.next.next.val)

print("Number 1:", a.val + b.val)
print("Number 2:", a.next.val + b.next.val)
print("Verify", 10%10)
print("Number 3:", a.next.next.val + b.next.next.val)


