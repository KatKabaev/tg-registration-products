from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from crud_functions import pu_1



api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Регистрация')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')

kb.add(button1)
kb.add(button2)
kb.add(button3)


kb_products = InlineKeyboardMarkup()
inline_button_1 = InlineKeyboardButton('Product 1', callback_data="product_buying")
inline_button_2 = InlineKeyboardButton('Product 2', callback_data="product_buying")
inline_button_3 = InlineKeyboardButton('Product 3', callback_data="product_buying")
inline_button_4 = InlineKeyboardButton('Product 4', callback_data="product_buying")
kb_products.add(inline_button_1)
kb_products.add(inline_button_2)
kb_products.add(inline_button_3)
kb_products.add(inline_button_4)

pu_1.initiate_db()
# запустить один раз:
pu_1.add_products()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Информация')
async def inform(mes):
    await mes.answer('Этот бот создан для продажи БАДов')

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    products = pu_1.get_all_products()
    number = 1
    for i in products:
        await message.answer(f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
        with open(f'{number}.jpg', "rb") as img:
            await message.answer_photo(img, f'Продукт {number}')
        number += 1
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_products)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if pu_1.is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    pu_1.add_user(data['username'], data['email'], data['age'])
    await message.answer("Вы успешно зарегистрировались!")
    await state.finish()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    pu_1.connection.close()
