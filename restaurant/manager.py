from restaurant.kitchen import Kitchen


class Manager:

    def __init__(self, cash_desk, kitchen, give_away):
        self.cash_desk = cash_desk
        self.kitchen = kitchen
        self.give_away = give_away

    def new_order(self):
        pass

    def prepare_meal(self):
        pass

    def meal_ready(self):
        pass

    def call_customer(self):
        pass

    def customer_collected_order(self):
        pass
