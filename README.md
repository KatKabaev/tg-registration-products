# Телеграм-бот для продажи продуктов
### Файл ```crud_functions.py```:
Класс ProductUser содержит следующие методы:
* initiate_db - создает в базе данных таблицы Products и Users.
* add_products - добавляет продукты
* add_user - добавляет пользователей
* get_all_products - возвращает все содержащиеся в базе данных продукты
* is_included - проверяет на наличие в базе данных пользователя

### Описание:
В файле ```mail.py``` содержится работа программы бота:
   * Кнопка для получения информации о боте.
   * Кнопка для регистрации пользователя.<br>
     Данные о пользователе будут сохраняться в ```database.db```:
     <p align="center">
    <img src="https://github.com/KatKabaev/tg-registration-products/blob/main/images/img1.png">
    </p>

   * Кнопка для продажи продуктов:
     <p align="center">
    <img src="https://github.com/KatKabaev/tg-registration-products/blob/main/images/img2.png" width="500">
    </p>

