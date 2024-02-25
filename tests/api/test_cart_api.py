import allure
from allure_commons.types import Severity
from assertpy import assert_that, soft_assertions

from api.requests.cart_api import CartApi
from api.schemas import cart_item_schema
from data import products

cart_api = CartApi()


@allure.tag("api")
@allure.label("owner", "Andrey R")
@allure.feature("Cart")
class TestCart:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Добавление в корзину")
    def test_add_item_to_cart(self):
        with allure.step("Отправляем запрос на добавление товара корзину"):
            product = products.caol_ila_12
            response = cart_api.add_to_cart_via_api(product=product, quantity=1)
        with allure.step(f"Проверяем продукт {product.name} в ответе"):
            with soft_assertions():
                assert_that(response.status_code == 200)
                assert_that(response.json()['productInfo']["id"] == product.id)
                assert_that(response.json()['productInfo']['total-products'] == 1)

        with allure.step('get it!'):
            response2 = cart_api.get_items_from_cart()
        print('ssss')

    @allure.severity(Severity.NORMAL)
    @allure.story("Корзина пользователя")
    @allure.title("Схема запроса на добавление в корзину")
    def test_schema_for_add_item_to_cart(self):
        with allure.step("Отправляем запрос на добавление товара корзину"):
            response = cart_api.add_to_cart_via_api(product=products.caol_ila_12, quantity=1)

        with allure.step("Проверяем схему на соответствие модели"):
            assert_that(
                cart_item_schema.CartItemModel.model_validate(response.json())).is_type_of(
                cart_item_schema.CartItemModel)

    # ============================for debug
    def test_some_api(self):
        cart_api = CartApi()
        response = cart_api.add_to_cart_via_api(product=products.caol_ila_12, quantity=1)
        assert response.status_code == 200
        response.json()
        response2 = cart_api.add_to_cart_via_api(product=products.caol_ila_12, quantity=1)
        assert response2.status_code == 200
