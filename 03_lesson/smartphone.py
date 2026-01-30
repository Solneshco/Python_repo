
class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
    
    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Номер: {self.phone_number}"
    
    def call(self, number_to_call):
        print(f"Дозваниваемся с номера {self.phone_number} на номер {number_to_call}")
    
    def send_sms(self, number_to_sms, message):
        print(f"Отправляем SMS с номера {self.phone_number} на номер {number_to_sms}")
        print(f"Сообщение: {message}")