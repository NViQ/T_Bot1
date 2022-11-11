import random
import time
import markup as markup
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message
from config import tg_bot_token
from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command, Text


bot = Bot(token=tg_bot_token, parse_mode="HTML")
dp = Dispatcher(bot)



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='6'),
        KeyboardButton(text='7')
        ],
        [
        KeyboardButton(text='8'),
        KeyboardButton(text='9'),
        ]
        ],
    resize_keyboard=True)




@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(f'Hello <b><u>{message.from_user.first_name} {message.from_user.last_name}</u></b>, I`m smart password generator. I can help you to create safety password.')
    time.sleep(1)
    await message.answer("How many symbols of password do you want to create?", reply_markup=menu)

@dp.message_handler()
async def get_password(message: types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if passlength > 21 or passlength < 5:
            await message.reply("We recommend to choose from 6 to 20 symbols", reply_markup=menu)
        else:
            a = "abcdefghijklmnopqrstuvwxyz"
            b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            с = "0123456789"
            d = "{}[]()?!*,-_$%#&@"
            all = a + b + с + d
            password = "".join(random.sample(all, passlength))
            await message.answer("Generation is going...")
            time.sleep(1)
            await message.answer(f"Your password: {password}")
            time.sleep(2)
            await message.answer("One more password? Just enter the number :)", reply_markup=menu)
    except Exception as ex2:
        print(ex2)
        await message.answer("Enter the number of symbols from 5 to 15")



if __name__ == "__main__":
    executor.start_polling(dp)