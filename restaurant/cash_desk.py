class CashDesk:

    def __init__(self, manager):
        self.manager = manager
        self.filename = 'cash_desk.log'

    def new_order(self, order):
        print(f'Kasa : Przyjąłem zamówienie na {order.name}')
        self.print_to_log(f'Kasa : Przyjąłem zamówienie na {order.name}')
        self.manager.new_order(order)

    def print_to_log(self,info):
        with open(self.filename,'a+') as f:
            f.write(info+'\n')