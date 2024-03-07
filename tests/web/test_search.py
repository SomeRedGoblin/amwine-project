import allure
from allure_commons.types import Severity

from amwine_project.pages.search_page import search_page


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Search Page")
class TestProductPage:
    @allure.severity(Severity.NORMAL)
    @allure.story("Страница поиска")
    @allure.title("Поиск не существующего товара")
    def test_open_product_page_by_url(self, start):
        search_page.search("some_random_text")

        search_page.check_nothing_found_message("some_random_text")
