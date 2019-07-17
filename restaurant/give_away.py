from time import time, sleep

class GiveAway:

    def __init__(self, manager):
        self.manager = manager
        self.filename = 'give_away.log'

    def call_customer(self,order):
        print(f'Wydawka : Czekam na klienta {order.name}')
        self.print_to_log(f'Wydawka : Czekam na klienta {order.name}')
        sleep(2)
        self.customer_collected_order(order)

    def customer_collected_order(self,order):
        order.collected_at = time()
        print(f'Wydawka : Wydalem klientowi {order.name}')
        self.print_to_log(f'Wydawka : Wydalem klientowi {order.name}')
        self.manager.customer_collected_order(order)

    def print_to_log(self,info):
        with open(self.filename,'a+') as f:
            f.write(info+'\n')