# 1. FizzBuzz varianti
# 1 dan 50 gacha sonlarni chop eting. 3 ga karrali sonlar uchun "Fizz", 5 ga karrali sonlar uchun "Buzz", ikkalasiga ham karrali bo'lsa "FizzBuzz" chop eting. Aks holda sonning o'zini chop eting.
# O'ylantiradigan joyi: if/elif shartlaringizning tartibi muhim — tartibni noto'g'ri qilsangiz, 15 ga karrali sonlar faqat "Fizz" deb chop etiladi.
def fizzbuzz():
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")   
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()

# 2. Raqamlar yig'indisi
# Berilgan butun sonning raqamlari yig'indisini qaytaring — sonni satrga (string) aylantirmasdan.
# Input: 1234 → Output: 10
# O'ylantiradigan joyi: raqamlarni birma-bir ajratib olish uchun % va // operatorlaridan foydalanishingiz, hamda siklingizning to'xtash shartini aniqlashingiz kerak.

def raqam(x):
    yigindi = 0
    while x > 0:
        raqam = x % 10
        yigindi += raqam
        x //= 10
    return yigindi 

print(raqam(1234)) 

# 3. Bu kabisa yil (leap year) emasmi?
# Berilgan yil kabisa yili bo'lsa True qaytaradigan funksiya yozing. Qoidalar: 4 ga bo'linadi, LEKIN 100 ga bo'linadigan yillar BUNDAN MUSTASNO, AGAR 400 ga ham bo'linmasa.
# 2000 → True   2100 → False   2024 → True   1900 → False
# O'ylantiradigan joyi: uchta shart, ikkitasi bir-biriga istisno — avval barcha to'rtta misolni qo'lda tekshirib chiqmasangiz, tartibni teskari qilib qo'yish oson.

def kabisa_yil(yil):
    if yil % 4 == 0:
        if yil % 100 == 0:
            if yil % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# 4. Sonni teskari aylantirish
# Berilgan butun sonning raqamlarini teskari tartibda qaytaring.
# Input: 1234 → Output: 4321
# Input: 1200 → Output: 21   (0021 emas)
# O'ylantiradigan joyi: satrga aylantirish taqiqlangan — teskari sonni faqat arifmetik amallar yordamida yarating.

def teskari_son(x):
    teskari = 0
    while x > 0:
        raqam = x % 10
        teskari = teskari * 10 + raqam
        x //= 10
    return teskari


# 5. Unlilarni sanash
# Berilgan gapda nechta unli tovush (a, e, i, o, u — katta-kichik harflarga bog'liq emas) borligini sanang.
# Input: "Hello World" → Output: 3
# O'ylantiradigan joyi: birinchi qarashda oddiy, lekin qaror qiling: har bir harfni ro'yxat bilan solishtirib tsikl yurasizmi, yoki .count() metodini besh marta chaqirasizmi? Qaysi biri aslida o'qish uchun soddaroq?

def unli_son(gap):
    unli = "aeiouAEIOU"
    soni = 0
    for harf in gap:
        if harf in unli:
            soni += 1
    return soni

print(unli_son("Hello World"))  


# 2-bosqich: Oddiy mantiq
# 6. Yagona (juftsiz) sonni toping
# Berilgan ro'yxatda har bir son ikki marta takrorlanadi, faqat bitta son bundan mustasno. Shu sonni toping — hozircha faqat oddiy sikllar va sanash yordamida
# Input: [4, 3, 2, 4, 1, 3, 2] → Output: 1


def yagona_son(sonlar):
    for son in sonlar:
        if sonlar.count(son) == 1:
            return son  
print(yagona_son([4, 3, 2, 4, 1, 3, 2]))


# 7. Oddiy parol tekshiruvchi
# Satr kamida 6 ta belgidan, katta harf VA kamida bitta raqam borligini tekshiring. True/False qaytaring.
# "Aabc123" → True
# "abcdef" → False  (raqam yo'q)
# "a1"     → False  (juda qisqa)
# "adasd123"     → False  (Katta harf yo’q)


def parol_tekshir(parol):
    if len(parol) < 6:
        return False
    katta_harf = False
    raqam = False
    for belgi in parol:
        if belgi.isupper():
            katta_harf = True
        elif belgi.isdigit():
            raqam = True
    return katta_harf and raqam