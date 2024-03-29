import allure
from selene import browser, have

from amwine_project.data.products import Product


class FavoritesPage:
    def __init__(self):
        self.product_items = browser.element('.selected-products')

    def check_product_in_favorites(self, product: Product) -> None:
        with allure.step(f"Проверяем, что {product.name} в избранном "):
            self.product_items.element('.product-list-item__name').should(
                have.exact_text(product.name))
            self.product_items.element('.align-center').element('[class=mt-1]').should(
                have.exact_text(f'Артикул {product.article}'))

    def clear_favorites(self) -> None:
        with allure.step(f"Удаляем товар из избранного"):
            self.product_items.element('.product-list-item__btn-select').click()

    def check_favorites_is_empty(self) -> None:
        with allure.step("Проверяем что корзина пуста"):
            self.product_items.element('h3').should(have.exact_text('У вас пока нет избранных товаров'))


favorites_page = FavoritesPage()
