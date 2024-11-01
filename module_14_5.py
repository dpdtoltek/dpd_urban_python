from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить'), KeyboardButton(text='Регистрация')]
    ],
    resize_keyboard=True)

kb_in = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ],
    resize_keyboard=True)

kb_in2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')]
    ],
    resize_keyboard=True)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text) is False:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer(f'Регистрация прошла успешно!', reply_markup=kb)
    await state.finish()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, len(pr) + 1):
        try:
            with open(f'images/{i}.jpg', 'rb') as img:
                await message.answer_photo(img,
                                           f'Название: {pr[i - 1][1]} | Описание: {pr[i - 1][2]} | Цена: {pr[i - 1][3]}')
        except FileNotFoundError:
            print(f'Файл {i} не найден!')
            await message.answer(f'Изображение временно отсутствует.\n'
                                 f'Название: {pr[i - 1][1]} | Описание: {pr[i - 1][2]} | Цена: {pr[i - 1][3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_in2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def set_age(call):
    await call.message.answer(f'Для мужчин:\n10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n'
                              f'Для женщин:\n10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_man = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    calories_woman = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    c_m = round(calories_man, 2)
    c_w = round(calories_woman, 2)
    await message.answer(f'Норма калорий для мужчины: {c_m}\nНорма калорий для женщины: {c_w}', reply_markup=kb)
    await state.finish()


@dp.message_handler(text='Информация')
async def set_age(message):
    await message.answer('Я - бот, помогающий рассчитать калории.')


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    initiate_db()
    pr = get_all_products()
    executor.start_polling(dp, skip_updates=True)
    connection.commit()
    connection.close()
