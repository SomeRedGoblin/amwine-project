# qa_quru_python_9_24
Дипломный проект

##  Дипломный проект по автоматизации тестирования сайта  
> <a target="_blank" href="https://amwine.ru">ссылка на сайт Ароматный Мир</a>

----

### Список UI автотестов

- [x] Добавление в корзину
- [x] Удаление товара из корзины
- [x] Добавление в избранное 
- [x] Удаление товара из избранного
- [x] Открытие страницы товара
- [x] Поиск не существующего товара 
- [x] Открытие страницы списка коктейлей

### Используемый стэк

<img title="Python" src="./resources/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="./resources/icons/pytest-original.svg" height="40" width="40"/> <img title="Pycharm" src="./resources/icons/pycharm.png" height="40" width="40"/> <img title="Selenium" src="./resources/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="./resources/icons/selene.png" height="40" width="40"/> <img title="GitHub" src="./resources/icons/github-original.svg" height="40" width="40"/> <img title="Allure Report" src="./resources/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="./resources/icons/AllureTestOps.png" height="40" width="40"/><img title="Telegram" src="./resources/icons/tg.png" height="40" width="40"/><img title="Jira" src="./resources/icons/jira-original.svg" height="40" width="40"/> 

----

### Локальный запуск автотестов

#### Выполнить в client:
> [!NOTE]
> Ключ выбора версии `--browser-version` не обязателен

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser-version=100
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C09-Rusak_UI_Diploma/">Ссылка</a>

#### Параметры сборки


* environment - параметр определяет окружение для запуска тестов
* comment - комментарий


#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C09-Rusak_UI_Diploma/">проект</a>
2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать: PROD
4. В поле "COMMENT" ввести комментарий
5. Нажать "Build"

----

### Allure отчет
#### Общие результаты

![allure_report_overview](resources/images/allure-all-report.png)

#### Список тест кейсов

![allure_reports_behaviors](resources/images/allure-list-test.png)

#### Отчет прохождения теста

![allure_reports_graphs](resources/images/allure-test.png)


----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/4095/dashboards">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](resources/images/testops-dashboard.png)

#### История запуска тестовых наборов

![allure_testops_launches](resources/images/testops-launches.png)

#### Тест кейсы

![allure_testops_suites](resources/images/testops-all-test.png)

----



### Оповещения в Telegram

<img src="./images/screenshots/tbot.png" width="300">
----

### Видео прохождения автотестов

![autotest_gif](resources/video/remove_from_favorites.gif)

----
#### Интеграция с JIRA

![allure_testops_suites](resources/images/jira-int.png)

----