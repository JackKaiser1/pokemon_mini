class Pokemon:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health 
        self.is_alive = True

    def get_health(self):
        return self.__health

    def get_name(self):
        return self.__name

    def check_status(self):
        return self.is_alive

    def get_type(self):
        return type(self).__base__.__name__
    
    def get_status(self):
        if self.__health <= 0:
            self.__health = 0
            self.is_alive = False
        return f"{self.__name} has {self.__health} health"
        
    def attack(self, move, target, damage):
        if self.is_alive == True:
            print(f"{self.__name} used {move} on {target.__name}!")
            target.take_damage(damage, self)
            return target.get_status()
        return f"{self.__name} is dead"

    def take_damage(self, damage, enemy):
        status_damage = damage * 2

        if (   self.get_type() == "FireType" and enemy.get_type() == "WaterType"
            or self.get_type() == "WaterType" and enemy.get_type() == "ElectricType"
            or self.get_type() == "WaterType" and enemy.get_type() == "GrassType"
            or self.get_type() == "GrassType" and enemy.get_type() == "FireType"
            ):
                self.__health -= status_damage
                print("It's super effective")
                print(f"{self.__name} took {status_damage} damage!")

        else: 
            self.__health -= damage
            print(f"{self.__name} took {damage} damage!")


class WaterType(Pokemon):
    def __init__(self, name, health):
        super().__init__(name, health)

    def aqua_jet(self, target):
        return self.attack("Aqua Jet", target, 40)


class Mudkip(WaterType):
    def __init__(self, name, health):
        super().__init__(name, health)

    def tackle(self, target):
        return self.attack("Tackle", target, 20)



class FireType(Pokemon):
    def __init__(self, name, health):
        super().__init__(name, health)

    def ember(self, target):
        return self.attack("Ember", target, 40)


class Charmander(FireType):
    def __init__(self, name, health):
        super().__init__(name, health)

    def scratch(self, target):
        return self.attack("Scratch", target, 20)



class ElectricType(Pokemon):
    def __init__(self, name, health):
        super().__init__(name, health)

    def bolt_strike(self, target):
        return self.attack("Bolt Strike", target, 40)


class Pikachu(ElectricType):
    def __init__(self, name, health):
        super().__init__(name, health)

    def tail_whip(self, target):
        return self.attack("Tail Whip", target, 20)



class GrassType(Pokemon):
    def __init__(self, name, health):
        super().__init__(name, health)

    def leaf_blade(self, target):
        return self.attack("Lead Blade", target, 40)


class Bulbasaur(GrassType):
    def __init__(self, name, health):
        super().__init__(name, health)

    def take_down(self, target):
        return self.attack("Take Down", target, 20)



        
    