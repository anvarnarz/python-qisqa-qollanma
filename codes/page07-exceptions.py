# Excpetions (istisnolar) xatolarni ushlab, dastur xato berib
# to'xtab qolishining oldini oladi
yosh = input("Yoshingizni kiriting:")

try:
    yosh = int(yosh)
except ValueError:
    print("Butun son kiriting.")
else:
    print("Rahmat.")