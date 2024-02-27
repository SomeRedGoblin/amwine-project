import allure
from allure_commons.types import Severity

from amwine_project.data import products
from amwine_project.pages.product_page import product_page


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Product Page")
class TestProductPage:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Страница продукта")
    @allure.title("Переход на страницу товара")
    def test_open_product_page_by_url(self, start):
        good_whiskey = products.caol_ila_12
        with allure.step(f"Открываем страницу продукта {good_whiskey.name}"):
            product_page.open_product_page(good_whiskey)

        with allure.step(f"Проверяем, что страница {good_whiskey.name} открыта "):
            product_page.check_product_page_is_opened(good_whiskey)
