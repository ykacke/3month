import asyncio
import logging

from bot_config import dp, bot, database
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.other_messages import echo_router
from handlers.dialog import opros_router


async def on_startup(bot):
    database.craze_tables()


async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(opros_router)

    # в самом конце
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())









# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from dotenv import dotenv_values
#
# token = dotenv_values(".env")["BOT_TOKEN"]
# bot = Bot(token=token)
# dp = Dispatcher()
#
#
# @dp.message(Command("start"))
# async def start_handler(message):
#     name = message.from_user.first_name
#     await message.answer(f'Привет {name}!')
#
#
# @dp.message()
# async def echo_handler(message: types.Message):
#     txt = message.text
#     message.from_user
#     await message.answer(txt)
#
#
# async def main():
#     запуск кода
    # await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
#     import asyncio
#     import logging
#
#     from bot_config import dp, bot
#     from handlers.start import start_router
#     from handlers.picture import picture_router
#     from handlers.other_messages import echo_router
#     from handlers.dialog import opros_router
#
#
#     async def main():
#         регистрация роутеров
        # dp.include_router(start_router)
        # dp.include_router(picture_router)
        # dp.include_router(opros_router)
        #
        # в самом конце
        # dp.include_router(echo_router)
        # запуск бота
        # await dp.start_polling(bot)
    #
    #
    # if __name__ == '__main__':
    #     logging.basicConfig(level=logging.INFO)
    #     asyncio.run(main())

