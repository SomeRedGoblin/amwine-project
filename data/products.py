import dataclasses


@dataclasses.dataclass
class Product:
    id: str
    full_name: str
    name: str
    description: str
    volume: str
    price: str
    brand: str
    category: str
    article: str
    country: str


caol_ila_12 = Product(id="520883", full_name="Виски Caol Ila 12 летней выдержки", name="«Каол Айла» 12 лет",
                      description="Caol Ila 12 летней выдержки", volume="0.7 л", price="6999.99", brand="Caol Ila",
                      category="Виски", article="45640612", country="Шотландия")

guinness = Product(id="180031", full_name="Тёмное пиво Guinness Draught", name="Guinness Draught",
                   description="Guinness Draught", volume="0.44 л", price="266", brand="Гиннесс",
                   category="Тёмное пиво", article="80003005", country="Ирландия")
