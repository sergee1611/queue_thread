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
        custom_num = 0
        custom_quan = 20
        while custom_num < custom_quan:
            custom_num += 1
            customer = Customer(custom_num)
            pprint(f'Посетитель номер {customer.number} прибыл')
            self.queue.put(customer)
            sleep(1)

    def serve_customer(self, customer):
        while True:
            for table in tables:
                if table.is_busy is False:
                    table.is_busy = True
                    pprint(f'Посетитель номер {customer.number} сел за стол {table.number}')
                    customer.start()


                # customer_eating_thread = threading.Thread(target=customer.eating)
                # customer_eating_thread.start()
                # customer_eating_thread.join()


class Customer(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        sleep(5)
        pprint(f'Посетитель номер {self.number} покушал и ушёл.')



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
# cafe.serve_customer(customer=cafe.queue.get())
# for i in range(cafe.queue.qsize()):
#     customer_serve_thread = Thread(target=cafe.serve_customer             )
#     customer_serve_thread.start()
#     threads.append(customer_serve_thread)

customer_arrival_thread.join()

# for thread in threads:
#     thread.join()




