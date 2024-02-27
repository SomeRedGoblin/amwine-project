import allure
from allure_commons.types import Severity

from amwine_project.pages.cocktails_page import cocktails_page


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Cocktails Page")
class TestProductPage:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Страница Коктейлей")
    @allure.title("Переход на страницу Коктейлей")
    def test_open_product_page_by_url(self, start):
        with allure.step(f"Открываем страницу Коктейлей"):
            cocktails_page.open()

        with allure.step(f"Проверяем, что страница Коктейлей открыта "):
            cocktails_page.check_cocktails_page_is_opened()
