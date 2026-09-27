from abc import ABC ,abstractmethod

class Bank():
   accountno=""
   balance=""
   def __init__(self, accountno, balance):
      self.__accountno=accountno
      self.__balance=balance

   def get(self):
         print(self.__accountno)
         print(self.__balance)

bank= Bank ("51521212115","5000")
bank.get()
print(bank.accountno)


class internal(ABC):
    @abstractmethod
    def sugar(self):
        pass

    @abstractmethod
    def coffee(self):
        pass

    @abstractmethod
    def milk(self):
        pass

    @abstractmethod
    def water(self):
        pass


class coffeeButton(internal):
     

    def sugar(self):
        print("sugar added")

    def coffee(self):
         print("cofee added")

    def milk(self):
        print("milk added")

    def water(self):
         print("milk added")


coffee=coffeeButton()
coffee.sugar()
coffee.coffee()
coffee.milk()
coffee.milk()


               
