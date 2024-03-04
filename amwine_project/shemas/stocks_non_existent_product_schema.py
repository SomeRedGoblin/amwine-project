from pydantic import BaseModel


class Data(BaseModel):
    contentFormatted: str


class StocksNonExistentProduct(BaseModel):
    type: str
    status: str
    data: Data
