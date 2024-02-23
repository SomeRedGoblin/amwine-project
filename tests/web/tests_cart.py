import allure
import pytest
from allure_commons.types import Severity
from selene import browser, have

from model.pages.cart_page import CartPage
from model.pages.main_page import MainPage
from api.requests.cart_api import CartApi
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
            cart_page.check_product_in_cart(good_whiskey)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Удаление товара из корзины")
    @pytest.mark.parametrize('product', [products.caol_ila_12])
    def test_remove_item_from_cart(self, product):
        good_whiskey = products.caol_ila_12
        with allure.step("Открываем страницу магазина"):
            main_page = MainPage()
            main_page.open_with_years_and_city_confirmation()

        # Не работает - видимо сессия
        # cart_api = CartApi()
        # response = cart_api.add_to_cart_via_api(product=products.caol_ila_12, quantity=1)
        # assert response.status_code == 200

        with allure.step(f"Ищем и добавляем товар в корзину {good_whiskey.name}"):
            main_page.add_product_to_cart_via_search(good_whiskey)

        with allure.step("Открываем страницу корзины"):
            cart_page = CartPage()
            main_page.open_cart_page()

        with allure.step(f"Удаляем товар из корзины {good_whiskey.name}"):
            cart_page.clear_cart()

        with allure.step("Проверяем что корзина пуста"):
            cart_page.check_cart_is_empty()
