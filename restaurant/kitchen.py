from time import time,sleep

class Kitchen:

    def __init__(self, manager):
        self.manager = manager
        self.filename = 'kitchen.log'

    def prepare_meal(self,order):
        print(f'Kuchnia : Zaczynam robić posiłek : {order.name}')
        self.print_to_log(f'Kuchnia : Zaczynam robić posiłek : {order.name}')
        sleep(2)
        self.meal_ready(order)

    def meal_ready(self,order):
        order.ready_at = time()
        print(f'Kuchnia : Zrobiłem posiłek {order.name}')
        self.print_to_log(f'Kuchnia : Zrobiłem posiłek {order.name}')
        self.manager.meal_ready(order)

    def print_to_log(self,info):
        with open(self.filename,'a+') as f:
            f.write(info+'\n')