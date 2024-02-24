import allure
import pytest
from allure_commons.types import Severity
from selene import browser, have

from model.pages.cart_page import CartPage
from model.pages.main_page import MainPage
from model.pages.favorites_page import FavoritesPage
from api.requests.cart_api import CartApi
from data import products


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Favorites")
class TestFavorites:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Избранное")
    @allure.title("Добавление в избранное")
    def test_add_item_to_cart(self, start):
        good_old_whiskey = products.caol_ila_12
        main_page = MainPage()
        favorites_page = FavoritesPage()

        with allure.step(f"Ищем товар и добавляем в избранное {good_old_whiskey.name}"):
            main_page.find_product_and_add_to_favorites(good_old_whiskey)

        with allure.step("Проверяем, что кол-во товара в избранном увеличилось"):
            browser.element('.header-fav').element('.header-cart-count').should(have.exact_text('1'))

        with allure.step("Открываем страницу избранного"):
            main_page.open_favorites_page()

        with allure.step(f"Проверяем, что {good_old_whiskey.name} в избранном "):
            favorites_page.check_product_in_favorites(good_old_whiskey)

    @allure.severity(Severity.NORMAL)
    @allure.story("Избранное")
    @allure.title("Удаление товара из избранного")
    @pytest.mark.parametrize('product', [products.caol_ila_12, products.guinness])
    def test_remove_item_from_cart(self, start, product):
        main_page = MainPage()
        favorites_page = FavoritesPage()

        with allure.step(f"Ищем товар и добавляем в избранное {product.name}"):
            main_page.find_product_and_add_to_favorites(product)

        with allure.step("Открываем страницу избранного"):
            main_page.open_favorites_page()

        with allure.step(f"Удаляем товар {product.name} из избранного"):
            favorites_page.clear_favorites()

        with allure.step("Проверяем что корзина пуста"):
            favorites_page.check_favorites_is_empty()
