# Lug'atdagi ma'lumotlar ikki qismdan iborat: kalit so'z va qiymat
car = {'model':'ferrari','rang':'qizil'}

# Lug'at elementiga kalit orqali murojat qilinadi
print(f"Avtomobil modeli {car['model']}, rangi {car['rang']}")

# Lug'atga yangi element qo'shish
car['yil']=2010
car['narh']=100000

# Lug'atdan element o'chirish
del car['narh']

# .items() - Lug'atdagi barcha elementlarni ko'rish
print(car.items())

# .keys() - Lug'at kalit so'zlarini ko'rish
print(car.keys())

# .values() - Lug'atdagi qiymatlarni ko'rish
print(car.values())

# for yordamida lug'at elementlarini chaqirish
telefonlar = {
    'ali':'iphone 12',
    'vali':'galaxy s21',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for kalit, qiymat in telefonlar.items():
    print(f"{kalit.title()}ning telefoni {qiymat}")