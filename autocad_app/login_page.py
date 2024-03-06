from playwright.sync_api import Page


class Login:

    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.locator('#sign-in-as')

    def sign_in(self, username, password):
        with self.page.expect_popup() as signin_popup_info:
            self.sign_in_button.click()
        sign_in_popup = self._SignInPopUp(signin_popup_info.value)
        sign_in_popup.sign_in(username, password)

    class _SignInPopUp:

        def __init__(self, page: Page):
            self.page = page
            self.username_input = page.locator('#userName')
            self.verify_button = page.locator('#verify_user_btn')
            self.password_input = page.locator('#password')
            self.sign_in_button = page.locator('#btnSubmit')

        def sign_in(self, username: str, password: str):
            self.username_input.fill(username)
            self.verify_button.click()
            self.password_input.fill(password)
            self.sign_in_button.click()
