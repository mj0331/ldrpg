"""
A character is an actor that has a name, combat stat blocks and combat logic.
"""

from .base_actor import BaseActor
from gamemodes.base_gamemode import BaseGamemode


class Character(BaseActor):
    def __init__(self, lore_resource=None, combat_stat_block_resource=None):
        super().__init__()
        self.lore = lore_resource
        self.combat_stats = combat_stat_block_resource

    def on_actor_begin(self):
        pass

    def on_actor_end(self):
        pass

    def on_actor_tick(self, gamemode: BaseGamemode):
        pass

    def __repr__(self):
        return f'<Character Lore: {self.lore}, CombatStats: {self.combat_stats}>'
