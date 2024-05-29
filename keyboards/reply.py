from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Каталог"),
            KeyboardButton(text = "Способ оплаты"),


        ],
        {
            KeyboardButton(text = "Способ доставки"),
            KeyboardButton(text = "О нас"),
            KeyboardButton(text = "Поддержка")
        }
    ],
    resize_keyboard=True,
    input_field_placeholder= "Что вас интересует?"
)


del_kby = ReplyKeyboardRemove()


catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Кастом одежды"),
     ],
        {
            KeyboardButton(text = "Бижютерия"),
        },
{
            KeyboardButton(text = "Вернуться в Меню"),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder= "Что вас интересует?"
)


bizh_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Колье"),
     ],
        {
            KeyboardButton(text = "Чокеры"),
        },
{
            KeyboardButton(text = "Кольца"),
        },
{
            KeyboardButton(text = "Подвески"),
        },
{
            KeyboardButton(text = "Браслеты"),
        },
{
            KeyboardButton(text = "Серьги"),
        },
{
            KeyboardButton(text = "Брелки"),
        },
{
            KeyboardButton(text = "Вернуться в Меню"),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder= "Что вас интересует?"
)


info_kv = ReplyKeyboardMarkup(
    keyboard=[
        [ KeyboardButton(text="Отправить номер телефона 📱", request_contact=True)

          ],


        {
            KeyboardButton(text="Отправить адрес доставки 🗺️", request_location=True)
        },

{
            KeyboardButton(text="Отправить ID товара ")
        },

{
            KeyboardButton(text = "Вернуться в Меню"),
        }

    ],
    resize_keyboard=True
)


ADMIN_KB = ReplyKeyboardMarkup(
    keyboard=[
        [ KeyboardButton(text="Добавить товар")

          ],

{
            KeyboardButton(text="Ассортимент")
        },
    ],
    resize_keyboard=True
)


TYPE_KB = ReplyKeyboardMarkup(
    keyboard=[
        [ KeyboardButton(text="Одежда ")

          ],


        {
            KeyboardButton(text="Бижютерия ")
        },

    ],
    resize_keyboard=True
)

admin_bizh_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Колье"),
     ],
        {
            KeyboardButton(text = "Чокеры"),
        },
{
            KeyboardButton(text = "Кольца"),
        },
{
            KeyboardButton(text = "Подвески"),
        },
{
            KeyboardButton(text = "Браслеты"),
        },
{
            KeyboardButton(text = "Серьги"),
        },
{
            KeyboardButton(text = "Брелки"),
        },
{
            KeyboardButton(text = "Вернуться в Админ-панель"),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder= "Что вас интересует?"
)

order_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Оформить заказ"),
     ],
        {
            KeyboardButton(text = "Вернуться в Меню"),
        },
    ],
    resize_keyboard=True,
    input_field_placeholder= "Что вас интересует?"
)


