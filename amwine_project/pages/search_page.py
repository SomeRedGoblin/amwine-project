from selene import browser, have


class SearchPage:
    def __init__(self):
        self.search_field = browser.element('.page-header__top .search__input')
        self.nothing_found_message = browser.element('[id="fix-search"] .digi-search-fixed .digi-title-alternative')

    def search(self, search_value: str) -> None:
        self.search_field.click().type(search_value).submit()

    def check_nothing_found_message(self, search_value) -> None:
        self.nothing_found_message.should(
            have.exact_text(f'По запросу «{search_value}» точного совпадения не найдено, посмотрите похожие товары'))


search_page = SearchPage()
