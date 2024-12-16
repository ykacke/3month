from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot_config import database


opros_router = Router()

class Opros(StatesGroup):
    name = State()
    age = State()
    genre = State()

@opros_router.message(Command("opros"))
async def start_opros(message: types.Message, state: FSMContext):
    await message.answer("Как вам зовут?")
    await state.set_state(Opros.name)

@opros_router.message(Opros.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    print(name)
    await state.update_data(name=message.text)
    await message.answer("Сколько вам лет?")
    await state.set_state(Opros.age)

@opros_router.message(Opros.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста вводите только цифры")
        return
    age = int(age)
    if age < 10 or age > 90:
        await message.answer("Укажите вохраст от 10 до 90")
        return
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Приключения"),
                types.KeyboardButton(text="Фентези")
            ],
            [
                types.KeyboardButton(text="Фантастика"),
                types.KeyboardButton(text="Ужасы")
            ],
        ]
    )

    await state.update_data(age=message.text)
    await message.answer("Укажите ваш любимый жанр?")
    await state.set_state(Opros.genre)

@opros_router.message(Opros.genre)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer("Спасибо за пройденный опрос")
    data = await state.get_data()
    print(data)
    database.save_survey(data)
    # остановка диалога
    await state.clear()