from typing import Any

from pydantic import BaseModel, Field


class ProductInfo(BaseModel):
    id: Any
    xmlID: Any
    title: Any
    url: Any
    ru_title: Any = Field(..., alias='ru-title')
    price_old: int
    price: int
    MP: Any
    article: Any
    productQuantity: int
    price_by_card: int
    total_summ: int = Field(..., alias='total-summ')
    totalsumm: int
    total_products: str = Field(..., alias='total-products')
    brandId: str
    brand: str
    categoryId: Any
    category: Any
    counterUrl: str


class CartNonExistentItem(BaseModel):
    productInfo: ProductInfo
    basket_position_id: bool
    result_new: bool = Field(..., alias='result-new')
    result: str
