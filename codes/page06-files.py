# Faylni ochish
faylnomi = "movies.txt"
with open(faylnomi) as file_object:
    qatorlar = file_object.readlines()

# Faylni qatormar-qator konsolga chiqarish
for qator in qatorlar:
    print(qator)

# Yangi faylga yozish - open(faylnomi,'w')
faylnomi = "kinolar.txt"
with open(faylnomi, "w") as file_object:
    file_object.write("Abdullajon \nTerminator")

# Mavjud faylga matn qo'shish - open(faylnomi,'a')
faylnomi = "kinolar.txt"
with open(faylnomi, "a") as file_object:
    file_object.write("\nBomba \nTitanic")
