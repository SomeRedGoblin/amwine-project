import allure
from selene import browser, have

from amwine_project.data.products import Product


class CartPage:
    def __init__(self):
        self.product_item = browser.element('.product-list-item__container')
        self.cart = browser.element('[id=basket-page]')

    def check_product_in_cart(self, product: Product) -> None:
        with allure.step(f"Проверяем, что {product.name} в корзине "):
            self.product_item.element('.product-list-item__properties').element('a').should(
                have.exact_text(product.full_name))
            self.product_item.element('.product-list-item__properties').element('.text-caption').should(
                have.exact_text(product.article))

    def clear_cart(self) -> None:
        with allure.step(f"Удаляем товар из корзины"):
            self.product_item.element('.product-list-item__delete').click()

    def check_cart_is_empty(self) -> None:
        with allure.step("Проверяем что корзина пуста"):
            self.cart.element('.app-card .text-center').should(have.exact_text('Ваша корзина пуста.'))


cart_page = CartPage()
