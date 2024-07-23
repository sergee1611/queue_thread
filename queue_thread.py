from queue import Queue
from threading import Thread
from time import sleep
from pprint import pprint


class Table:
    def __init__(self, number, is_busy=False):
        self.number = number
        self.is_busy = is_busy


class Cafe:

    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables

    def customer_arrival(self):
        custom_num = 1
        custom_quan = 20
        while custom_num <= custom_quan:
            customer = Customer(custom_num, self)
            pprint(f'Посетитель номер {customer.number} прибыл')
            customer.start()
            custom_num += 1
            sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if table.is_busy is False:
                table.is_busy = True
                pprint(f'Посетитель номер {customer.number} сел за стол {table.number}')
                sleep(5)
                pprint(f'Посетитель номер {customer.number} покушал и ушёл.')
                table.is_busy = False
                self.check_queue()
                break
        else:
            pprint(f'Посетитель номер {customer.number} ожидает свободный стол')
            self.queue.put(customer)

    def check_queue(self):
        if not self.queue.empty():
            customer = self.queue.get()
            self.serve_customer(customer)


class Customer(Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)

customer_arrival_thread.start()

customer_arrival_thread.join()





