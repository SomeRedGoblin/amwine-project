import dataclasses


@dataclasses.dataclass
class Product:
    url: str
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


caol_ila_12 = Product(url="/catalog/krepkie_napitki/viski/caol_ila_12_letney_vyderzhki/", id="520883",
                      full_name="Виски Caol Ila 12 летней выдержки", name="Caol Ila 12 летней выдержки",
                      description="Виски Caol Ila 12 летней выдержки", volume="0.7 л", price="6999.99",
                      brand="Caol Ila",
                      category="Виски", article="45640612", country="Шотландия")

guinness = Product(url="/catalog/pivo/dark/pivo_ginness_draft/", id="180031",
                   full_name="Тёмное пиво Guinness Draught",
                   name="Guinness Draught",
                   description="Тёмное пиво Guinness Draught Stout", volume="0.44 л", price="266", brand="Гиннесс",
                   category="Тёмное пиво", article="80003005", country="Ирландия")
