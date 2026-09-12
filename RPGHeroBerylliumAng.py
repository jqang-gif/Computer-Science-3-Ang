class Hero: #HeroName
    def __init__(self, heroname, hp):

        self.heroname = heroname
        self.hp = hp

    def stats(self):
        return f"{self.heroname} : {self.hp}"

    def take_damage(self, damageamount):
        self.hp = self.hp - damageamount

hero1 = Hero("Arthur", 100)
hero2 = Hero("Morgana", 100)

hero1.take_damage(10)

print(hero1.stats())
print(hero2.stats())
