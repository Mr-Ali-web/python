# 1. Navbatma-navbat yig‘indi (Alternating Sum)
# Butun sonlardan iborat ro‘yxat berilgan. Juft indeksli elementlarni qo‘shing, toq indeksli elementlarni esa ayiring. Yakuniy natijani chiqaring.
# Misol:
# nums = [5, 3, 8, 2, 6]
# Natija:
# 14
# Izoh: 5 − 3 + 8 − 2 + 6 = 14.
# Cheklov: sum() funksiyasidan foydalanmang va qo‘shimcha ro‘yxat yaratmang.


from unittest import result


nums = [5,3,8,2,6]

result = 0 
for i in range(len(nums)):
    if i % 2 == 0:
        result += nums[i]
    else:
        result -= nums[i]
print(result)

# 2. Yo‘nalish o‘zgarishlarini sanash (Count Direction Changes)
# Sonlar ro‘yxati berilgan. O‘sish yo‘nalishi pasayishga yoki pasayish yo‘nalishi o‘sishga necha marta o‘zgarganini aniqlang. Ketma-ket teng qiymatlar yo‘nalish hisoblanmaydi.
# Misol:
# nums = [2, 5, 8, 6, 4, 7, 7, 3]
# Natija:
# 2
# Izoh: Yo‘nalish 8 sonidan keyin o‘sishdan pasayishga, 4 sonidan keyin esa pasayishdan o‘sishga o‘zgaradi. 7, 7 teng qiymatlari yangi yo‘nalish hosil qilmaydi.
# Cheklov: Sikllar va taqqoslashlardan foydalaning. Tashqi kutubxonalardan foydalanmang.


nums = [2,5,8,6,4,7,7,3]

direction = 0
count = 0

for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        new = 1
    elif nums[i] < nums[i-1]:
        new = -1
    else:
        new = 0 

    if new != 0 and direction != 0 and new != direction:
        count += 1

    direction = new

print(count) 

# 4. Eng uzun uzluksiz o‘suvchi ketma-ketlik (Longest Consecutive Increase)
# Butun sonlardan iborat ro‘yxat berilgan. Undagi har bir keyingi element oldingisidan qat’iy katta bo‘lgan eng uzun uzluksiz qismning uzunligini toping.
# Misol:
# nums = [2, 4, 6, 3, 5, 8, 10, 1]
# Natija:
# 4
# Izoh: Eng uzun uzluksiz o‘suvchi qism [3, 5, 8, 10]. Uning uzunligi 4 ga teng.
# Cheklov: Ro‘yxat bo‘ylab bir marta yurib yeching. Qo‘shimcha xotira sarfi O(1) bo‘lishiga intiling.

nums = [2,4,6,3,5,8,10,1]

current = 1
best = 1

for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        current += 1
    else:
        current = 1     

    if current > best:
        best = current 
print(best)

# 5. Teng yig‘indili bo‘linish (Balanced Split)
# Manfiy bo‘lmagan butun sonlardan iborat ro‘yxat berilgan. Ro‘yxatni shunday pozitsiyada ikkiga ajratish mumkinligini aniqlangki, chap tomondagi elementlar yig‘indisi o‘ng tomondagi elementlar yig‘indisiga teng bo‘lsin. Bo‘linish pozitsiyasidagi element ikkala yig‘indiga ham kiritilmaydi.
# Misol:
# nums = [1, 2, 3, 3]
# Natija:
# True
# Izoh: Chap qism [1, 2], yig‘indisi 3. O‘ng qism [3], yig‘indisi ham 3.
# Cheklov: Har bir pozitsiyada ikkala tomondagi yig‘indini qaytadan hisoblamang. Masalani O(n) vaqt ichida yechishga harakat qiling.

nums = [1,2,3,3]

total = sum(nums)
left = 0 
result = False

for i in range(len(nums)):
    right = total - left - nums[i]
    if left == right:
        result = True 
        break 
    left += nums[i]

print(result)

