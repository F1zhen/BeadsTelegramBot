from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_list, Bold, as_marked_section
from keyboards import reply
from filters.chat_types import ChatTypeFilter, IsAdmin
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm_query import *

admin_router_bizh = Router()
@admin_router_bizh.message(F.text.lower() == "бижютерия")
async def start(message: types.Message):
    await message.answer("Выберите интересуюеще", reply_markup=reply.admin_bizh_kb)


@admin_router_bizh.message(F.text.lower() == "колье")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productKolye(session):
        await message.answer_photo(
            product.image,
            caption=f" {product.name}\
                    \n Описание:  {product.description} \n Стоимость: {round(product.price, 2)} тенге "
        )
    await message.answer('Колья ⬆️   ')


@admin_router_bizh.message(F.text.lower() == "чокеры")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productChoker(session):
        await message.answer_photo(
            product.image,
            caption=f" {product.name}\
                                \n Описание:  {product.description} \n Стоимость: {round(product.price, 2)} тенге "
        )
    await message.answer('Чокеры ⬆️   ')


@admin_router_bizh.message(F.text.lower() == "кольца")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productRing(session):
        await message.answer_photo(
            product.image,
            caption=f" {product.name}\
                                \n Описание:  {product.description} \n Стоимость: {round(product.price, 2)} тенге "
        )
    await message.answer('Кольца ⬆️   ')


@admin_router_bizh.message(F.text.lower() == "подвески")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productPodveska(session):
        await message.answer_photo(
            product.image,
            caption=f" {product.name}\
                                \n Описание:  {product.description} \n Стоимость: {round(product.price, 2)} тенге "
        )
    await message.answer('Подвески ⬆️   ')

@admin_router_bizh.message(F.text.lower() == "браслеты")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productBraslet(session):
        await message.answer_photo(
            product.image,
            caption=f" {product.name}\
                                \n Описание:  {product.description} \n Стоимость: {round(product.price, 2)} тенге "
        )
        await message.answer('Браслеты ⬆️   ')


@admin_router_bizh.message(F.text.lower() == "серьги")
async def start(message: types.Message, session: AsyncSession):
    for product in await orm_get_productSergy(session):
        await message.answer_photo(
            product.image,
            caption=f" {product.name}\
                                \n Описание:  {product.description} \n Стоимость: {round(product.price, 2)} тенге "
        )
        await message.answer('Серьги ⬆️  ')
