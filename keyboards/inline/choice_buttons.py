from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Дверь в гараже", callback_data="close:garage:True"),
        ],
        [
            InlineKeyboardButton(text="Дверь дома", callback_data="close:home:True"),
        ],
        [
            InlineKeyboardButton(text="Дача - Входная дверь на веранду", callback_data="close:villa_entrance:True"),
        ],
        [
            InlineKeyboardButton(text="Дача - Ворота", callback_data="close:villa_car_gate:True"),
        ],
        [
            InlineKeyboardButton(text="Дача - Калитка", callback_data="close:villa_gate:True"),
        ],
        [
            InlineKeyboardButton(text="Дача - Дом", callback_data="close:villa_home:True"),
        ],
        [
            InlineKeyboardButton(text="Дача - Подспобка", callback_data="close:villa_utility_room:True"),
        ],
    ]
)
menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Меню",callback_data="menu")]])
