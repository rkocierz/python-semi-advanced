class Arena: #historia gier i rankingowanie zawodnikow
    def __init__(self):
        self.games = []
        self.players = []
        #self.standing = []

    def add(self,game):
        self.games.append(game)

    @property
    def standing(self):
        for game in self.games:
            if game.white not in self.players:
                self.players.append(game.white)
            if game.black not in self.players:
                self.players.append(game.black)

            if game.whiteWon():
                game.white.ranking += 1
            else:
                game.black.ranking += 1

        return sorted(self.players, key = lambda c: c.ranking, reverse=True)

class Player:   #info o zawodniku, name i rankign
    def __init__(self,name, ranking):
        self.name = name
        self.ranking = ranking

    def description(self):
        return f"My name is {self.name} and my ranking is {self.ranking}."

    def __str__(self):
        return self.description()


class Game: # bialy, czarny i wynik
    def __init__(self,white,black,win_side):
        self.white = white
        self.black = black
        self.win_side = win_side

    def whiteWon(self):
        return self.win_side==1

    def blackWon(self):
        return self.win_side==2
