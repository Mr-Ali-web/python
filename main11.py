# 1. Talabaning davomatini tekshirish
# Universitet talabaning davomat foizi va bahosiga qarab imtihonga kirish yoki qayta topshirish holatini aniqlaydi.
# Qoidalar:
# • Davomat ham, ball ham 0 dan 100 gacha bo‘lishi kerak.
# • Davomat 60% dan kam bo‘lsa, talaba imtihonga qo‘yilmaydi.
# • Aks holda, ball 40 dan kam bo‘lsa, talaba qayta topshiradi.
# • Qolgan holatlarda talaba o‘tadi.
# Har bir juftlik (davomat, ball) tartibida berilgan.
# students = {
#     "Ali": (90, 75),
#     "Vali": (45, 80),
#     "Malika": (85, 30),
#     "Aziza": (70, 60)
# }
# Kutiladigan natija:
# Ali: O‘tdi
# Vali: Imtihonga qo‘yilmaydi
# Malika: Qayta topshiradi
# Aziza: O‘tdi
# Qo‘shimcha vazifa: Natijani aniqlashdan oldin ikkala qiymatni ham tekshiring.

students = {
    "Ali": (90, 75),
    "Vali": (45, 80),
    "Malika": (85, 30),
    "Aziza": (70, 60)
}

for student, (attendance, score) in students.items():
    if attendance < 0 or attendance > 100 or score < 0 or score > 100:
        print(f"{student}: Noto‘g‘ri qiymatlar")
    elif attendance < 60:
        print(f"{student}: Imtihonga qo‘yilmaydi")
    elif score < 40:
        print(f"{student}: Qayta topshiradi")
    else:
        print(f"{student}: O‘tdi")


# 2. Shubhali to‘lovlarni aniqlash
# Onlayn to‘lov tizimi tranzaksiya summasi, hisob holati va joylashuvga qarab xavfni baholaydi.
# Qoidalar:
# • Tranzaksiya summasi manfiy bo‘lsa, qiymat noto‘g‘ri.
# • Hisob faol bo‘lmasa, to‘lov rad etiladi.
# • Summa 10 000 000 so‘mdan katta bo‘lsa, qo‘lda tekshirishga yuboriladi.
# • Summa 2 000 000 so‘mdan katta bo‘lib, notanish joydan amalga oshirilsa, qo‘lda tekshirishga yuboriladi.
# • Qolgan to‘lovlar tasdiqlanadi.
# Namuna:
# amount = 3500000
# account_active = True
# familiar_location = False
# Kutiladigan natija:
# To‘lov qo‘lda tekshirishga yuborildi
# Qo‘shimcha vazifa: Noto‘g‘ri tranzaksiyalarni boshqa shartlarni tekshirishdan oldin aniqlang.

amount = 3500000
account_active = True
familiar_location = False

if amount < 0:
    print("Noto‘g‘ri qiymat")
elif not account_active:
    print("Hisob faol emas, to‘lov rad etildi")
elif amount > 10000000:
    print("To‘lov qo‘lda tekshirishga yuborildi")
elif amount > 2000000 and not familiar_location:
    print("To‘lov qo‘lda tekshirishga yuborildi")
else:
    print("To‘lov tasdiqlandi")
        
# 3. Yig‘ilish xonasini band qilish
# Kompaniyada sig‘imi va bo‘sh vaqt oralig‘i turlicha bo‘lgan yig‘ilish xonalari mavjud.
# Qoidalar:
# • Ishtirokchilar soni kamida 1 bo‘lishi kerak.
# • Tashqi yig‘ilishda kamida 5 ishtirokchi bo‘lishi kerak.
# • Xona sig‘imi ishtirokchilar soniga yetishi kerak.
# • So‘ralgan vaqt xona uchun bo‘sh bo‘lishi kerak.
# • Barcha talablarni bajargan xonalar orasidan eng kichigini tanlang.
# • Mos xona bo‘lmasa, “Mos xona mavjud emas” deb chiqaring.
# Namuna:
# rooms = {
#     "A xona": {
#         "capacity": 5,
#         "available_times": {"09:00", "10:00", "14:00"}
#     },
#     "B xona": {
#         "capacity": 12,
#         "available_times": {"10:00", "11:00", "14:00"}
#     },
#     "C xona": {
#         "capacity": 30,
#         "available_times": {"09:00", "11:00"}
#     }
# }

# participants = 10
# requested_time = "10:00"
# is_internal = True
# Kutiladigan natija:
# B xona tanlandi

rooms = {
    "A xona": {
        "capacity": 5,
        "available_times": {"09:00", "10:00", "14:00"}
    },
    "B xona": {
        "capacity": 12,
        "available_times": {"10:00", "11:00", "14:00"}
    },
    "C xona": {
        "capacity": 30,      
        "available_times": {"09:00", "11:00"}
    }
}

participants = 10
requested_time = "10:00"
is_internal = True

if participants < 1:
    print("Ishtirokchilar soni kamida 1 bo‘lishi kerak")
elif not is_internal and participants < 5:
    print("Tashqi yig‘ilishda kamida 5 ishtirokchi bo‘lishi kerak")
else:
    suitable_rooms = []
    for room_name, room_info in rooms.items():
        if room_info["capacity"] >= participants and requested_time in room_info["available_times"]:
            suitable_rooms.append((room_name, room_info["capacity"]))

    if not suitable_rooms:
        print("Mos xona mavjud emas")
    else:
        # Eng kichik sig‘imli xonani tanlash
        suitable_rooms.sort(key=lambda x: x[1])
        selected_room = suitable_rooms[0][0]
        print(f"{selected_room} tanlandi")



# 4. Avtoturargohga kirishni boshqarish
# Avtoturargoh tizimi joylar soni, transport turi va to‘lov holatini tekshiradi.
# Qoidalar:
# ●	Bo‘sh joylar soni 0 yoki undan kam bo‘lsa, yangi mashina kiritilmaydi.
# ●	To‘lov qilinmagan bo‘lsa, kirish taqiqlanadi.
# ●	Elektr avtomobillar uchun maxsus joy mavjud bo‘lsa, u yerga yo‘naltiriladi.
# ●	Boshqa mashinalar oddiy joyga yo‘naltiriladi.
# ●	Bo‘sh joylar soni manfiy qiymat bo‘lsa, tizim ma’lumot xatosini bildiradi.
# Boshlang‘ich ma’lumotlar:
# available_spaces = 4
# payment_completed = True
# is_electric = True
# special_spaces_available = True
# Kutiladigan natija:
# Kirishga ruxsat berildi
# Elektr avtomobili uchun maxsus joyga yo‘naltirildi
# Qo‘shimcha vazifa: Ma’lumot xatosi, joy yo‘qligi va to‘lov holatini to‘g‘ri ketma-ketlikda tekshiring.

available_spaces = 4
payment_completed = True
is_electric = True
special_spaces_available = True 

if available_spaces < 0:
    print("Ma’lumot xatosi")
elif available_spaces == 0:
    print("Bo‘sh joylar mavjud emas, kirish rad etildi")
elif not payment_completed:
    print("To‘lov qilinmagan, kirish rad etildi")
else:
    print("Kirishga ruxsat berildi")
    if is_electric and special_spaces_available:
        print("Elektr avtomobili uchun maxsus joyga yo‘naltirildi")
    else:
        print("Oddiy joyga yo‘naltirildi")


# 5. Yetkazib berish xodimini buyurtmaga biriktirish
# Logistika tizimi buyurtmaning og‘irligi, hududi va kuryerning bandlik holatiga qarab kuryerni tanlaydi.
# Qoidalar:
# ●	Buyurtma og‘irligi 0 dan katta bo‘lishi kerak.
# ●	Kuryer band bo‘lsa, unga yangi buyurtma berilmaydi.
# ●	Og‘irligi 20 kg dan katta buyurtma faqat og‘ir yuk tashiy oladigan kuryerga beriladi.
# ●	Shahar tashqarisidagi buyurtma uchun kuryer shu hududga xizmat ko‘rsatishi kerak.
# ●	Barcha shartlar bajarilsa, buyurtma biriktiriladi; aks holda sabab ko‘rsatiladi.
# Boshlang‘ich ma’lumotlar:
# weight = 24
# courier_busy = False
# can_carry_heavy = True
# serves_outside_city = True
# outside_city = True
# Kutiladigan natija:
# Buyurtma kuryerga biriktirildi
# Qo‘shimcha vazifa: Bir nechta mustaqil shartni and operatori bilan tekshiring.


weight = 24
courier_busy = False
can_carry_heavy = True
serves_outside_city = True
outside_city = True


if weight <= 0:
    print("Buyurtma og‘irligi 0 dan katta bo‘lishi kerak")
elif courier_busy:
    print("Kuryer band, buyurtma berilmaydi")
elif weight > 20 and not can_carry_heavy:
    print("Og‘irligi 20 kg dan katta buyurtma faqat og‘ir yuk tashiy oladigan kuryerga beriladi")
elif outside_city and not serves_outside_city:
    print("Shahar tashqarisidagi buyurtma uchun kuryer shu hududga xizmat ko‘rsatishi kerak")
else:
    print("Buyurtma kuryerga biriktirildi")

# 6. Uchrashuv uchun xona tanlash
# Ofis tizimi yig‘ilish qatnashchilari soni va so‘ralgan vaqtga qarab eng kichik mos xonani tanlaydi.
# Qoidalar:
# ●	Qatnashchilar soni kamida 1 bo‘lishi kerak.
# ●	Har bir xona uchun sig‘im va bo‘sh vaqtlar to‘plami beriladi.
# ●	Xona sig‘imi yetarli va so‘ralgan vaqt bo‘sh bo‘lishi kerak.
# ●	Shartlarga mos xonalar orasidan eng kichik sig‘imli xona tanlanadi.
# ●	Mos xona topilmasa, bu haqda xabar chiqaring.
# Boshlang‘ich ma’lumotlar:
# rooms = {
#     "A": {"capacity": 4, "times": {"09:00", "10:00"}},
#     "B": {"capacity": 10, "times": {"10:00", "11:00"}},
#     "C": {"capacity": 20, "times": {"09:00", "11:00"}}
# }
# participants = 8
# requested_time = "10:00"
# Kutiladigan natija:
# B xona tanlandi
# Qo‘shimcha vazifa: Xonalarni sikl bilan ko‘rib chiqing va eng kichik mos xonani tanlang.


rooms = {
    "A": {"capacity": 4, "times": {"09:00", "10:00"}},
    "B": {"capacity": 10, "times": {"10:       00", "11:00"}},
    "C": {"capacity": 20, "times": {"09:00", "11:00"}}
}
participants = 8
requested_time = "10:00"        

if participants < 1:
    print("Qatnashchilar soni kamida 1 bo‘lishi kerak")
else:
    suitable_rooms = []
    for room_name, room_info in rooms.items():
        if room_info["capacity"] >= participants and requested_time in room_info["times"]:
            suitable_rooms.append((room_name, room_info["capacity"]))

    if not suitable_rooms:
        print("Mos xona topilmadi")
    else:
        # Eng kichik sig‘imli xonani tanlash
        suitable_rooms.sort(key=lambda x: x[1])
        selected_room = suitable_rooms[0][0]
        print(f"{selected_room} xona tanlandi")



