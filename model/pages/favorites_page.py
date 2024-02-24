from selene import browser, have

from data.products import Product


class FavoritesPage:
    def __init__(self):
        self.product_items = browser.element('.selected-products')
        # self.cart = browser.element('[id=basket-page]')

    def check_product_in_favorites(self, product: Product) -> None:
        self.product_items.element('.product-list-item__name').should(
            have.exact_text(product.description))
        self.product_items.element('.align-center').element('[class=mt-1]').should(
            have.exact_text(f'Артикул {product.article}'))

    def clear_favorites(self) -> None:
        self.product_items.element('.product-list-item__btn-select').click()

    def check_favorites_is_empty(self) -> None:
        self.product_items.element('h3').should(have.exact_text('У вас пока нет избранных товаров'))
