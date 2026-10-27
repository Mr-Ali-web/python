# 1. Haroratlarni toifalarga ajratish
# Haroratlar ro‘yxati berilgan. Bir marta sikldan foydalanib, issiq (> 30), mo‘tadil (15–30) va sovuq (< 15) kunlar sonini hisoblang. Uchta hisoblagichdan foydalaning.

# Namuna:

# temperatures = [12, 18, 35, 30, 8, 27, 32, 14]

# Kutiladigan natija:
# Issiq kunlar: 2
# Mo'tadil kunlar: 3
# Sovuq kunlar: 3

# Eslatma: 15 va 30 daraja mo‘tadil toifaga kiradi.

temperatures = [12, 18, 35, 30, 8, 27, 32, 14]
hot_days = 0
moderate_days = 0
cold_days = 0

for temp in temperatures:
    if temp > 30:
        hot_days += 1
    elif 15 <= temp <= 30:
        moderate_days += 1
    else:
        cold_days += 1

print(f"Issiq kunlar: {hot_days}")
print(f"Mo'tadil kunlar: {moderate_days}")
print(f"Sovuq kunlar: {cold_days}")


# 2. Mahalliy maksimumni topish (Local Peak)
# Sonlar ro‘yxatidan chap va o‘ng qo‘shnisidan katta bo‘lgan birinchi sonni toping. Birinchi va oxirgi elementlarni tekshirmang, chunki ularning ikkala tomonida ham qo‘shni yo‘q.

# Namuna:

# numbers = [2, 5, 3, 8, 4, 6, 1]

# Kutiladigan natija:
# 5

# Eslatma: 5 > 2 va 5 > 3, shuning uchun u shartga mos keladigan birinchi element.

numbers = [2, 5, 3, 8, 4, 6, 1]
local_peak = None

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        local_peak = numbers[i]
        break

print(local_peak)

# 3. Voyaga yetmaganlarni hisoblash
# Yoshlar ro‘yxati berilgan. 18 yoshga to‘lmaganlar sonini va ular orasidagi eng kichik yoshni bitta siklda aniqlang.

# Namuna:

# ages = [21, 16, 14, 19, 17, 12, 25]

# Kutiladigan natija:
# Voyaga yetmaganlar soni: 4
# Eng kichik yosh: 12

# Eslatma: Agar ro‘yxatda voyaga yetmaganlar bo‘lmasa, bu holatni ham to‘g‘ri qayta ishlang.


ages = [21, 16, 14, 19, 17, 12, 25]
minor_count = 0
min_age = None

for age in ages:
    if age < 18:
        minor_count += 1
        if min_age is None or age < min_age:
            min_age = age

print(f"Voyaga yetmaganlar soni: {minor_count}")
print(f"Eng kichik yosh: {min_age}")



# 4. Baholarni harfli bahoga aylantirish
# Talaba ismi va sonli bahosi saqlangan lug‘at berilgan. Har bir talabaning ismini va bahosiga mos harfli bahosini chiqaring.

# Namuna:

# grades = {
#    "Ali": 95,
#    "Vali": 82,
#    "Malika": 71,
#    "Sardor": 45
# }

# Kutiladigan natija:
# Ali: A
# Vali: B
# Malika: C
# Sardor: F

# Eslatma: Baholash mezoni: 90–100 → A; 80–89 → B; 60–79 → C; 0–59 → F.

grades = {
    "Ali": 95,
    "Vali": 82,
    "Malika": 71,
    "Sardor": 45
}

for student, score in grades.items():
    if 90 <= score <= 100:
        letter_grade = "A"
    elif 80 <= score <= 89:
        letter_grade = "B"
    elif 60 <= score <= 79:
        letter_grade = "C"
    else:
        letter_grade = "F"

    print(f"{student}: {letter_grade}")



# 5. Matndagi so‘zlar sonini hisoblash
# Gapdagi har bir so‘z necha marta uchraganini lug‘at yordamida hisoblang. Katta-kichik harflarni farqlamang va tinish belgilarini olib tashlang. Masalan, “Cat” va “cat.” bir xil so‘z hisoblanadi.

# Namuna:

# sentence = "Cat, dog, cat! Dog. CAT."

# Kutiladigan natija:
# {"cat": 3, "dog": 2}

# Eslatma: Natijadagi so‘zlarni kichik harflarda saqlang.


sentence = "Cat, dog, cat! Dog. CAT."
words = sentence.lower().strip(".,!?").split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
