# SyntaxError - dasturlash tili qoidalariga amal qilmaslik
print "Hello World!"

# EOL va EOF xatolik - qator (funksiya) oxirini yopmaslik
print("Hello World

# IndentantionError - bo'sh joy tashlamaslik yoki no'rin tashlash
def funksiya():
print("Hello!")

# NameError - mavjud bo'lmagan o'zgaruvchi (funksiya,obyekt)ga murojat
ism = 'Anvar'
print(isim) 

# ValueError - funksiyaga noto'g'ri qiymat yuborish
x = "5.6"
int(x)

# IndexError - ro'yxatda mavjud bo'lmagan indeksga murojat qilish
nums = [20, 10, 15]
nums[3]

# ZeroDivisionError - 0 ga bo'lish xatoligi
x = 10
y = 20/(x-10)
