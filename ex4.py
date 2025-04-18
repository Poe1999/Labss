class BankAccount:
    __balance = None
    __transactions = []
    def __init__(self, balance):
        self.__balance = balance
        self.__transactions = []
# Создаем класс БанковскийСчет и назначаем Приватные атрибуты с помощью "__№"

    @property
    def balance(self):
        return self.__balance
#Геттер (позволяет получить доступ к приватным значениям класса) баланса

    def deposite(self, amount):
        while amount > 0:
            self.__balance += amount
            break
        self.__transactions.append(f"Deposite: +{amount}")
#Пополнение счета и записть транзакции

    def withdraw(self,amount):
        if (self.__balance - amount) >= 0:
            self.__balance -= amount
        else:
            print("Not enough money loser")
        self.__transactions.append(f"Withdraw: -{amount}")
#Снятие со счета и запись транзакции

    def transactions(self):
        return self.__transactions.copy() #копируем значения из списка
# Исория транзакций

# Пример:
if __name__ == "__main__":
    account = BankAccount(1000)

    account.deposite(200)
    account.withdraw(300)

    account.withdraw(1500)  # пробуем снять больше денег, чем есть на счете

    print(f"Balance: {account.balance}")  # выводим баланс
    print(account.transactions())  # выводим историю транзакций


