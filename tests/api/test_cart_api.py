import allure
import requests.sessions
from allure_commons.types import Severity
from assertpy import assert_that, soft_assertions

from amwine_project.shemas import cart_item_schema, cart_non_existent_items_schema
from amwine_project.data import products
from amwine_project.utils.api_helper import do_request, headers
from conftest import BASE_URL


@allure.tag("api")
@allure.label("owner", "Andrey R")
@allure.feature("Cart")
class TestCart:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Добавление в корзину через API")
    def test_add_item_to_cart(self):
        product = products.caol_ila_12
        with allure.step(f"Отправляем запрос на добавление товара {product.name} корзину"):
            url = f"/local/templates/am/ajax/header.basket.line.php?id={product.id}&action=add"
            data = {"quantity": 1}
            response = do_request(base_url=BASE_URL, url=url, method="POST", headers=headers(), data=data)
        with allure.step(f"Проверяем продукт {product.name} в ответе"):
            with soft_assertions():
                assert_that(response.status_code == 200)
                assert_that(response.json()['productInfo']["id"] == product.id)
                assert_that(response.json()['productInfo']['total-products'] == 1)
        with allure.step("Проверяем схему ответа на соответствие модели"):
            assert_that(
                cart_item_schema.CartItemModel.model_validate(response.json())).is_type_of(
                cart_item_schema.CartItemModel)

    @allure.severity(Severity.NORMAL)
    @allure.story("Корзина пользователя")
    @allure.title("Добавление не существующего товара")
    def test_change_item_quantity_in_cart(self):
        product = products.caol_ila_12
        with allure.step(f"Отправляем запрос на добавление не существующего товара корзину"):
            url = f"/local/templates/am/ajax/header.basket.line.php?action=add&id=1234567890"
            data = {"quantity": 1}
            response = do_request(base_url=BASE_URL, url=url, method="POST", headers=headers(), data=data)
        with allure.step(f"Проверяем ответ"):
            with soft_assertions():
                assert_that(response.status_code == 200)
                assert_that(response.json()['result'] == 'failed')
                assert_that(response.json()['productInfo']["id"] == 'null')
                assert_that(response.json()['productInfo']['total-products'] == 0)
        with allure.step("Проверяем схему ответа на соответствие модели"):
            assert_that(
                cart_non_existent_items_schema.CartNonExistentItem.model_validate(response.json())).is_type_of(
                cart_non_existent_items_schema.CartNonExistentItem)
