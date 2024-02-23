import allure
import pytest
import json
from allure_commons.types import Severity

from model.pages.main_page import MainPage
from api.requests.cart_api import CartApi
from data import products
from api.requests.api_functions import CartApi
from assertpy import assert_that, soft_assertions
from api.schemas import cart_item_schema


@allure.tag("api")
@allure.label("owner", "Andrey R")
@allure.feature("Cart")
class TestCart:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Добавление в корзину")
    def test_add_item_to_cart(self):
        cart_api = CartApi()
        response = cart_api.add_to_cart_via_api()

        assert response.status_code == 200

    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Удаление товара из корзины")
    @pytest.mark.parametrize('product', [products.caol_ila_12])
    def test_remove_item_from_cart(self, make_api_request, product):
        # cart_api = CartApi
        # resp = cart_api.add_to_cart_via_api(self, product, 2)
        product_id = product.id
        action = "add"
        url = f"https://amwine.ru/local/templates/am/ajax/header.basket.line.php?id={product_id}&action={action}"
        data = {"quantity": 2}
        headers = {'Content-Type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
                   }
        response = make_api_request(url, method="POST", data=data, headers=headers)

        assert response.status_code == 200

    def test_some_api(self):
        cart_api = CartApi()

        response = cart_api.add_to_cart_via_api(product=products.caol_ila_12, quantity=1)
        assert response.status_code == 200
        response.json()
        # assert_that(
        #     cart_item_schema.CartItemModel.model_validate(response.json())).is_type_of(cart_item_schema.CartItemModel)

        response2 = cart_api.add_to_cart_via_api(product=products.caol_ila_12, quantity=1)
        assert response.status_code == 200
