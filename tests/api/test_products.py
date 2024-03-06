import allure
from allure_commons.types import Severity
from assertpy import assert_that, soft_assertions

from amwine_project.shemas import stocks_non_existent_product_schema
from amwine_project.utils.api_helper import do_request, headers
from tests.conftest import BASE_URL


@allure.tag("api")
@allure.label("owner", "Andrey R")
@allure.feature("Products")
class TestProducts:
    @allure.severity(Severity.NORMAL)
    @allure.story("Наличие товара")
    @allure.title("Проверка наличия не существующего товара через API")
    def test_check_stock_for_non_existent_product(self):
        with allure.step("test"):
            url = '/local/templates/am/ajax/product.stocks.php'
            data = {'article': '123456789'}
            response = do_request(base_url=BASE_URL, url=url, method="POST", headers=headers(), data=data)
            with allure.step(f"Проверяем ответ"):
                with soft_assertions():
                    assert_that(response.status_code == 200)
                    assert_that(response.json()['status'] == 'error')
                    assert_that(response.json()['data']['contentFormatted'] == 'нет в наличии')
            with allure.step("Проверяем схему ответа на соответствие модели"):
                assert_that(
                    stocks_non_existent_product_schema.StocksNonExistentProduct.model_validate(
                        response.json())).is_type_of(
                    stocks_non_existent_product_schema.StocksNonExistentProduct)
