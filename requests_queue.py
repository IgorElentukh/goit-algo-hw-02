from queue import Queue
from datetime import date
from enum import Enum


class ServiceType(Enum):
    PASS = "Видача закордонного паспорта"
    ID = "Видача ID картки"
    RESIDENCE = "Реєстрація місця проживання"
    TAX_ID = "Видача ІПН"


class Request:
    _last_date = date.today()
    _last_id = 0

    def __init__(self, request: ServiceType):
        self.check_date()
        Request._last_id += 1
        self.id = Request._last_id
        self.request = request
        self.created_at = date.today()

    @classmethod
    def check_date(cls):
        current_date = date.today()

        if current_date > cls._last_date:
            cls._last_date = current_date
            cls._last_id = 0


class Service:
    def __init__(self):
        self.requests = Queue()


    def generate_request(self, request):
        if not isinstance(request, ServiceType):
            print("Невідомий тип послуги")
            return
        
        new_request = Request(request)
        self.requests.put(new_request)
        print(f"Заявка №{new_request.id} створена: {request.value}")
              

    def process_requests(self):
        print("\n---- Починаємо обробку заявок -----")
        while not self.requests.empty():
            print(f"Заявка №{self.requests.get().id} була успішно оброблена")
        else:
            print("\nНа даний момент немає жодної заявки")


if __name__ == "__main__":
    service = Service()
    service.generate_request(ServiceType.PASS)
    service.generate_request(ServiceType.ID)
    service.generate_request(ServiceType.RESIDENCE)
    service.generate_request(ServiceType.TAX_ID)

    service.process_requests()




