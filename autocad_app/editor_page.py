from playwright.sync_api import Page, expect
from enum import Enum


class Editor:

    class LayerColor(Enum):
        RED = 'Red'
        BLUE = 'Blue'
        GREEN = 'Green'

    def __init__(self, page: Page):
        self.page = page
        self.properties_layer_color_dropdown = page.get_by_test_id('layer-color')
        self.command_line = page.locator('.class-cmdline-command-input')
        self.drawing_area = page.locator('div.input-adapter canvas')
        self.layout_tabs = page.locator('div.layout-tab-item')
        self.layout_tab_selected = page.locator('div.layout-tab-item.selected')

    def select_layer_color(self, layer_color: LayerColor):
        self.properties_layer_color_dropdown.click()
        self.page.get_by_test_id('menu-contents-container').get_by_text(layer_color.value).click()

    def create_circle_with_radius(self, center: str, radius: float):
        """Creates a circle from command line

        :param center: Example '0,0'
        :param radius: Example 350
        :return:
        """
        self.command_line.fill('CIRCLE')
        self.page.keyboard.press('Enter')
        self.page.get_by_text('Specify center point for circle or').wait_for()
        self.command_line.fill(center)
        self.page.keyboard.press('Enter')
        self.page.get_by_text('Specify radius of circle or').wait_for()
        self.command_line.fill(str(radius))
        self.page.keyboard.press('Enter')

    def create_rectangle_with_dimensions(self, first_corner: str, dimensions: str):
        """Creates a rectangle using command line

        :param first_corner: example: '0,0'
        :param dimensions: example: '250,300'
        :return:
        """
        self.command_line.fill('RECTANGLE')
        self.page.keyboard.press('Enter')
        self.page.get_by_text('Specify first corner of rectangle').wait_for()
        self.command_line.fill(first_corner)
        self.page.keyboard.press('Enter')
        self.page.get_by_text('Specify opposite corner of rectangle or').wait_for()
        self.command_line.fill(dimensions)
        self.page.keyboard.press('Enter')

    def go_to_layout_tab(self, tab_name: str):
        self.layout_tabs.filter(has_text=tab_name).click()
        self.layout_tab_selected.filter(has_text=tab_name).wait_for()
        # Alternative for layer change
        # self.page.get_by_test_id('layer-item').locator('[data-color="0,0,0,255"]').wait_for()

    def set_grid(self, value:str):
        self.command_line.fill('GRID')
        self.page.keyboard.press('Enter')
        self.page.get_by_text('Specify grid spacing(X) or').wait_for()
        self.command_line.fill(value)
        self.page.keyboard.press('Enter')

    def get_drawing_screenshot(self) -> bytes:
        return self.drawing_area.screenshot()

