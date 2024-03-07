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
        cocktails_page.open()

        cocktails_page.check_cocktails_page_is_opened()
