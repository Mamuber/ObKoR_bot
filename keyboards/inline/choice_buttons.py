from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


city_doors = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Дверь в гараже", callback_data="close:garage:True"),
        ],
        [
            InlineKeyboardButton(text="Дверь дома", callback_data="close:home:True"),
        ],
    ]
)
farm_doors = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Входная дверь на веранду", callback_data="close:villa_entrance:True"),
        ],
        [
            InlineKeyboardButton(text="Ворота", callback_data="close:villa_car_gate:True"),
        ],
        [
            InlineKeyboardButton(text="Калитка", callback_data="close:villa_gate:True"),
        ],
        [
            InlineKeyboardButton(text="Дом", callback_data="close:villa_villa:True"),
        ],
        [
            InlineKeyboardButton(text="Подспобка", callback_data="close:villa_utility_room:True"),
        ],
    ]
)

menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Меню",callback_data="menu")]])


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Двери в городе", callback_data="city"),
        ],
        [
            InlineKeyboardButton(text="Двери на даче", callback_data="farm"),
        ],
    ]
)