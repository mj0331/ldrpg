"""
Base class for devtools pages.
"""
import abc


class BasePage(abc.ABC):
    def __init__(self, ui):
        self.ui = ui

    @abc.abstractmethod
    def build_ui(self):
        pass
