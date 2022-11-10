import random
import time

import markup as markup
from aiogram.types import ReplyKeyboardMarkup

from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


reply_keyboard = [["/start"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Hello, I`m smart password generator. I can help you to create safety password.")
    time.sleep(1)
    await message.answer("How many symbols of password do you want to create?")

@dp.message_handler()
async def get_password(message: types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if passlength > 15 or passlength < 5:
            await message.reply("We recommend to choose from 5 to 12 symbols")
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
            await message.answer("One more password? Just enter the number :)")
    except Exception as ex2:
        print(ex2)
        await message.answer("Enter the number of symbols from 5 to 15")
if __name__ == "__main__":
    executor.start_polling(dp)