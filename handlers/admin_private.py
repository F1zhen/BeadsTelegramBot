from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from filters.chat_types import ChatTypeFilter, IsAdmin

from keyboards.reply import ADMIN_KB, bizh_kb, admin_bizh_kb

from db.orm_query import orm_add_product, orm_delete_product, orm_update_product, orm_get_productsClothes, orm_get_products

from sqlalchemy.ext.asyncio import AsyncSession

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())


@admin_router.message(Command('admin'))
async def add_product(message: types.Message):
    await message.answer("Выберите действие", reply_markup=ADMIN_KB)


@admin_router.message(F.text == "Ассортимент")
async def starring_at_product(message: types.Message, session: AsyncSession):
    await message.answer("ОК, вот список товаров", reply_markup=admin_bizh_kb)


@admin_router.message(F.text == "Вернуться в Админ-панель")
async def start(message: types.Message):
    await message.answer("Возрат..", reply_markup=ADMIN_KB)


#Код ниже для машины состояний (FSM)
class AddProduct(StatesGroup):
    name = State()
    description = State()
    price = State()
    image = State()


@admin_router.message(StateFilter(None), F.text == "Добавить товар")
async def add_product(message: types.Message, state: FSMContext):
    await message.answer(
        "Введите название товара", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(AddProduct.name)



@admin_router.message(StateFilter(""), Command("отмена"))
@admin_router.message(StateFilter(""), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("Действия отменены", reply_markup=ADMIN_KB)


@admin_router.message(StateFilter('*'),Command("назад"))
@admin_router.message(StateFilter('*'),F.text.casefold() == "назад")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state == AddProduct.name:
        await message.answer('Ошибка, введите "отмена" ')
        return

    previous = None
    for step in AddProduct.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f"Вы вернулиcь к прошлому шагу")
            return
        previous = step


@admin_router.message(AddProduct.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text.lower())
    await message.answer("Введите описание товара")
    await state.set_state(AddProduct.description)


@admin_router.message(AddProduct.description, F.text)
async def add_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите стоимость товара")
    await state.set_state(AddProduct.price)


@admin_router.message(AddProduct.price, F.text)
async def add_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Загрузите изображение товара")
    await state.set_state(AddProduct.image)

@admin_router.message(AddProduct.image, F.photo)
async def add_image(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(image=message.photo[-1].file_id)
    data = await state.get_data()
    try:
        await orm_add_product(session, data)

        await message.answer("Товар добавлен", reply_markup=ADMIN_KB)
        await state.clear()

    except Exception as e:
        await message.answer(f"Ошибка, обратитесь к программисту ", reply_markup=ADMIN_KB)
        await state.clear()

