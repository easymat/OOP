class Employee:
    vacation_days = 28

    def __init__(
            self,
            first_name: str,
            last_name: str,
            gender: str
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self._employee_id = self.__generate_employee_id(first_name, last_name, gender)
        self.remaining_vacation_days = self.vacation_days

    def __generate_employee_id(
            self,
            first_name: str,
            last_name: str,
            gender: str
    ):
        employee_id = hash(first_name + last_name + gender)
        return employee_id

    def consume_vacation(self, days: int):
        self.remaining_vacation_days -= days

    def get_remaining_vacation_days(self) -> int:
        return self.remaining_vacation_days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):

    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)

    def get_unpaid_vacation(self, first_vacation_day, number_of_days):
        self.first_day = first_vacation_day
        self.number_of_days = number_of_days

        return f'Начало неоплачиваемого отпуска: {self.first_day}, продолжительность: {self.number_of_days} дней.'


class PartTimeEmployee(Employee):

    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)


class OfficeEmployee(Employee):

    def __init__(self, first_name, last_name, gender, worker_class: int, salary: int):
        self.worker_class = worker_class
        self.__salary = salary
        super().__init__(first_name, last_name, gender)

    def get_remaining_vacation_days(self) -> int:
        return self.remaining_vacation_days + self.worker_class * 2

    def get_vacation_payment(self, days_of_vacation):
        self.how_much_to_pay = self.__salary * days_of_vacation // 60
        return self.how_much_to_pay


# Пример использования:
office_employee = OfficeEmployee(first_name='Иван', last_name='Иванов', gender='м', worker_class=2, salary=45000)

vacation_days = 10

office_employee.consume_vacation(vacation_days)

remaining_days = office_employee.get_remaining_vacation_days()
print(f'У сотрудника осталось {remaining_days} дн. отпуска.')

vacation_payment = office_employee.get_vacation_payment(vacation_days)
print(f'За {vacation_days} дн. отпуска сотрудник получит {vacation_payment} руб.')

#full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
#print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
#part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
#print(part_time_employee.get_vacation_details())
