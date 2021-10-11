class Foydalanuvchi:
    """Foydalanuvchi klassi"""

    def __init__(self, ism, familiya, email):
        """Foydalanuvchi xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.email = email

    def get_info(self):
        """Foydalanuvchi haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. email: {self.email}"


sariqdev = Foydalanuvchi("Anvar", "Narzullaev", "sariqdev@gmail.com")
print(sariqdev.get_info())

# Boshqa klassdan yangi klass yaratish vorislik deyiladi
class Talaba(Foydalanuvchi):
    """Talaba klassi"""

    def __init__(self, ism, familiya, email, talabaID):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, email)
        self.talabaID = talabaID
        self.bosqich = 1


# Voris klass super klassning metodlariga murojat qila oladi
talaba = Talaba("Alijon", "Valiyev", "ali2020@gmail.com", "N00111")
print(talaba.get_info())

# Polimorfizm - voris klass super klassdan meros qolgan metodni o'zgartirishi
class Talaba(Foydalanuvchi):
    """Talaba klassi"""

    def __init__(self, ism, familiya, email, talabaID):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, email)
        self.talabaID = talabaID
        self.bosqich = 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}, ID:{self.talabaID}"


talaba = Talaba("Alijon", "Valiyev", "ali2020@gmail.com", "N00111")
print(talaba.get_info())

# Inkapsulyasiya - obyektning xususiyatlariga murojaat qilishni yopish
class Avto:
    """Avtomobil klassi"""

    def __init__(self, model, rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km

    def get_km(self):
        return self.__km

    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")
