# 1. Bankomatdan pul yechish
# Bankomat foydalanuvchining hisobidagi mablag‘ va yechmoqchi bo‘lgan pul miqdorini tekshiradi.
# Qoidalar:
# • Pul miqdori musbat bo‘lishi kerak.
# • Yechiladigan summa hisobdagi mablag‘dan oshmasligi kerak.
# • Summa 50 000 so‘mga qoldiqsiz bo‘linishi kerak.
# • Barcha shartlar bajarilsa, pul yechishga ruxsat bering. Aks holda, rad etish sababini chiqaring.
# Namuna:
# balance = 500000
# amount = 175000
# Kutiladigan natija:
# Pul yechish rad etildi: summa 50 000 so‘mga karrali bo‘lishi kerak
# Qo‘shimcha vazifa: Shartlarni to‘g‘ri tartibda tekshiring: noto‘g‘ri summani hisobdagi mablag‘ bilan solishtirishdan oldin aniqlang.



balance = 500000
amount = 175000

if amount <= 0:
    print("Pul yechish rad etildi: summa musbat bo‘lishi kerak")
elif amount > balance:
    print("Pul yechish rad etildi: yechiladigan summa hisobdagi mablag‘dan oshmasligi kerak")
elif amount % 50000 != 0:
    print("Pul yechish rad etildi: summa 50 000 so‘mga karrali bo‘lishi kerak")
else:
    print("Pul yechishga ruxsat berildi")

# 2. Elektr energiyasi uchun to‘lov
# Uy xo‘jaligining bir oyda ishlatgan elektr energiyasi miqdori bo‘yicha to‘lovni hisoblang.
# Qoidalar:
# • Sarf manfiy bo‘lsa, qiymat noto‘g‘ri hisoblanadi.
# • Dastlabki 100 kVt·soat uchun har bir birlik 450 so‘m.
# • Keyingi 100 kVt·soat uchun har bir birlik 900 so‘m.
# • 200 kVt·soatdan ortiq qism uchun har bir birlik 1 500 so‘m.
# Namuna:
# consumption = 250
# Kutiladigan natija:
# Jami to‘lov: 210000 so‘m
# Qo‘shimcha vazifa: Tariflarni bosqichma-bosqich hisoblang. Eng yuqori tarifni barcha sarflangan birliklarga qo‘llamang.

consumption = 250
total_cost = 0

if consumption < 0:
    print("Sarf manfiy bo‘lsa, qiymat noto‘g‘ri hisoblanadi")
else:
    if consumption <= 100:
        total_cost = consumption * 450
    elif consumption <= 200:
        total_cost = 100 * 450 + (consumption - 100) * 900
    else:
        total_cost = 100 * 450 + 100 * 900 + (consumption - 200) * 1500

    print(f"Jami to‘lov: {total_cost} so‘m")

# 3. Yetkazib berish narxi
# Internet-do‘kon buyurtma qiymati va yetkazib berish hududiga qarab yetkazib berish narxini belgilaydi.
# Qoidalar:
# • Buyurtma 30 000 so‘mdan kam bo‘lsa, qabul qilinmaydi.
# • Buyurtma kamida 200 000 so‘m bo‘lsa, yetkazib berish bepul.
# • Boshqa holatlarda shahar ichida yetkazib berish 15 000 so‘m, shahar tashqarisida 30 000 so‘m.
# • Manfiy buyurtma qiymati noto‘g‘ri hisoblanadi.
# Namuna:
# order_total = 120000
# is_inside_city = False
# Kutiladigan natija:
# Buyurtma qabul qilindi
# Yetkazib berish narxi: 30000 so‘m
# Jami: 150000 so‘m
# Qo‘shimcha vazifa: Buyurtma qabul qilinishini, yetkazib berish narxini va yakuniy summani alohida aniqlang.



order_total = 120000
is_inside_city = False


if order_total < 0:
    print("Manfiy buyurtma qiymati noto‘g‘ri hisoblanadi")
elif order_total < 30000:
    print("Buyurtma qabul qilinmaydi")
else:
    if order_total >= 200000:
        delivery_cost = 0
    else:
        delivery_cost = 15000 if is_inside_city else 30000

    final_total = order_total + delivery_cost

    print("Buyurtma qabul qilindi")
    print(f"Yetkazib berish narxi: {delivery_cost} so‘m")
    print(f"Jami: {final_total} so‘m")



# 4. Universitetga qabul
# Universitet abituriyentning imtihon bali, suhbat natijasi va yoshini tekshiradi.
# Qoidalar:
# • Ball 0 dan 100 gacha bo‘lishi kerak; aks holda, qiymat noto‘g‘ri.
# • Yoshi 16 dan kichik abituriyent qabul qilinmaydi.
# • Ball kamida 85 bo‘lsa va suhbatdan muvaffaqiyatli o‘tsa, stipendiya beriladi.
# • Ball kamida 70 bo‘lsa va suhbatdan muvaffaqiyatli o‘tsa, o‘qishga qabul qilinadi.
# • Qolgan holatlarda rad etiladi.
# Namuna:
# score = 88
# age = 18
# interview_passed = True
# Kutiladigan natija:
# Stipendiya berildi
# Qo‘shimcha vazifa: Stipendiyaga loyiq abituriyentni oddiy qabul qilingan abituriyent sifatida belgilab qo‘ymang.


score = 88
age = 18
interview_passed = True

if score < 0 or score > 100:
    print("Ball noto‘g‘ri hisoblanadi")
elif age < 16:
    print("Yoshi 16 dan kichik abituriyent qabul qilinmaydi")
elif score >= 85 and interview_passed:
    print("Stipendiya berildi")
elif score >= 70 and interview_passed:
    print("O‘qishga qabul qilindi")
else:
    print("Rad etildi")



