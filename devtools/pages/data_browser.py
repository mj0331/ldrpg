"""
Browser GUI for LDRPG data.
"""
import resources
from .base_page import BasePage


class DataBrowserPage(BasePage):
    def __init__(self, ui, resource_manager: resources.ResourceManager | None = None):
        super().__init__(ui)
        self.resource_manager = resource_manager

    def build_ui(self):
        self.ui.label(f"Data root: {self.resource_manager.data_root.absolute()}")
        print(self.resource_manager.resources.keys())
        self.ui.table(columns=[
            {"name": "resource", "label": "Resource", "field": "resource", "sortable": True, "align": "left"}
        ],
            rows=[
                {"resource": key} for key in self.resource_manager.resources.keys()
            ])
