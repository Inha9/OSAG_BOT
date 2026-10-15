from aiogram import types

async def start_menu_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        types.KeyboardButton("📂 Наши услуги"),
        types.KeyboardButton("👤 Профиль"),
        types.KeyboardButton("☎️ Обратная связь"),
        types.KeyboardButton("💥Телеграм канал"),
    )
    return btn




