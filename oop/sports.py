class Arena: #historia gier i rankingowanie zawodnikow
    pass

class Player:   #info o zawodniku, name i rankign
    def __init__(self,name, ranking):
        self.name = name
        self.ranking = ranking

    def description(self):
        return f"My name is {self.name} and my ranking is {self.ranking}."

    pass

class Game: # bialy, czarny i wynik
    pass