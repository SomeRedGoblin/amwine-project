from selene import browser, have
from data.products import Product


class CartPage:
    def __init__(self):
        self.product_item = browser.element('.product-list-item__container')

    def check_product(self, product: Product):
        self.product_item.element('.product-list-item__properties').element('a').should(
            have.exact_text(product.full_name))
        self.product_item.element('.product-list-item__properties').element('.text-caption').should(
            have.exact_text(product.article))
