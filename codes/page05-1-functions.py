# Oddiy funksiya
def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalom alaykum")


# Oddiy funksiyaga murojat qilish
salom_ber()

# Argument oluvchi funksiya
def salom_ber(ism):
    """Salom beruvchi funksiya"""
    print(f"Assalom alaykum, {ism}")


# Funksiyaga parametr uzatish
salom_ber("Anvar")

# Parametrlarga standart qiymat berish
def yosh_hisobla(tyil, joriy_yil=2021):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    yosh = joriy_yil - tyil
    print(f"Siz {yosh} yoshdasiz")


# Standart qiymatli funksiyaga parametr uzatish
yosh_hisobla(1983)
yosh_hisobla(1983, 2022)

# Funksiyadan qiymat qaytarish
def aylana_uzunligi(radius, pi=3.14159):
    return 2 * pi * radius


print(aylana_uzunligi(5))
