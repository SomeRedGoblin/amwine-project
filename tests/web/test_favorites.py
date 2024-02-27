import allure
import pytest
from allure_commons.types import Severity
from selene import browser, have

from amwine_project.pages.main_page import main_page
from amwine_project.pages.favorites_page import favorites_page
from amwine_project.data import products


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Favorites")
class TestFavorites:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Избранное")
    @allure.title("Добавление в избранное")
    @pytest.mark.parametrize('product', [products.caol_ila_12, products.guinness])
    def test_add_item_to_favorites(self, start, product):


        with allure.step(f"Ищем товар и добавляем в избранное {product.name}"):
            main_page.find_product_and_add_to_favorites(product)

        with allure.step("Проверяем, что кол-во товара в избранном увеличилось"):
            browser.element('.header-fav').element('.header-cart-count').should(have.exact_text('1'))

        with allure.step("Открываем страницу избранного"):
            main_page.open_favorites_page()

        with allure.step(f"Проверяем, что {product.name} в избранном "):
            favorites_page.check_product_in_favorites(product)

    @allure.severity(Severity.NORMAL)
    @allure.story("Избранное")
    @allure.title("Удаление товара из избранного")
    def test_remove_item_from_favorites(self, start):
        good_old_whiskey = products.caol_ila_12
        with allure.step(f"Ищем товар и добавляем в избранное {good_old_whiskey.name}"):
            main_page.find_product_and_add_to_favorites(good_old_whiskey)

        with allure.step("Открываем страницу избранного"):
            main_page.open_favorites_page()

        with allure.step(f"Удаляем товар {good_old_whiskey.name} из избранного"):
            favorites_page.clear_favorites()

        with allure.step("Проверяем что корзина пуста"):
            favorites_page.check_favorites_is_empty()
