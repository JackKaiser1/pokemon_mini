class Pokemon:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health 


    def get_health(self):
        return self.__health

    def get_name(self):
        return self.__name

    def take_damage(self, damage, enemy):
        status_damage = damage * 2

        if self.get_type() == "FireType" and enemy.get_type() == "WaterType":
            self.__health -= status_damage
            print("It's super effective")
            print(f"{self.__name} took {status_damage} damage!")
            return self.__health

        elif self.get_type() == "WaterType" and enemy.get_type() == "ElectricType":
            self.__health -= status_damage
            print("It's super effective")
            print(f"{self.__name} took {status_damage} damage!")
            return self.__health

        elif self.get_type() == "WaterType" and enemy.get_type() == "GrassType":
            self.__health -= status_damage
            print("It's super effective")
            print(f"{self.__name} took {status_damage} damage!")
            return self.__health

        elif self.get_type() == "GrassType" and enemy.get_type() == "FireType":
            self.__health -= status_damage
            print("It's super effective")
            print(f"{self.__name} took {status_damage} damage!")
            return self.__health

        else:
            self.__health -= damage
            print(f"{self.__name} took {damage} damage!")
            return self.__health


    def attack(self, target):
        return f"{self.__name} attacks {target.__name}!"
    
    def get_type(self):
        return type(self).__name__
        


class WaterType(Pokemon):
    def __init__(self, name, health):
        super().__init__(name, health)

    def aqua_jet(self, target):
        print(f"{self.get_name()} used Aqua Jet!")
        target.take_damage(50, self)

class FireType(Pokemon):
    pass
class ElectricType(Pokemon):
    pass
class GrassType(Pokemon):
    pass





poke1 = WaterType("Mudkip", 100)
poke2 = GrassType("Leafer", 100)

print(poke1.aqua_jet(poke2))
# print(poke2.get_type())

# print(poke1.attack(poke2), poke2.take_damage(20))
# input()
# print(poke2.attack(poke1), poke1.take_damage(35))

# print(f"{poke1.get_name()} is ready for battle!")
# poke1.take_damage(50)
# print(f"{poke1.get_name()} took 50 damage. They now have {poke1.get_health()} health.")
        
    