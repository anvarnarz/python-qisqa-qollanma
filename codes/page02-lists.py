# Ro'yxat yaratish
mevalar = ['olma','anor','uzum','banan']
narhlar = [3000, 5000, 4500, 12000]

# range() - sonlar ketma-ketligi
sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
sonlar = list(range(10,51,10)) # [10, 20, 30, 40, 50]

# Birinchi element
mevalar[0]

# Oxirgi element
mevalar[-1]

# Elementni o'zgartirish
mevalar[1] = 'anjir'

# Ro'yxatni kesish
sonlar[:2] # ro'yxat boshidan 2 element olish
narhlar[3:] # 4-elementdan ro'yxat oxirigacha keish
mevalar[2:4] # 2 va 3-elementlarni olish

# Ro'yxatdan nusxa olish
haridlar = mevalar[:]

# Ro'yxatga element qo'shish
cars = [] # bo'sh ro'yxat
cars.append('bmw')
cars.append('toyota')

# Ro'yxatdan element o'chirish
del mevalar[0] # 0-mevani o'chirdik

# Element sug'urib olish
meva1 = mevalar.pop() # oxirgi elementni sug'urib olish
meva2 = mevalar.pop(1) # 2-elemetni sug'urib olish

# Ro'yxat uzunligini ko'rish (elementlar soni)
len(mevalar)

# Ro'yxat elementlari bilan ishlash
for car in cars:
  print(cars)
 
nums = []
for x in range(11):
  nums.append(x**2) # 1-10 gacha sonlar kvadrati

# Bir qatorda ro'yxat yaratish
kvadratlar = [x**2 for x in range(11)] # 1-10 gacha sonlar kvadrati