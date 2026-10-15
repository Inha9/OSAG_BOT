import logging

from aiogram import Bot, Dispatcher, executor, types

from btn import *
from inline import end_menu_btn, inline2_handler

API_TOKEN = '5928816783:AAFZfSptFPbk03dVDheMbHPe866YlM39qHA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    btn = await start_menu_btn()
    await message.answer("<strong>🙋‍♀️Привет дорогой друг! \nМеня зовут Осаго Макс</strong>""\n\n Я был создан, чтобы помочь тебе оформить Электронный осаго и диагностические карты  на твой автомобиль."
                         "\n\nОбещаю не занимать у тебя много времени, <strong>время = деньги</strong>, поэтому все будет очень просто, быстро и максимально понятно."
                         "\n\n⏳Заказы обрабатываются:<strong>с 09:00 до 22:00 по Московскому времени, а принимаются 24/7</strong>"
                         "\n\nВыбери нужный пункт из меню и я с радостью тебе помогу😌", reply_markup=btn)



@dp.message_handler(text = ['📂 Наши услуги'])
async def echo(message: types.Message):
    btn = await end_menu_btn()
    await message.answer(message.text, reply_markup=btn)

@dp.message_handler(text='👤 Профиль')
async def send_welcome(message: types.Message):
    btn = await inline2_handler()
    user = message.from_user.id
    await message.answer(f"""👤 Ваш Профиль
\n🆔 ID: {user}
💰 Баланс: 0.0 руб.
\nРеф.ссылка: https://t.me/Osagoa_bot?start={user}""", reply_markup=btn)

@dp.message_handler(text='☎️ Обратная связь')
async def send_welcome(message: types.Message):
    await message.answer("✳️ Гл.Админ бота: @osagomaksc")



@dp.message_handler(text='💥Телеграм канал')
async def send_welcome(message: types.Message):
    await message.answer("✳️ Наш канал: @osagomak")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)