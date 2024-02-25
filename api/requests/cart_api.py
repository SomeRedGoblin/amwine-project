from conftest import BASE_URL
from data.products import Product
from utils.api_helper import do_request, headers


# @pytest.fixture()


class CartApi:
    def __init__(self) -> None:
        self.ses_id = None
        self.base_url = BASE_URL
        self.endpoint = '/local/templates/am/ajax'
        if self.ses_id is None:
            self.ses_id = self.get_ses_id()

    def add_to_cart_via_api(self, product: Product, quantity):
        product_id = product.id
        action = "add"
        url = f"{self.endpoint}/header.basket.line.php?id={product_id}&action={action}"
        data = {"quantity": quantity}
        cookie = {"PHPSESSID": self.ses_id[0], "AMWINE__GUEST_ID": self.ses_id[1]}
        response = do_request(base_url=self.base_url, url=url, method="POST", headers=headers(), data=data,
                              cookies=cookie)
        return response

    def get_items_from_cart(self):
        url = f"{self.endpoint}/get-products-data-in-basket.php"
        cookie = {"PHPSESSID": self.ses_id[0], "AMWINE__GUEST_ID": self.ses_id[1]}
        responce = do_request(base_url=self.base_url, url=url, method="GET", headers=headers(), cookies=cookie)
        return responce

    def get_ses_id(self):
        url = f"{self.base_url}/"
        responce = do_request(base_url=self.base_url, url=url, method="POST", headers=headers())
        return responce.cookies["PHPSESSID"], responce.cookies['AMWINE__GUEST_ID']
