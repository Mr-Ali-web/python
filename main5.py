# 1. Eng katta son va uning indeksini topish
# Sonlar ro‘yxati berilgan. Ro‘yxatdagi eng katta sonni va uning indeksini toping. Faqat sonning o‘zini emas, balki u qaysi indeksda joylashganini ham qaytaring.

# Misol — kirish:

# nums = [4, 9, 2, 15, 7]

# Kutiladigan natija:

# Eng katta son: 15
# Indeksi: 3

# Eslatma: Python’da indekslar 0 dan boshlanadi.

nums = [4, 9, 2, 15, 7]
max_num = nums[0]
max_index = 0
for i in range(1, len(nums)):
    if nums[i] > max_num:
        max_num = nums[i]
        max_index = i
print(f"Eng katta son: {max_num}")
print(f"Indeksi: {max_index}")


# 2. Sonlarni juft va toq ro‘yxatlarga ajratish
# Sonlar ro‘yxati berilgan. Bitta aylanish (pass) davomida sonlarni ikkita yangi ro‘yxatga ajrating: juft sonlar va toq sonlar.

# Misol — kirish:

# nums = [1, 2, 3, 4, 5, 6]

# Kutiladigan natija:

# Juft sonlar: [2, 4, 6]
# Toq sonlar: [1, 3, 5]

# Talab: ro‘yxatni bir marta aylanib chiqish kifoya.

nums = [1, 2, 3, 4, 5, 6]
even_nums = []
odd_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)
print("Juft sonlar:", even_nums)
print("Toq sonlar:", odd_nums)


# 3. Manfiy sonlarni 0 bilan almashtirish
# Sonlar ro‘yxati berilgan. Har bir manfiy sonni 0 bilan almashtiring. O‘zgarishlar aynan berilgan ro‘yxatning o‘zida bajarilsin (in place), yangi ro‘yxat yaratmang.

# Misol — kirish:

# nums = [3, -1, 0, -7, 5]

# Kutiladigan natija:

# [3, 0, 0, 0, 5]

# Talab: mavjud ro‘yxat elementlarini indekslar orqali o‘zgartiring.

nums = [3, -1, 0, -7, 5]
for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0
print(nums)


# 4. Uzunligi N dan katta bo‘lgan so‘zlarni tanlash
# So‘zlar ro‘yxati berilgan. Foydalanuvchi kiritgan N sonidan uzun bo‘lgan so‘zlardan yangi ro‘yxat tuzing. So‘z uzunligi N dan qat’iy katta bo‘lishi kerak.

# Misol — kirish:

# words = ["olma", "anor", "banan", "uzum", "shaftoli"]
# N = 4

# Kutiladigan natija:

# ["banan", "shaftoli"]

# Eslatma: uzunligi aynan 4 ta belgidan iborat bo‘lgan “olma”, “anor” va “uzum” tanlanmaydi.

words = ["olma", "anor", "banan", "uzum", "shaftoli"]
N = 4
long_words = []
for word in words:
    if len(word) > N:
        long_words.append(word)
print(long_words)


# Sonlar ro‘yxati o‘sish tartibida joylashgan yoki joylashmaganini aniqlang. sorted() funksiyasidan foydalanmang; yonma-yon turgan elementlarni taqqoslang.

# Misol — kirish:

# nums = [1, 2, 2, 5, 9]

# Kutiladigan natija:

# True

# Tartib o‘suvchi bo‘lishi uchun har bir keyingi son oldingisidan kichik bo‘lmasligi kerak. Masalan, [1, 4, 3] uchun natija False.

nums = [1, 2, 2, 5, 9]
is_increasing = True
for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        is_increasing = False
        break
print(is_increasing)


# 6. Imtihon natijalarini toifalar bo‘yicha sanash
# Imtihon ballari ro‘yxati berilgan. Bir marta aylanish davomida quyidagi toifalarning har birida nechta natija borligini hisoblang: A — 90 va undan yuqori; B — 80–89; C — 70–79; 70 dan past — alohida toifa.

# Misol — kirish:

# scores = [95, 82, 76, 68, 90, 84, 59]

# Kutiladigan natija:

# A: 2
# B: 2
# C: 1
# 70 dan past: 2

# Talab: har bir toifa uchun alohida hisoblagich (counter) ishlating va ro‘yxatni faqat bir marta aylanib chiqing.

scores = [95, 82, 76, 68, 90, 84, 59]
count_A = 0
count_B = 0
count_C = 0
count_below_70 = 0  

for score in scores:
    if score >= 90:
        count_A += 1
    elif score >= 80:
        count_B += 1
    elif score >= 70:
        count_C += 1
    else:
        count_below_70 += 1

print(f"A: {count_A}")
print(f"B: {count_B}")
print(f"C: {count_C}")
print(f"70 dan past: {count_below_70}")


# 7. Ketma-ket o‘sib boruvchi eng uzun bo‘lakni topish
# Sonlar ro‘yxatida ketma-ket elementlari qat’iy o‘sib boradigan eng uzun uzluksiz bo‘lakni toping. Natijada shu bo‘lakning uzunligini aniqlang.

# Misol — kirish:

# nums = [1, 2, 3, 1, 2, 9, 10]

# Kutiladigan natija:

# Eng uzun o‘suvchi bo‘lak: [1, 2, 3]
# Uzunligi: 3

# Faqat yonma-yon elementlar hisobga olinadi. [1, 2, 3] va [1, 2, 9, 10] bo‘laklaridan ikkinchisi ham o‘suvchi va uzunligi 4 — shuning uchun ushbu misolning to‘g‘ri natijasi [1, 2, 9, 10], uzunligi 4.

nums = [1, 2, 3, 1, 2, 9, 10]
max_length = 1
current_length = 1
start_index = 0
max_start_index = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            max_start_index = start_index
        current_length = 1
        start_index = i
        if current_length > max_length:
            max_length = current_length
            max_start_index = start_index

print(f"Eng uzun o‘suvchi bo‘lak: {nums[max_start_index:max_start_index + max_length]}")
print(f"Uzunligi: {max_length}")