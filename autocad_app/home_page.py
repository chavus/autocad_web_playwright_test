from playwright.sync_api import Page

class Home:

    URL = '/acad/me'

    def __init__(self, page: Page):
        self.page = page
        self.new_drawing_button = page.get_by_title('New Drawing')
        self.initializing_modal = page.get_by_text('Initializing AutoCAD -')

    def wait_for(self):
        self.page.wait_for_url(self.URL)

    def create_new_drawing(self):
        self.new_drawing_button.click()
        self.initializing_modal.wait_for(state='visible')
        self.initializing_modal.wait_for(state='hidden', timeout=90000)
