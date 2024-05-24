"""
Devtools UI home/start/landing page
"""

import nicegui

import resources
from .pages.data_browser import DataBrowserPage


class DevToolsUI:
    def __init__(self, resource_manager: resources.ResourceManager | None = None):
        self.ui = nicegui.ui
        self.data_browser = DataBrowserPage(self.ui, resource_manager)

    def run(self):
        self.data_browser.build_ui()

        self.ui.run()

