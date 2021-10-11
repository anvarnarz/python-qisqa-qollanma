# while tsikli toki berilgan shart bajarilsa qaytarilaveradi
x = 1
while x <= 5:
    print(x)
    x += 1

# while tsikli yordamida dastur tugashini nazorat qilish mumkin
qiymat = ""
while qiymat != "ha":
    # Dastur badani
    qiymat = input("Dasturni to'xtatasizmi (ha/yo'q)? ")

# break yordamida tsiklni to'xtatish
while True:
    # Dastur badani
    qiymat = input("Dasturni to'xtatasizmi (ha/yo'q)? ")
    if qiymat == "ha":
        break
