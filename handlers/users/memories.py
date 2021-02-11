from datetime import datetime

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_buttons import choice
from loader import dp

@dp.message_handler(Command("start"))
async def show_memories(message: Message):
    await message.answer(text="""Привет , я бот для запоминания даты и времени закрытия дверей в гараже и дома \n
                              """
                              ,
                         reply_markup=choice)

@dp.message_handler(Command("memo"))
async def show_memories(message: Message):
    await message.answer(text="",
                         reply_markup=choice)


@dp.callback_query_handler(text_contains="garage")
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл дверь ГАРАЖА  "+ date)

@dp.callback_query_handler(text_contains="home")
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл дверь ДОМА "+ date)
