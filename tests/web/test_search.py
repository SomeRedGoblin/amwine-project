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
        with allure.step(f"Ищем не существующий товар"):
            search_page.search("some_random_text")

        with allure.step(f"Проверяем, что сообщение о ненайденном товаре содержит тест запроса "):
            search_page.check_nothing_found_message("some_random_text")
