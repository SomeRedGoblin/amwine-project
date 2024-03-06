import allure
from allure_commons.types import Severity
from assertpy import assert_that, soft_assertions

from amwine_project.data import products
from amwine_project.shemas import favorites_item_adding_schema, favorites_get_items_schema
from amwine_project.utils.api_helper import do_request, headers
from tests.conftest import BASE_URL


@allure.tag("api")
@allure.label("owner", "Andrey R")
@allure.feature("Favorites")
class TestCart:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Избранное")
    @allure.title("Добавление в избранное через API")
    def test_add_item_to_favorites(self):
        product = products.guinness
        with allure.step(f"Отправляем запрос на добавление товара {product.name} в избранное"):
            url = f"/local/templates/am/ajax/favorite.php?type=product&id={product.id}"
            response = do_request(base_url=BASE_URL, url=url, method="POST", headers=headers())
        with allure.step(f"Проверяем ответ"):
            with soft_assertions():
                assert_that(response.status_code == 200)
                assert_that(response.json()['result'] == "ok")
        with allure.step("Проверяем схему ответа на соответствие модели"):
            assert_that(
                favorites_item_adding_schema.FavoritesItemAddingModel.model_validate(response.json())).is_type_of(
                favorites_item_adding_schema.FavoritesItemAddingModel)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Избранное")
    @allure.title("Получение данных о товарах в избранном")
    def test_get_favorite_products(self):
        product1 = products.caol_ila_12
        product2 = products.guinness
        with allure.step(f"Отправляем запрос на получение избранных товаров"):
            cookie = {"AMWINE__fav_product": f"{product1.id}%2C{product2.id}"}
            url = "/local/templates/am/ajax/get-favorite-products.php"
            response = do_request(base_url=BASE_URL, url=url, method="GET", headers=headers(), cookies=cookie)
        with allure.step(f"Проверяем ответ"):
            with soft_assertions():
                assert_that(response.status_code == 200)
                assert_that(response.json()['id'] == f'[{product1.id},{product2.id}]')
                assert_that(response.json()['artnum'] == f'[{product1.article},{product2.article}]')
        with allure.step("Проверяем схему на соответствие модели"):
            assert_that(
                favorites_get_items_schema.FavoritesGetItemModel.model_validate(response.json())).is_type_of(
                favorites_get_items_schema.FavoritesGetItemModel)
