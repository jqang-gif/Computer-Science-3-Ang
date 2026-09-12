class Hero: #Class Name
    def __init__(self, heroname, hp):

        self.heroname = heroname #Hero name
        self.hp = hp #Hero health

    def stats(self):
        #How it will print when called
        return f"{self.heroname} : {self.hp}"

    def take_damage(self, damageamount):
        self.hp = self.hp - damageamount #Damage to Hero health

hero1 = Hero("Arthur", 100) #Arthur Stats
hero2 = Hero("Morgana", 100) #Morgana Stats

hero1.take_damage(10) #Damage to Arthur's hp

print(hero1.stats()) #Print Arthur's stats
print(hero2.stats()) #Print Morgana's stats
