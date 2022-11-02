#1. Recept
# Bude mít 3 atributy:

# nazev - string, jmeno kucharky
# narocnost - necham na vas jak ji budete reprezentovat (muze byt cislo, muze byt slovni vyjadreni)
# url_adresa - string, odkaz na recept
# vyzkouseno - bool, metoda __init__ ji vzdy nastavi na False
# nazev,narocnost, url_adresa budou atributy metody __init__, tedy uzivatel si je muze zvolit pri vytvareni objektu.

# A bude mít také 3 metody:

# __str___(self)
# vraci hezky vypis receptu (necham na vas ktere atributy chcete do vypisu dat)
# zmen_narocnost(self, nova_hodnota)
# zmeni narocnost, tedy zmeni atribut narocnost na nova_hodnota
# zkusit(self)
# zmeni atribut vyzkouseno na True

# 2. Kucharka
# Bude mít 3 atributy:

# nazev - string, jmeno kucharky
# autor - string, jmeno autora kucharky
# recepty - list objektu tridy Recept, metoda __init__ ji nastavuje vzdy na prazdny seznam []
# nazev a autor budou atributy metody __init__, tedy uzivatel si je muze zvolit pri vytvareni objektu.

# A bude mít také 3 metody:

# __str___(self)
# vraci hezky vypis kucharky (necham na vas ktere atributy chcete do vypisu dat)
# pocet_receptu(self)
# vraci cislo reprezentujici pocet receptu v atributu recepty
# pridej_recept(self, recept)
# prida do atributu recepty objekt recepty ktery je v argumentu recept


class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False

    def __str__(self):
        pass

#definice metod? 

class Kucharka:
    pass

