'''
Klasa ma przechowyhwać nazwę posiłki,
    godzinę złożenia,
    godzinę wykonania,
    godzinę odbioru zamówienia
'''
from time import time, gmtime, strftime

def format_time(time):
    return strftime("%H:%M:%S", gmtime(time))

class Order:
    def __init__(self,name:str):  #ctrl+0 - podpowiedz jakie są metody klasy
        self.name:str=name
        self.created_at:float=time()
        self.ready_at:float=0.0
        self.collected_at:float=0.0

    def __str__(self) -> str:
        return f'Order: {self.name}, {format_time(self.created_at)},' \
            f' {format_time(self.ready_at)}, {format_time(self.collected_at)}'




