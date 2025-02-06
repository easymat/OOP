class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        dial_type = dial_type_value

    def ring(self):
        print('Дзззззззыыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}')


class MobilePhone(Phone):

    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        self.network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    def start_game(self):
        print('Игра запущена!')


rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный', 'LTE')

print(rotary_phone.line_type)
rotary_phone.ring()

print(mobile_phone.line_type)
mobile_phone.ring()

print(mobile_phone.battery_type)
print(mobile_phone.network_type)
mobile_phone.start_game()
print(rotary_phone.__str__())