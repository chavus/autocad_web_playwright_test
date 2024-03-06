from playwright.sync_api import Page
from autocad_app.home_page import Home
from autocad_app.editor_page import Editor
import pytest


# Test suites can be represented by a class
class TestBasicDrawing:

    @pytest.mark.smoke  # Pytest markers are used to group test cases
    @pytest.mark.regression
    # Test cases can be represented by a method
    def test_draw_circles(self, logged_in_page: Page, assert_snapshot):
        page = logged_in_page
        Home(page).create_new_drawing()
        editor = Editor(page)
        editor.select_layer_color(Editor.LayerColor.RED)
        editor.set_grid("OFF")
        editor.create_circle_with_radius('300,300', 250)
        page.wait_for_timeout(4000)  # Waits for commands history to disappear
        editor.go_to_layout_tab('Layout1')
        assert_snapshot(editor.get_drawing_screenshot(), threshold=0.2)

    @pytest.mark.regression
    def test_draw_rectangles(self, logged_in_page, assert_snapshot):
        page = logged_in_page
        Home(page).create_new_drawing()
        editor = Editor(page)
        editor.set_grid("OFF")
        editor.select_layer_color(Editor.LayerColor.RED)
        editor.create_rectangle_with_dimensions('0,0', '250,250')
        page.wait_for_timeout(4000)  # Waits for commands history to disappear
        editor.go_to_layout_tab('Layout1')
        assert_snapshot(editor.get_drawing_screenshot(), threshold=0.2)







