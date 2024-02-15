import allure
from allure_commons.types import Severity
from selene import browser, have

from model.pages.cart_page import CartPage
from model.pages.main_page import MainPage

from data import products


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Cart")
class TestCart:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Добавление в корзину")
    def test_add_item_to_cart(self):
        good_whiskey = products.caol_ila_12

        with allure.step("Открываем страницу магазина"):
            main_page = MainPage()
            main_page.open_with_years_and_city_confirmation()

        with allure.step(f"Ищем и добавляем товар в корзину {good_whiskey.name}"):
            main_page.add_product_to_cart_via_search(good_whiskey)

        with allure.step("Проверяем, что кол-во товара в корзине увеличилось"):
            browser.element('[id="header-basket-page"]').element('.header-cart-count').should(have.exact_text('1'))

        with allure.step("Открываем страницу корзины"):
            cart_page = CartPage()
            main_page.open_cart_page()

        with allure.step(f"Проверяем, что в корзине {good_whiskey.name}"):
            cart_page.check_product(good_whiskey)
