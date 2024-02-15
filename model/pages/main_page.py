from selene import browser
from data.products import Product


class MainPage:
    def __init__(self):
        self.search_field = browser.element('.page-header__top .search__input')
        self.cart = browser.element('.header-cart ').element('a')

    def open(self):
        browser.open('/')

    def open_with_years_and_city_confirmation(self):
        browser.open('/')
        browser.element('[id="confirmation-popup"]').click()
        browser.element('.page-header__top .header-contacts__city-dropdown .btn-active').click()

    def add_product_to_cart_via_search(self, product: Product):
        self.search_field.click().type(product.full_name)
        browser.element(f'[data-product_id="{product.id}"]').click()

    def open_cart_page(self):
        self.cart.click()
