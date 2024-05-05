# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from gamemodes.turn_based_combat_gamemode import TurnBasedCombatGamemode
from actors.character import Character
from resources.resource_manager import ResourceManager
from pathlib import Path

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    resource_manager = ResourceManager(Path('data'))
    print(resource_manager.resources)

    char1 = Character(lore_resource=resource_manager.resources['ldrpg_base/characters/lore/geoff'],
                      combat_stat_block_resource=resource_manager.resources[
                          'ldrpg_base/characters/combat_stats/warrior'])
    char2 = Character(lore_resource=resource_manager.resources['ldrpg_base/characters/lore/anna'],
                      combat_stat_block_resource=resource_manager.resources[
                          'ldrpg_base/characters/combat_stats/warrior'])

    print(char1)
    print(char2)

    gm = TurnBasedCombatGamemode(characters=[char1, char2])

    # Just run a fixed number of ticks for testing
    MAX_TICKS = 0
    current_tick = 0

    gm.begin_gamemode()

    while current_tick < MAX_TICKS:
        gm.on_gamemode_tick()
        current_tick += 1

    gm.end_gamemode()
