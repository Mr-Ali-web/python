# def missing_number(nums):
#     n = len(nums)
#     return n * (n + 1) // 2 - sum(nums)
# from collections import Counter

# def first_uniq_char(s):
#     count = Counter(s)
#     for i, ch in enumerate(s):
#         if count[ch] == 1:
#             return i
#     return -1

# def merge_sorted(a, b):
#     i = j = 0
#     res = []
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             res.append(a[i])
#             i += 1
#         else:
#             res.append(b[j])
#             j += 1
#     res.extend(a[i:])
#     res.extend(b[j:])
#     return res


# if __name__ == "__main__":
#     print("missing_number:", missing_number([3, 0, 1]))
#     print("first_uniq_char:", first_uniq_char("leetcode"))
#     print("merge_sorted:", merge_sorted([1, 3, 5], [2, 4, 6]))


#1. Takroriy Elementlarni Olib Tashlash
#Ro'yxatdan takroriy elementlarni olib tashlab yangi ro'yxat yarating.
nim = [1, 2, 3, 4, 5, 1, 2, 3]


def remove_duplicates(nim):
    result = []
    for item in nim:
        if item not in result:
            result.append(item)
    return result

print("Remove duplicates:", remove_duplicates(nim))



#2. Ikkinchi Eng Katta Son
# Ro'yxatdagi ikkinchi eng katta sonni toping
lst = [1, 2, 3, 4, 5]


def second_largest(lst):
    unique_values = sorted(set(lst))
    if len(unique_values) < 2:
        return None
    return unique_values[-2]

print("Remove duplicates:", remove_duplicates(nim))
print("Second largest:", second_largest(lst))



# 3. Palindrom Tekshirish
# So'z oldidan va orqasidan bir xil o'qiladimi tekshiring.
s = "A man, a plan, a canal: Panama"


def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


print("Is palindrome:", is_palindrome(s))


# 4. Yetishmayotgan Sonni Topish
# Ketma-ketlikdagi yetishmayotgan sonни toping.
nums = [3, 0, 1]


def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


print("Missing number:", find_missing_number(nums))


# 5. Takrorlanishlar Sonini Hisoblash
# Har bir so'z necha marta uchrashganini hisoblang.

from collections import Counter

def count_occu(words):
    return Counter(words)

print("Occurrences:", count_occu(["apple", "banana", "apple", "cherry"]))


# 6. Saralash Algoritmi
# sorted() ishlatmasdan sonlarni o'sish tartibida saralang.

def sarala(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Bubble sort:", sarala([64, 34, 25, 12, 22, 11, 90]))

# 7. Talabalar Baholari
# O'rtacha baho va eng yuqori bahoni toping.

def student_grades(grades):
    average = sum(grades) / len(grades)
    highest = max(grades)
    return average, highest

print("Student grades:", student_grades([85, 90, 78, 92, 88]))

# 8. Kassa Masalasi
# Jami narxni hisoblang, eng qimmat mahsulotni toping va 100 dan katta narxlar sonini aniqlang.

def cash_register(prices):
    total = sum(prices)
    most_expensive = max(prices)
    count_above_100 = sum(1 for price in prices if price > 100)
    return total, most_expensive, count_above_100

print("Cash register:", cash_register([50, 150, 200, 75, 120]))
