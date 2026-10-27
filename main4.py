# 1. Ro‘yxatni teskari tartibda chiqarish (Reverse a List)
# Ro‘yxat berilgan. for yoki while siklidan foydalanib, ro‘yxat elementlarini teskari tartibda joylashtiring.
# Cheklov: Slicing ([::-1]) va .reverse() metodidan foydalanmang

whl = [1, 2, 3, 4, 5]
i = len(whl) - 1
while i >= 0:
    print(whl[i], end=' ')
    i -= 1
print() 

# 2. Ikkita ro‘yxat elementlarini qo‘shish (Element-wise Sum)
# Uzunligi bir xil bo‘lgan ikkita ro‘yxat berilgan. Ularning mos indekslarda joylashgan elementlarini qo‘shib, natijalarni uchinchi ro‘yxatga joylashtiring.
# a = [1, 2, 3]
# b = [4, 5, 6]
# Natija = [5, 7, 9]

a = [1, 2, 3]
b = [4, 5, 6]
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
print("Element-wise sum:", result)


# 3. Talabalar baholarini lug‘atda saqlash (Student Grades)
# Talabalarning ismi va bahosini saqlaydigan lug‘at (dictionary) yarating. So‘ng bahosi 80 dan yuqori bo‘lgan barcha talabalarni ekranga chiqaring.
# grades = {
#    "Ali": 85,
#    "Vali": 72,
#    "Malika": 95,
#    "Aziza": 80
# }
# Ali: 85
# Malika: 95

grades = {
    "Ali": 85,
    "Vali": 72,
    "Malika": 95,
    "Aziza": 80
}
for student, grade in grades.items():
    if grade > 80:
        print(f"{student}: {grade}")    


    #         4. Eng arzon mahsulotni topish (Lowest Price)
    # Mahsulotlar nomi va ularning narxlarini saqlaydigan lug‘at berilgan. Eng arzon mahsulotning nomi va narxini ekranga chiqaring.
    # prices = {
    #    "Olma": 12000,
    #    "Banan": 18000,
    #    "Nok": 10000,
    #    "Uzum": 15000
    # }
    # Nok: 10000
    
prices = {
    "Olma": 12000,
    "Banan": 18000,
    "Nok": 10000, 
    "Uzum": 15000
}
for product, price in prices.items():
    if price == min(prices.values()):
        print(f"{product}: {price}")
