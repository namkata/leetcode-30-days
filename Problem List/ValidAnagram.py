"""
En:
- Given two strings s and t, return true if t is an anagram of s, and false otherwise.
- An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
- Example 1:
    - Input: s = "anagram", t = "nagaram"
    - Output: true
- Example 2:
    - Input: s = "rat", t = "car"
    - Output: false
----------
Vi:
- Cho 2 chuỗi s và t, trả về true nếu t là 1 anagram của s, và false nếu không phải.
- Anagram là 1 từ hoặc cụm từ được tạo thành bằng cách sắp xếp lại các chữ cái của 1 từ khác, thường sử dụng tất cả các chữ cái gốc đúng 1 lần.
- Ví dụ 1:
    - Input: s = "anagram", t = "nagaram"
    - Output: true
- Ví dụ 2:
    - Input: s = "rat", t = "car"
    - Output: false
"""

"""
Solutions:
Mục tiêu là sắp xếp lại t thành 1 chuỗi giống s
- Cách 1: Sử dụng hàm sort 
    - Sắp xếp lại 2 chuỗi s và t
    - So sánh 2 chuỗi đã sắp xếp
    Eg: s = "anagram", t = "nagaram"
        sorted(s) = ['a', 'a', 'g', 'n', 'r', 'm']
        sorted(t) = ['a', 'a', 'g', 'n', 'r', 'm']
    
    Ưu điểm:
    - Dễ implement
    - Không cần phải đếm số lần xuất hiện của từng ký tự
    Nhược điểm:
    - Phải sắp xếp lại 2 chuỗi, có thể tốn nhiều thời gian
    - Nếu 2 chuỗi có độ dài khác nhau, thì phải so sánh độ dài trước, có thể tốn nhiều thời gian

- Cách 2: Sử dụng hàm count
    - Đếm số lần xuất hiện của từng ký tự trong chuỗi s
    - So sánh số lần xuất hiện của từng ký tự trong chuỗi t
    Eg: s = "anagram", t = "nagaram"
        Counter(s) = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        Counter(t) = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
    
    Ưu điểm:
    - Dễ implement
    - Không cần phải sắp xếp lại 2 chuỗi
    Nhược điểm:
    - Nếu 2 chuỗi có độ dài khác nhau, thì phải so sánh độ dài trước, có thể tốn nhiều thời gian

- Cách 3: Sử dụng hàm set (Kiem tra thi sai, tai vi no chi dua ky tu thoi)
    - Tạo 1 set từ chuỗi s
    - So sánh set của s và t
    - Nếu 2 set giống nhau, thì t là 1 anagram của s
    Eg: s = "anagram", t = "nagaram"
        set(s) = {'a', 'n', 'g', 'r', 'm'}
        set(t) = {'a', 'n', 'g', 'r', 'm'}
    
    Ưu điểm:
    - Dễ implement
    - Không cần phải sắp xếp lại 2 chuỗi
    Nhược điểm:
    - Nếu 2 chuỗi có độ dài khác nhau, thì phải so sánh độ dài trước, có thể tốn nhiều thời gian
    - Nếu 2 chuỗi có 1 ký tự khác nhau, thì phải so sánh từng ký tự, có thể tốn nhiều thời gian

- Cách 4: Sử dụng hàm set và count
    - Tạo 1 set từ chuỗi s
    - So sánh set của s và t
    - Nếu 2 set giống nhau, thì so sánh số lần xuất hiện của từng ký tự
    Eg: s = "anagram", t = "nagaram"
        set(s) = {'a', 'n', 'g', 'r', 'm'}
        set(t) = {'a', 'n', 'g', 'r', 'm'}
        Counter(s) = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

Hàm sort:
    - Sắp xếp lại 2 chuỗi s và t
    - So sánh 2 chuỗi đã sắp xếp

Hàm count:
    - Đếm số lần xuất hiện của từng ký tự _srong chuỗi s
    - So sánh số lần xuất hiện của từng ký tự trong chuỗi t

Hàm set:
    - Tạo 1 set từ chuỗi s
    - So sánh set của s và t

Hàm set và count:
    - Tạo 1 set từ chuỗi s
    - So sánh set của s và t
    - Nếu 2 set giống nhau, thì so sánh số lần xuất hiện của từng ký tự

Tôi muốn tự ghi hàm sắp xếp lại:
def sort_string(s: str) -> str:
    s = list(s)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]
    return ''.join(s)
"""

from typing import Counter

class Solution:
    # Correct
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    # Correct
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    # Wrong
    def isAnagram3(self, s: str, t: str) -> bool:
        # Missing s=aa, t=a
        return set(s) == set(t)

# s = 'anagram'
# t = 'nagaram'
# print(Solution().isAnagram(s, t))
# print(Solution().isAnagram2(s, t))
# print(Solution().isAnagram3(s, t))

# s = 'rat'
# t = 'car'
# print(Solution().isAnagram(s, t))
# print(Solution().isAnagram2(s, t))
# print(Solution().isAnagram3(s, t))

s = "aa"
t = "a"
print(Solution().isAnagram(s, t))
print(Solution().isAnagram2(s, t))
print(Solution().isAnagram3(s, t))