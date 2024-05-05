"""
D&D-style turn-based combat game mode, featuring a turn order of characters.
"""
from actors.character import Character
from .base_gamemode import BaseGamemode


class TurnBasedCombatGamemode(BaseGamemode):
    def __init__(self, characters: list[Character] = None):
        super().__init__()
        self.characters = characters if characters is not None else []

    def on_gamemode_begin(self) -> None:
        print('TBC GM started.')
        for character in self.characters:
            character.activate_actor()

    def on_gamemode_end(self) -> None:
        print('TBC GM ended.')
        for character in self.characters:
            character.deactivate_actor()

    def on_gamemode_tick(self):
        print('TBC Tick')
        for character in self.characters:
            character.tick_actor(self)