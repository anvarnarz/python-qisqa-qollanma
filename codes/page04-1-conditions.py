x, y, yosh = 7, 8, 12
# Taqqoslash operatorlari
x == y  # tenglik
x != y  # tengsizlik
x > y  # katta
x >= y  # katta yoki teng
x < y  # kichik
x <= y  # kichik yoki teng

# Ro'yxat tarkibini tekshirish
cars = ["malibu", "lacetti", "toyota", "mazda"]
"nexia" in cars  # False qaytaradi
"nexia" not in cars  # True qaytaradi

# Mantiqiy qiymatlar
ish_tugadi = True
boshlandi = False

# if - yagona shartni tekshirish
if yosh < 7:
    print("Sizga avtobus bepul")

# if-elif-else - bir nechta shartlarni tekshirish
if yosh < 7:
    narh = 0
elif yosh < 12:
    narh = 5000
else:
    narh = 10000
print(f"Chipta narhi: {narh} so'm")
