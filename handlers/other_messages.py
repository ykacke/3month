from aiogram import Router, types

echo_router = Router()

@echo_router.message()
async def echo_handler(message: types.Message):
    txt = message.text # текст собщения пользователя
    await message.answer(txt)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="Я Вас не понимаю"
    )