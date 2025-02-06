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

    def ring(self):
        print('Дзынь-дзынь!')


rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный')

print(rotary_phone.line_type)
rotary_phone.ring()

print(mobile_phone.line_type)
mobile_phone.ring()
