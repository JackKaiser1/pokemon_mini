from classes_and import Pokemon, WaterType, FireType, ElectricType, GrassType, Mudkip, Charmander, Pikachu, Bulbasaur

mudkip = Mudkip("Mudkip", 100)
charmander = Charmander("Charmander", 100)
pikachu = Pikachu("Pikachu", 100)
bulbasaur = Bulbasaur("Bulbasaur", 100)

def main():
    print("---------------------")
    print("Pokemon Battle")
    print()
    print(pikachu.bolt_strike(mudkip))
    print()
    print(mudkip.tackle(pikachu))

    

main()