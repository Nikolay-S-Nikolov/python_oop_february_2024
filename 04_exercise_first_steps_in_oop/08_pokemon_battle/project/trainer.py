from typing import List

from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        # Option 1
        # pokemon = None
        #
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         pokemon = p
        #         break

        # Option 2
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return "Pokemon is not caught"

        # Option 3

        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))

        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemon_data = "\n".join(f"- {p.pokemon_details()}" for p in self.pokemons)
        return f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemons)}\n" \
               f"{pokemon_data}"

