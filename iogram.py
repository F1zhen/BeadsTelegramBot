import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from db.engine import create_db, drop_db, session_maker

from handlers.user_private import user_router
from handlers.admin_private import admin_router
from handlers.admin_group import user_group_router
from handlers.user_private_bizh import user_router_bizh
from handlers.admin_private_bizh import admin_router_bizh

from MiddleWare.db import DataBaseSession

from common.bot_cmds_list import private






ALLOWED_UPDATES = ["message", "edited_message"]

bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
bot.my_admins_list = []
dp = Dispatcher(fsm_strategy = FSMStrategy.USER_IN_CHAT)


dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(user_group_router)
dp.include_router(user_router_bizh)
dp.include_router(admin_router_bizh)

async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()

    await create_db()
async def on_shutdown(bot):
    print("Извините, но произошла ошибка и я перестал работать")

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())