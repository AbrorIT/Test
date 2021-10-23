# class Airplane:
#     def __init__ (self, mark, model, year, max_speed):
#         self.mark = mark
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = 0
#         self.is_flying = False 



class Purse:
    def __init__ (self, valuta, name="неизвестно"):
        if valuta not in ("USD", "EUR", "KGS", "RUB"):
            raise("Только 4 валюты")
        self.valuta = valuta
        self.name = name
        self.money = 0.00

    def top_up_balance(self, howmany):
        self.money += howmany
        return howmany

    def top_down_balance(self, howmany):
        if self.money - howmany < 0:
            print("Недостаточно средств ")
            raise ValueError("Недостаточно средств")
        self.money -= howmany
        print(f"Успешно снял {howmany}")
        return f"остаток {self.money}"

    def info(self):
        print(f"{self.money}, {self.valuta}, {self.name}")


kuma = Purse("USD", "kuma")
kuma.top_up_balance(5000)
print(kuma.money)
kuma.top_down_balance(2000)
kuma.info()

    
