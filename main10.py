# 1. Yetkazib berish buyurtmasini tekshirish
# Internet-do‘kon buyurtmani yetkazib berishdan oldin uning qiymati, manzili va mahsulot mavjudligini tekshiradi.
# Qoidalar:
# ●	Buyurtma qiymati 0 dan katta bo‘lishi kerak.
# ●	Agar mahsulot omborda bo‘lmasa, buyurtma rad etiladi.
# ●	Buyurtma qiymati 100 000 so‘m yoki undan ko‘p bo‘lsa, yetkazib berish bepul.
# ●	Boshqa holatlarda shahar ichida yetkazib berish 15 000 so‘m, shahar tashqarisida 25 000 so‘m.
# ●	Yakuniy natijada buyurtma holati, yetkazib berish narxi va umumiy summa ko‘rsatiladi.
# Boshlang‘ich ma’lumotlar:
# order_total = 85000
# product_available = True
# inside_city = False
# Kutiladigan natija:
# Buyurtma qabul qilindi
# Yetkazib berish: 25000 so‘m
# Jami: 110000 so‘m
# Qo‘shimcha vazifa: Mahsulot mavjud emasligi boshqa qoidalardan oldin tekshirilsin.

order_total = 85000
product_available = True
inside_city = False

if order_total <= 0:
    print("Buyurtma qiymati 0 dan katta bo‘lishi kerak")
elif not product_available: 
    print("Mahsulot omborda mavjud emas, buyurtma rad etildi")
else:
    if order_total >= 100000:
        delivery_cost = 0
    else:
        delivery_cost = 15000 if inside_city else 25000

    final_total = order_total + delivery_cost

    print("Buyurtma qabul qilindi")
    print(f"Yetkazib berish: {delivery_cost} so‘m")
    print(f"Jami: {final_total} so‘m")



#     2. Mehmonxonada xona band qilish
# Mehmonxona mijozning yoshi, bo‘sh xona borligi va tunash kunlari soniga qarab bronni qabul qiladi.
# Qoidalar:
# ●	Tunash kunlari kamida 1 bo‘lishi kerak.
# ●	18 yoshdan kichik mijoz faqat voyaga yetgan hamroh bilan joylashishi mumkin.
# ●	Bo‘sh xona bo‘lmasa, bron rad etiladi.
# ●	3 kundan ortiq qolgan mijozga umumiy xona narxidan 10% chegirma beriladi.
# ●	Bron qabul qilinsa, yakuniy narx hisoblanadi.
# Boshlang‘ich ma’lumotlar:
# age = 17
# has_adult_companion = True
# room_available = True
# nights = 4
# price_per_night = 200000
# Kutiladigan natija:
# Bron qabul qilindi
# Jami: 720000 so‘m
# Qo‘shimcha vazifa: Avval bron qilish mumkinligini tekshiring, keyin chegirmani hisoblang.


age = 17               
has_adult_companion = True
room_available = True
nights = 4

price_per_night = 200000

if nights < 1:
    print("Tunash kunlari kamida 1 bo‘lishi kerak")
elif age < 18 and not has_adult_companion:
    print("18 yoshdan kichik mijoz faqat voyaga yetgan hamroh bilan joylashishi mumkin")
elif not room_available:
    print("Bo‘sh xona mavjud emas, bron rad etildi")
else:
    total_price = nights * price_per_night

    if nights > 3:
        discount = total_price * 0.10
        total_price -= discount

    print("Bron qabul qilindi")
    print(f"Jami: {total_price} so‘m")


# 3. Taksi buyurtmasini baholash
# Taksi ilovasi safar masofasi, ob-havo va haydovchi mavjudligiga qarab narxni belgilaydi.
# Qoidalar:
# ●	Masofa 0 dan katta bo‘lishi kerak.
# ●	Haydovchi topilmasa, buyurtma bajarilmaydi.
# ●	Boshlang‘ich to‘lov 5 000 so‘m, har bir kilometr uchun 3 000 so‘m.
# ●	Yomg‘ir yog‘ayotgan bo‘lsa, hisoblangan narxga 20% qo‘shiladi.
# ●	Masofa 30 km dan ortiq bo‘lsa, safar qo‘lda tasdiqlanishi kerak.
# Boshlang‘ich ma’lumotlar:
# distance = 12
# is_raining = True
# driver_available = True
# Kutiladigan natija:
# Safar tasdiqlandi
# Yakuniy narx: 48200 so‘m
# Qo‘shimcha vazifa: 30 km dan ortiq safar uchun narxni oddiy tasdiqlangan safar sifatida chiqarmang.


distance = 12
is_raining = True
driver_available = True

if distance <= 0:
    print("Masofa 0 dan katta bo‘lishi kerak")
elif not driver_available:
    print("Haydovchi topilmadi, buyurtma bajarilmaydi")
else:
    base_fare = 5000
    cost_per_km = 3000
    total_cost = base_fare + (distance * cost_per_km)

    if is_raining:
        total_cost *= 1.20

    if distance > 30:
        print("Safar qo‘lda tasdiqlanishi kerak")
    else:
        print("Safar tasdiqlandi")

    print(f"Yakuniy narx: {total_cost} so‘m")


#     4. Onlayn to‘lovni xavfsizlik tekshiruvidan o‘tkazish
# To‘lov tizimi xarid summasi, hisob holati va foydalanuvchi joylashuvini tekshiradi.
# Qoidalar:
# ●	Summa 0 dan katta bo‘lishi kerak.
# ●	Hisob bloklangan bo‘lsa, to‘lov rad etiladi.
# ●	Summa 5 000 000 so‘mdan katta bo‘lsa, qo‘lda tekshirishga yuboriladi.
# ●	Summa 1 000 000 so‘mdan katta va joylashuv notanish bo‘lsa, qo‘lda tekshirishga yuboriladi.
# ●	Qolgan to‘lovlar tasdiqlanadi.
# Boshlang‘ich ma’lumotlar:
# amount = 1800000
# account_blocked = False
# known_location = False
# Kutiladigan natija:
# To‘lov qo‘lda tekshirishga yuborildi
# Qo‘shimcha vazifa: Shartlar tartibini tanlang va bitta tranzaksiya uchun faqat mos natijani chiqaring


amount = 1800000
account_blocked = False
known_location = False      

if amount <= 0:
    print("Summa 0 dan katta bo‘lishi kerak")
elif account_blocked:
    print("Hisob bloklangan, to‘lov rad etildi")
elif amount > 5000000:
    print("To‘lov qo‘lda tekshirishga yuborildi")
elif amount > 1000000 and not known_location:
    print("To‘lov qo‘lda tekshirishga yuborildi")
else:
    print("To‘lov tasdiqlandi")


# 5. Ishga qabul qilish uchun dastlabki saralash
# Kompaniya nomzodning tajribasi, texnik sinov bali va suhbat natijasini ko‘rib chiqadi.
# Qoidalar:
# ●	Tajriba yillari va sinov bali manfiy bo‘lishi mumkin emas; sinov bali 100 dan oshmasligi kerak.
# ●	Texnik sinovdan 85 yoki undan yuqori ball olgan va suhbatdan o‘tgan nomzod keyingi bosqichga o‘tadi.
# ●	Sinovdan kamida 70 ball olgan va suhbatdan o‘tgan nomzod qo‘shimcha ko‘rib chiqiladi.
# ●	Qolgan nomzodlar rad etiladi.
# Boshlang‘ich ma’lumotlar:
# experience_years = 2
# technical_score = 88
# interview_passed = True
# Kutiladigan natija:
# Keyingi bosqichga o‘tdi
# Qo‘shimcha vazifa: Yuqori ball olgan nomzodni pastroq toifadagi natijaga tushirib yubormang.


experience_years = 2
technical_score = 88
interview_passed = True

if experience_years <= 0 or experience_years >= 100:
  print("tajriba yuq yoki no aniq ")
elif technical_score >= 85 and interview_passed:
  print("keyingi bosqichga otdiz ")
elif technical_score >= 70 and interview_passed:
  print("qoshimcha koribchiqilmoqda")
else:
  print("rad etildi ")



  membership_active = True
payment_complated = False
has_debt = True


# 6. Sport zaliga a’zolikni yangilash
# Sport zali mijozning a’zolik muddati, to‘lov holati va qarzdorligini tekshiradi.
# Qoidalar:
# ●	A’zolik muddati tugamagan va to‘lov qilingan bo‘lsa, kirishga ruxsat beriladi.
# ●	To‘lov qilinmagan bo‘lsa, avval to‘lovni amalga oshirish haqida xabar beriladi.
# ●	Mijozda qarzdorlik bo‘lsa, qarzdorlik bartaraf etilmaguncha kirish taqiqlanadi.
# ●	A’zolik muddati tugagan bo‘lsa, yangilash kerakligi ko‘rsatiladi.
# ●	Bir nechta muammo mavjud bo‘lsa, qarzdorlik haqidagi xabar ustuvor bo‘lsin.
# Boshlang‘ich ma’lumotlar:
# membership_active = True
# payment_completed = False
# has_debt = True
# Kutiladigan natija:
# Kirish taqiqlangan: qarzdorlik mavjud
# Qo‘shimcha vazifa: Ustuvorlikni if-elif-else orqali ifodalang.


if membership_active and not payment_complated:
  print("hush kelibsiz")
elif payment_complated:
  print("tolov qabul qilinmagan")
elif not has_debt:
  print("qarzni uz bich ")
elif not membership_active:
  print("azolikgingiz tugagan yangilen ")
else:
  if not membership_active and not has_debt and payment_complated:
    print("qarzdorlik ")





    