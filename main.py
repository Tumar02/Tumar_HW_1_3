import random

from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging
from random import choice

TOKEN = config('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def start_quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('NEXT', callback_data="button_1")
    markup.add(button_1)

    question = "The capital of South Korea?"
    answer = [
        "Seoul",
        "Bangkok,"
        "Pekin",
        "Busan",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        open_period=5,
        reply_markup=markup,
    )


@dp.callback_query_handler(text="button_1")
async def start_quiz_2(call: types.CallbackQuery):
    question = "Which of them is Korean food?"
    answer = [
        "Pizza",
        "Lagman"
        "Kimchi",
        "Pasta",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=5,
    )


@dp.message_handler(commands=['mem'])
async def bot(message: types.Message):
    memes = ['https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.beamliving.com%2Fstories%2Ffunny-2021-memes&psig=AOvVaw2Mt_XRAvY3sgydMayDkooH&ust=1681407229398000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOiX2pbwpP4CFQAAAAAdAAAAABAE'
             'https://www.ourmindfullife.com/wp-content/uploads/2021/04/funny-best-friends-memes-and-friendship-memes-3.jpg'
             'https://img.buzzfeed.com/buzzfeed-static/static/2019-04/18/11/campaign_images/buzzfeed-prod-web-05/these-are-the-funniest-parenting-memes-from-2019--2-19497-1555599787-0_dblbig.jpg?resize=1200:*']
    mem = random.choice(memes)
    await bot.send_photo(chat_id=message.from_user.id, photo=mem)


@dp.message_handler(commands=['start'])
async def number_or_word(message: types.Message):
    if message.text == int:
        await bot.send_message(chat_id=message.from_user.id, text=message.text**2)
    elif message.text == str:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


@dp.message_handler()
async def bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)