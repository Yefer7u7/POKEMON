
import pandas as pd

# Clase Pokemon que representa a un Pokémon
class Pokemon:
    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.salud = int(salud)

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Ataque: {self.ataque}, Defensa: {self.defensa}, Salud: {self.salud}"

    def recibir_dano(self, danio):
        self.salud -= danio
        if self.salud < 0:
            self.salud = 0

    def esta_vivo(self):
        return self.salud > 0

# Clase PokemonBattle que maneja las batallas entre dos Pokémon
class PokemonBattle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def simular_batalla(self):
        print(f"¡Comienza la batalla entre {self.pokemon1.nombre} y {self.pokemon2.nombre}!")
        
        # Simulación de la batalla
        while self.pokemon1.esta_vivo() and self.pokemon2.esta_vivo():
            # Pokémon 1 ataca a Pokémon 2
            danio = self.pokemon1.ataque - self.pokemon2.defensa
            if danio > 0:
                self.pokemon2.recibir_dano(danio)
            print(f"{self.pokemon1.nombre} ataca a {self.pokemon2.nombre}. Salud de {self.pokemon2.nombre}: {self.pokemon2.salud}")
            
            # Pokémon 2 ataca a Pokémon 1
            danio = self.pokemon2.ataque - self.pokemon1.defensa
            if danio > 0:
                self.pokemon1.recibir_dano(danio)
            print(f"{self.pokemon2.nombre} ataca a {self.pokemon1.nombre}. Salud de {self.pokemon1.nombre}: {self.pokemon1.salud}")

        # Determinar el ganador
        if self.pokemon1.esta_vivo():
            print(f"¡{self.pokemon1.nombre} ha ganado la batalla!")
        elif self.pokemon2.esta_vivo():
            print(f"¡{self.pokemon2.nombre} ha ganado la batalla!")
        else:
            print("La batalla terminó en empate.")

# Clase PokemonManager para gestionar el listado de Pokémon
class PokemonManager:
    def __init__(self, archivo_csv):
        self.pokemons = self.cargar_pokemons(archivo_csv)

    def cargar_pokemons(self, archivo_csv):
        # Cargar datos desde el archivo CSV
        pokemon_data = pd.read_csv(archivo_csv)
        pokemons = []
        for _, row in pokemon_data.iterrows():
            pokemons.append(Pokemon(row['nombre'], row['tipo'], row['ataque'], row['defensa'], row['salud']))
        return pokemons

    def agregar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def modificar_pokemon(self, nombre, nuevo_pokemon):
        for i, pokemon in enumerate(self.pokemons):
            if pokemon.nombre == nombre:
                self.pokemons[i] = nuevo_pokemon
                return True
        return False

    def eliminar_pokemon(self, nombre):
        for i, pokemon in enumerate(self.pokemons):
            if pokemon.nombre == nombre:
                del self.pokemons[i]
                return True
        return False

    def mostrar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)

# Función principal
def main():
    # Crear un manejador de pokémons
    pokemon_manager = PokemonManager('pokemon.csv')

    # Mostrar los pokémons cargados
    print("Pokémons cargados:")
    pokemon_manager.mostrar_pokemons()

    # Agregar un nuevo Pokémon
    nuevo_pokemon = Pokemon("Charizard", "Fuego", 100, 80, 150)
    pokemon_manager.agregar_pokemon(nuevo_pokemon)

    # Modificar un Pokémon
    pokemon_modificado = Pokemon("Pikachu", "Eléctrico", 60, 50, 100)
    pokemon_manager.modificar_pokemon("Pikachu", pokemon_modificado)

    # Eliminar un Pokémon
    pokemon_manager.eliminar_pokemon("Bulbasaur")

    # Mostrar los pokémons después de las modificaciones
    print("\nPokémons después de modificaciones:")
    pokemon_manager.mostrar_pokemons()

    # Simular una batalla
    print("\nSimulando batalla entre Pikachu y Charizard...")
    pokemon1 = pokemon_manager.pokemons[0]  # Suponemos que Pikachu es el primero
    pokemon2 = pokemon_manager.pokemons[1]  # Suponemos que Charizard es el segundo
    batalla = PokemonBattle(pokemon1, pokemon2)
    batalla.simular_batalla()

if __name__ == "__main__":
    main()
