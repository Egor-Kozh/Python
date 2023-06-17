import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv, find_dotenv

from keybord import markup, markup2, markup3, markup4, markup5, markup6, markup7
from parse_apteka import parses_apteka
from parses_hospital import parse_doctors, parse_services

load_dotenv(find_dotenv())

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

HELP_COMMAND = """
Основные команды для работы с ботом:
/start - начать работу с ботом
/help - основные команды для работы с ботом"""
n = 0

@dp.message_handler(commands = ['start', 'Меню'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hi\nВыбирете нужный пункт', reply_markup = markup)


@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
    await message.answer(text = HELP_COMMAND)


@dp.message_handler(commands = ['Препараты'])
async def medication_command(message: types.Message):
    await bot.send_message(message.from_user.id, text = "Введите название препарата", reply_markup = markup7)

    @dp.message_handler(content_types = ['text'])
    async def treatment(message: types.Message):
        await message.answer(text = f"{parses_apteka(message.text)}")


@dp.message_handler(commands = ['Услуги', 'Назад'])
async def medication_command(message: types.Message):
    await bot.send_message(message.from_user.id, text = "Выбирете действие", reply_markup = markup2)


@dp.message_handler(commands = ['Кардиология'])
async def kard_command(message: types.Message):
    n = 1
    await bot.send_message(message.from_user.id, text = "Выбирете действие", reply_markup = markup3)

    @dp.message_handler(commands = ['Врачи(кардиология)'])
    async def doctor_kr_command(message: types.Message):
        await message.answer(text = f"{parse_doctors(n)}")

    @dp.message_handler(commands = ['Стоимость(кардиология)'])
    async def doctor_kr_command(message: types.Message):
        await message.answer(text = f"{parse_services(n)}")


@dp.message_handler(commands = ['Стоматология'])
async def stom_command(message: types.Message):
    n = 2
    await bot.send_message(message.from_user.id, text = "Выбирете действие", reply_markup = markup4)

    @dp.message_handler(commands = ['Врачи(стоматология)'])
    async def doctor_st_command(message: types.Message):
        await message.answer(text = f"{parse_doctors(n)}")

    @dp.message_handler(commands = ['Стоимость(стоматология)'])
    async def doctor_st_command(message: types.Message):
        await message.answer(text = f"{parse_services(n)}")


@dp.message_handler(commands = ['Медосмотр'])
async def med_command(message: types.Message):
    n = 3
    await bot.send_message(message.from_user.id, text = "Выбирете действие", reply_markup = markup5)

    @dp.message_handler(commands = ['Врачи(медосмотр)'])
    async def doctor_med_command(message: types.Message):
        await message.answer(text = f"{parse_doctors(n)}")

    @dp.message_handler(commands=['Стоимость(медосмотр)'])
    async def doctor_med_command(message: types.Message):
        await message.answer(text = f"{parse_services(n)}")


@dp.message_handler(commands = ['Генетика'])
async def gen_command(message: types.Message):
    n = 4
    await bot.send_message(message.from_user.id, text = "Выбирете действие", reply_markup = markup6)

    @dp.message_handler(commands = ['Врачи(генетика)'])
    async def doctor_gen_command(message: types.Message):
        await message.answer(text = f"{parse_doctors(n)}")

    @dp.message_handler(commands = ['Стоимость(генетика)'])
    async def doctor_gen_command(message: types.Message):
        await message.answer(text = f"{parse_services(n)}")


async def on_startup(_):
    print('Бот успешно запущен!')


if __name__ == '__main__':
    executor.start_polling(dispatcher = dp, skip_updates = True, on_startup = on_startup)



