from datetime import datetime
from typing import Union

from aiogram import Bot
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, inline_keyboard,message

from keyboards.inline.choice_buttons import choice, menu,farm_doors, city_doors
from loader import dp

@dp.message_handler(Command("start"))
async def show_memories(message: Message):
    await message.answer(text="""Привет , я бот для запоминания даты и времени закрытия дверей \n
                              """
                              ,
                         reply_markup=choice)

@dp.message_handler(Command("memo"))
async def show_memories(message: Message):
   await message.answer(text="Меню", reply_markup=menu)

@dp.callback_query_handler(text=["menu"])
async def close_garage_door(call: CallbackQuery):
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer(text="Меню:",reply_markup=choice)


@dp.callback_query_handler(text=["farm"])
async def close_garage_door(call: CallbackQuery):
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer(text="Двери на даче ",reply_markup=farm_doors)
@dp.callback_query_handler(text=["city"])
async def close_garage_door(call: CallbackQuery):
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer(text="Двери на даче ",reply_markup=city_doors)

@dp.callback_query_handler(text_contains=["garage"])
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл дверь ГАРАЖА  "+ date, reply_markup=menu)

@dp.callback_query_handler(text_contains="home")
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл дверь ДОМА В ГОРОДЕ "+ date, reply_markup=menu)

@dp.callback_query_handler(text_contains="villa_entrance")
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл дверь НА ВЕРАНДЕ "+ date, reply_markup=menu)
@dp.callback_query_handler(text_contains="villa_car_gate")
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл ВОРОТА "+ date, reply_markup=menu)
@dp.callback_query_handler(text_contains="villa_gate")
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл КАЛИТКУ "+ date, reply_markup=menu)

@dp.callback_query_handler(text_contains="villa_villa")
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл дверь ВХОДНУЮ ДВЕРЬ ДАЧИ "+ date, reply_markup=menu)


@dp.callback_query_handler(text_contains="villa_utility_room")
async def close_garage_door(call: CallbackQuery):
    date = str(datetime.now())
    await call.answer(cache_time=3)
    callback_data =  call.data
    await call.message.answer("Красавчик ты ТОЧНО закрыл дверь ВХОДНУЮ ДВЕРЬ ПОДСОБКИ "+ date, reply_markup=menu)

