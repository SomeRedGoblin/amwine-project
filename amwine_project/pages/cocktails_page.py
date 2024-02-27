from selene import browser, have


class CocktailsPage:
    def __init__(self):
        self.banner = browser.element('.banner__text')

    def open(self) -> None:
        browser.open('/cocktails')

    def check_cocktails_page_is_opened(self) -> None:
        self.banner.should(
            have.exact_text(
                f'Алкогольные коктейли\n'
                f'Сделать вечеринку или семейный ужин запоминающимися помогут вкусные '
                f'и необычные алкогольные коктейли. У нас вы найдете рецепты самых популярных из них, как крепких, '
                f'так и слабоалкогольных. Не забудьте поделиться ими с друзьями!'))


cocktails_page = CocktailsPage()
