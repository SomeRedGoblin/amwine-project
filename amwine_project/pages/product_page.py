import allure
from selene import browser, have

from amwine_project.data.products import Product


class ProductPage:
    def __init__(self):
        self.product = browser.element('[id="catalog-element-main"] .catalog-element-info')

    def open_product_page(self, product: Product) -> None:
        with allure.step(f"Открываем страницу продукта {product.name}"):
            browser.open(product.url)

    def check_product_page_is_opened(self, product: Product) -> None:
        with allure.step(f"Проверяем, что страница {product.name} открыта "):
            self.product.element('.catalog-element-info__title').should(
                have.exact_text(f'{product.description} {product.volume}'))


product_page = ProductPage()
