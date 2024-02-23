# from __future__ import annotations

from pydantic import BaseModel, Field


class MP(BaseModel):
    UF_ARTICLE: int
    MIDDLE_PRICE: str
    VALUE: str
    ALL_PRICES_SIMILAR: bool


class ProductInfo(BaseModel):
    id: str
    imageUrl: str
    xmlID: str
    title: str
    url: str
    ru_title: str = Field(..., alias='ru-title')
    price_old: int
    price: float
    MP: MP
    article: int
    price_by_card: int
    productQuantity: int
    total_summ: float = Field(..., alias='total-summ')
    totalsumm: float
    total_products: str = Field(..., alias='total-products')
    brandId: str
    brand: str
    categoryId: str
    category: str
    score: int
    counterUrl: str


class CartItemModel(BaseModel):
    productInfo: ProductInfo
    basket_position_id: int
    result_new: int = Field(..., alias='result-new')
    result: str

