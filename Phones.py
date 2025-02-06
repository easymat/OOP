class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value
        self._serial_number = id(dial_type_value)

    def ring(self):
        print('Дзззззззыыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}')

    def get_info(self):
        print(f'Серийный №: {self._serial_number}')


class MobilePhone(Phone):

    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        self.__network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    def start_game(self):
        print('Игра запущена!')

    def __str__(self):
        return f'У мобильного телефона {self.dial_type} тип набора номера'

    def get_info(self):
        print(f'Серийный №: {self._serial_number}, тип: {self.__network_type}')


rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный', 'LTE')
mobile_phone_2 = MobilePhone('кнопочный', 'GSM')

print(rotary_phone.line_type)
print(rotary_phone.dial_type)
rotary_phone.ring()

print(mobile_phone.line_type)
mobile_phone.ring()

print(mobile_phone.battery_type)
mobile_phone.start_game()

print(rotary_phone)
print(mobile_phone)

mobile_phone.call('35-05-23')

rotary_phone.get_info()
mobile_phone.get_info()
mobile_phone_2.get_info()
