from aiogram import types, Router, F
from keyboards import reply
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram.filters import Command, or_f

from aiogram.utils.keyboard import InlineKeyboardBuilder
from db.orm_query import *


user_router_bizh = Router()

class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int

def create_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Сделать заказ⚡",
        callback_data=MyCallback(foo="ex", bar=42)
    )
    return builder.as_markup()


@user_router_bizh.callback_query(MyCallback.filter(F.foo == "ex"))
async def my_callback_foo(query: CallbackQuery, callback_data: MyCallback):
    await query.message.answer("Для оформления заказа, предоставьте интересующий товар в @Fizhen 🙌🏽")
    print("bar =", callback_data.bar)

@user_router_bizh.message(F.text.lower() == "бижютерия")
async def start(message: types.Message):
    await message.answer("Выберите интересуюеще", reply_markup=reply.bizh_kb)

@user_router_bizh.message(F.text.lower() == "колье")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productKolye(session):
        await message.answer_photo(
            product.image,
            caption=f"{product.name}\nОписание: {product.description}\nСтоимость: {round(product.price, 2)} тенге"
        )
    await message.answer('Колья ⬆️', reply_markup=reply.order_KB)

@user_router_bizh.message(F.text.lower() == "чокеры")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productChoker(session):
        await message.answer_photo(
            product.image,
            caption=f"{product.name}\nОписание: {product.description}\nСтоимость: {round(product.price, 2)} тенге"
        )
    await message.answer('Чокеры ⬆️', reply_markup=reply.order_KB)

@user_router_bizh.message(F.text.lower() == "кольца")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productRing(session):
        await message.answer_photo(
            product.image,
            caption=f"{product.name}\nОписание: {product.description}\nСтоимость: {round(product.price, 2)} тенге"
        )
    await message.answer('Кольца ⬆️', reply_markup=reply.order_KB)

@user_router_bizh.message(F.text.lower() == "подвески")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productPodveska(session):
        await message.answer_photo(
            product.image,
            caption=f"{product.name}\nОписание: {product.description}\nСтоимость: {round(product.price, 2)} тенге"
        )
    await message.answer('Подвески ⬆️', reply_markup=reply.order_KB)

@user_router_bizh.message(F.text.lower() == "браслеты")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productBraslet(session):
        await message.answer_photo(
            product.image,
            caption=f"{product.name}\nОписание: {product.description}\nСтоимость: {round(product.price, 2)} тенге"
        )
    await message.answer('Браслеты ⬆️', reply_markup=reply.order_KB)

@user_router_bizh.message(F.text.lower() == "серьги")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productSergy(session):
        await message.answer_photo(
            product.image,
            caption=f"{product.name}\nОписание: {product.description}\nСтоимость: {round(product.price, 2)} тенге"
        )
    await message.answer('Серьги ⬆️', reply_markup=reply.order_KB)


@user_router_bizh.message(F.text.lower() == "брелки")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productBrelky(session):
        await message.answer_photo(
            product.image,
            caption=f" {product.name}\
                                \n Описание:  {product.description} \n Стоимость: {round(product.price, 2)} тенге "
        )
        await message.answer('Брелки ⬆️  ',reply_markup=reply.order_KB)


@user_router_bizh.message(or_f(Command('order'), (F.text.lower() == "оформить заказ")))
async def start(message: types.Message):
    await message.answer('для оформления заказа, пришлите интересующий товар в @F1zhen   ')