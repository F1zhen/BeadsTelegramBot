from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_list, Bold, as_marked_section
from keyboards import reply
from filters.chat_types import ChatTypeFilter, IsAdmin


user_router = Router()

@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет я твой помощник', reply_markup=reply.start_kb)


@user_router.message(or_f(Command('catalog'), (F.text.lower() == "каталог")))
async def start(message: types.Message):
    await message.answer('Каталог:  ', reply_markup=reply.catalog_kb)

@user_router.message(or_f(Command('id')))
async def start(message: types.Message):
    await message.answer(f"{message.from_user.id}")

@user_router.message(or_f(Command('order'), (F.text.lower() == "сделать заказ")))
async def start(message: types.Message):
    await message.answer('для завершения заказа, заполните данные ниже ', reply_markup=reply.info_kv)




@user_router.message(or_f(Command('payment'), (F.text.lower() == "способ оплаты")))
async def start(message: types.Message):
    text = as_marked_section(
        Bold("Варианты оплаты: "),
        "Картой в боте",
        "При получении Карта/Наличные",
        marker='😊 '
    )
    await message.answer(text.as_html())


@user_router.message(or_f(Command('shipping'), (F.text.lower() == "способ доставки")))
async def start(message: types.Message):
    text = as_marked_section(
        Bold("Варианты доставки: "),
        "Курьер",
        "Почта",
        marker='😊 '
    )
    await message.answer(text.as_html())


@user_router.message(or_f(Command('about'), (F.text.lower() == "о нас")))
async def start(message: types.Message):
    await message.answer('О нас:   ')

@user_router.message(or_f(Command('direct'), (F.text.lower() == "Поддержка")))
async def start(message: types.Message):
    await message.answer('поддержка:   ')


@user_router.message(F.text.lower() == "одежда")
async def start(message: types.Message):
    await message.answer('Ассортимент одежды:   ')

@user_router.message(F.text.lower() == "бижютерия")
async def start(message: types.Message):
    await message.answer("Выберите интересуюеще", reply_markup=reply.bizh_kb)


@user_router.message(F.text.lower() == "вернуться в меню")
async def start(message: types.Message):
    await message.answer("Возрат..", reply_markup=reply.start_kb)








