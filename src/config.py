import os
from dotenv import find_dotenv, load_dotenv
import json
from typing import Any

import localization.ru as language

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("No token found!")
    exit(1)
PAYMENTPROVIDER_TOKEN = os.environ.get("PAYMENT_PROVIDER_TOKEN")
ADMINS = os.getenv("ADMINS")


TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
JSON_USER = '{"r": "user"}'
JSON_MANAGER = '{"r": "manager"}'
JSON_ADMIN = '{"r": "admin"}'

###

# filename = "config.json"
# class Config:
#     def __repr__(self):
#         return self.__data 

#     def __iter__(self):
#         return self.__data

#     def __getitem__(self, item):
#         return self.__data[item]

#     def __str__(self) -> str:
#         return self.__raw 

#     @property
#     def __raw(self) -> str:
#         with open(filename, "r") as f:
#             return f.read()

#     @property
#     def __data(self):
#        return json.loads(self.__raw) 

#     def set(self, param: str | tuple[str, str], value: Any) -> None:
#         modified_data = self.__data

#         if isinstance(param, tuple):
#             modified_data[param[0]][param[1]] = value
#         else:
#             modified_data[param] = value

#         backup_filename = f"{filename}.bak"
#         if os.path.exists(backup_filename):
#             os.remove(backup_filename)
#         with open(backup_filename, "w") as f:
#             json.dump(modified_data, f, indent=2)        
#         os.remove(filename)
#         with open(filename, "w") as f:
#             json.dump(modified_data, f, indent=2)

#     def init(self) -> None:
#         with open(filename, "w") as f:
#             data = {
#                 "settings": {
#                     "language": "ru",
#                     "currency": "RUB",
#                     "currency_symbol": "₽",
#                 },
#                 "delivery": {
#                     "price": 0,
#                     "enabled": False,
#                 },
#                 "checkout": {
#                     "adress": True,
#                     "phone": True,
#                     "email": True,
#                     "captcha": True,
#                 },
#                 "payment_methods": {
#                     "telegram_api": {
#                         "title": "Оплата через Telegram",
#                         "enabled": False,
#                     },
#                   },
#                 "info": {
#                     "greeting": "Приветствуем в нашем магазине!",
#                     "contacts": "Телефон: +7 (999) 999-99-99\nАдрес: г. Москва, ул. Ленина, д. 1",
#                     "refund_policy": "Политика возврата",
#                     "item_template": "Название: %n\nКатегория: %c\nЦена: %p\n\nОписание: %d",
#                 },
#             }
#             json.dump(data, f, indent=2)
    
# config = Config()

# if not os.path.exists("config.json"):
#     config.init()