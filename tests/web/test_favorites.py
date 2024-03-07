import allure
import pytest
from allure_commons.types import Severity

from amwine_project.data import products
from amwine_project.pages.favorites_page import favorites_page
from amwine_project.pages.main_page import main_page


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Favorites")
class TestFavorites:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Избранное")
    @allure.title("Добавление в избранное")
    @pytest.mark.parametrize('product', [products.caol_ila_12, products.guinness])
    def test_add_item_to_favorites(self, start, product):
        main_page.find_product_and_add_to_favorites(product)
        main_page.check_increasing_items_in_favorites()
        main_page.open_favorites_page()

        favorites_page.check_product_in_favorites(product)

    @allure.severity(Severity.NORMAL)
    @allure.story("Избранное")
    @allure.title("Удаление товара из избранного")
    def test_remove_item_from_favorites(self, start):
        good_old_whiskey = products.caol_ila_12
        main_page.find_product_and_add_to_favorites(good_old_whiskey)
        main_page.open_favorites_page()

        favorites_page.clear_favorites()
        favorites_page.check_favorites_is_empty()
