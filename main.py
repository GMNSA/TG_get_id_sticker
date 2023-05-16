import asyncio

import logging
from config_reader import config

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram import F

logging.basicConfig(level=logging.INFO)

bot = Bot(config.bot_token.get_secret_value())

dp = Dispatcher()


COMMAND_HELP = """
How To
Just send sticker to this bot and you'll get the sticker id.
I am a bots developer and sometimes I need to get Sticker ID, so I
create this bot.
I hope this simpole bot also useful for you.

Find a problem? Chat @getIDstickerChat
coded by @piterparkerX
"""

COMMAND_HELP_RUS = """
Как
Просто отправьте стикер этому боту, и вы получите идентификатор стикера.
Я разработчик ботов, и иногда мне нужно получить идентификатор стикера,
поэтому я создаю этого бота.
Я надеюсь, что этот простой бот также полезен для вас.

Нашли проблему? Чат @getIDstickerChat
Cozdatel  @peterparker
"""


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Hi.. Send me a sticker and I'll reply with it's ID. "
                         " This can be helpful for bots developer.")


@dp.message(F.sticker)
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message(Text('HELP'))
async def help_answer(message: types.Message):
    await message.answer(COMMAND_HELP)


@dp.message(Text('HELP_RUS'))
async def help_rus_answer(message: types.Message):
    await message.answer(COMMAND_HELP_RUS)


@dp.message()
async def handler_message(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='HELP'),
            types.KeyboardButton(text='HELP_RUS')
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer('Oh ... sorry ... please send me a sticker only ...',
                         reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
