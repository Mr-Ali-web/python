# 1. Takrorlangan chipta IDlarini aniqlash
# Nosoz tizim yaratgan chipta IDlari ro‘yxati berilgan. Bir martadan ko‘p uchragan har bir IDni va uning necha marta uchraganini toping. Masalani bitta aylanishda, O(n) vaqt murakkabligida yeching.

# Misol — kirish:

# ticket_ids = [101, 203, 101, 305, 203, 101, 410]
# Kutiladigan natija:

# 101: 3 marta
# 203: 2 marta

ticket_ids = [101, 203, 101, 305, 203, 101, 410]
id_count = {}

for id in ticket_ids:
    id_count[id] = id_count.get(id, 0) + 1

for id, count in id_count.items():
    if count > 1:
        print(f"{id}: {count} marta")



# 2. So‘zlardagi harflar naqshini tekshirish
# Ikkita satr bir xil harf naqshiga amal qilishini tekshiring. Har bir harf doim bir xil harfga mos kelishi, ikki xil harf esa bitta harfga mos kelmasligi kerak.

# Misol — kirish:

# s1 = "paper"
# s2 = "title"
# Kutiladigan natija:

# True
# Tushuntirish: Moslik: p→t, a→i, p→t, e→l, r→e. Takrorlangan p harfi yana t ga mos keladi.

s1 = "paper"
s2 = "title"
if len(s1) != len(s2):
    print(False)
else:
    mapping = {}
    reverse_mapping = {}
    is_isomorphic = True
    i = 0

    while i < len(s1):
        char1 = s1[i]
        char2 = s2[i]

        if char1 in mapping:
            if mapping[char1] != char2:
                is_isomorphic = False
                break
        else:
            mapping[char1] = char2

        if char2 in reverse_mapping:
            if reverse_mapping[char2] != char1:
                is_isomorphic = False
                break
        else:
            reverse_mapping[char2] = char1

        i += 1

    print(is_isomorphic)
    