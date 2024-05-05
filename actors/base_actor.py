"""
Base class for all actors.
Actors are anything that has data blocks and logic that should be executed during the game.
BaseActor shall not be instantiated directly.
"""
from gamemodes.base_gamemode import BaseGamemode

import abc
import uuid


class BaseActor(abc.ABC):
    def __init__(self):
        self._active = False
        self.id = str(uuid.uuid4())
        pass

    def tick_actor(self, gamemode: BaseGamemode) -> None:
        print(f'[Actor@{self.id}] Tick...')
        if self._active:
            self.on_actor_tick(gamemode)

    def activate_actor(self) -> None:
        print(f'[Actor@{self.id}] Activating...')
        self._active = True
        self.on_actor_begin()

    def deactivate_actor(self) -> None:
        print(f'[Actor@{self.id}] Deactivating...')
        self._active = False
        self.on_actor_end()

    @abc.abstractmethod
    def on_actor_begin(self):
        """
        Implement this method to execute when the actor becomes active.
        """
        pass

    @abc.abstractmethod
    def on_actor_end(self):
        """
        Implement this method to execute when the actor becomes inactive.
        """
        pass

    @abc.abstractmethod
    def on_actor_tick(self, gamemode: BaseGamemode) -> None:
        """
        Implement this method to execute when the game update ticks every frame.
        """
        pass