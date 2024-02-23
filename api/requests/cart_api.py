import allure
import pytest
import requests

from data.products import Product
from conftest import BASE_URL
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
        # cookie = {"PHPSESSID": "2Aj12T0DhXuM2MgkNzBbop2ojlM4NZ07", "AMWINE__GUEST_ID": "149089532"}
        # 1.27
        cookie = {"PHPSESSID": "CJ9LU31t1V5iVdmTQ7qaEoPRoFS031GL", "AMWINE__GUEST_ID": "149217360"}

        response = do_request(base_url=self.base_url, url=url, method="POST", headers=headers(), data=data,
                              cookies=cookie)
        return response

    def get_ses_id(self):
        url = f"{self.base_url}/"
        responce = requests.get(url=url, headers=headers())
        # responce = do_request(base_url=self.base_url, url=url, method="POST", headers=headers())
        #  request("post", url, data=data, json=json, **kwargs)
        # cook = responce.headers._store['set-cookie'][1]
        return responce.cookies["PHPSESSID"], responce.cookies['AMWINE__GUEST_ID']
