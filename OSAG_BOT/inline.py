from aiogram import types

async def end_menu_btn():
     btn = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)


     btn.row(
        types.InlineKeyboardButton("📑Купить ОСАГО", callback_data="oca"),
     )
     btn.row(
        types.InlineKeyboardButton("📑Техосмотр", callback_data="texo"),
     )
     btn.row(
        types.InlineKeyboardButton("📸Фотошоп техосмотр", callback_data="photo"),
     )
     btn.row(
        types.InlineKeyboardButton("🏪 КАСКО для банка", callback_data="bank"),
     )
     return btn

async def inline2_handler():
    btn = types.InlineKeyboardMarkup(resize_keyboard=True)
    # btn.add(
    #     types.InlineKeyboardButton("💳Пополнить баланс", callback_data="Pop"),
    #     types.InlineKeyboardButton("👜История заказов (0)", callback_data="Tarix"),
    # )
    btn.row(
        types.InlineKeyboardButton("💳Пополнить баланс", callback_data="Pop"),
    )
    btn.row(
        types.InlineKeyboardButton("👜История заказов (0)", callback_data="Tarix"),
    )

    return btn