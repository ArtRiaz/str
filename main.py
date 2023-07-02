from aiogram import types, executor
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text


async def on_startup(_):
    print('Бот запущен')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет')


@dp.message_handler(Text(equals='photo'))
async def get_photo(message: types.Message):
    with open('test.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
