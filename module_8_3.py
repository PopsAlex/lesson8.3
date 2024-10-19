class Car:

    def __init__(self, model, __vin, __numbers):
        self.model = str(model)
        self.__vin = int(__vin)
        self.__numbers = str(__numbers)
        Car.__is_valid_vin(self, self.__vin)
        Car.__is_valid_numbers(self, self.__numbers)
    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        if isinstance(self.vin_number, int) == False:
            raise IncorrectVinNumber(message ='Некорректный тип vin номер')
        elif 1000000 > self.vin_number or self.vin_number > 9999999:
            raise IncorrectVinNumber(message ='Неверный диапазон для vin номера')
        else:
            return True
    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if isinstance(self.numbers, str) == False:
            raise IncorrectCarNumbers(message ='Некорректный тип данных для номеров')
        elif len(self.numbers) != 6:
            raise IncorrectCarNumbers(message ='Неверная длина номера')
        else:
            return True
class IncorrectVinNumber(Exception):

   def __init__(self, message):
       self.message = message
class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')