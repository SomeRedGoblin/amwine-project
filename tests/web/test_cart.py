import allure
from allure_commons.types import Severity

from amwine_project.data import products
from amwine_project.pages.cart_page import cart_page
from amwine_project.pages.main_page import main_page


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Cart")
class TestCart:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Добавление в корзину")
    def test_add_item_to_cart(self, start):
        good_old_whiskey = products.caol_ila_12

        main_page.add_product_to_cart_via_search(good_old_whiskey)
        main_page.check_increasing_items_in_cart()
        main_page.open_cart_page()

        cart_page.check_product_in_cart(good_old_whiskey)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Удаление товара из корзины")
    def test_remove_item_from_cart(self, start):
        good_whiskey = products.caol_ila_12

        main_page.add_product_to_cart_via_search(good_whiskey)
        main_page.open_cart_page()

        cart_page.clear_cart()
        cart_page.check_cart_is_empty()
