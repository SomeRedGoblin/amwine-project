import dataclasses


@dataclasses.dataclass
class Product:
    id: str
    full_name: str
    name: str
    volume: str
    price: str
    brand: str
    category: str
    article: str
    country: str


caol_ila_12 = Product(id="520883", full_name="Виски Caol Ila 12 летней выдержки", name="«Каол Айла» 12 лет",
                      volume="0.7 л", price="6999.99", brand="Caol Ila",
                      category="Виски", article="45640612", country="Шотландия")
