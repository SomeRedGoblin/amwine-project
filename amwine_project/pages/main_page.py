import allure
from selene import browser, have

from amwine_project.data.products import Product


class MainPage:
    def __init__(self):
        self.search_field = browser.element('.page-header__top .search__input')
        self.cart = browser.element('.header-cart ').element('a')
        self.favorites = browser.element('.header-fav')
        self.cart_counter = browser.element('[id="header-basket-page"]').element('.header-cart-count')
        self.favorites_counter = browser.element('.header-fav').element('.header-cart-count')

    def open(self) -> None:
        browser.open('/')

    def open_with_years_and_city_confirmation(self) -> None:
        with allure.step("Открываем страницу магазина, подтверждаем возраст и город"):
            browser.open('/')
            browser.element('[id="confirmation-popup"]').click()
            browser.element('.page-header__top .header-contacts__city-dropdown .btn-active').click()

    def add_product_to_cart_via_search(self, product: Product) -> None:
        with allure.step(f"Ищем и добавляем товар {product.name} в корзину"):
            self.search_field.click().type(product.full_name)
            browser.element(f'[data-product_id="{product.id}"]').click()
            browser.wait_until(browser.element('[id="header-basket-page"]').element('.dropdown__content'))

    def check_increasing_items_in_cart(self) -> None:
        with allure.step("Проверяем, что кол-во товара в корзине увеличилось"):
            self.cart_counter.should(have.exact_text('1'))

    def check_increasing_items_in_favorites(self) -> None:
        with allure.step("Проверяем, что кол-во товара в избранном увеличилось"):
            self.favorites_counter.should(have.exact_text('1'))

    def open_cart_page(self) -> None:
        with allure.step("Открываем страницу корзины"):
            self.cart.click()

    def open_favorites_page(self) -> None:
        with allure.step("Открываем страницу избранного"):
            self.favorites.click()

    def find_product_and_add_to_favorites(self, product: Product) -> None:
        with allure.step(f"Ищем товар и добавляем в избранное {product.name}"):
            self.search_field.click().type(product.full_name)
            browser.element('.digi-ac-block .digi-favorite-button').click()
            browser.wait_until(self.favorites.element('.header-fav-count'))


main_page = MainPage()
