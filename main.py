from aiogram import Bot, Dispatcher, executor, types
from Config import API_TOKEN
import asyncio

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    await message.reply('Введите команду /start, чтобы начать общение.')


executor.start_polling(dp, skip_updates=True)
