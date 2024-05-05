"""
Base gamemode that all other gamemodes should inherit from.
BaseGamemode shall not be instantiated directly.
"""
import abc


class BaseGamemode(abc.ABC):
    def __init__(self):
        self._running = False
        pass

    def tick_gamemode(self) -> None:
        print(f'[{self.__class__.__name__}] Tick...')
        if self._running:
            self.on_gamemode_tick()

    def begin_gamemode(self) -> None:
        print(f'[{self.__class__.__name__}] Beginning gamemode...')
        self._running = True
        self.on_gamemode_begin()

    def end_gamemode(self) -> None:
        print(f'[{self.__class__.__name__}] Ending gamemode...')
        self._running = False
        self.on_gamemode_end()

    @abc.abstractmethod
    def on_gamemode_tick(self) -> None:
        """
        Function called every tick to update the gamemode.
        Implement this in your gamemode to add your tick-level GM update logic.
        """
        pass

    @abc.abstractmethod
    def on_gamemode_begin(self) -> None:
        """
        Function called when gamemode is started.
        Implement this to add your gamemode-specific initialization logic.
        """
        pass

    @abc.abstractmethod
    def on_gamemode_end(self) -> None:
        """
        Function called when gamemode is finished.
        Implement this to add your gamemode-specific shutdown & cleanup logic.
        """
        pass
