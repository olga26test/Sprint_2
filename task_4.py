class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        cls.name = name
        email = f"{cls.name.lower()}@email.com" # добавила метод .lower(), т.к. эл.почта обычно в низком регистре
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment
        return cls.hourly_payment

    def salary(self):
        salary = self.hours * self.hourly_payment
        # кроме зарплаты добавила в возврат имя, часы и почту для наглядности
        return f'Сотрудник: {self.name}, отработанные часы: {self.hours}, эл. почта: {self.email}, зарплата за неделю: {salary}'

    
# дополнительно добавила вызовы методов для проверки их работы:
employee_salary_1 = EmployeeSalary.get_hours('Black', 2, 'black@mail.ru')
print(employee_salary_1.salary())

employee_salary_2 = EmployeeSalary.get_email('Smith', 30, 2)
print(employee_salary_2.salary())

employee_salary_3 = EmployeeSalary.set_hourly_payment(500)
print(EmployeeSalary.hourly_payment)
employee_salary_3 = EmployeeSalary('Lebedev', 10, 4, 'lebedev@mail.ru')
print(employee_salary_3.salary())

